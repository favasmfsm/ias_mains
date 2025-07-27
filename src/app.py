import streamlit as st
import csv
import os
from datetime import datetime
from prompt_functions import prompt_creator, prompt_to_answer, ans_summarizer


def log_to_csv(question, prompt_ans, final_ans):
    """Log the question and answers to a CSV file"""
    csv_file = "data/question_logs.csv"

    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Check if file exists to determine if we need to write headers
    file_exists = os.path.exists(csv_file)

    # Prepare data for logging
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Convert prompt_ans dict to string for CSV storage
    prompt_ans_str = ""
    for step, answer in prompt_ans.items():
        prompt_ans_str += f"{step}: {answer}\n\n"

    # Write to CSV
    with open(csv_file, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write headers if file is new
        if not file_exists:
            writer.writerow(["Timestamp", "Question", "Prompt_Answers", "Final_Answer"])

        # Write the data
        writer.writerow([timestamp, question, prompt_ans_str, final_ans])


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

            # Log the question and answers to CSV
            log_to_csv(qn_prompt, prompt_ans, final_ans)

            # Display the answer in a nice format
            st.success("Answer generated successfully!")
            st.markdown("### Generated Answer:")
            st.write(final_ans)
    else:
        st.error("Please enter a question before generating an answer.")
