
from new_nba import enums
from new_nba.utils import clean_locals
from new_nba.endpoints.baseendpoint import BaseEndpoint


class PlayByPlay(BaseEndpoint):

    def playbyplay(self, GameID, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default):
        """
        Play by play data for a given game, comments from home, away and neutral perspective.
    
        :param GameID: ID of the game to get data for.
        :type GameID: str
        :param StartPeriod: starting period filter on the data.
        :type StartPeriod: nba.nba.bin.enums.StartPeriod
        :param EndPeriod: ending period filter on the data.
        :type EndPeriod: nba.nba.bin.enums.EndPeriod
        :returns: play by play event descriptions and details of players involved
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'playbyplayv2'
        r = self.request(params, endpoint)
        df = self.process_response(r, 0, 'resultSets')
        return df
