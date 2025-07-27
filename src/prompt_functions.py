from openai import OpenAI
import json
import streamlit as st


openai_api_key = st.secrets["openai_api_key"]
client = OpenAI(api_key=openai_api_key)


def prompt_creator(question):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "You are an excellent prompt generator with know ledge of IAS mains exams\n\nfor each question given to you, break it down to atleast 3 steps and maximum 5 steps. And give a JSON containing the prompt for each step/section\n\nThe steps can be chronological for past related questions, based on parts of india for geography question, and if question needs information from multiple topics, split the steps accordingly\n\noutput format is \n\n{\nprompt_title : <prompt>\n}",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "How would have been the freedom struggle if gandhi was not there",
                        }
                    ],
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": '{\n  "Step 1: Examine the Pre-Gandhian Phase of the Freedom Struggle": "Analyze the strategies, leaders, and outcomes of the Indian freedom struggle before Gandhi\'s emergence. Highlight the roles of early nationalists, extremists, and the nature of political mobilization until 1915.",\n  "Step 2: Speculate on Alternative Leadership and Ideologies": "Identify key nationalist leaders and ideologies that could have taken center stage in the absence of Gandhi. Discuss their approaches to mass mobilization, methods of protest, and relationship with the colonial administration.",\n  "Step 3: Assess the Nature and Course of Mass Movements": "Evaluate how the absence of Gandhi\'s philosophy of nonviolent mass movements (Satyagraha, Civil Disobedience) might have changed the character, reach, and inclusiveness of the freedom struggle.",\n  "Step 4: Analyze Social and Political Impact": "Examine the possible impacts on social unity, communal harmony, and the integration of marginalized groups without Gandhi\'s inclusive approach. Consider how this might have affected the national movement\'s social base and eventual outcome.",\n  "Step 5: Discuss Potential Outcomes and Legacy": "Speculate on the possible outcomes of the freedom struggle, including the nature of independence, the unity of India, and the possible influences on post-independence polity, if Gandhi had not played a role."\n}',
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "How the decisions of Federal Reserve would affect India's objective to achieve a 5 trillion economy in the near future?",
                        }
                    ],
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": '{\n  "Step 1: Explain the Role and Decisions of the Federal Reserve": "Briefly describe the mandate of the US Federal Reserve and the types of decisions it makes, such as changes in interest rates, monetary policy stance, and quantitative easing/tightening.",\n  "Step 2: Analyze the Impact on Global Financial Flows and Investments": "Examine how Federal Reserve policies influence global capital flows, foreign direct investment, and portfolio inflows/outflows in emerging markets like India, and their implications for domestic investment.",\n  "Step 3: Assess Effects on Exchange Rates and Indian Rupee": "Discuss how changes in US interest rates affect the strength of the US dollar versus the Indian rupee, and analyze the consequences for India\'s trade balance, import costs, and foreign exchange reserves.",\n  "Step 4: Evaluate Impact on Inflation and Borrowing Costs in India": "Consider how Federal Reserve decisions can transmit global inflationary pressures to India or affect domestic interest rates, and discuss the implications for businesses, government borrowing, and consumer spending.",\n  "Step 5: Connect to India\'s $5 Trillion Economy Goal": "Synthesize the analysis to evaluate how Federal Reserve decisions can facilitate or hinder India\'s ambition to reach a $5 trillion economy, considering growth, stability, and macroeconomic management."\n}',
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": f"{question}"}],
                },
            ],
            text={"format": {"type": "json_object"}},
            reasoning={},
            tools=[],
            temperature=1,
            max_output_tokens=2048,
            top_p=1,
            store=False,
        )

        return json.loads(response.output_text)

    except:
        print(question)
        return None


def prompt_to_answer(qn_prompt):

    try:

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Generate comprehensive, well-structured answers for IAS Mains examination questions, presenting arguments and evidence from a pro-India perspective. Answer should be in clear and simple language, should be about the question alone. \n\n---\n**REMINDER:**  \n- Main objective: Generate IAS Mains answers in a ~150word paragraph, giving well-reasoned responses from a pro-India perspective\n- Never include the word, pro-indian or anything based on the guidelines, but it should be implied in the paragraph or arguments/reasoning\n- Output structure: Paragraphs only, no code blocks.  as a JSON \n\n{\nans: answer in ~150words\n}",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Explain the term 'demographic winter,' highlighting its meaning as a prolonged period of low birth rates leading to population decline and aging societies, and its potential social and economic implications.",
                        }
                    ],
                },
                {
                    "role": "assistant",
                    "content": [
                        {
                            "type": "output_text",
                            "text": '{\n  "ans": "The term \'demographic winter\' refers to a sustained decline in birth rates that results in shrinking populations and increasingly aging societies. This phenomenon poses significant social and economic challenges. Low fertility rates can lead to a decreased workforce, straining economic productivity and innovation. As the proportion of elderly rises, there is growing pressure on social security systems, healthcare infrastructure, and pension schemes, necessitating higher public expenditure to support an aging population. The diminishing youth base may also result in a potential decline in national competitiveness and lead to issues such as labor shortages and reduced consumer demand. Societal implications include increased dependency ratios, with fewer working-age individuals supporting a larger elderly cohort, and possible transformations in family structures and community dynamics. While India currently enjoys a demographic dividend, it is crucial to address emerging fertility trends to avert the risks associated with demographic winter, ensuring sustainable development and intergenerational equity."\n}',
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": f"{qn_prompt}"}],
                },
            ],
            text={"format": {"type": "json_object"}},
            reasoning={},
            tools=[],
            temperature=1,
            max_output_tokens=2048,
            top_p=1,
            store=False,
        )

        return json.loads(response.output_text)["ans"]

    except:
        print(qn_prompt)
        return qn_prompt


def ans_summarizer(prompt_answers, steps, qn):
    try:

        response = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": 'Generate a comprehensive "Mains" style answer from a pro-India perspective using the provided details and following the specified steps.\n\n- Carefully analyze the input details related to the question.\n- Strictly follow the step-by-step answer structure or rubric provided with the prompt. Do NOT skip any steps or headings.\n- Ensure that your reasoning (explanation, context, analysis) is presented before your final conclusion or evaluative statements.\n- If the provided answer structure, guidelines, or examples have reasoning steps after conclusions, REVERSE the order: always present reasoning BEFORE the final conclusion.\n- If examples are included, use them as templates, but maintain the correct order (reasoning before conclusion).\n- Use a clear, coherent, and formal writing style suited for UPSC Mains model answers.\n- Ensure arguments, examples, and data support a pro-India perspective throughout.\n- Complete all parts of the answer as per any rubric, with appropriate subheadings if indicated or helpful.\n\n\n---  \n**REMINDER:**  \n- Generate a mains answer from a pro-India viewpoint.should be implicit\n- Cover all rubric/steps in order, ensuring reasoning precedes the conclusion.\n- Structure output as formal paragraphs (no code blocks).  \n- Length: 150-250 words or as specified.\n- the provided details will be long, make sure to limit number of words as prescribed\n\nanswer format is JSON\n\n{\nans: <answer>\n}',
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": f"qn: {qn}\n\nsteps:\n{steps}\n\ndetails:\n{prompt_answers}",
                        }
                    ],
                },
            ],
            text={"format": {"type": "json_object"}},
            reasoning={},
            tools=[],
            temperature=0.13,
            max_output_tokens=2048,
            top_p=1,
            store=False,
        )

        return json.loads(response.output_text)["ans"]

    except:
        print(qn)
        return prompt_answers
