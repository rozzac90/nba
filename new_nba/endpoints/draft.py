
from nba import enums
from nba.utils import request_data, parse_result_json


def draftcombinedrillresults(LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
    """
    Combine drill results for a given year.

    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonYear: draft season.
    :type SeasonYear: str('%Y-%y')
    :returns: Combine drill results by player.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'draftcombinedrillresults'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def draftcombinenonstationaryshooting(LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
    """
    Moving shooting scores broken down by movement type.

    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonYear: draft season.
    :type SeasonYear: str('%Y-%y')
    :returns: Movement shooting results by player.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'draftcombinenonstationaryshooting'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def draftcombineplayeranthro(LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
    """
    Detailed breakdown of players measurements and physical stats.

    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonYear: draft season.
    :type SeasonYear: str('%Y-%y')
    :returns: Measurements and physical information by player.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'draftcombineplayeranthro'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def draftcombinespotshooting(LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
    """
    Get raw and pct shooting results from draft combine for a given year.

    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonYear: draft season.
    :type SeasonYear: str('%Y-%y')
    :returns: Combine shooting results by player.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'draftcombinespotshooting'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def draftcombinestats(LeagueID=enums.LeagueID.Default, SeasonYear='2016-17'):
    """
    Get combine results for a draft year.

    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonYear: draft season.
    :type SeasonYear: str('%Y-%y')
    :returns: Combine results by player.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'draftcombinestats'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def drafthistory(LeagueID=enums.LeagueID.Default):
    """
    Breakdown of pick number and player data for historical drafts.

    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :returns: Player pick numbers for historic drafts.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'drafthistory'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def franchisehistory(idx_data, LeagueID=enums.LeagueID.Default):
    """
    Breakdown of each franchise's record in the NBA.

    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: define league to look at, nba.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :returns: franchise information.
    :rtype: Dataframe


    ========   =================   ==================================================
    idx_data          Name                        Description
    ========   =================   ==================================================
        0       FranchiseHistory   Win/Loss Record and Titles Info for franchises.
        1       DefunctTeams       Franchises no longer in NBA.
    ========   =================   ==================================================

    """
    params = locals()
    endpoint = 'franchisehistory'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return r
