import DBcm

config = {
    "host": "127.0.0.1",
    "database": "leagueTracker2",
    "user": "leagueAdmin",
    "password": "trackerPass",
}

SQL_unplayedMatches = "select * from matchdetails where status = 'Not Played'"
SQL_appendMatch = "update matchdetails set Winner = %s, status ='Played' where MatchID = %s"
SQL_createPLayer = "insert into players "
SQL_orderedLeague = "select * from player order by LeaguePoints desc"

def leagueTable():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execut(SQL_orderedLeague)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))
    
    leagueTable = data
    return leagueTable


def unplayedMatches():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_unplayedMatches)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print('Your query broke:', str(err))

    unplayed = data
    return unplayed

def appendMatch(winner, mId):
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_appendMatch,(
                winner,
                mId,
                )
            )
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))
