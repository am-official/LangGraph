REPO='LangGraph'
HEADLINE='Stateful systems.<br><span>Built with evidence.</span>'
SUBTITLE='Explore state, routing, persistence, and recovery through 65 runnable graph labs.'
STYLE='<style>.stApp{background:radial-gradient(ellipse at 0% 0%,#15343A,#101521 65%);color:#edf1f8}.block-container{max-width:1200px;padding-top:5rem}h1{font-size:clamp(2.6rem,6vw,4.8rem)!important;letter-spacing:-.05em;line-height:1.06!important;max-width:920px}h1 span{color:#77E4C8}h2,h3{letter-spacing:-.025em}.eyebrow{color:#77E4C8;letter-spacing:.18em;font-size:.72rem;font-weight:700}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:2rem 0}.stats>div{background:#192232;border:1px solid #344052;border-radius:16px;padding:20px}.stats span{display:block;font-size:.7rem;color:#bac5d8;letter-spacing:.1em}.stats strong{display:block;font-size:2rem;color:#77E4C8;margin-top:6px}button[kind^="primary"]{color:#101521!important;font-weight:650}button{min-height:44px;border-radius:12px!important}@media(max-width:600px){.stats{grid-template-columns:repeat(2,1fr)}.stats>div{padding:16px}}</style>'
from pathlib import Path
import json
import streamlit as st
ROOT=Path(__file__).resolve().parent

def catalog():return json.loads((ROOT/'docs/catalog.json').read_text())
def search_catalog(rows,stage,query):
    return [r for r in rows if (stage=='All' or r['level']==stage) and query.casefold() in (r['code']+' '+r['title']+' '+r['concept']).casefold()]

def main():
    st.set_page_config(page_title=REPO+' · Engineering Labs',page_icon='◆',layout='wide')
    st.html(STYLE)
    st.html('<div class="eyebrow">'+REPO.upper()+' / ENGINEERING LABS</div>')
    st.html('<h1>'+HEADLINE+'</h1>')
    st.write(SUBTITLE)
    st.html('<div class="stats"><div><span>BEGINNER</span><strong>20</strong></div><div><span>INTERMEDIATE</span><strong>20</strong></div><div><span>ADVANCED</span><strong>20</strong></div><div><span>CAPSTONES</span><strong>5</strong></div></div>')
    labs,practice=st.tabs(['Hands-on labs','Interview practice'])
    rows=catalog()
    with labs:
        st.subheader('Find the next lab')
        left,right=st.columns([1,2])
        stage=left.selectbox('Learning stage',['Beginner','Intermediate','Advanced','Capstone','All'])
        query=right.text_input('Search by topic or code',placeholder='Checkpoints, evaluation, or B01')
        matches=search_catalog(rows,stage,query)
        st.caption(str(len(matches))+(' lab matches' if len(matches)==1 else ' labs match')+' your filters')
        for index in range(0,len(matches),2):
            columns=st.columns(2,gap='medium')
            for column,row in zip(columns,matches[index:index+2]):
                with column,st.container(border=True):
                    st.caption(row['code']+' / '+row['level'].upper())
                    st.markdown('### '+row['title'])
                    st.write(row['description'])
                    st.caption(row['status'].replace('_',' '))
                    with st.expander('Launch and explore'):
                        st.code('cd "'+row['path']+'"\npython -m streamlit run app.py',language='sh')
                        st.write('Install this folder’s requirements in your active environment first. Full cross-platform commands are in INSTRUCTIONS.md.')
                        st.code('python -m pytest "'+row['path']+'/tests" -q',language='sh')
                        st.write('Interview focus: '+row['concept'])
        if not matches:st.info('Try a broader topic or select All learning stages.')
    with practice:
        st.subheader('Explain. Diagnose. Defend.')
        st.write('Choose a lab, rehearse its mechanism, then work through a failure and an architecture tradeoff. Use tests and sample evidence to support your answer.')
        chosen=st.selectbox('Interview topic',rows,format_func=lambda row:row['code']+' · '+row['title'])
        st.markdown('### '+chosen['concept'].capitalize())
        st.write(chosen['tradeoff'])
        with st.expander('A concrete reasoning task',expanded=True):
            example=chosen['example'];st.write('Predict the result before running this input:');st.json(example['input'])
            if st.toggle('Show expected evidence'):
                st.json(example['expected_fields'])
                st.write('Explain which operation produces each field. Then change one boundary input and predict the failure.')
        st.markdown('#### Score your explanation')
        scores=[]
        for label in ['Mechanism grounded in the code','Failure case with observable evidence','Tradeoff and alternative design','Verification limits stated precisely']:
            scores.append(st.slider(label,0,2,0,key=chosen['code']+label))
        st.metric('Practice score',str(sum(scores))+' / 8')
        st.caption('0 = missing or unsupported · 1 = correct concept · 2 = mechanism plus evidence')
        st.write('Continue with '+chosen['path']+'/INTERVIEW.md and EXERCISES.md.')
    st.divider()
    st.caption('Local labs work without API keys. Optional account operations are identified in each project. Validation details: docs/VALIDATION.md.')

if __name__=='__main__':main()
