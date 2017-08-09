from nba import enums
from nba.utils import request_data, parse_result_json


def playbyplay(GameID, StartPeriod=enums.StartPeriod.Default, EndPeriod=enums.EndPeriod.Default):
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
    params = locals()
    endpoint = 'playbyplayv2'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


