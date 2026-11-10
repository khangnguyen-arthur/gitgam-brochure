'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const puppeteer = require('/Volumes/Data/Project/GitGam/PMS-Storage/node_modules/puppeteer-core');

const reportRoot = __dirname;
const screenshotRoot = path.join(reportRoot, 'screenshots');
const results = [];

async function checkDocument(Param) {
    const page = await Param.browser.newPage();
    const errors = [];
    const externalRequests = [];
    page.on('pageerror', function recordError(error) {
        errors.push(error.message);
    });
    await page.setRequestInterception(true);
    page.on('request', function handleRequest(request) {
        if (/^https?:/.test(request.url())) {
            externalRequests.push(request.url());
            request.abort();
        } else {
            request.continue();
        }
    });
    await page.setViewport({ width: Param.width, height: 960, deviceScaleFactor: 1 });
    await page.emulateMediaFeatures([{ name: 'prefers-reduced-motion', value: 'reduce' }]);
    const filename = Param.locale === 'vi' ? 'index.html' : 'en.html';
    await page.goto(pathToFileURL(path.join(Param.product.path, filename)).href, { waitUntil: 'load' });
    await page.evaluate(async function waitForFonts() {
        await document.fonts.ready;
    });
    const observation = await page.evaluate(function inspectDocument() {
        const overflows = Array.from(document.querySelectorAll('body *')).filter(function isOverflowing(element) {
            const rect = element.getBoundingClientRect();

            return rect.width > 0 && (rect.right > innerWidth + 1 || rect.left < -1);
        }).map(function describe(element) {
            return `${element.tagName}.${element.className?.baseVal || element.className}`;
        });
        const missingAssets = Array.from(document.images).filter(function isBroken(image) {
            return !image.complete || !image.naturalWidth;
        }).map(function source(image) {
            return image.getAttribute('src');
        });
        const missingTargets = Array.from(document.querySelectorAll('a[href^="#"]')).filter(function isMissing(link) {
            return !document.getElementById(link.hash.slice(1));
        }).map(function href(link) {
            return link.getAttribute('href');
        });

        return {
            lang: document.documentElement.lang,
            headingCount: document.querySelectorAll('h1').length,
            headings: Array.from(document.querySelectorAll('h2')).map(function title(heading) {
                return heading.textContent;
            }),
            overflows,
            missingAssets,
            missingTargets,
            text: document.body.innerText,
            height: document.documentElement.scrollHeight,
            stylesheetLoaded: getComputedStyle(document.querySelector('.hero')).display === 'grid'
        };
    });
    assert.equal(observation.lang, Param.locale);
    assert.equal(observation.headingCount, 1);
    assert.equal(observation.headings.length, 5);
    assert.equal(observation.stylesheetLoaded, true);
    assert.deepEqual(observation.overflows, [], `${Param.product.repo}/${Param.locale}/${Param.width}: overflow ${observation.overflows.join(', ')}`);
    assert.deepEqual(observation.missingAssets, []);
    assert.deepEqual(observation.missingTargets, []);
    assert.deepEqual(errors, []);
    assert.deepEqual(externalRequests, [], 'Brochure must load offline without external requests');
    assert.match(observation.text, /GitGam Cloud/);
    assert.match(observation.text, /On-premises/);
    await page.click('a[href="#features"]');
    assert.equal(await page.evaluate(function scrollPosition() {
        return window.scrollY > 50;
    }), true, 'Feature navigation should scroll the document');
    await page.evaluate(function resetScroll() {
        window.scrollTo(0, 0);
    });

    if (Param.width !== 320) {
        const device = Param.width === 1280 ? 'desktop' : 'mobile';
        await page.screenshot({ path: path.join(screenshotRoot, `${Param.product.repo}-${Param.locale}-${device}.png`), fullPage: true });
    }

    const otherLocale = Param.locale === 'vi' ? 'en' : 'vi';
    await Promise.all([
        page.waitForNavigation({ waitUntil: 'load' }),
        page.click(`.languages a[lang="${otherLocale}"]`)
    ]);
    assert.equal(await page.evaluate(function documentLanguage() {
        return document.documentElement.lang;
    }), otherLocale, 'Language link should open the translated document');
    results.push({ product: Param.product.repo, language: Param.locale, width: Param.width, height: observation.height, passed: true });
    await page.close();
}

async function run() {
    await fs.mkdir(screenshotRoot, { recursive: true });
    const products = JSON.parse(await fs.readFile(path.join(reportRoot, 'manifest.json'), 'utf8'));
    const browser = await puppeteer.launch({
        executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless: true,
        args: ['--no-first-run', '--disable-default-apps', '--disable-background-networking']
    });

    try {
        for (const product of products) {
            for (const locale of ['vi', 'en']) {
                for (const width of [1280, 390, 320]) {
                    await checkDocument({ browser, product, locale, width });
                }
            }

            process.stdout.write(`${product.repo}: VI/EN, desktop/mobile/narrow, assets and links passed\n`);
        }
    } finally {
        await browser.close();
        await fs.writeFile(path.join(reportRoot, 'browser-results.json'), JSON.stringify(results, null, 4) + '\n');
    }

    process.stdout.write(`Passed ${results.length} render/navigation checks. Saved ${products.length * 4} screenshots.\n`);
}

run().catch(function reportFailure(error) {
    process.stderr.write(error.stack + '\n');
    process.exitCode = 1;
});
