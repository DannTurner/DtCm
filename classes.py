class Match:
    def __init__(match, id, player1, player2, status, winner):
        match.id = id
        match.player1 = player1
        match.player2 = player2
        match.status = status
        match.winner = winner


class Player:
    def __init__(player, name, team, notes):
        player.name = name
        player.team = team
        player.notes = notes