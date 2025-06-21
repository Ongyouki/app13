# 1. Clone the repo

# 2. Install uv (if not already installed)

curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Create the virtual environment

uv venv

# 4. Install all project dependencies

uv pip install

# 5. Run the app (example for FastAPI)

uv run uvicorn app.main:app --reload
