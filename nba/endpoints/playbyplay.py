
from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class PlayByPlay(BaseEndpoint):

    def play_by_play(self, game_id, start_period=enums.StartPeriod.AllQuarters, end_period=enums.EndPeriod.AllQuarters):
        """
        Play by play data for a given game, comments from home, away and neutral perspective.
    
        :param game_id: ID of the game to get data for.
        :type game_id: str
        :param start_period: starting period filter on the data.
        :type start_period: nba.nba.bin.enums.StartPeriod
        :param end_period: ending period filter on the data.
        :type end_period: nba.nba.bin.enums.EndPeriod
        :returns: play by play event descriptions and details of players involved
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'playbyplayv2'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
