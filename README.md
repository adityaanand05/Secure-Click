# Microsoft Hackathon Project

A concise, self-contained Python web project created for the Microsoft Hackathon. It includes a small Python web application and a static frontend page.

## Quick Summary
- **Purpose:** Demo web app and UI prototype for hackathon submission.
- **Stack:** Python (Flask or simple HTTP), HTML/CSS frontend.

## Tech & Files
- `app.py` — Python server entrypoint (Flask or simple HTTP server).
- `index.html` — Single-page frontend served statically or opened directly in a browser.
- `requirements.txt` — Python dependencies.

## Prerequisites
- **Python:** 3.8 or newer (3.10+ recommended).
- **OS:** Windows (instructions below use PowerShell), Linux/macOS commands similar.
- Optional: an editor (VS Code) and Git for version control.

## Setup (Windows PowerShell)
1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
& .venv\Scripts\Activate.ps1
```

2. Upgrade pip and install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. (Optional) If this is a Flask app, set environment variables for development:

```powershell
$env:FLASK_ENV = "development"
$env:FLASK_APP = "app.py"
```

## Running the Project

Option A — Run as a Python web app (Flask or similar):

```powershell
python app.py
# or for Flask built-in server
flask run
```

Then open the URL shown in the terminal (commonly http://127.0.0.1:5000).

Option B — Open the static frontend directly:

1. Open [index.html](index.html) in your browser (double-click or `File -> Open`).
2. If the frontend expects API endpoints from `app.py`, run Option A concurrently.

## Configuration & Notes
- If `app.py` expects configuration (API keys, database URLs), set them as environment variables before running.
- If CORS or fetch requests from `index.html` fail when opened as a file, prefer serving the frontend via the Python app or a simple static server (e.g., `python -m http.server 8000`).

## Project Structure

- `app.py` — server: routes, API handlers, and app startup.
- `index.html` — frontend UI, static assets may be alongside it.
- `requirements.txt` — freeze of Python packages used by the project.

## Development Tips
- Use the virtual environment for development to avoid dependency conflicts.
- Open the project in VS Code and use the built-in debugger to step through `app.py`.
- Add a `.gitignore` to exclude `.venv/`, `__pycache__/`, and other artifacts.

## Testing
- No automated tests are included yet. Add a `tests/` folder and use `pytest` for unit tests.

## Troubleshooting
- "ModuleNotFoundError": ensure the virtual environment is activated and `pip install -r requirements.txt` has been run.
- "Port in use": change the port in `app.py` or use `flask run --port 5001`.

## Contributing
- Feel free to open issues or PRs. Add implementation notes and tests when possible.

## License
- Add a `LICENSE` file to clarify reuse. For hackathon submissions, an MIT or Apache-2.0 license is common.

## Contact
### Krisita Chhetry - Lead(Frontend + AI)

[GitHub Profile](https://github.com/krisitachhetry25-hue)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/krisita-chhetry-319028379)

### Aditya Anand - Member(AI + Backend)
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://adityaanandportfolio.web.app/)

[GitHub Profile](https://github.com/adityaanand05)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/adityaanand05)

### Manjulika - Member(Frontend)

[GitHub Profile](https://github.com/manjulikagithub)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/manjulika-bachar-29920022a)

### Nitish Raj - Member(backend)

[GitHub Profile]()

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)]()




---



