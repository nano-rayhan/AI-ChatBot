# 🤖 LangChain Chatbot using RunnableBranch & RunnableParallel

## Project Overview

This project is an AI-powered chatbot developed using the latest LangChain APIs. It demonstrates the implementation of:

* PromptTemplate
* RunnableBranch
* RunnableParallel
* Pydantic Structured Output
* Streamlit Chat Interface
* Google Gemini LLM

The chatbot automatically detects the user's query category (Programming, Mathematics, or General), selects the appropriate prompt using RunnableBranch, generates multiple outputs in parallel using RunnableParallel, validates the final response with a Pydantic schema, and displays the results in a Streamlit web application.

---

# Features

* Latest LangChain APIs
* Google Gemini Integration
* PromptTemplate-based Prompt Engineering
* RunnableBranch for intelligent routing
* RunnableParallel for concurrent response generation
* Pydantic Structured Output
* Streamlit Chat UI
* Chat History
* Secure API Key Management using `.env`

---

# Project Structure

```text
langchain-chatbot/
│
├── app.py
├── chatbot.py
├── prompts.py
├── schemas.py
├── requirements.txt
├── .env.example
├── README.md
└── assets/
```

---

# RunnableBranch Implementation

The chatbot first determines the user's question category.

### Programming

Uses the Programming PromptTemplate.

### Mathematics

Uses the Mathematics PromptTemplate.

### General

Uses the General Assistant PromptTemplate.

This routing is implemented using LangChain's RunnableBranch.

---

# RunnableParallel Implementation

After generating the main answer, RunnableParallel simultaneously generates:

* Summary
* Keywords

This improves efficiency by executing multiple chains concurrently.

---

# Pydantic Structured Output

The chatbot validates every response using the following schema:

* answer
* summary
* confidence
* category
* keywords

This ensures a consistent and structured response format.

---

# Technologies Used

* Python 3.12+
* LangChain
* LangChain Core
* LangChain Google GenAI
* Google Gemini
* Streamlit
* Pydantic
* python-dotenv

---

# Installation

Clone the repository:

```bash
git clone https://github.com/nano-rayhan/AI-ChatBot.git
```

Move into the project directory:

```bash
cd langchain-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

# Example Workflow

User Question

↓

RunnableBranch

↓

Programming / Mathematics / General Prompt

↓

RunnableParallel

↓

Answer + Summary + Keywords

↓

Pydantic Structured Output

↓

Streamlit Chat UI

---

# Future Improvements

* Conversation Memory
* RAG with PDF Support
* Voice Input
* Image Understanding
* Multi-language Support

---


# Author

**Md Rayhan**

B.Sc. in Computer Science & Engineering

---

# License

This project is developed for educational purposes.
