## How to setup FastPAI project using uv

1. Create a Folder ---> Navigate to it
2. Run `uv init`
3. Run `uv add fastapi --extra standard`
4. Create an app folder in root
5. move `main.py` file to `app/main.py`

```
├── .venv/
├── app/
│   └── main.py       <---- Here
├── .python-version
├── pyproject.toml
├── uv.lock
└── README.md
```

6. Write simple fastapi code
7. Run `uv run fastapi dev`
