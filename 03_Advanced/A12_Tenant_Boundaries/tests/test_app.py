import importlib.util
import sys
import json
import shutil
from pathlib import Path
import pytest
from streamlit.testing.v1 import AppTest
APP=Path(__file__).resolve().parents[1]/'app.py'
spec=importlib.util.spec_from_file_location('lab_'+APP.parent.name,APP)
app=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=app
spec.loader.exec_module(app)
CASES=json.loads((APP.parent/'sample_data/examples.json').read_text())
@pytest.mark.parametrize('case',CASES)
def test_acceptance(case,tmp_path,monkeypatch):
    monkeypatch.setattr(app,'DATA_DIR',tmp_path)
    output=app.run(case['input'])
    json.dumps(output,allow_nan=False)
    for key,value in case['expected_fields'].items():assert output[key]==value

def test_missing_input():
    with pytest.raises((ValueError,KeyError,TypeError)):app.run({})

def test_form_execution_and_reset(tmp_path):
    isolated=tmp_path/'lesson'
    shutil.copytree(APP.parent,isolated,ignore=shutil.ignore_patterns('.local','.venv','__pycache__','.pytest_cache'))
    ui=AppTest.from_file(str(isolated/'app.py')).run(timeout=30)
    assert not ui.exception
    ui.button[-1].click().run(timeout=30)
    assert not ui.exception and not ui.error and ui.success
    ui.button[0].click().run(timeout=30)
    assert not ui.success and not ui.exception

def test_missing_trusted_claim_rejected():
    with pytest.raises(ValueError):app.authorized_documents({},[{'tenant':'team-a','text':'secret'}])
