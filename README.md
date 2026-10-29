## How It Works: The Journey of Your Code

This Intelligent Tutoring System (ITS) does not just check if your code runs; it reads your code like a human teacher would. It uses a Flask web backend to connect a user interface with three advanced AI-driven educational modules. 

Here is exactly what happens when you click "Analyze Code":

### 1. Code Submission (The Frontend)
When you type Python code into the web interface and hit submit, the browser sends your code via an API request to the Flask backend server (`app.py`).

### 2. Structural Parsing (Semantic Code Analyzer)
Instead of just running test cases, the system passes your code to `ast_analyzer.py`. This module uses Python's built-in Abstract Syntax Tree (`ast`) library to break your code down into its structural components. It scans the tree to detect:
* **Syntax Errors:** Is the code written legally?
* **Algorithmic Inefficiencies:** Are there O(n²) nested loops?
* **Logical Traps:** Is there a `while True` loop missing a `break` statement?
* **Code Quality:** Are there unused variables or missing docstrings?

### 3. Cognitive Tracking (Bayesian Knowledge Tracing)
Once the code is analyzed, the results are sent to `bkt_student_model.py`. This module acts as the AI's "memory" of you. It uses a statistical model called Bayesian Knowledge Tracing (BKT) to calculate the mathematical probability that you understand specific concepts (like `for_loops` or `while_loops`). 
* If you make a mistake, your mastery score for that concept slightly decreases.
* If you write perfect code for that concept, your mastery score increases.

### 4. Adaptive Scaffolding (Pedagogical Engine)
Next, `pedagogical_engine.py` generates your feedback. It looks at both the **errors found** and your **current mastery level**. 
* **If you are a beginner (Low Mastery):** It gives you a highly specific hint (e.g., *"You must add a `break` statement inside an `if` block"*).
* **If you are advanced (High Mastery):** It gives you a conceptual nudge instead of handing you the answer (e.g., *"Infinite loop detected. Remember to manage your control flow exits"*).

### 5. Dynamic UI Update
Finally, the backend sends the generated feedback and your updated mastery scores back to the webpage. The JavaScript on the page updates the tutor's chat box and animates your cognitive progress bars in real-time, completing the learning loop!
