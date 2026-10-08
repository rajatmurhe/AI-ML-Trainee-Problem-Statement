# AI / ML Trainee Problem Statement Submission

**Author:** Rajat Murhe  
**Education:** B.Tech in Computer Science (AI & Machine Learning), VIT Chennai  
**Profiles:** [GitHub Profile](https://github.com/rajatmurhe) | [LinkedIn Profile](https://www.linkedin.com/in/rajat-murhe/) | [Portfolio](https://rajat-murhe.github.io)  
**Email:** [rajatmurhe1@gmail.com](mailto:rajatmurhe1@gmail.com)  

---

This repository contains my complete submissions for both **Problem Statement 1** (REST API ingestion, data visualization, SQLite import, and complex code links) and **Problem Statement 2** (LLM chatbot architecture, self-assessment, and vector database selection).

The in-depth research paper for Problem Statement 2 is also included as a standalone PDF: [`Problem Statement 2/Rajat_Murhe_Assignment2_LLM_VectorDB.pdf`](./Problem%20Statement%202/Rajat_Murhe_Assignment2_LLM_VectorDB.pdf).

---

## Repository Structure

```text
AI-ML-Trainee-Problem-Statement/
├── Problem Statement 1/
│   ├── task1.py                 # REST API book fetching & SQLite storage
│   ├── task2.py                 # Student score analysis & Matplotlib visualization
│   ├── task3.py                 # CSV ingestion with regex validation into SQLite
│   ├── scores.json              # Sample student test score dataset
│   ├── student_scores.png       # Generated score visualization chart
│   ├── users.csv                # Sample user records for CSV import
│   ├── books.db                 # Populated SQLite database (Books)
│   └── users.db                 # Populated SQLite database (Users)
├── Problem Statement 2/
│   └── Rajat_Murhe_Assignment2_LLM_VectorDB.pdf  # 5-page research & architecture report
├── Rajat_Murhe_Assignment2_LLM_VectorDB.pdf      # Root copy for direct accessibility
├── requirements.txt             # Project dependencies (requests, matplotlib)
├── .gitignore                   # Standard ignore patterns
└── README.md                    # Project documentation & solutions overview
```

---

## Quick Setup & Execution

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/rajatmurhe/AI-ML-Trainee-Problem-Statement.git
cd AI-ML-Trainee-Problem-Statement

# Optional: set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 2. Run the Tasks
```bash
# Task 1: Fetch books from REST API & store in SQLite
python3 "Problem Statement 1/task1.py"

# Task 2: Process student test scores & generate chart
python3 "Problem Statement 1/task2.py"

# Task 3: Import and validate user records from CSV to SQLite
python3 "Problem Statement 1/task3.py"
```

---

## Problem Statement 1 Walkthrough

### Task 1: API Data Retrieval & SQLite Storage (`task1.py`)

- **Objective:** Query an external REST API for a list of books, persist the records in a local SQLite database, and display the stored records.
- **API Used:** [OpenLibrary Search API](https://openlibrary.org/search.json) (`https://openlibrary.org/search.json?q={topic}&limit=10`).
- **Implementation Highlights:**
  - Dynamic user prompt for topic (defaults to `"machine learning"` on Enter).
  - Handles variable/missing API fields gracefully (e.g., missing author names default to `"Unknown"`, extracts primary publish year).
  - Creates table `books` with schema:
    ```sql
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT,
        year INTEGER,
        UNIQUE(title, author)
    );
    ```
  - Employs `INSERT OR IGNORE` to make repeated script executions idempotent without duplicate records.
  - Queries and prints the full database catalogue in a readable console format.

**Sample Terminal Output:**
```text
Enter book name or topic (press Enter for 'machine learning'): python
Books found: 10
New books added: 7

Books stored in database
--------------------------------------------------
ID: 1 | Title: Core Python Programming | Author: R. Nageswara Rao | Year: 2016
ID: 2 | Title: Black Hat Python        | Author: Justin Seitz     | Year: 2014
ID: 3 | Title: Fluent Python           | Author: Luciano Ramalho  | Year: 2015
...
```

---

### Task 2: Data Processing & Visualization (`task2.py`)

- **Objective:** Fetch student test score data from an API, compute the class average, and visualize the marks using a bar chart.
- **Implementation Highlights:**
  - Prompts for an API URL, with automatic fallback to the bundled `scores.json` dataset if you press Enter or run offline.
  - Parses the payload, extracts numerical scores, and calculates the arithmetic mean (`round(average, 2)`).
  - Generates a customized Matplotlib bar chart:
    - **Green bars:** Students scoring at or above the class average.
    - **Red bars:** Students scoring below the class average.
    - **Dashed reference line:** Clearly indicates the class average threshold.
  - Automatically saves the high-resolution figure to `student_scores.png`.

**Output Chart:**

![Student Test Scores Chart](./Problem%20Statement%201/student_scores.png)

**Console Summary:**
```text
Student Scores
------------------------------
Aarav   : 76.0
Bhavna  : 91.0
Chirag  : 55.0
Deepika : 83.0
Elan    : 67.0
Farida  : 94.0

Class Average: 77.67
```

---

### Task 3: CSV Data Import to SQLite (`task3.py`)

- **Objective:** Read user records (name, email) from a CSV file, validate the data, and insert the clean records into a local SQLite database.
- **Source Data:** `users.csv` containing comma-separated user rows.
- **Implementation Highlights:**
  - Reads data using `csv.DictReader` and verifies required header columns (`name`, `email`).
  - Strict email format validation via regular expression (`r"^[^@\s]+@[^@\s]+\.[^@\s]+$"`). Skips malformed or empty rows.
  - Creates table `users` with schema:
    ```sql
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    ```
  - Uses `INSERT OR IGNORE` to maintain `UNIQUE` constraint on emails without throwing runtime exceptions.
  - Prints newly added count alongside all currently saved database entries.

**Sample Terminal Output:**
```text
Users added: 5

Users in database
---------------------------------------------
ID: 1 | Name: Ravi Kumar  | Email: ravi@gmail.com
ID: 2 | Name: Priya Shah  | Email: priya@gmail.com
ID: 3 | Name: Arjun Mehta | Email: arjun@gmail.com
ID: 4 | Name: Sneha Patel | Email: sneha@gmail.com
ID: 5 | Name: Karan Singh | Email: karan@gmail.com
---------------------------------------------
```

---

## Links to Most Complex Code Written

As requested in Problem Statement 1, here are links to production repositories showcasing my most complex codebases in Python and Database engineering:

### 1. Most Complex Python Code
* **Project:** **[TradeAlpha — AI Stock Forecasting & Portfolio Optimization](https://github.com/rajatmurhe/TradeAlpha)**  
  * **Core Files:** [`future_prediction_engine.py`](https://github.com/rajatmurhe/TradeAlpha/blob/main/future_prediction_engine.py) & [`dashboard.py`](https://github.com/rajatmurhe/TradeAlpha/blob/main/dashboard.py)  
  * **Why it's complex:** TradeAlpha implements a hybrid quantitative finance pipeline combining **Proximal Policy Optimization (PPO)** reinforcement learning agents with **XGBoost** regression models. The engine engineers technical market indicators (RSI, MACD, Bollinger Bands, ATR), normalizes multi-asset continuous state spaces, trains an RL agent to maximize Sharpe ratio under transaction cost penalties, and delivers multi-horizon forecasting via an interactive Streamlit UI.
* **Alternative LLM System:** **[ClinicVoice AI — Multi-Agent Healthcare Assistant](https://github.com/rajatmurhe/clinicvoice-ai)**  
  * **Core Agent:** [`booking_agent.py`](https://github.com/rajatmurhe/clinicvoice-ai/blob/main/python-agents/agents/booking_agent.py)  
  * **Why it's complex:** Multi-agent conversational system featuring LLM tool calling (Google Calendar API), appointment slot resolution, session memory, dual-sided guardrails, and deterministic fallback logic.

### 2. Most Complex Database Code
* **Project:** **[AI Job Assistant — PostgreSQL + pgvector Migration Schema](https://github.com/rajatmurhe/ai-job-assistant)**  
  * **Core File:** [`0001_initial_schema.py`](https://github.com/rajatmurhe/ai-job-assistant/blob/main/backend/app/db/migrations/versions/0001_initial_schema.py)  
  * **Why it's complex:** A production Alembic migration managing a hybrid relational-and-vector database architecture. It activates PostgreSQL's `pgvector` extension (`Vector(768)` embedding dimensions), structures `JSONB` document stores for parsed resume and job descriptions, handles UUID primary keys, and enforces relational integrity across users, applications, skills, and ATS gap analysis reports.
* **Analytical / Data Warehouse System:** **[Retail Sales ETL Analytics Pipeline](https://github.com/rajatmurhe/Retail-Sales-ETL-Analytics-Pipeline)**  
  * **Core File:** [`analytics.sql`](https://github.com/rajatmurhe/Retail-Sales-ETL-Analytics-Pipeline/blob/main/analytics.sql)  
  * **Why it's complex:** Implements an enterprise Star Schema warehouse (`fact_sales` surrounded by customer, product, and date dimension tables) built with Python/SQLAlchemy and 15+ analytical SQL queries evaluating cohort revenue, rolling transaction volume, and profit margins.

---

## Problem Statement 2 (Assignment 2 Overview)

The complete 5-page research document submitted for Assignment 2 is available as [`Problem Statement 2/Rajat_Murhe_Assignment2_LLM_VectorDB.pdf`](./Problem%20Statement%202/Rajat_Murhe_Assignment2_LLM_VectorDB.pdf). Below is an executive summary of the core sections:

### 1. Self-Assessment

| Area | Rating | Basis of Rating |
| :--- | :---: | :--- |
| **LLM** | **A** | Built multi-agent voice assistants with tool calling & safety layers (*ClinicVoice AI*), and production RAG systems on vector stores (*RAG Intelligence*, *AI Job Assistant*). Worked with Gemini APIs and locally hosted models via Ollama. |
| **Deep Learning** | **A** | Fine-tuned BERT in PyTorch and benchmarked against Random Forest and XGBoost (*NeuroAI*). Designed custom PyTorch detection architecture and training pipelines (*RV Vision 0.1*). |
| **AI** | **A** | Designed agentic workflows with tool use and human-in-the-loop review (*FieldProof AI*); trained reinforcement learning agents using PPO (*TradeAlpha*, indoor navigation). |
| **ML** | **A** | Built Scikit-learn and XGBoost pipelines with cross-validation and hyperparameter search (*CreditX*), paired with SHAP explainability (*NeuroAI*). |

*(Scale: **A** = can code independently; **B** = can code under supervision; **C** = little or no understanding)*

---

### 2. Key Architectural Components of an LLM-Based Chatbot

The LLM is only one piece of an enterprise chatbot; most of the quality, safety, latency control, and operational cost depend on the surrounding architecture.

#### Request Flow Lifecycle:
```text
  [ User ]
     │ (Message / Voice)
     ▼
[ API & Orchestration ] (FastAPI / State Machine Routing)
     │
     ├──► [ Input Guardrails ] ──► (Checks for prompt injection & scope)
     │
     ├──► [ Session Memory ]   ──► (Loads conversation history from Redis / DB)
     │
     ├──► [ Retriever / RAG ]  ──► (Embeds query, searches Vector Store with RBAC filter)
     │
     ▼
[ Prompt Builder ] ────────────► (Combines system instructions, context, history, query)
     │
     ▼
  [ LLM ] ─────────────────────► (Generates response OR requests tool call)
     │
     ├──► [ Tool Layer ]       ──► (Validates permissions, executes DB/API action)
     │
     ▼
[ Output Guardrails ] ─────────► (Validates policy, grounding against context, PII check)
     │
     ▼
[ Streaming Response ] ────────► [ User ] (Answer streamed token-by-token)
     │
     └──► [ Tracing & Logging ] (Logs latency, tokens, cache hits, evaluation metrics)
```

#### Core Design Decisions:
1. **RAG Before Fine-Tuning:** Business knowledge updates frequently. Retrieval enables instant document updates and source attribution without costly retraining cycles.
2. **The Model Proposes, the Backend Decides:** The LLM never writes to external databases directly. It requests a typed tool call, which the backend authenticates, validates, and logs.
3. **Dual-Sided Guardrails:** Input filtering catches prompt injection, but output verification is equally vital to eliminate hallucinated policies or ungrounded claims.
4. **Latency & Cost Optimization:** Token streaming provides immediate perceptual feedback; semantic caching avoids duplicate model calls for frequent queries.

---

### 3. Vector Databases & Technology Selection

#### Understanding Vector Databases
Vector databases store high-dimensional numeric embeddings generated by embedding models. Semantic similarity is quantified via distance metrics—primarily **Cosine Similarity** (comparing vector angles, standard for text) or **Euclidean Distance / Dot Product**.

To handle millions of vectors within interactive response windows (sub-50ms), vector databases use **Approximate Nearest Neighbor (ANN)** indexing algorithms:
- **HNSW (Hierarchical Navigable Small World):** Multi-layered graph traversal; provides high recall and ultra-fast queries at the cost of higher RAM usage.
- **IVF (Inverted File Index):** Clusters vectors into centroids; lower memory footprint and faster build times, with recall dependent on cluster search depth ($n_{\text{probe}}$).
- **Quantization (Product / Scalar):** Compresses vector embeddings into fewer bytes to reduce memory at massive scale.

#### Hypothetical Problem Definition:
*An internal enterprise knowledge assistant for a company answering employee questions from HR policies, engineering docs, contracts, and finance reports across 40 departments (~3 million chunks, growing steadily). Access control is paramount: each query must strictly adhere to the employee's role and departmental permissions.*

#### Candidate Evaluation:

| Candidate | Category | Core Strength | Trade-Off / Limitation |
| :--- | :--- | :--- | :--- |
| **pgvector (Postgres)** | **Relational Extension** | **Single-query RBAC joins, zero data drift, no new infrastructure** | Reaches scaling limits at hundreds of millions of vectors |
| **Qdrant** | Purpose-built Engine | High-speed filtered ANN, native payload filtering | Requires running and syncing a second database cluster |
| **Pinecone** | Fully Managed SaaS | Zero operational overhead, serverless scaling | Ongoing SaaS cost; sensitive company data leaves internal boundary |
| **Milvus** | Distributed Engine | Built for billions of vectors with cluster sharding | Excessive operational complexity for a 3M chunk workload |
| **FAISS / Chroma** | Embedded / Library | Great for local notebooks and offline experimentation | Lacks built-in RBAC, multi-user concurrency, and ACID transactions |

#### Final Decision: **pgvector with HNSW Index**
1. **Unified Access Control:** Permissions and semantic search execute together in a single SQL query joined against existing employee and role tables.
2. **Zero Data Drift:** When documents are modified or permissions revoked, vector embeddings update in the same ACID transaction—preventing data leaks.
3. **Optimal Scale Fit:** 3 million chunks comfortably fit within PostgreSQL's memory and disk capacity with an HNSW index.
4. **Lean Engineering Footprint:** Fits the existing two-person backend team without managing separate vector infrastructure.

```sql
-- Core Query Sketch in pgvector
CREATE INDEX ON chunks USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);

SET hnsw.ef_search = 80;

SELECT id, text, source
FROM chunks
WHERE department_id = ANY(:allowed_departments)
ORDER BY embedding <=> :query_embedding
LIMIT 5;
```

---

## Candidate Information

- **Name:** Rajat Murhe
- **Email:** [rajatmurhe1@gmail.com](mailto:rajatmurhe1@gmail.com)
- **Phone:** +91 75076 61881
- **GitHub:** [https://github.com/rajatmurhe](https://github.com/rajatmurhe)
- **LinkedIn:** [https://www.linkedin.com/in/rajat-murhe/](https://www.linkedin.com/in/rajat-murhe/)
- **Document Attached:** [`Rajat_Murhe_Assignment2_LLM_VectorDB.pdf`](./Problem%20Statement%202/Rajat_Murhe_Assignment2_LLM_VectorDB.pdf)
