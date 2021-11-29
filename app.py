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
        heading="ITC Pool League Standings",
        table=leagueTable(),
    )


@app.get("/notplayed")
def notplayed():
    return render_template(
        "who.html",
        title="League Standings",
        heading="ITC Pool League Standings",
        table=leagueTable(),
    )


if __name__ == "__main__":
    app.run(debug=True)
