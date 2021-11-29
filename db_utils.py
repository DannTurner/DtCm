import DBcm

config = {
    "host": "redtosh.ddns.net",
    "database": "leagueTracker",
    "user": "leagueAdmin",
    "password": "trackerPass",
}

SQL_unplayedMatches = "select * from matchdetails where status = 'Not Played'"
SQL_unplayedMatchesFiltered = "select * from matchdetails where (Status = 'Not Played' and Player1 = %s) or (Status = 'Not Played' and Player2 = %s)"
SQL_appendMatch = (
    "update matchdetails set Winner = %s, Status ='Played' where MatchID = %s"
)
SQL_createPLayer = "insert into players "
SQL_orderedLeague = "select * from player order by LeaguePoints desc"


def leagueTable():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_orderedLeague)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))

    return data


def unplayedMatches():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_unplayedMatches)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))

    return data


def unplayedMatchesFiltered():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_unplayedMatchesFiltered)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))

    playerList = []
    for g in data:
        if g[1] == "Ciaran Maye":
            playerList.append(g[2])
        else:
            playerList.append(g[1])

    return playerList


def appendMatch(winner, mId):
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_appendMatch, (winner, mId,))
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))
