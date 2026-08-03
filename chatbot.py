
from operator import itemgetter

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnableParallel

from prompt import (
    programming_prompt,
    math_prompt,
    general_prompt,
    summary_prompt,
    keywords_prompt,
)

from schema import ChatResponse

load_dotenv()




llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
   
)

parser = StrOutputParser()

structured_llm = llm.with_structured_output(ChatResponse)


def detect_category(question: str) -> str:
    q = question.lower()

    programming_keywords = [
        "python", "java", "c++", "code", "program",
        "algorithm", "bug", "html", "css",
        "javascript", "sql", "api", "function"
    ]

    math_keywords = [
        "math", "solve", "equation", "integral",
        "derivative", "matrix", "probability",
        "statistics", "algebra", "geometry"
    ]

    if any(word in q for word in programming_keywords):
        return "Programming"

    if any(word in q for word in math_keywords):
        return "Mathematics"

    return "General"


branch = RunnableBranch(

    (
        lambda x: detect_category(x["question"]) == "Programming",
        programming_prompt | llm | parser,
    ),

    (
        lambda x: detect_category(x["question"]) == "Mathematics",
        math_prompt | llm | parser,
    ),

    general_prompt | llm | parser,
)


parallel = RunnableParallel(

    answer=RunnableLambda(lambda x: x["answer"]),

    summary=(
        summary_prompt | llm | parser
    ),

    keywords=(
        keywords_prompt | llm | parser
    ),
)


def chat(question: str):

    category = detect_category(question)

    answer = branch.invoke(
        {
            "question": question
        }
    )

    parallel_result = parallel.invoke(
        {
            "answer": answer
        }
    )

    structured = structured_llm.invoke(
        f"""
Generate a structured response.

Category:{category}

Answer:{parallel_result["answer"]}

Summary:{parallel_result["summary"]}

Keywords:{parallel_result["keywords"]}

Confidence:
Return a value between 0 and 1.
"""
    )

    return structured