class Player:

    def __init__(self, player_name: str, position: str) -> None:
        self.player_name = player_name
        self.position = position
        self.total_points = 0

    def add_points(self, game_points: int) -> None:
        if game_points > 0:
            self.total_points += game_points

    def __str__(self) -> str:
        return self.player_name + " " + f"plays centre and has a total of {self.total_points} points"


class Team:

    def __init__(self, team_name: str) -> None:
        self.team_name = team_name
        self.players = []

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def get_players_by_position(self, position: str) -> list[Player]:
        players_by_position = []
        for player in self.players:
            if player.position == position:
                players_by_position.append(player)
        return players_by_position


t = Team('Furies')
p1 = Player('Shea', 'goalie')
t.add_player(p1)
p2 = Player('Elaine', 'defense')
t.add_player(p2)
p3 = Player('Renata', 'defense')
t.add_player(p3)
defenders = t.get_players_by_position('defense')

print(defenders[0] == p2)
