import os
from apikey import apikey

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SimpleSequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper
os.environ['OPENAI_API_KEY'] = apikey
import streamlit as st
from langchain.llms import OpenAI
st.title('🦜🔗  GPT Creator')
prompt = st.text_input('Plug in ur prompt here')
# prompt templates 
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'], 
    template='write me a youtube video script based on this title TITLE: {title} while leveraging this wikipedia reserch:{wikipedia_research} '
)
#llms
# show stuff to the screen if there is a prompt 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm,prompt=title_template,verbose=True)
script_chain = LLMChain(llm=llm,prompt=script_template,verbose=True)
wiki = WikipediaAPIWrapper()


if prompt:
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title,wikipedia_research=wiki_research)
    st.wrtie(title)
    st.wrtie(script)

    with st.expander('Title History'):
        st.info(title_memory.buffer)
    with st.expander('Script History'):
        st.infor(script_memory.buffer)
    with st.expander('Wikipedia Research'):
        st.info(wiki_research)









