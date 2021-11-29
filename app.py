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
        option_list=getPlayerList(),
    )


@app.route("/notplayed", methods=["POST"])
def notplayed():
    theplayer = request.form["option"]
    return render_template(
        "who.html",
        title="Who do I need to play",
        heading="You need to play",
        results=unplayedMatchesFiltered(theplayer),
    )


if __name__ == "__main__":
    app.run(debug=True)
