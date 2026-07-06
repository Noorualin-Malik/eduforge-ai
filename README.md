# 🎓 EduForge
### AI-Powered Multi-Agent Learning Assistant

> Transform any learning goal into a personalized roadmap, curated resources, interactive quizzes, and expert feedback using an AI-powered multi-agent system.

---

## 🚀 Overview

Learning a new skill often requires searching through countless articles, videos, roadmaps, and tutorials. Beginners frequently struggle with information overload and lack a structured learning path.

**EduForge** solves this problem by orchestrating multiple AI agents that collaborate to design a complete, personalized learning experience from a single user prompt.

Built with **LangGraph**, **Google Gemini 2.5 Flash**, **Tavily Search**, and **Streamlit**, EduForge demonstrates how AI agents can work together to perform planning, research, assessment, and evaluation in a real-world educational application.

---

# ✨ Key Features

✅ Multi-Agent Architecture powered by LangGraph

✅ Personalized learning roadmaps

✅ Real-time web research using Tavily Search

✅ AI-generated quizzes with explanations

✅ Automated quality evaluation and feedback

✅ Structured JSON communication between agents

✅ Professional Streamlit interface

✅ Optional ChromaDB memory

✅ Modular and scalable codebase

---

# 🧠 Why EduForge?

Unlike traditional AI chatbots that generate a single response, EduForge decomposes the learning process into specialized AI agents.

Each agent focuses on a specific responsibility, resulting in more accurate, structured, and reliable outputs.

Instead of asking:

> "Teach me AI"

Users receive:

- 📅 12-week roadmap
- 🎯 Learning objectives
- 📚 Curated learning resources
- 💡 Recommended projects
- 📝 Knowledge assessment
- 📊 AI-generated evaluation
- ✅ Actionable improvement suggestions

---

# 🏗️ Multi-Agent Architecture

```
                     User
                       │
                       ▼
               🎯 Orchestrator
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
   Planner       Researcher        Quiz Agent
       │               │               │
       └───────────────┼───────────────┘
                       ▼
               Evaluator Agent
                       │
                       ▼
              Supervisor Agent
                       │
                       ▼
                 Final Learning Package
```

---

# 🤖 AI Agents

## 🎯 Planner Agent

Designs a personalized learning roadmap including:

- Weekly schedule
- Learning objectives
- Estimated duration
- Difficulty level

---

## 🔍 Research Agent

Uses Tavily Search to gather:

- Latest learning resources
- Official documentation
- GitHub repositories
- Books
- Courses
- Best practices

---

## 📝 Quiz Agent

Generates assessment quizzes to reinforce learning.

Includes:

- Multiple-choice questions
- Correct answers
- Explanations

---

## 📊 Evaluator Agent

Reviews the generated learning plan and provides:

- Overall score
- Strengths
- Weaknesses
- Improvement suggestions

---

## 🛡️ Supervisor Agent

Validates the complete workflow before delivering the final response.

---

# ⚙️ Technology Stack

| Technology | Purpose |
|------------|---------|
| LangGraph | Multi-Agent Workflow |
| Google Gemini 2.5 Flash | Reasoning & Content Generation |
| Tavily Search | Real-Time Web Research |
| Streamlit | User Interface |
| Pydantic | Structured State Management |
| ChromaDB | Optional Memory |
| Python 3.11 | Core Language |

---

# 📂 Project Structure

```
EduForge/
│
├── agents/
│   ├── orchestrator.py
│   ├── planner.py
│   ├── researcher.py
│   ├── quiz.py
│   ├── evaluator.py
│   └── supervisor.py
│
├── prompts/
├── tools/
├── utils/
├── tests/
│
├── app.py
├── graph.py
├── state.py
├── config.py
├── requirements.txt
└── README.md
```

---

# 🔄 Workflow

```
User Input

↓

Planner Agent

↓

Research Agent

↓

Quiz Agent

↓

Evaluator Agent

↓

Supervisor Agent

↓

Final Learning Package
```

---

# 🖥️ Sample Output

Given the prompt:

```
AI in 3 Months
```

EduForge generates:

- 🎯 Learning Objectives
- 📅 Weekly Learning Plan
- 📚 Curated Study Notes
- 🚀 Practical Projects
- 📝 Interactive Quiz
- 📊 Performance Evaluation
- 💬 Personalized Feedback

---

# 📸 Screenshots

> *(Add screenshots here)*

### Home Screen

![Home](assets/home.png)

### Generated Roadmap

![Roadmap](assets/roadmap.png)

### Quiz

![Quiz](assets/quiz.png)

### Evaluation

![Evaluation](assets/evaluation.png)

---

# 🚀 Installation

```bash
git clone https://github.com/yourusername/EduForge.git

cd EduForge

python -m venv .venv

pip install -r requirements.txt

streamlit run app.py
```

---

# 🔑 Environment Variables

```
GOOGLE_API_KEY=your_key

TAVILY_API_KEY=your_key
```

---

# 🧪 Running Tests

```
pytest
```

---
<<<<<<< HEAD

# 🎯 Future Improvements

- Multi-language support
- Voice interaction
- PDF learning plans
- Flashcard generation
- Progress tracking dashboard
- Learning analytics
- RAG-powered document ingestion
- Adaptive learning recommendations

---

# 💡 Why This Project Matters

EduForge demonstrates how multiple AI agents can collaborate to solve a real-world educational challenge.

Rather than relying on a single LLM response, specialized agents plan, research, assess, evaluate, and validate the learning experience, producing structured, high-quality educational content.

This project showcases practical applications of:

- Agentic AI
- LangGraph
- Prompt Engineering
- Tool Calling
- State Management
- LLM Orchestration
- AI-assisted Education

---

# 👩‍💻 Built For

🏆 Kaggle × Google AI Agents Intensive Capstone Project

Developed to demonstrate production-ready multi-agent systems using modern LLM orchestration techniques.
=======
>>>>>>> 92b2fe0dfd7177d569893e4f3729f1ab882a5f1f
