# ITS Web Application

This is the web-based version of the Intelligent Tutoring System using Flask.

## How to Run Locally
1. Ensure you have Python installed.
2. Open your terminal in this folder and install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Open your web browser and go to `http://127.0.0.1:5000`.

## How to Deploy (To Render.com)
1. Push this entire folder to a new **GitHub Repository**.
2. Go to [Render.com](https://render.com) and sign up.
3. Click "New" -> "Web Service".
4. Connect your GitHub account and select your repository.
5. Render will automatically detect it is a Python app.
6. Settings:
   * Build Command: `pip install -r requirements.txt`
   * Start Command: `gunicorn app:app`
7. Click "Create Web Service". You will get a live URL (e.g., `https://your-its-app.onrender.com`).
