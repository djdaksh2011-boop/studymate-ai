import streamlit as st
from src.engine import summarize,keywords,flashcards,quiz,study_plan
st.set_page_config(page_title='StudyMate AI',page_icon='🎓',layout='wide')
st.markdown('''<style>.block-container{max-width:1100px;padding-top:2rem}h1{color:#6655dc}div[data-testid="stMetric"]{background:#f2f0ff;padding:14px;border-radius:14px}</style>''',unsafe_allow_html=True)
st.title('🎓 StudyMate AI')
st.caption('Privacy-friendly, offline NLP study toolkit | No API key required')
st.info('Demo uses transparent extractive NLP, not a generative LLM. Results should be checked against original notes.')
tab1,tab2,tab3=st.tabs(['📚 Notes intelligence','🧠 Practice lab','🗓️ Study planner'])
with tab1:
    uploaded=st.file_uploader('Upload a .txt file',type=['txt'])
    default='Machine learning is a branch of artificial intelligence that enables computers to learn from data. Supervised learning uses labeled training data to predict outcomes. Unsupervised learning discovers patterns in unlabeled data. Classification predicts discrete categories, while regression predicts continuous values. Model evaluation measures performance on unseen examples.'
    notes=st.text_area('Paste your notes',value=uploaded.getvalue().decode('utf-8',errors='replace') if uploaded else default,height=190)
    c1,c2,c3=st.columns(3)
    c1.metric('Words',len(notes.split()));c2.metric('Key concepts',len(keywords(notes)));c3.metric('Flashcards',len(flashcards(notes)))
    if st.button('Analyze notes',type='primary'):
        st.subheader('Key points')
        for x in summarize(notes):st.write('•',x)
        st.subheader('Keywords');st.write(', '.join(keywords(notes)))
        st.download_button('Download summary', '\n'.join(summarize(notes)),file_name='summary.txt')
with tab2:
    st.subheader('Flashcards')
    cards=flashcards(notes)
    if not cards:st.warning('For flashcards, include definitions such as “Photosynthesis is ...”.')
    for i,c in enumerate(cards,1):
        with st.expander(f'{i}. {c["question"]}'):st.write(c['answer'])
    st.subheader('Fill-in-the-blank quiz')
    questions=quiz(notes)
    if not questions:st.warning('Add longer sentences to generate practice questions.')
    for i,q in enumerate(questions,1):
        st.write(f'{i}. {q["question"]}')
        with st.expander('Reveal answer'):st.code(q['answer'])
with tab3:
    topics=st.text_area('Topics (comma separated)','Python, Data Structures, Mathematics, AI fundamentals')
    days=st.slider('Number of days',1,30,7)
    plan=study_plan(topics,days)
    st.dataframe(plan,use_container_width=True,hide_index=True)
    st.download_button('Download plan (CSV)','day,focus,activity\n'+'\n'.join(f'{p["day"]},{p["focus"]},{p["activity"]}' for p in plan),file_name='study_plan.csv')
st.divider();st.caption('StudyMate AI | Educational prototype | No external data transfer')
