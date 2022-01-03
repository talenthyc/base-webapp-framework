"""
Same reason as:
https://github.com/microsoft/python-sample-vscode-flask-tutorial/blob/master/startup.py
"""
from src.webapp import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
