'use strict';

const fs = require('node:fs/promises');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const puppeteer = require('/Volumes/Data/Project/GitGam/PMS-Storage/node_modules/puppeteer-core');

async function run() {
    const manifest = JSON.parse(await fs.readFile(path.join(__dirname, 'manifest.json'), 'utf8'));
    const browser = await puppeteer.launch({
        executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless: true,
        args: ['--no-first-run', '--disable-background-networking']
    });

    try {
        const page = await browser.newPage();
        await page.setViewport({ width: 1536, height: 1240, deviceScaleFactor: 1 });

        for (const device of ['desktop', 'mobile']) {
            for (let group = 0; group < 3; group += 1) {
                const cards = (await Promise.all(manifest.slice(group * 9, group * 9 + 9).map(async function card(product) {
                    const bytes = await fs.readFile(path.join(__dirname, 'screenshots', `${product.repo}-vi-${device}.png`));
                    const source = 'data:image/png;base64,' + bytes.toString('base64');

                    return `<figure><figcaption>${product.repo}</figcaption><img src="${source}"></figure>`;
                }))).join('');
                await page.setContent(`<style>body{margin:8px;background:#e8ede8;font:14px Arial}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}figure{margin:0;height:400px;overflow:hidden;background:white}figcaption{height:25px;padding:5px;box-sizing:border-box}img{display:block;width:100%;height:375px;object-fit:cover;object-position:top}body.mobile img{width:300px;margin:auto}</style><body class="${device}"><div class="grid">${cards}</div></body>`);
                await page.evaluate(async function waitForImages() {
                    await Promise.all(Array.from(document.images).map(function decodeImage(image) {
                        return image.decode();
                    }));
                });
                await page.screenshot({ path: path.join(__dirname, `review-${device}-${group + 1}.png`) });
            }
        }
    } finally {
        await browser.close();
    }

    process.stdout.write('Created six visual review sheets covering all 27 products.\n');
}

run().catch(function reportError(error) {
    process.stderr.write(error.stack + '\n');
    process.exitCode = 1;
});
