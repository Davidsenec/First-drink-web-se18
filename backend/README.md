# First Drink - Party Check-In API Backend

Welcome to the backend project for **First Drink**! This API is built using **FastAPI** (Python 3.12+) and **PostgreSQL** as our primary database.

To make package management and virtual environments fast and reliable, we use a modern tool called **`uv`**.

---

## 🛠️ Prerequisites

Before you start, make sure you have the following installed on your machine:
1. **Python 3.12+**
2. **`uv`** (Astral's fast Python package manager)
   * **WSL / Linux / macOS:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
   * **Windows (PowerShell):** `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
3. **Docker & Docker Desktop**
   * *For WSL Devs:* You must enable "WSL integration" in Docker Desktop Settings -> Resources so WSL can access the Docker engine.
   * *For Native Windows Devs:* No extra settings are needed.


---

## 🚀 First-Time Setup

Follow these steps to set up your local development environment:

### 1. Configure Environment Variables
Copy the template environment file to create your local `.env` configuration:
```bash
cp .env.example .env
```
*Note: The `.env` file is gitignored. Never commit your `.env` file to version control.*

### 2. Create the Virtual Environment
Create an isolated virtual environment (`.venv`) inside the backend folder:
```bash
uv venv
```

### 3. Activate the Environment
You must activate the virtual environment in your terminal session before installing or running code:

* **WSL / Linux / macOS:**
  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell):**
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **Windows (Command Prompt):**
  ```cmd
  .venv\Scripts\activate.bat
  ```
*(Your terminal prompt should now be prefixed with `(.venv)`).*


### 4. Install Dependencies
Sync all required libraries and generate your local environment packages:
```bash
uv sync
```
This reads from `pyproject.toml` and lockfile `uv.lock` to install the exact versions for our team.

---

## 💻 How to Run the App (Choose a Workflow)

### Workflow A: Hybrid Development (Recommended for coding & debugging)
This setup runs the database inside Docker but runs your Python FastAPI code locally. It provides the fastest autocompletion, real-time debugging, and quick reloading:

1. **Start the database in the background:**
   ```bash
   docker compose up db -d
   ```
2. **Start the FastAPI backend locally:**
   ```bash
   uvicorn app.main:app --reload
   ```

---

### Workflow B: Full Container Development (Recommended before merging)
This setup runs both the database and the backend API inside isolated Docker containers, matching our production environment on AWS:

1. **Launch the entire stack:**
   ```bash
   docker compose up --build
   ```
   *(To run in the background instead of streaming logs, add the `-d` flag).*

2. **To stop and wipe database caches (clean reset):**
   ```bash
   docker compose down -v
   ```

---

## 🔗 Useful Endpoints

Once the application is running, open your browser and navigate to:
* **Interactive API docs (Swagger):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **API Healthcheck:** [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

---

## 🗄️ Database Migrations (Alembic)

Whenever you add, remove, or change fields in the SQLAlchemy models (under `app/models/`), you must generate a migration script to update the PostgreSQL tables:

1. **Generate a migration script:**
   ```bash
   alembic revision --autogenerate -m "describe your changes here"
   ```
2. **Apply the migrations to your database:**
   ```bash
   alembic upgrade head
   ```

## 📦 Adding New Dependencies

Since we use `pyproject.toml` and `uv.lock`, **do not edit pyproject.toml manually** to add packages. Instead, use the `uv` command-line tool. This guarantees that your `uv.lock` file stays updated and matching:

* **To add a production dependency:**
  ```bash
  uv add <package-name>
  ```
  *(Example: `uv add passlib`)*

* **To add a development dependency (like formatting or testing tools):**
  ```bash
  uv add --dev <package-name>
  ```
  *(Example: `uv add --dev black`)*

Both commands will automatically update `pyproject.toml`, update `uv.lock`, and install the package inside your local `.venv`. Remember to commit both modified files to Git!

---

## 💡 Best Practices
* **Keep imports clean:** Follow the Controller-Service-Repository (CSR) structure.
* **Use type-hints:** FastAPI and Pydantic rely heavily on type-hinting for automatic validation and document generation.
* **Run tests before pushing:** Run `pytest` to ensure you haven't introduced any regression bugs.


