import DBcm

config = {
    "host": "redtosh.ddns.net",
    "database": "leagueTracker",
    "user": "leagueAdmin",
    "password": "trackerPass",
}

SQL_unplayedMatches = "select * from matchdetails where status = 'Not Played'"
SQL_appendMatch = (
    "update matchdetails set Winner = %s, Status ='Played' where MatchID = %s"
)
SQL_createPLayer = "insert into players "
SQL_orderedLeague = "select * from player order by LeaguePoints desc"
SQL_playerList = "select StudentName from player order by StudentName asc"


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


def unplayedMatchesFiltered(player):
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_unplayedMatches)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))

    playerList = []
    for g in data:
        if g[1] == player:
            playerList.append(g[2])
        elif g[2] == player:
            playerList.append(g[1])

    return playerList


def getPlayerList():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_playerList)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))

    playerList = []
    for e in data:
        playerList.append(e[0])

    return playerList


def appendMatch(winner, mId):
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_appendMatch, (winner, mId,))
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))
