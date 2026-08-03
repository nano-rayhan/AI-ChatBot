from langchain_core.prompts import PromptTemplate


programming_prompt = PromptTemplate.from_template("""
You are an expert Programming Assistant.

Answer the following programming question clearly.

Question:
{question}

Instructions:
- Explain in simple language.
- Give code examples if necessary.
- Mention best practices.
""")


math_prompt = PromptTemplate.from_template("""
You are an expert Mathematics Tutor.

Solve the following problem.

Question:
{question}

Instructions:
- Show step-by-step solution.
- Explain formulas.
- Keep the explanation easy to understand.
""")


general_prompt = PromptTemplate.from_template("""
You are a helpful AI Assistant.

Answer the following question.

Question:
{question}

Instructions:
- Be accurate.
- Keep the answer concise.
- Use simple language.
""")



summary_prompt = PromptTemplate.from_template("""
Summarize the following answer in 2-3 sentences.

Answer:
{answer}
""")


keywords_prompt = PromptTemplate.from_template("""
Extract the 5 most important keywords from the following text.

Text:
{answer}

Return only the keywords separated by commas.
""")