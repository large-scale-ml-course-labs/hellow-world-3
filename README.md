# hellow-world-3

Your third lab. Goal: make the program print **`hellow world 3`** and submit the
result as a Pull Request. An automated check will grade it.

## Steps

1. **Fork** this repository to your own GitHub account (the **Fork** button,
   top-right).
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/hellow-world-3.git
   cd hellow-world-3
   ```
3. Open `print.py` and replace `# your code here` so the program prints exactly:
   ```
   hellow world 3
   ```
   i.e.
   ```python
   print("hellow world 3")
   ```
4. Run it and save the output to `output.txt`:
   ```bash
   python print.py > output.txt
   ```
5. Commit **both** `print.py` and `output.txt` on a new branch and push:
   ```bash
   git checkout -b solution
   git add print.py output.txt
   git commit -m "solution"
   git push -u origin solution
   ```
6. Open a **Pull Request** from your fork's `solution` branch to this repository's
   `main` branch.

## Grading

A GitHub Action runs automatically on your PR and checks `output.txt`:

- ✅ **green check** → your answer is correct.
- ❌ **red cross** → open the check's log to see what was expected vs. what you
  submitted, fix it, and push again (the PR updates automatically).
