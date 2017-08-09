import datetime

from nba import enums
from nba.utils import request_data, parse_result_json



def playoffpicture(idx_data, SeasonID=enums.Season.Default, LeagueID=enums.LeagueID.Default):
    """
    Get information on how current playoff matchups and conference standings are.

    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: league to filter for.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonID: Season for which to get stat leaders.
    :type SeasonID: nba.nba.bin.enums.Season
    :returns: A view of playoff or standings, as show in idx_data table breakdown below.
    :rtype: Dataframe

    ========   =======================   ==================================================================
    idx_data           Name                                   Description
    ========   =======================   ==================================================================
        0       EastConfPlayoffPicture    Breakdown of how East Conference playoff matchups currently look.
        1       WestConfPlayoffPicture    Breakdown of how West Conference playoff matchups currently look.
        2       EastConfStandings         Current standing for East Conference.
        3       WestConfStandings         Current standing for West Conference.
        4       EastConfRemainingGames    Breakdown of games remaining in East Conference.
        5       WestConfRemainingGames    Breakdown of games remaining in East Conference.
    ========   =======================   ==================================================================


    """
    params = locals()
    endpoint = 'playoffpicture'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df

def videoStatus(GameDate=datetime.datetime.today().strftime('%Y-%m-%d'), LeagueID=enums.LeagueID.Default):
    """
    Breakdown of which games are available on video on a given date.

    :param GameDate: date to check.
    :type GameDate: str('%Y-%m-%d')
    :param LeagueID: league to filter for.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :returns: games on the given date and whether they are available on video.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'videoStatus'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df
