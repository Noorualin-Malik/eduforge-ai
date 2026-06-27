# 🎓 EduForge

EduForge is a production-quality AI-powered educational assistant built with **Streamlit**, **LangGraph**, **Google Gemini 2.5 Flash**, and **Tavily Search**.

It generates personalized learning roadmaps, gathers high-quality learning resources, creates quizzes, evaluates the generated learning plan, and returns a validated final response through a modular multi-agent workflow.

---

# Features

- Multi-agent architecture using LangGraph
- Google Gemini 2.5 Flash for all reasoning tasks
- Tavily Search integration for current learning resources
- Professional Streamlit interface
- Structured JSON outputs
- Modular and maintainable codebase
- Optional ChromaDB memory support
- Type hints throughout
- PEP-8 compliant
- Lightweight architecture without unnecessary infrastructure

---

# Tech Stack

- Python 3.11+
- Streamlit
- LangGraph
- Google Gemini 2.5 Flash
- Google Generative AI SDK
- Tavily Search API
- ChromaDB (optional)
- Pydantic

---

# Project Structure

```text
EduForge/
│
├── app.py
├── graph.py
├── state.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
├── agents/
│   ├── orchestrator.py
│   ├── planner.py
│   ├── researcher.py
│   ├── quiz.py
│   ├── evaluator.py
│   └── supervisor.py
│
├── tools/
│   ├── gemini.py
│   ├── search.py
│   └── memory.py
│
├── prompts/
│   ├── planner.md
│   ├── researcher.md
│   ├── quiz.md
│   └── evaluator.md
│
├── utils/
│   ├── logger.py
│   └── helpers.py
│
└── tests/
    └── test_agents.py
```

---

# Multi-Agent Workflow

```
User
   │
   ▼
Orchestrator
   │
   ▼
Planner
   │
   ▼
Researcher
   │
   ▼
Quiz
   │
   ▼
Evaluator
   │
   ▼
Supervisor
   │
   ▼
Final Output
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/EduForge.git
cd EduForge
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file from `.env.example`.

```env
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Application Workflow

1. User enters a learning topic.
2. Orchestrator initializes the workflow.
3. Planner creates a learning roadmap.
4. Researcher retrieves relevant resources using Tavily Search.
5. Gemini summarizes the resources.
6. Quiz agent generates assessment questions.
7. Evaluator scores the generated content.
8. Supervisor validates the output.
9. Streamlit displays the complete learning package.

---

# Design Principles

- Single Gemini client shared across agents
- Linear LangGraph workflow
- Minimal dependencies
- Modular architecture
- Reusable utility functions
- No circular imports
- No placeholder code
- No complex retry logic
- No Docker
- No FastAPI
- No Redis
- No Celery
- No Kubernetes

---

# Optional Memory

If ChromaDB is configured, EduForge can store generated learning plans for lightweight retrieval.

The application functions normally without persistent memory.

---

# Testing

Run:

```bash
pytest
```

---
