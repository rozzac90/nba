from nba.baseclient import BaseClient
from nba import endpoints


class APIClient(BaseClient):
    def __init__(self):
        super(APIClient, self).__init__()

        self.boxscores = endpoints.Boxscores(self)
        self.common = endpoints.Common(self)
        self.draft = endpoints.Draft(self)
        self.events = endpoints.Events(self)
        self.homepage = endpoints.Homepage(self)
        self.misc = endpoints.Misc(self)
        self.playbyplay = endpoints.PlayByPlay(self)
        self.player = endpoints.Player(self)
        self.scoreboard = endpoints.Scoreboard(self)
        self.team = endpoints.Team(self)
