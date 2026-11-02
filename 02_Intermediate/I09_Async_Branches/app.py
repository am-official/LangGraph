"""Async work without shared mutation — executable workshop."""
from pathlib import Path
from contextlib import contextmanager
from datetime import datetime,timezone,timedelta
import json
import math
import os
import re
import sqlite3
import uuid
import hashlib
import time
import streamlit as st
from dotenv import load_dotenv
load_dotenv(Path(__file__).with_name('.env'),override=False)
DATA_DIR=Path(__file__).with_name('.local')

def text(value,limit=10000):
    if not isinstance(value,str) or not value.strip() or len(value)>limit:raise ValueError(f'Enter nonempty text up to {limit} characters.')
    return value.strip()

def items(value,maximum=100):
    result=json.loads(value) if isinstance(value,str) else value
    if not isinstance(result,list) or not 1<=len(result)<=maximum:raise ValueError(f'Supply an array of 1–{maximum} items.')
    return result

def number(value,minimum=0,maximum=1e12):
    if isinstance(value,bool):raise ValueError('A boolean is not a numeric measurement.')
    result=float(value)
    if not math.isfinite(result) or not minimum<=result<=maximum:raise ValueError(f'Use a finite number between {minimum} and {maximum}.')
    return result

@contextmanager
def database(name='lab.sqlite'):
    DATA_DIR.mkdir(parents=True,exist_ok=True)
    db=sqlite3.connect(DATA_DIR/name,timeout=5)
    db.execute('PRAGMA foreign_keys=ON')
    try:
        with db:yield db
    finally:db.close()

def integer(value,minimum=0,maximum=1000000000000):
    if type(value) is not int:raise ValueError('Use an integer; fractional values and booleans are not accepted.')
    return int(number(value,minimum,maximum))

def cloud_client():
    from langsmith import Client
    key=os.getenv('LANGSMITH_API_KEY','').strip()
    if not key or key=='YOUR_LANGSMITH_API_KEY_HERE':raise ValueError('Set LANGSMITH_API_KEY in .env for this optional cloud operation.')
    return Client(api_key=key,timeout_ms=15000)
from typing import Annotated,Literal
from typing_extensions import TypedDict
import operator
from langgraph.graph import StateGraph,START,END
from langgraph.types import Command,Send,interrupt,RetryPolicy
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage,SystemMessage,RemoveMessage
from langgraph.graph.message import add_messages

def evidence(graph,result):
    drawing=graph.get_graph()
    dot='digraph workflow { rankdir=LR; '+''.join(json.dumps(e.source)+' -> '+json.dumps(e.target)+';' for e in drawing.edges)+' }'
    return {**dict(result),'diagram':drawing.draw_mermaid(),'dot':dot}
TITLE = 'Async work without shared mutation'
DESCRIPTION = 'Run asynchronous graph branches and merge their independent results.'
CODE = 'I09'
LEVEL = 'Intermediate'
WORKSHOP = 'Graph Workshop'
DEFAULTS = {'text': 'async state'}
CHOICES = {}
LIVE = False
LIMITATION = 'Local deterministic workflow; model intelligence and managed deployment are separate concerns.'
STYLE = '<style>.stApp{background:radial-gradient(ellipse at top left,#142E35,#101521 65%);color:#edf1f8}.block-container{max-width:1180px;padding-top:5rem;padding-bottom:3rem}h1{font-size:clamp(2.3rem,5vw,4rem)!important;letter-spacing:-.045em;line-height:1.12!important}h2,h3{letter-spacing:-.025em}.eyebrow{color:#77E4C8;letter-spacing:.16em;font-size:.72rem;font-weight:700}button[kind^="primary"]{color:#101521!important;font-weight:650}button{min-height:44px;border-radius:12px!important}</style>'
CRITERIA = ['For sample 1, expected fields are {"results": ["reverse:cba", "upper:ABC"]}', 'For sample 2, expected fields are {"results": ["reverse:eno", "upper:ONE"]}', 'For sample 3, expected fields are {"results": ["reverse:dc ba", "upper:AB CD"]}']
INTERVIEW = 'Explain ainvoke and asynchronous node boundaries. Then discuss: Why does async execution not make CPU-bound work automatically faster?'

import asyncio
class State(TypedDict):text:str;results:Annotated[list[str],operator.add]
async def uppercase(state):
    await asyncio.sleep(0);return {'results':['upper:'+state['text'].upper()]}
async def reverse(state):
    await asyncio.sleep(0);return {'results':['reverse:'+state['text'][::-1]]}
async def execute(content):
    builder=StateGraph(State);builder.add_node('uppercase',uppercase);builder.add_node('reverse',reverse);builder.add_edge(START,'uppercase');builder.add_edge(START,'reverse');builder.add_edge('uppercase',END);builder.add_edge('reverse',END);graph=builder.compile()
    result=await graph.ainvoke({'text':content,'results':[]});result['results'].sort();return evidence(graph,result)
def run(data):return asyncio.run(execute(text(data['text'],2000)))



def main():
    st.set_page_config(page_title=TITLE+' · '+WORKSHOP,page_icon='◆',layout='wide')
    st.html(STYLE)
    st.html('<div class="eyebrow">'+WORKSHOP.upper()+' / '+CODE+' / '+LEVEL.upper()+'</div>')
    st.title(TITLE)
    st.write(DESCRIPTION)
    st.caption('INPUT → EXECUTION → EVIDENCE → REVIEW')
    left,right=st.columns([1,1.15],gap='large')
    with left:
        st.subheader('Configure the experiment')
        live=st.toggle('Use my LangSmith account',value=False) if LIVE else False
        st.caption('Writes or reads your configured LangSmith account. Use non-sensitive learning data.' if live else 'Local execution · No API key required')
        if st.button('Reset results'):
            st.session_state.pop('result',None)
        with st.form('lab'):
            values={};parse_errors=[]
            for key,default in DEFAULTS.items():
                label=key.replace('_',' ').capitalize()
                if key in CHOICES: value=st.selectbox(label,CHOICES[key],index=CHOICES[key].index(default))
                elif isinstance(default,bool):value=st.checkbox(label,value=default)
                elif isinstance(default,int):value=st.number_input(label,value=default,step=1)
                elif isinstance(default,float):value=st.number_input(label,value=default)
                elif isinstance(default,(list,dict)):
                    raw=st.text_area(label+' (JSON)',value=json.dumps(default,indent=2,ensure_ascii=False),height=170)
                    try:value=json.loads(raw)
                    except json.JSONDecodeError:parse_errors.append(label+': use valid JSON with double quotes.');value=None
                else:value=st.text_area(label,value=default,height=90)
                values[key]=value
            submitted=st.form_submit_button('Run experiment',type='primary',use_container_width=True)
        if submitted:
            st.session_state.pop('result',None)
            try:
                if parse_errors:raise ValueError(' '.join(parse_errors))
                started=time.perf_counter()
                with st.spinner('Executing the workflow…'):
                    result=run_cloud(values) if live else run(values)
                json.dumps(result,allow_nan=False)
                st.session_state.result={'output':result,'input':values,'duration_ms':round((time.perf_counter()-started)*1000,2),'mode':'LangSmith account' if live else 'local'}
            except (ValueError,KeyError,TypeError) as error:
                st.error('Check the input: '+str(error))
            except Exception:
                st.error('Execution failed. Check TROUBLESHOOTING.md, service permissions, and the selected runtime. Your previous result was cleared.')
    with right:
        st.subheader('Inspect the evidence')
        saved=st.session_state.get('result')
        with st.container(border=True):
            if saved:
                st.caption(saved['mode'].upper()+' · '+str(saved['duration_ms'])+' ms')
                output=saved['output'];public={k:v for k,v in output.items() if k not in ('dot','diagram')}
                if 'answer' in public:st.write(public['answer'])
                st.json(public,expanded=True)
                st.success('Execution complete. Compare the result with the acceptance criteria below.')
                st.download_button('Download evidence',json.dumps(saved,indent=2,ensure_ascii=False),'lab-result.json','application/json')
            else:
                st.markdown('### Ready for the first run')
                st.write('The prepared input exercises the main path. Run it, inspect each result field, then change one variable.')
        if saved and saved['output'].get('dot'):
            with st.expander('Workflow architecture',expanded=True):st.graphviz_chart(saved['output']['dot'])
            with st.expander('Mermaid source'):st.code(saved['output']['diagram'],language='mermaid')
        with st.expander('Acceptance criteria',expanded=True):
            for criterion in CRITERIA:st.write('• '+criterion)
        with st.expander('Interview discussion'):
            st.write(INTERVIEW)
            st.caption('See INTERVIEW.md for expected reasoning, follow-up questions, and common mistakes.')
    st.divider()
    st.caption(WORKSHOP+' · '+LIMITATION)

if __name__=='__main__':main()
