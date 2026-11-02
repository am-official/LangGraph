import importlib.util
from pathlib import Path
from streamlit.testing.v1 import AppTest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('portal_LangGraph',ROOT/'portal.py');portal=importlib.util.module_from_spec(spec);spec.loader.exec_module(portal)
def test_catalog_contract():
    rows=portal.catalog()
    assert len(rows)==65 and len({r['code'] for r in rows})==65
    assert len(portal.search_catalog(rows,'Beginner',''))==20
    assert len(portal.search_catalog(rows,'All','B01'))==1
    assert len(portal.search_catalog(rows,'Advanced','B01'))==0

def test_portal_search_and_practice():
    ui=AppTest.from_file(str(ROOT/'portal.py')).run(timeout=30)
    assert not ui.exception
    ui.text_input[0].set_value('B01').run()
    assert any('1 lab matches' in c.value for c in ui.caption)
    ui.toggle[0].set_value(True).run()
    assert not ui.exception
