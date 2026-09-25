# 🔬 ResearchNexus

### Multi-Agent AI Research Assistant

ResearchNexus is an AI-powered research assistant that uses a **multi-agent architecture** to transform a research question into a structured, evidence-based research report.

The system autonomously searches the web, collects relevant information, analyzes the collected material, generates a research report, evaluates the report using a critic agent, and revises the report when necessary.

Built with **Python, LangGraph, LangChain, Hugging Face, Tavily, BeautifulSoup, and Streamlit**.

---

## ✨ Features

- 🔎 **Automated Web Research**
  - Searches the web using Tavily.
  - Collects relevant sources and URLs.
  - Extracts webpage content using BeautifulSoup.

- 🧠 **AI Research Analysis**
  - Identifies key findings.
  - Extracts important evidence.
  - Detects agreements and conflicts between sources.
  - Identifies research gaps and uncertainties.

- ✍️ **AI Report Generation**
  - Generates structured research reports.
  - Produces executive summaries, findings, analysis, conclusions, and sources.
  - Uses the collected research rather than relying solely on model knowledge.

- 🔍 **AI Critic Agent**
  - Evaluates generated reports.
  - Checks accuracy, relevance, completeness, evidence, consistency, and clarity.
  - Identifies unsupported or overstated claims.

- 🔄 **Self-Revision Loop**
  - Critic feedback is passed back to the Writer Agent.
  - The Writer revises the report.
  - The workflow supports bounded revision cycles.

- 🧩 **LangGraph Orchestration**
  - Uses shared state between agents.
  - Supports conditional routing.
  - Allows the workflow to loop between Writer and Critic.

- 🖥️ **Streamlit Interface**
  - Interactive research interface.
  - Research progress indicators.
  - Final report visualization.
  - Source inspection.
  - Critic feedback and analyst findings.
  - Markdown report download.

---

# 🏗️ Architecture

ResearchNexus follows a multi-agent workflow orchestrated using **LangGraph**.

```text
                         ┌─────────────────────┐
                         │      User Query     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Research Agent    │
                         │                     │
                         │ Tavily Search       │
                         │ BeautifulSoup       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │   Analyst Agent     │
                         │                     │
                         │ Findings            │
                         │ Evidence            │
                         │ Conflicts           │
                         │ Research Gaps       │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Writer Agent     │
                         │                     │
                         │ Generate Report     │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Critic Agent     │
                         │                     │
                         │ Accuracy            │
                         │ Relevance           │
                         │ Completeness        │
                         │ Evidence            │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    Decision Node    │
                         └──────────┬──────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                    ▼                               ▼
             Revision Required                  Approved
                    │                               │
                    ▼                               ▼
             ┌─────────────┐                ┌──────────────┐
             │    Writer   │                │ Final Report │
             │   Revision  │                └──────────────┘
             └─────────────┘


Agent Workflow:

User
  │
  ▼
Research Agent
  │
  ▼
Analyst Agent
  │
  ▼
Writer Agent
  │
  ▼
Critic Agent
  │
  ▼
Decision Node
  │
  ├── APPROVED ───────────────► Final Report
  │
  └── REVISION_REQUIRED ──────► Writer Agent             