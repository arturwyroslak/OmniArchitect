# OmniArchitect 🏗️🧠

**OmniArchitect** is a next-generation AI development platform that synthesizes entire full-stack applications from high-level descriptions.

Inspired by **OpenUI** (for real-time UI generation), **GraphRAG** (for structured knowledge context), and **Agentic Workflows**, OmniArchitect bridges the gap between visual design and backend logic.

## 🚀 Key Features

- **Knowledge Graph Requirements**: Unlike standard code generators that "guess", OmniArchitect first builds a Knowledge Graph (Neo4j/NetworkX) of your domain entities and their relationships.
- **Graph-Guided UI Generation**: The UI is not just hallucinated; it is grounded in the entity graph, ensuring that every form field corresponds to a database column.
- **Self-Correcting Agents**: A swarm of agents (Architect, Frontend Dev, Backend Dev) collaborate to write code, using the graph as the single source of truth.

## 🛠️ Architecture

1.  **Input Layer**: User describes the app (e.g., "A CRM for a Dentist").
2.  **Cognitive Layer (The Brain)**:
    *   **GraphBuilder**: Extracts entities (e.g., `Patient`, `Appointment`) and relationships (`Patient HAS Appointment`).
    *   **SpecGenerator**: Creates an OpenAPI spec derived from the graph.
3.  **Generation Layer (The Hands)**:
    *   **UI Synthesizer**: Generates React/Tailwind components mapping to the spec.
    *   **Backend Synthesizer**: Generates FastAPI routes and Pydantic models.

## 📦 Tech Stack

- **Core**: Python 3.10+
- **API**: FastAPI
- **AI Orchestration**: LangChain / LangGraph
- **Graph DB**: NetworkX (in-memory for demo), compatible with Neo4j.
- **Frontend**: Generated React + Tailwind CSS.

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- OpenAI API Key (or compatible)

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/OmniArchitect.git
   cd OmniArchitect
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn openai networkx pydantic
   ```

3. Run the Core Server:
   ```bash
   python backend/main.py
   ```

4. Open the interface:
   Open `frontend/index.html` in your browser.

## 💡 Usage

1. Enter a prompt: *"Create a kanban board for tracking software bugs."*
2. Watch as OmniArchitect:
   - Identifies entities (`Bug`, `Status`, `User`).
   - Builds a dependency graph.
   - Generates the `Bug` Pydantic model.
   - Generates a React component for the Kanban column.

## 📄 License

MIT
