import pandas as pd

from nba import enums
from nba.utils import request_data, parse_result_json


def team_stats(LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
               PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
               PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
               GameScope=enums.GameScope.Blank, TeamID=enums.TeamID.Default, College=enums.College.Default,
               Conference=enums.Conference.Default, Country=enums.Country.Default, DateFrom=enums.DateFrom.Default,
               DateTo=enums.DateTo.Default, Division=enums.Division.Default, GameSegment=enums.GameSegment.Default,
               Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
               Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.dDefault, Outcome=enums.Outcome.Default,
               PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
               PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default,
               StarterBench=enums.StarterBench.Default, VsConference=enums.VsConference.Default,
               VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown.

    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param GameScope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
    :type GameScope: nba.nba.bin.enums.GameScope
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PlayerExperience: Filter to only include players of specific experience level. Default '' returns all.
    :type PlayerExperience: nba.nba.bin.enums.PlayerExperience
    :param PlayerPosition: Filter to only include players of certain position. Default '' returns all.
    :type PlayerPosition: nba.nba.bin.enums.PlayerPosition
    :param StarterBench: Filter to only include starts or bench. Default '' returns all.
    :type StarterBench: nba.nba.bin.enums.StarterBench
    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param Conference: Filter for players from specific conference. Default '' returns all.
    :type Conference: nba.nba.bin.enums.Conference
    :param Country: Filter for players from specific country. Default '' returns all.
    :type Country: nba.nba.bin.enums.Country
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'leaguedashteamstats'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_lineups(TeamID, GameID=enums.Default_Values.Blank, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                 PerMode=enums.PerMode.Default, GroupQuantity=enums.GroupQuantity.Default, MeasureType=enums.MeasureType.Default,
                 PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                 DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                 Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                 Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                 SeasonSegment=enums.SeasonSegment.Default, Conference=enums.Conference.Default, Division=enums.Division.Default,
                 VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Top 250 team lineup combinations of specified group quantity, by minutes played descending.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param GroupQuantity: no. of players to group into ranking. Default 5. Required.
    :type GroupQuantity: int
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param VsConference: Filter to only include only teams from specific conference. Default '' returns all.
    :type VsConference: nba.nba.bin.enums.VsConference
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team lineup combinations of GroupQuantity, ranked by StatCategory after applying all filters.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'teamdashlineups'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 1, 'resultSets')
    return df


def team_lineups_rank(Season=enums.Season.Default, SeasonType=enums.SeasonType.Default, PerMode=enums.PerMode.Default,
                      GroupQuantity=enums.GroupQuantity.Default, MeasureType=enums.MeasureType.Default, TeamID=enums.TeamID.Default,
                      PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                      DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                      Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                      Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                      SeasonSegment=enums.SeasonSegment.Default, Conference=enums.Conference.Default, Division=enums.Division.Default,
                      VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Top 250 team lineup combinations of specified group quantity, ranked by stat category.

    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param GroupQuantity: no. of players to group into ranking. Default 5. Required.
    :type GroupQuantity: int
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :type TeamID: filter for specific team. Default 0 returns all.
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param VsConference: Filter to only include only teams from specific conference. Default '' returns all.
    :type VsConference: nba.nba.bin.enums.VsConference
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team lineup combinations of GroupQuantity, ranked by StatCategory after applying all filters.
    :rtype: Dataframe

    """
    params=locals()
    endpoint = 'leaguedashlineups'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_shotlocations(LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                       PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                       PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                       GameScope=enums.GameScope.Blank, TeamID=enums.TeamID.Default, Conference=enums.Conference.Default,
                       DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, Division=enums.Division.Default,
                       GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                       Location=enums.Location.Default, Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default,
                       Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
                       PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default, StarterBench=enums.StarterBench.Default,
                       VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Team shot stats breakdown, default broken down by shot category.

    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams stats from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param GameScope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
    :type GameScope: nba.nba.bin.enums.GameScope
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PlayerExperience: Filter to only include players of specific experience level. Default '' returns all. Required.
    :type PlayerExperience: nba.nba.bin.enums.PlayerExperience
    :param PlayerPosition: Filter to only include players of certain position. Default '' returns all. Required.
    :type PlayerPosition: nba.nba.bin.enums.PlayerPosition
    :param StarterBench: Filter to only include starts or bench. Default '' returns all. Required
    :type StarterBench: nba.nba.bin.enums.StarterBench
    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param Conference: Filter for teams from specific conference. Default '' returns all.
    :type Conference: nba.nba.bin.enums.Conference
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: team shot stats by shot category after applying all filters.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'leaguedashteamshotlocations'
    r = request_data(params, endpoint)
    df = pd.DataFrame(data=r.get('resultSets').get('rowSet'), columns=r.get('resultSets').get('headers')[1].get('columnNames'))
    return df


def team_ptshot(LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                PerMode=enums.PerMode.Default, CloseDefDistRange=enums.CloseDefDistRange.Default, DribbleRange=enums.DribbleRange.All,
                ShotClockRange=enums.ShotClockRange.Default, ShotDistRange=enums.Default_Values.Blank,
                TouchTimeRange=enums.Default_Values.Blank, GeneralRange=enums.Default_Values.Blank, TeamID=enums.TeamID.Default,
                Conference=enums.Conference.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                Division=enums.Division.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                LastNGames=enums.LastNGames.Default, PORound=enums.PORound.Default, Location=enums.Location.Default,
                Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                VsDivision=enums.VsDivision.Default):
    """
    Team shot stats breakdown.

    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param CloseDefDistRange: Filter stats to include of shots with specific closest defender range. Default '' returns all.
    :type CloseDefDistRange: nba.nba.bin.enums.CloseDefDistRange
    :param DribbleRange: Filter stats to include only shots where specific no. of dribbles occured. Default '' returns all.
    :type DribbleRange: nba.nba.bin.enums.DribbleRange
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :param ShotDistRange: Filter stats to include only shots in specified distance range. Default '' returns all.
    :type ShotDistRange: unsure.
    :param TouchTimeRange: Filter by how long ball is held prior to shot. Default '' returns all.
    :type TouchTimeRange: unsure.
    :param GeneralRange: No idea what this does.
    :type GeneralRange: unsure.
    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param Conference: Filter for players from specific conference. Default '' returns all.
    :type Conference: nba.nba.bin.enums.Conference
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param Location: Filter for home or road games only. Default '' returns all.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
    :type Month: nba.nba.bin.enums.Month
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all.
    :type Outcome nba.nba.bin.enums.Outcome
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param StarterBench: Filter to only include starts or bench. Default '' returns all.
    :type StarterBench: nba.nba.bin.enums.StarterBench
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all.
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :returns: Team shot stats after applying all filters.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'leaguedashteamptshot'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_ptdefend(LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                  PerMode=enums.PerMode.Default, DefenseCategory=enums.DefenseCategory.Default, Conference=enums.Conference.Default,
                  DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, Division=enums.Division.Default,
                  GameScope=enums.GameScope.Default, TeamID=enums.TeamID.Default, GameSegment=enums.GameSegment.Default,
                  Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                  Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                  PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                  VsDivision=enums.VsDivision.Default):
    """
    Team defensive stats breakdown.

    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param DefenseCategory: Filter to include only defense of shots from specific distance bucket. Default 'Overall' returns all. Required.
    :type DefenseCategory: nba.nba.bin.enums.DefenseCategory
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all.
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param Conference: Filter for players from specific conference. Default '' returns all.
    :type Conference: nba.nba.bin.enums.Conference
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :returns: Team defensive stats after applying all filters.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'leaguedashptdefend'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_clutch(LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                ClutchTime=enums.ClutchTime.mins5, AheadBehind=enums.AheadBehind.Default, PointDiff=100, GameScope=enums.GameScope.Blank,
                PlayerExperience=enums.PlayerExperience.Default, PlayerPosition=enums.PlayerPosition.Default,
                StarterBench=enums.StarterBench.Default, MeasureType=enums.MeasureType.Default, PerMode=enums.PerMode.Default,
                PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                Outcome=enums.Outcome.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                SeasonSegment=enums.SeasonSegment.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                OpponentTeamID=enums.OpponentTeamID.Default, VsConference=enums.VsConference.Default,
                VsDivision=enums.VsDivision.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                LastNGames=enums.LastNGames.Default, Conference=enums.Conference.Default, Division=enums.Division.Default,
                TeamID=enums.TeamID.Default, PORound=enums.PORound.Default, ShotClockRange=enums.ShotClockRange.Default):
    """
    Team clutch stats breakdown.

    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams data from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param ClutchTime: Filter for stats occurring with less than this amount of time to play in the game. Default 5mins. Required.
    :type ClutchTime: nba.nba.bin.enums.ClutchTime
    :param AheadBehind: filter to only include when team is behind|ahead. Default includes all. Required
    :type AheadBehind: nba.nba.bin.enums.AheadBehind
    :param PointDiff: Absolute difference between teams for stats to be included. Required.
    :type PointDiff: int
    :param GameScope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
    :type GameScope: nba.nba.bin.enums.GameScope
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PlayerExperience: Filter to only include players of specific experience level. Default '' returns all. Required.
    :type PlayerExperience: nba.nba.bin.enums.PlayerExperience
    :param PlayerPosition: Filter to only include players of certain position. Default '' returns all. Required.
    :type PlayerPosition: nba.nba.bin.enums.PlayerPosition
    :param StarterBench: Filter to only include starts or bench. Default '' returns all. Required
    :type StarterBench: nba.nba.bin.enums.StarterBench
    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param Conference: Filter for players from specific conference. Default '' returns all.
    :type Conference: nba.nba.bin.enums.Conference
    :param Division: Filter by specific division. Default '' returns all.
    :type Division: nba.nba.bin.enums.Division
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team clutch stats after applying all filters.
    :rtype: Dataframe

     """
    params = locals()
    endpoint = 'leaguedashteamclutch'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_passing(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                 PerMode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                 LastNGames=enums.LastNGames.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                 OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default,
                 VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Team pass stats breakdown by received|made.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get team data from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :returns: Team stats after applying all filters by passes made|received. Shown in idx_data table below.
    :rtype: Dataframe

    ========   ===============   ==================================================
    idx_data        Name                           Description
    ========   ===============   ==================================================
        0       PassesMade        Breakdown of passes made by player thrown by.
        1       PassesReceived	  Breakdown of passes received by player thrown to.
    ========   ===============   ==================================================

    """
    params = locals()
    endpoint = 'teamdashptpass'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_rebounding(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                    PerMode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                    GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                    Location=enums.Location.Default, Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default,
                    Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                    VsDivision=enums.VsDivision.Default):
    """
    Team rebounding stats breakdown by shot|shot distance|rebound distance|contest or overall.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :returns: Team stats after applying all filters by passes made|received. Shown in idx_data table below.
    :rtype: Dataframe

    ========   =======================   ========================================================
    idx_data            Name                            Description
    ========   =======================   ========================================================
        0       OverallRebounding         Overall Team rebounding stats..
        1       ShotTypeRebounding	      Team rebounding stats by shot type.
        2       NumContestedRebounding    Team rebounding stats by number of people contesting.
        3       ShotDistanceRebounding    Team rebounding stats by shot distance.
        4       RebDistanceRebounding     Team rebounding stats by rebound distance.
    ========   =======================   ========================================================

    """
    params = locals()
    endpoint = 'teamdashptreb'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_shooting(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                  PerMode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                  GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                  Location=enums.Location.Default, Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default,
                  Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                  VsDivision=enums.VsDivision.Default):
    """
    Team shot success stats breakdown.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams data from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param TeamID: ID of the team to filter for. Default 0 returns all. Required.
    :type TeamID: int
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :returns: Team shooting stats after applying all filters by shot success.
    :rtype: Dataframe

    ========   ================================   ========================================================
    idx_data            Name                                   Description
    ========   ================================   ========================================================
        0       Overall                            Overall Team shooting stats..
        1       GeneralShooting	                   Team shooting stats by basic shot type.
        2       ShotClockShooting                  Team shooting stats by time on shotclock buckets.
        3       DribbleShooting                    Team shooting stats by number of dribbles taken.
        4       ClosestDefenderShooting            Team shooting stats by distance to closest defender.
        5       ClosestDefender10ftPlusShooting    Team shooting stats Defender > 10ft.
        6       TouchTimeShooting                  Team shooting stats by time touching ball buckets.
    ========   ================================   ========================================================

    """
    params = locals()
    endpoint = 'teamdashptshots'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_vs_players(TeamID, VsPlayerID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default,
                    SeasonType=enums.SeasonType.Default, PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                    PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                    ShotClockRange=enums.ShotClockRange.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                    GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                    Location=enums.Location.Default, Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default,
                    Outcome=enums.Outcome.Default, Conference=enums.Conference.Default, Division=enums.Division.Default,
                    SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                    VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown vs specific player by player on|off court, shot distance and shot area.

    :param TeamID: Team ID of the base team in comparison. Required.
    :type TeamID: int
    :param VsPlayerID: player ID for comparison. Required.
    :type VsPlayerID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams data from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters. Shown in idx_data table below.
    :rtype: Dataframe

    ========   =====================   ================================================================================
    idx_data        Name                                           Description
    ========   =====================   ================================================================================
        0       Overall                 Overall team stats.
        1       vsPlayerOverall         Team stats overall versus specific player.
        2       OnOffCourt              Team stats while specific player is on|off court.
        3       ShotDistanceOverall     Team overall shooting stats by shooting distance.
        4       ShotDistanceOnCourt     Team shooting stats by shooting distance when specific player is on court.
        5       ShotDistanceOffCourt    Team shooting stats by shooting distance when specific player is off court.
        6       ShotAreaOverall         Team overall shooting stats by shot area.
        7       ShotAreaOnCourt         Team shooting stats by shot area when specific player is on court.
        8       ShotAreaOffCourt        Team shooting stats by shot area when specific player is off court.
    ========   =====================   ================================================================================

    """
    params = locals()
    endpoint = 'teamvsplayer'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_byclutch(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                  PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                  PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                  DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                  Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                  Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                  PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                  VsDivision=enums.VsDivision.Default):
    """
    Team clutch stats breakdown.

    :param TeamID: Team to get stats for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team clutch stats after applying all filters.
    :rtype: Dataframe

    ========   =======================================   ==============================================================
    idx_data                   Name                                            Description
    ========   =======================================   ==============================================================
        0       OverallTeamDashboard                      Overall Team clutch stats breakdown.
        1       Last5Min5PointTeamDashboard               Team stats with time to play <= 5mins and point diff <= 5
        2       Last3Min5PointTeamDashboard               Team stats with time to play <= 3mins and point diff <= 5
        3       Last1Min5PointTeamDashboard               Team stats with time to play <= 1mins and point diff <= 5
        4       Last30Sec3PointTeamDashboard              Team stats with time to play <= 30secs and point diff <= 3
        5       Last10Sec3PointTeamDashboard              Team stats with time to play <= 10secs and point diff <= 3
        6       Last5MinPlusMinus5PointTeamDashboard      Team stats with time to play <= 5mins or point diff <= 5
        7       Last3MinPlusMinus5PointTeamDashboard      Team stats with time to play <= 3mins or point diff <= 5
        8       Last1MinPlusMinus5PointTeamDashboard      Team stats with time to play <= 1mins or point diff <= 5
        9       Last30Sec3Point2TeamDashboard             Team stats with time to play <= 30secs and point diff <= 2
        10      Last10Sec3Point2TeamDashboard             Team stats with time to play <= 10secs and point diff <= 2
    ========   =======================================   ==============================================================

    """
    params = locals()
    endpoint = 'teamdashboardbyclutch'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_bygamesplits(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                      PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                      PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                      DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                      Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                      Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                      PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                      VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by score bucket|period|half or overall.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams data from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   ==============================   ====================================================================
    idx_data                   Name                                           Description
    ========   ==============================   ====================================================================
        0       OverallTeamDashboard           Overall Team stats with no splits.
        1       ByHalfTeamDashboard            Team stats split by half in which they occurred.
        2       ByPeriodTeamDashboard          Team stats split by period in which they occurred.
        3       ByScoreMarginTeamDashboard     Team stats split by absolute point diff bucket when they occurred.
        4       ByActualMarginTeamDashboard    Team stats split by actual point diff bucket when they occurred.
    ========   ==============================   ====================================================================

    """
    params = locals()
    endpoint = 'teamdashboardbygamesplits'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_bygeneralsplits(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                         PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                         PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                         DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                         Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                         Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                         PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                         VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by score bucket|period|half or overall.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Teams stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   ==============================   ====================================================================
    idx_data              Name                                           Description
    ========   ==============================   ====================================================================
        0       OverallTeamDashboard             Overall Team stats with no splits.
        1       LocationTeamDashboard            Team stats split by home|road location in which they occurred.
        2       WinsLossesTeamDashboard          Team stats split by game result in which they occurred.
        3       MonthTeamDashboard               Team stats split by month in which they occurred.
        4       PrePostAllStarTeamDashboard      Team stats split by pre post all star break.
        5       StartingPosition                 Team stats split by whether Team started or was on bench.
        6       DaysRestTeamDashboard            Team stats split by no. days rest.
    ========   ==============================   ====================================================================

    """
    params = locals()
    endpoint = 'teamdashboardbygeneralsplits'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_bylastngames(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                      PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                      PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                      DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                      Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                      Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                      PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                      VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by pre defined number of most recent games or overall.

    :param TeamID: Team for which to retrieve data.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters in previous N games or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   ==========================   =======================================================
    idx_data              Name                            Description
    ========   ==========================   =======================================================
        0       OverallTeamDashboard         Overall Team stats with no splits.
        1       Last5TeamDashboard           Team stats in most recent 5 games.
        2       Last10TeamDashboard          Team stats in most recent 10 games.
        3       Last15TeamDashboard          Team stats in most recent 15 games.
        4       Last20TeamDashboard          Team stats in most recent 20 games.
        5       GameNumberTeamDashboard      Team stats split by buckets of 10 most recent games.
    ========   ==========================   =======================================================

    """
    params = locals()
    endpoint = 'teamdashboardbylastngames'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_byopponent(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                    PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                    PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                    DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                    Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                    Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                    PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                    VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by opponent or overall.

    :param TeamID: Team for which to retrieve data.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters by conference|division|team or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   =========================   ====================================================================
    idx_data              Name                                      Description
    ========   =========================   ====================================================================
        0       OverallTeamDashboard        Overall Team stats with no splits.
        1       ConferenceTeamDashboard     Team stats split by conference of team against whom they occurred.
        2       DivisionTeamDashboard       Team stats split by division of team against whom they occurred.
        3       OpponentTeamDashboard       Team stats split by team against whom they occurred.
    ========   =========================   ====================================================================

    """
    params = locals()
    endpoint = 'teamdashboardbyopponent'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_byshootingsplits(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                          PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                          PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                          DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                          Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                          Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                          PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                          VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by shot type, zone and distance or overall.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters by shot zone|type|distance|assist or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   ==============================   ====================================================================
    idx_data              Name                                           Description
    ========   ==============================   ====================================================================
        0       OverallTeamDashboard             Overall Team stats with no splits.
        1       Shot5FTTeamDashboard             Team stats split by shot distance as granular as 5ft range.
        2       Shot8FTTeamDashboard             Team stats split by shots distance as granular as 8ft range.
        3       ShotAreaTeamDashboard            Team stats split by shot area.
        4       AssitedShotTeamDashboard         Team stats split by Assisted|Unassisted.
        5       ShotTypeSummaryTeamDashboard     Team stats split by Shot Type.
        6       ShotTypeTeamDashboard            Team stats split by more granular shot type.
        7       AssistedBy                       Team stats split by Team assisting.
    ========   ==============================   ====================================================================

    """
    params = locals()
    endpoint = 'teamdashboardbyshootingsplits'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_byteamperformance(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                           PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                           PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                           DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                           Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                           Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                           PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                           VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by team performance or overall.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters by points for|against|difference or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   =================================   ====================================================================
    idx_data                Name                                           Description
    ========   =================================   ====================================================================
        0       OverallTeamDashboard                Overall Team stats with no splits.
        1       ScoreDifferentialTeamDashboard      Team stats split by games final score differential.
        2       PointsScoredTeamDashboard           Team stats split by total points scored by Teams team in game.
        3       PontsAgainstTeamDashboard           Team stats split by total points scored by opposing team in game.
    ========   =================================   ====================================================================

    """
    params = locals()
    endpoint = 'teamdashboardbyteamperformance'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_byyear(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                Month=enums.Month.Default, OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                VsDivision=enums.VsDivision.Default):
    """
    Team stats breakdown by year or overall.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param idx_data: the index to retrieve data from json.
    :type idx_data: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
    :type GameSegment: nba.nba.bin.enums.GameSegment
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
    :type PORound: nba.nba.bin.enums.PORound
    :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
    :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
    :returns: Team stats after applying all filters by season or overall. Shown in idx_data table below.
    :rtype: Dataframe

    ========   ========================   ======================================
    idx_data           Name                          Description
    ========   ========================   ======================================
        0       OverallTeamDashboard     Overall Team stats with no splits.
        1       ByYearTeamDashboard      Team stats split by season.
    ========   ========================   ======================================

    """
    params = locals()
    endpoint = 'teamdashboardbyyearoveryear'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df


def team_byseason(TeamID, LeagueID=enums.LeagueID.Default, SeasonType=enums.SeasonType.Default, PerMode=enums.PerMode.Default):
    """
    Team stats breakdown by season.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :returns: Team stats after applying all filters by season.
    :rtype: Dataframe

    """
    params = locals()
    endpoint = 'teamyearbyyearstats'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_gamelog(TeamID, Season=enums.Season.Current, SeasonType=enums.SeasonType.Default, DateFrom=enums.DateFrom.Default,
                 DateTo=enums.DateTo.Default):
    """
    Team game logs.

    :param TeamID: Team to retrieve data for.
    :type TeamID: int
    :param Season: Season to get teams from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :returns: Team game logs after applying all filters.
    :rtype: Dataframe

    """
    params= locals()
    endpoint = 'teamgamelog'
    r = request_data(params, endpoint)
    df = parse_result_json(r, 0, 'resultSets')
    return df


def team_playeronoff(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default, SeasonType=enums.SeasonType.Default,
                     PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                     PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, DateFrom=enums.DateFrom.Default,
                     DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                     LastNGames=enums.LastNGames.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                     OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default,
                     VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Team stats details breakdown by player when on|off court.

    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :returns: Team stats details breakdown by player when on|off court..
    :rtype: Dataframe

    ========   ======================================   =============================================
    idx_data                  Name                                      Description
    ========   ======================================   =============================================
        0       OverallTeamPlayerOnOffDetails            Overall Team stats with no splits.
        1       PlayersOnCourtTeamPlayerOnOffDetails     Team stats by player when they are on court.
        2       PlayersOffCourtTeamPlayerOnOffDetails    Team stats by player when they are on court.
    ========   ======================================   =============================================

    """
    params = locals()
    endpoint = 'teamplayeronoffdetails'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df

def team_playerstats(TeamID, idx_data, LeagueID=enums.LeagueID.Default, Season=enums.Season.Default,
                     SeasonType=enums.SeasonType.Default,
                     PerMode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                     PlusMinus=enums.PlusMinus.Default,
                     PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, DateFrom=enums.DateFrom.Default,
                     DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                     Period=enums.Period.Default,
                     LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                     Month=enums.Month.Default,
                     OpponentTeamID=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                     SeasonSegment=enums.SeasonSegment.Default,
                     VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
    """
    Team stats details breakdown by player.

    :param TeamID: ID of specific team to filter. Default 0, returns all.
    :type TeamID nba.nba.bin.enums.TeamID
    :param LeagueID: ID of the league to get data for. Default 00. Required.
    :type LeagueID: nba.nba.bin.enums.LeagueID
    :param Season: Season to get players from. Required.
    :type Season: nba.nba.bin.enums.Season
    :param SeasonType: part of season to pull data from. Required.
    :type SeasonType: nba.nba.bin.enums.SeasonType
    :param PerMode: grouping of stat data. Totals or PerGame accepted. Required.
    :type PerMode: nba.nba.bin.enums.PerMode
    :param MeasureType: Type of stats to return. Default 'Base'. Required
    :type MeasureType: nba.nba.bin.enums.MeasureType
    :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
    :type PlusMinus: nba.nba.bin.enums.PlusMinus
    :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
    :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
    :param Rank: whether to include stat ranks, Y|N. Default N. Required
    :type Rank: nba.nba.bin.enums.Rank
    :param Outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
    :type Outcome nba.nba.bin.enums.Outcome
    :param Location: Filter for home or road games only. Default '' returns all. Required.
    :type Location: nba.nba.bin.enums.Location
    :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
    :type Month: nba.nba.bin.enums.Month
    :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
    :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
    :param DateFrom: Minimum date cutoff to include data from. Default '' returns all. Required.
    :type DateFrom: nba.nba.bin.enums.DateFrom
    :param DateTo:  Maximum date cutoff to include data to. Default '' returns all. Required.
    :type DateTo: nba.nba.bin.enums.DateTo
    :param OpponentTeamID: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
    :type OpponentTeamID: nba.nba.bin.enums.TeamID
    :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
    :type VsConference: nba.nba.bin.enums.VsConference
    :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
    :type VsDivision: nba.nba.bin.enums.VsDivision
    :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
    :type Period: nba.nba.bin.enums.Period
    :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
    :type LastNGames: nba.nba.bin.enums.LastNGames
    :returns: Team stats details breakdown by player when on|off court..
    :rtype: Dataframe

    ========   ====================   =============================================
    idx_data          Name                          Description
    ========   ====================   =============================================
        0       TeamOverall            Overall Team stats with no splits.
        1       PlayersSeasonTotals    Players season total stats.
    ========   ====================   =============================================

    """
    params = locals()
    endpoint = 'teamplayeronoffdetails'
    r = request_data(params, endpoint)
    df = parse_result_json(r, idx_data, 'resultSets')
    return df
