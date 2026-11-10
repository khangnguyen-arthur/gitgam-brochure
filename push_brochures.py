from pathlib import Path
import json
import subprocess

report = Path(__file__).resolve().parent
commits = json.loads((report / 'commits.json').read_text())
results = []


def git(root, *args):
    process = subprocess.run(['git', '-C', str(root), *args], text=True,
                             capture_output=True, timeout=90)
    if process.returncode:
        raise RuntimeError(process.stderr.strip() or process.stdout.strip())

    return process.stdout.strip()


for item in commits:
    root = Path('/Volumes/Data/Project/GitGam') / item['repo']
    record = dict(repo=item['repo'], branch=item.get('branch'), commit=item.get('commit'))
    try:
        if not item.get('committed'):
            raise RuntimeError('Brochure commit was not prepared.')

        if git(root, 'rev-parse', 'HEAD') != item['commit']:
            raise RuntimeError('Branch has changed since the brochure commit; refusing to push other work.')

        ref = 'refs/heads/' + item['branch']
        git(root, 'push', 'origin', item['commit'] + ':' + ref)
        remote_line = git(root, 'ls-remote', '--exit-code', 'origin', ref)
        remote_sha = remote_line.split()[0]
        if remote_sha != item['commit']:
            raise RuntimeError('Remote branch does not match the brochure commit.')

        record.update(pushed=True, remote_commit=remote_sha)
        print(item['repo'] + ': pushed and verified ' + remote_sha[:12], flush=True)
    except Exception as error:
        record['error'] = str(error)
        print(item['repo'] + ': ERROR ' + str(error), flush=True)

    results.append(record)
    (report / 'push-results.json').write_text(json.dumps(results, ensure_ascii=False, indent=4) + '\n')

if any('error' in result for result in results):
    raise SystemExit(1)
