# OmniCore ⚡️

**OmniCore** is an accelerated, high-intensity curriculum repository designed to bridge the gap between foundational Python programming and advanced Machine Learning (ML) architecture. 

It strips away the overhead of Jupyter Notebooks in favor of test-driven, raw Python executable quests—engineering your syntax into algorithmic intuition.

---

## 🚀 The 2026 Learning Methodology

You cannot learn strict ML architecture using legacy tutorials. This codebase is explicitly engineered to be executed inside an **AI-Native Agentic IDE** (such as Cursor or Windsurf). 

To master Python for AI in record time, you must follow the Agentic Loop:

1. **Clone & Load:** `git clone https://github.com/Cyrax321/NeuroForge.git` and open the directory inside an AI-optimized IDE.
2. **Execute:** Run the curriculum files locally in your terminal (e.g., `python curriculum/01_beginner_fundamentals/...`).
3. **Engage the Agent:** If you hit an algorithmic wall, encounter an assertion error from the internal test runner, or simply do not understand *why* a list comprehension behaves the way it does—**Do not Google it.** Highlight the code and command your AI agent to explain the logic, trace the error, and teach you the underlying concept directly inside your editor. 

This repository acts as your physical training ground. Your AI IDE is your private tutor.

---

## 🔬 System Architecture

The core curriculum is decoupled into three master namespaces, representing the chronological learning path required for AI/ML engineering:

### `[ 01 ]` curriculum/
The primary educational engine.
* **`01_beginner_fundamentals/`** 
  * Core programmatic building blocks: State Management (Variables), Control Flow, Iterators, and Hash Maps (Dictionaries).
* **`02_intermediate_core/`** 
  * Algorithmic training targeting ML preprocessing patterns: Log Parsing, Feature Extraction, OOP Base Classes, and Matrix Operations.
* **`03_advanced_algorithms/`** 
  * Intensive data structure problem sets (Two Pointers, Matrices, Standard Deviation, KNN logic).
* **`04_projects/`** 
  * Standalone Capstones. Includes a from-scratch, pure-Python implementation of a structured Dataframe (`mini_pandas.py`).

### `[ 02 ]` sandbox/
* **`experimental_models/`**: Unstructured workspace containing loose scripts, early prototypes, and temporary testing algorithms.

### `[ 03 ]` archive/
* Frozen state. Historical research, legacy datasets, and collegiate CS50 assignments safely compartmentalized.

---

## ⚙️ Testing & Telemetry

Every curriculum chapter acts as a standalone executable containing built-in runtime tests. To execute a test suite, run the python script directly.

```bash
# Example Execution
python curriculum/01_beginner_fundamentals/01_variables_and_printing.py
```

### Execution Status Codes
The runner system utilizes a specialized ASCII telemetry protocol to report test status directly to `stdout`.

- `[PASS]  <3`  -- Function executes strictly within parameters.
- `[FAIL]  :( ` -- Critical logic failure or assertion miss.
- `[WARN]  o_O` -- Syntax warning or undefined behavior.
- `[DONE]  (*^▽^*)` -- Module successfully validated.
- `[CAPS]  ★ ` -- Project Capstone passed successfully.

---
*Developed by Cyrax321 / 2026*
