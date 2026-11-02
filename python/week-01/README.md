# Week 1 — Python Fundamentals

Ten small functions. Each one teaches exactly one idea you'll reuse forever.

**Run the tests:**

```powershell
python test_exercises.py
```

Red = not done yet. Green = done. Don't move on until all ten pass.

---

## The exercises

### 1. `welcome(name)`
Return a greeting string.

```python
welcome("Steve")  ->  "Welcome, Steve!"
```

**Teaches:** functions, parameters, f-strings.

---

### 2. `player_status(name, health)`
Return a status line.

```python
player_status("Alex", 20)  ->  "Alex: 20 HP"
```

**Teaches:** multiple parameters, f-strings.

---

### 3. `format_time(total_seconds)`
Convert seconds into `MM:SS`. Minutes can go above 59.

```python
format_time(125)   ->  "02:05"
format_time(59)    ->  "00:59"
format_time(3600)  ->  "60:00"
```

**Teaches:** arithmetic, `divmod`, zero-padding with `:02d`.

---

### 4. `check_health(health)`
Return `"Alive"` if health is above 0, otherwise `"You died"`.

```python
check_health(10)  ->  "Alive"
check_health(0)   ->  "You died"
```

**Teaches:** `if / else`, comparison operators.

---

### 5. `count_items(inventory)`
Return how many items are in a list.

```python
count_items(["sword", "pickaxe", "torch"])  ->  3
count_items([])                             ->  0
```

**Teaches:** lists, `len()`.

---

### 6. `apply_damage(health, damage)`
Subtract damage, but health can never go below 0.

```python
apply_damage(20, 7)   ->  13
apply_damage(5, 10)   ->  0
```

**Teaches:** `max()`, thinking about edge cases.

---

### 7. `best_score(scores)`
Return the highest score. Return `None` for an empty list.

```python
best_score([3, 9, 4])  ->  9
best_score([])         ->  None
```

**Teaches:** lists, `max()`, empty-input handling.

---

### 8. `count_blocks(mined)`
Count how many times each block appears.

```python
count_blocks(["dirt", "stone", "dirt"])
->  {"dirt": 2, "stone": 1}
```

**Teaches:** dictionaries, loops, counting patterns.

---

### 9. `save_profile(path, profile)` and `load_profile(path)`
Write a dictionary to a JSON file, then read it back.

```python
save_profile("player.json", {"name": "Alex", "level": 12})
load_profile("player.json")
->  {"name": "Alex", "level": 12}
```

**Teaches:** file I/O, `json`, `with open(...)`.

---

### 10. `safe_int(text)`
Convert text to an integer. If it can't, return `None` instead of crashing.

```python
safe_int("42")   ->  42
safe_int("abc")  ->  None
```

**Teaches:** `try / except`.

---

## Rules

- Type every line yourself. No copy-paste from a chat window.
- If a test fails, read the error. It tells you the line and the reason.
- Stuck for 20+ minutes? Ask me with the exact error and what you tried.
- When all ten pass, `git commit` and start the Clip Idea Tracker project.

---

## If this is too easy

Skip to Week 2 (`PYTHON-PLAN.md`, Phase 1) and build the File Organizer. But still run the tests
once — it costs 30 seconds.
