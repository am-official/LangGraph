# Run A state contract
## 1. Prerequisites
Python 3.12, a terminal, and a browser. Internet is needed to install dependencies. Local mode needs no account. No API keys are used by this lab.

## 2. Install in this folder
Windows PowerShell:
```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```
macOS/Linux:
```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## 3. Configure the environment
Windows: `Copy-Item .env.example .env`. macOS/Linux: `cp .env.example .env`. Local mode needs no edits. The sample environment intentionally contains no credential requirements.

## 4. Launch
Windows: `.venv\Scripts\python.exe -m streamlit run app.py`

macOS/Linux: `.venv/bin/python -m streamlit run app.py`

Open the address printed by Streamlit. Run from this folder to load its theme. Ctrl+C stops the server. Persisted data, when used, stays in the ignored .local folder.

## 5. Three hands-on runs
1. Input `{"quantity": 3, "price": 4.5}`. Expected fields: `{"total": 13.5}`.
2. Input `{"quantity": 1, "price": 0}`. Expected fields: `{"total": 0.0}`.
3. Input `{"quantity": 2, "price": 1.25}`. Expected fields: `{"quantity": 2, "price": 1.25, "total": 2.5}`.

Edit the corresponding fields. Array/object fields use valid JSON. Click Run experiment and compare each expected field. Download the result to preserve your observations. Reset results clears the displayed evidence, not a persisted workflow or database.

## 6. Explain the result
typed state versus runtime validation is visible in the returned fields and implementation. TypedDict documents a contract but does not validate every value at runtime. Where should validation occur? The success indicator establishes that execution finished; assess the returned evidence against the contract before concluding that a design is correct.

## 7. Extend the experiment
1. Change one input and predict the result before running it.
2. Add a boundary case and define its expected behavior in a test.
3. Extend the pipeline with one measurable property while retaining the existing contracts.

## 8. Diagnose a failure
Reproduce an empty or malformed input, identify the validation boundary, and confirm that the previous successful result is cleared. For persisted examples use a new thread/key or the intended resume action; do not blindly delete user data.

## 9. Test
Windows: `.venv\Scripts\python.exe -m pytest -q` and `.venv\Scripts\python.exe -m pip check`.

macOS/Linux: `.venv/bin/python -m pytest -q` and `.venv/bin/python -m pip check`.

Tests assert concrete expected fields, invalid-input behavior, and actual form submission. Any service boundary tests use fixtures and are identified as such; they do not certify cloud behavior.

## 10. Interview rehearsal
Explain the workflow without reading the code, state its invariant, and justify its tradeoff. Then work through INTERVIEW.md. Local deterministic workflow; model intelligence and managed deployment are separate concerns.
