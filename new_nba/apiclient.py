
from new_nba.baseclient import BaseClient
from new_nba import endpoints


class APIClient(BaseClient):

    def __init__(self):
        super(APIClient, self).__init__()

        self.boxscores = endpoints.Boxscores(self)
        self.common = endpoints.Account(self)
        self.draft = endpoints.MarketData(self)
        self.events = endpoints.ReferenceData(self)
        self.homepage = endpoints.Reporting(self)
        self.misc = endpoints.
        self.playbyplay = endpoints.
        self.player = endpoints.
        self.scoreboard = endpoints.
        self.team = endpoints.
