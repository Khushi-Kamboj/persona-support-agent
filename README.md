# 🎭 Persona-Adaptive Customer Support Agent

An AI-powered customer support system that adapts its response style based on the customer's communication persona while ensuring factual accuracy through Retrieval-Augmented Generation (RAG).

## LIVE URL:
https://persona-support-agent-2xfp.onrender.com/

## 🚀 Project Overview

Traditional customer support chatbots provide generic responses regardless of the user's communication style. This project solves that problem by combining:

* **Persona Classification**
* **Retrieval-Augmented Generation (RAG)**
* **Gemini LLM**
* **ChromaDB Vector Database**
* **Streamlit User Interface**

The system first identifies the user's persona, retrieves relevant support information from a knowledge base, and then generates a response tailored to the user's communication style.

---

## 🎯 Features

### Persona Detection

The system automatically classifies users into one of three categories:

* **Technical Expert**

  * Detailed troubleshooting
  * Technical explanations
  * Step-by-step diagnostics

* **Frustrated User**

  * Empathetic responses
  * Simple instructions
  * Clear guidance

* **Business Executive**

  * Concise summaries
  * Business impact focus
  * Resolution timelines

---

### Retrieval-Augmented Generation (RAG)

The chatbot only answers using information retrieved from the knowledge base.

Supported document formats:

* PDF
* Markdown
* Text Files

Knowledge Base Examples:

* Password Reset Guide
* API Troubleshooting Handbook
* Billing Policy Documentation

---

### Semantic Search

The system uses:

* Gemini Embeddings
* ChromaDB Vector Store
* Cosine Similarity Search

to retrieve the most relevant document chunks before generating responses.

---

### Human Escalation Workflow

The system can flag conversations for escalation when:

* Retrieval confidence is low
* Legal or sensitive issues are detected
* Insufficient information exists in the knowledge base

A structured handoff summary is generated for human agents.

---

## 🏗️ System Architecture

```text
User Query
     │
     ▼
Persona Classification
     │
     ▼
RAG Retrieval Pipeline
     │
     ├── Document Parsing
     ├── Text Chunking
     ├── Embedding Generation
     └── ChromaDB Search
     │
     ▼
Persona-Adaptive Response Generator
     │
     ▼
Customer Response
```

---

## 📂 Project Structure

```text
persona-support-agent/
│
├── data/
│   ├── api_troubleshooting.md
│   ├── billing_policy.txt
│   └── password_reset_guide.pdf
│
├── src/
│   ├── __init__.py
│   ├── classifier.py
│   ├── rag_pipeline.py
│   ├── generator.py
│   ├── escalator.py
│   └── main.py
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Technology Stack

### AI & LLM

* Gemini 2.5 Flash
* Gemini Embedding Model

### Vector Database

* ChromaDB

### Frameworks

* Streamlit
* LangChain

### Utilities

* Python
* PyPDF
* Python Dotenv

---

## 🔄 Workflow

### Step 1: Persona Classification

The user query is classified into:

* Technical Expert
* Frustrated User
* Business Executive

### Step 2: Document Retrieval

Relevant document chunks are retrieved using semantic similarity search.

### Step 3: Response Generation

The system combines:

* User Query
* Persona
* Retrieved Context

to generate a persona-specific response.

### Step 4: Escalation Check

If the issue cannot be safely resolved, the system creates a structured human handoff report.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/persona-support-agent.git
cd persona-support-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 🧪 Example Queries

### Technical Expert

```text
My API authentication is failing with a 401 error.
```

### Frustrated User

```text
I've been trying to reset my password for hours and nothing works.
```

### Business Executive

```text
What is the business impact of this authentication issue?
```

---

## 📈 Future Enhancements

* Multi-turn conversation memory
* Sentiment analysis
* Advanced confidence scoring
* Agentic RAG workflows
* Analytics dashboard
* Multi-language support

---

## 👩‍💻 Author

**Khushi Kamboj**

Final Year B.Tech Computer Science Student

Interests:

* Full Stack Development
* Artificial Intelligence
* Generative AI Applications
* Retrieval-Augmented Generation (RAG)

---

## 📄 License

This project is developed for educational and research purposes.
