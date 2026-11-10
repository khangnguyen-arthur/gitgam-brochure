from pathlib import Path
import json
import subprocess

report = Path(__file__).resolve().parent
manifest = json.loads((report / 'manifest.json').read_text())
results = []


def git(root, *args):
    process = subprocess.run(['git', '-C', str(root), *args], text=True,
                             capture_output=True, timeout=90)
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or process.stdout.strip())

    return process.stdout.strip()


for item in manifest:
    root = Path(item['path']).parent
    record = dict(repo=item['repo'])
    try:
        head_before = git(root, 'rev-parse', 'HEAD')
        branch = git(root, 'symbolic-ref', '--short', 'HEAD')
        ahead = git(root, 'rev-list', '--count', '@{upstream}..HEAD')
        if ahead != '0':
            raise RuntimeError('Existing unpushed commits detected; preserving the current branch for review.')

        files = [str(file.relative_to(root)) for file in (root / 'brochure').rglob('*') if file.is_file()]
        if len(files) != 7:
            raise RuntimeError('Unexpected brochure file count: ' + str(len(files)))

        git(root, 'add', '--', 'brochure')
        git(root, 'diff', '--cached', '--check', '--', 'brochure')
        git(root, 'commit', '--only', '-m',
            'docs(brochure): introduce business products in Vietnamese and English',
            '--', 'brochure')
        head = git(root, 'rev-parse', 'HEAD')
        changed = git(root, 'diff-tree', '--no-commit-id', '--name-only', '-r', 'HEAD').splitlines()
        if sorted(changed) != sorted(files):
            raise RuntimeError('Committed paths did not match the prepared brochure files.')

        record.update(branch=branch, commit=head, parent=head_before,
                      paths=changed, committed=True)
        print(item['repo'] + ': committed ' + head[:12], flush=True)
    except Exception as error:
        record['error'] = str(error)
        print(item['repo'] + ': ERROR ' + str(error), flush=True)

    results.append(record)
    (report / 'commits.json').write_text(json.dumps(results, ensure_ascii=False, indent=4) + '\n')

if any('error' in result for result in results):
    raise SystemExit(1)
