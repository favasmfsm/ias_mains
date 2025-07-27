import streamlit as st
from prompt_functions import prompt_creator, prompt_to_answer, ans_summarizer


st.title("IAS Mains Answer Generator")

# Text area for question input
qn_prompt = st.text_area(
    "Enter the question", height=150, placeholder="Type your IAS Mains question here..."
)

# Button to generate answer
if st.button("Generate Answer", type="primary", use_container_width=True):
    if qn_prompt.strip():
        with st.spinner("Generating your answer..."):
            # Generate the answer
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

            # Display the answer in a nice format
            st.success("Answer generated successfully!")
            st.markdown("### Generated Answer:")
            st.write(final_ans)
    else:
        st.error("Please enter a question before generating an answer.")
