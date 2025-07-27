import streamlit as st
from prompt_functions import prompt_creator, prompt_to_answer, ans_summarizer

st.title("IAS Mains Answer Generator")


qn_prompt = st.text_area("Enter the question")
ans = prompt_creator(qn_prompt)

prompt_ans = {}
for i in ans:
    prompt_ans[i] = prompt_to_answer(ans[i])

steps = ""
prompt_answers = ""
for i in prompt_ans:
    steps += i
    steps += "\n"
    prompt_answers += prompt_ans[i]
    prompt_answers += "\n\n"

final_ans = ans_summarizer(prompt_answers, steps, qn_prompt)
st.write(final_ans)
