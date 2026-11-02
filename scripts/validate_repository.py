"""Check curriculum structure and source without calling external services."""
from pathlib import Path
from collections import Counter
import ast
import json
import re
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=('app.py','requirements.txt','.env.example','.gitignore','README.md','INSTRUCTIONS.md','EXPLANATION.md','EXERCISES.md','INTERVIEW.md','TROUBLESHOOTING.md','tests/test_app.py','sample_data/examples.json')
def validate():
    rows=json.loads((ROOT/'docs/catalog.json').read_text());errors=[];paths=set();sources=0
    if len(rows)!=65:errors.append('Expected 65 labs.')
    if Counter(r['level'] for r in rows)!=Counter({'Beginner':20,'Intermediate':20,'Advanced':20,'Capstone':5}):errors.append('Stage counts differ from curriculum.')
    if len({r['code'] for r in rows})!=65:errors.append('Duplicate lab IDs.')
    for row in rows:
        path=row['path'];folder=(ROOT/path).resolve()
        if not folder.is_relative_to(ROOT) or path in paths:errors.append('Unsafe/duplicate path: '+path);continue
        paths.add(path)
        for name in REQUIRED:
            file=folder/name
            if not file.is_file() or not file.read_text().strip():errors.append('Missing or empty: '+path+'/'+name)
        samples=json.loads((folder/'sample_data/examples.json').read_text())
        if len(samples)<3:errors.append(path+': fewer than three contracts')
        for sample in samples:
            if not sample.get('expected_fields') or not sample.get('input'):errors.append(path+': invalid sample contract')
        for file in folder.rglob('*.py'):
            if any(x in file.parts for x in ('.venv','.local','__pycache__')):continue
            code=file.read_text();sources+=1
            try:ast.parse(code,filename=str(file))
            except SyntaxError as exc:errors.append(str(exc))
            if re.search(r'sk-[A-Za-z0-9]{25,}',code):errors.append('Possible hardcoded credential: '+str(file))
            if 'sys.path.insert' in code or 'sys.path.append' in code:errors.append('Unexpected path injection: '+str(file))
    for name in ('portal.py','README.md','requirements.lock.txt','pyproject.toml','05_Interview_Preparation/README.md','06_Reference_Guides/Study_Plan.md'):
        if not (ROOT/name).is_file():errors.append('Missing root file: '+name)
    if '--hash=sha256:' not in (ROOT/'requirements.lock.txt').read_text():errors.append('Expected hashed dependency lock.')
    if errors:raise SystemExit('\n'.join(errors))
    print(f'Validated {len(rows)} self-contained labs, {sources} project Python files, and {sum(len(json.loads((ROOT/r["path"]/"sample_data/examples.json").read_text())) for r in rows)} sample contracts.')
if __name__=='__main__':validate()
