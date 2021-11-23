import DBcm

config = {
    "host": "127.0.0.1",
    "database": "leagueTracker",
    "user": "leagueTracker",
    "password": "trackerpass",
}

SQL_unplayedMatches = "select * from matchdetails where status = 'Not Played'"
SQL_appendMatch = "update matchdetails where MatchID = '%s' set Winner = '%s'"
SQL_createMatch = ""

def unplayedMatches():
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_unplayedMatches)
            data = db.fetchall()
        except DBcm.SQLError as err:
            print('Your query broke:', str(err))

    unplayed = data
    return unplayed

def appendMatch(mId, winner):
    with DBcm.UseDatabase(config) as db:
        try:
            db.execute(SQL_appendMatch,(
                mId,
                winner,
                )
            )
        except DBcm.SQLError as err:
            print("Your query broke:", str(err))
