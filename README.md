# 🤖 AI Learning Portfolio — CS50 AI & Agentic AI Engineering

> **Shikha Sachdeva** · Senior Software Engineering Manager · AI & Cloud Modernization  
> 📍 Austin, TX · [LinkedIn](https://www.linkedin.com/in/shikha-sachdeva-061b2213/) · [GitHub](https://github.com/ShikhaGSachdeva)

---

## About This Repository

This repository documents my hands-on AI engineering journey — from classical AI fundamentals through modern agentic AI systems. With 17+ years of experience leading large-scale engineering programs in healthcare and cloud modernization, I am upskilling into AI engineering to build, govern, and scale intelligent systems.

Each project here is implemented from scratch — no black-box frameworks, no shortcuts. The goal is deep understanding, not surface familiarity.

---

## 🎓 Learning Path

| Course | Institution | Status |
|---|---|---|
| CS50's Introduction to AI with Python | Harvard University | 🟡 In Progress |
| Generative AI with Large Language Models | DeepLearning.AI / Coursera | 🔜 Up Next |
| AI Agents in LangGraph | DeepLearning.AI | 🔜 Planned |
| Complete Agentic AI Engineering | Udemy | 🔜 Planned |
| IBM RAG & Agentic AI Professional Certificate | IBM / Coursera | 🔜 Planned |
| AWS Certified AI Practitioner | Amazon Web Services | 🔜 Planned |
| MIT xPRO: AI Products & Services | MIT | 🔜 Planned |

---

## 📂 Projects

### Week 0 — Search

#### ✅ [Degrees of Separation](./Week0-Search/)

**Concept:** Breadth-First Search (BFS) applied to real-world graph traversal

**Problem:** Given any two actors in Hollywood, find the shortest path connecting them through shared movies — inspired by the Six Degrees of Kevin Bacon game.

**What I built:**
- Implemented `shortest_path()` using BFS via a `QueueFrontier`
- Built path tracing by walking back through parent node pointers
- Handles edge cases: same person, no path exists, duplicate actor names
- Tested on both small (local) and large (thousands of actors) IMDb datasets

**Key concepts applied:**
- Breadth-First Search guarantees shortest path (vs DFS which does not)
- Node structure with state, parent, and action enables full path reconstruction
- Explored set prevents revisiting nodes and infinite loops
- QueueFrontier (FIFO) vs StackFrontier (LIFO) — why the difference matters

**Tech:** Python 3.12 · Graph Search · BFS · IMDb dataset (CSV)

```
$ python degrees.py large
Loading data...
Data loaded.
Name: Emma Watson
Name: Jennifer Lawrence
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

---

### Week 0 — Search *(coming soon)*

#### 🔜 Tic-Tac-Toe — Minimax Algorithm

An AI agent that plays Tic-Tac-Toe optimally using the Minimax adversarial search algorithm. The AI will never lose.

---

### Week 1 — Knowledge *(coming soon)*
### Week 2 — Uncertainty *(coming soon)*
### Week 3 — Optimization *(coming soon)*
### Week 4 — Learning *(coming soon)*
### Week 5 — Neural Networks *(coming soon)*
### Week 6 — Language *(coming soon)*

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Primary language for all CS50 AI projects |
| VS Code | Development environment |
| Git | Version control and CS50 submission |
| LangChain / LangGraph | Planned — agent building projects |
| CrewAI / AutoGen | Planned — multi-agent systems |
| AWS Bedrock | Planned — cloud AI deployment |

---

## 💡 Engineering Background

Before this AI journey, my 17+ years of experience spans:

- **Engineering Leadership** — Led distributed teams of engineers, architects, and delivery managers across large-scale enterprise programs
- **Cloud Modernization** — Drove legacy-to-cloud transformation programs with governance frameworks and delivery alignment
- **Healthcare Systems** — Designed and delivered scalable healthcare technology platforms at enterprise scale
- **Program Execution** — Established execution frameworks, delivery governance, and stakeholder alignment across complex, cross-functional programs

This background gives me a unique lens on AI engineering — I don't just build AI systems, I understand how to scale, govern, and deliver them in production enterprise environments.

---

## 🗺️ Why AI Engineering

The intersection of **large-scale engineering leadership** and **agentic AI** is where I'm headed. Enterprises deploying AI at scale need engineers who understand both the technical depth of how agents work and the operational reality of running them in production. That combination is rare — and it's what I'm building toward.

---

## 📈 Progress Tracker

- [x] Python environment setup (Python 3.12, VS Code, virtual environment)
- [x] CS50 AI Week 0 — Search lecture completed
- [x] Degrees of Separation — BFS implementation submitted
- [ ] CS50 AI Week 0 — Tic-Tac-Toe (Minimax)
- [ ] CS50 AI Week 1 — Knowledge
- [ ] CS50 AI Week 2 — Uncertainty
- [ ] CS50 AI Week 3 — Optimization
- [ ] CS50 AI Week 4 — Learning
- [ ] CS50 AI Week 5 — Neural Networks
- [ ] CS50 AI Week 6 — Language
- [ ] Generative AI with LLMs
- [ ] First LangGraph agent built
- [ ] AWS AI Practitioner certified

---

## 📬 Connect

If you're working on similar AI engineering challenges or want to discuss enterprise AI delivery, I'd love to connect.

[LinkedIn](https://www.linkedin.com/in/) · [GitHub](https://github.com/ShikhaGSachdeva)

---

*Updated: May 2026 · Austin, TX*
