from flask import (
    Flask,
    request,
    render_template,
)  # Case sensitive imports the Flask class from the flask library

from classes.py

app = Flask(__name__)

@app.get("/")  # HTTP Request: Get /
def index():
    return render_template(
        "index.html", title="Welcome!", heading="Welcome to the ITC Pool League!"
    )

if __name__ == "__main__":  # Must be the last line isn a flask object
    app.run(debug=True)