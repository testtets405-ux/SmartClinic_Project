---
description: "Generates the complete Smart Clinic System (Backend, DB, Frontend) iteratively based on the project rules."
---

# Smart Clinic Build Workflow

1. **Step 1: Scaffolding**
   - Create the folder structure as defined in the Rules.
   - Create `requirements.txt` and `config.py`.

2. **Step 2: Database Layer**
   - Create `models.py` using SQLAlchemy.
   - Define User, Patient, and Appointment models.
   - Run a script to initialize `clinic.db`.

3. **Step 3: Core Logic (The Smart Algorithm)**
   - Create `utils.py` or helper functions in `routes.py`.
   - Implement the `calculate_priority` function strictly according to the Rules.

4. **Step 4: Backend Routes**
   - Create `app.py` (or `routes.py` with Blueprints).
   - Implement routes for: Home, Kiosk (Form), Queue Display (JSON API), Doctor Dashboard.

5. **Step 5: Frontend**
   - Create `templates/layout.html` (Bootstrap base).
   - Create `index.html`, `queue.html`, `doctor.html`, `admin.html`.
   - Ensure `queue.html` uses JavaScript to auto-refresh data every 5 seconds.

6. **Step 6: Verification**
   - Create a dummy test script `test_app.py` to verify the priority logic works.

Add a strict rule inside it explaining the 'File-Based Wrapper' method. Instruct your future self that whenever running a background terminal command on Windows in this project, it MUST use the _agent_task.ps1 and _agent_output.txt routing method because direct stdout capture is broken.

Write this rule clearly and save the file."