# Python Workspace

Everything you build lives here. One folder per week, one repo at the end.

```
python/
  week-01/
    README.md
    exercises.py
    test_exercises.py
```

## How to run a file

Open a terminal in this folder and run:

```powershell
python week-01\exercises.py
```

## How to run the Week 1 tests

```powershell
python week-01\test_exercises.py
```

You'll see failures until you finish each function. That's the point — the tests tell you what
"done" means.

## How to make your first virtual environment (Week 2)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install requests
```

If PowerShell blocks the activation script, run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Rules

- Write code yourself. Don't paste answers from an AI without typing them out and understanding
  each line.
- Commit every day.
- If you're stuck for more than 20 minutes, ask me with the exact error message.
