from db_utils import *

from flask import (
    Flask,
    request,
    render_template,
)

app = Flask(__name__)


@app.get("/")
def index():
    return render_template(
        "index.html",
        title="League Standings",
        heading="Welcome to the ITC Pool League!",
        table=leagueTable(),
    )


if __name__ == "__main__":
    app.run(debug=True)
