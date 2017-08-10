
from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Player(BaseEndpoint):
    
    def ranked_stats_breakdown(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, 
                               season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, 
                               stat_category=enums.Stat.PTS, scope=enums.Scope.Default, ActiveFlag=True):
        """
        Player ranked stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
        :param stat_category: stat to rank players by. Default 'PTS'. Required.
        :type stat_category: nba.nba.bin.enums.Stat
        :param scope: defines the type of players to include. Default 'S' returns all. Required.
        :type scope: nba.nba.bin.enums.Scope
        :param ActiveFlag: whether to only include active players. Default True.
        :returns: players ranked by stat specified.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leagueleaders'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSet')
        return df
    
    
    def player_bio(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                   per_mode=enums.PerMode.Default, team_id=enums.TeamID.Default, College=enums.College.Default,
                   Conference=enums.Conference.Default, Country=enums.Country.Default, DateFrom=enums.DateFrom.Default,
                   DateTo=enums.DateTo.Default, Division=enums.Division.Default, DraftPick=enums.DraftPick.Default,
                   DraftYear=enums.DraftYear.Default, GameSegment=enums.GameSegment.Default,
                   Height=enums.Height.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                   Weight=enums.Weight.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                   Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default, PORound=enums.PORound.Default,
                   PlayerExperience=enums.PlayerExperience.Default, PlayerPosition=enums.PlayerPosition.Default,
                   SeasonSegment=enums.SeasonSegment.Default, ShotClockRange=enums.ShotClockRange.Default,
                   StarterBench=enums.StarterBench.Default, VsConference=enums.VsConference.Default,
                   VsDivision=enums.VsDivision.Default):
        """
        Player bio data and stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param DateFrom: Minimum date cutoff to include data from. Default '' returns all.
        :type DateFrom: nba.nba.bin.enums.DateFrom
        :param DateTo:  Maximum date cutoff to include data to. Default '' returns all.
        :type DateTo: nba.nba.bin.enums.DateTo
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
        :type GameSegment: nba.nba.bin.enums.GameSegment
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
        :type Period: nba.nba.bin.enums.Period
        :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games.
        :type LastNGames: nba.nba.bin.enums.LastNGames
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param Location: Filter for home or road games only. Default '' returns all.
        :type Location: nba.nba.bin.enums.Location
        :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
        :type Month: nba.nba.bin.enums.Month
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
        :param Outcome: Filter to only include stats for won or lost games. Default '' returns all.
        :type Outcome nba.nba.bin.enums.Outcome
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param PlayerExperience: Filter to only include players of specific experience level. Default '' returns all.
        :type PlayerExperience: nba.nba.bin.enums.PlayerExperience
        :param PlayerPosition: Filter to only include players of certain position. Default '' returns all.
        :type PlayerPosition: nba.nba.bin.enums.PlayerPosition
        :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :param StarterBench: Filter to only include starts or bench. Default '' returns all.
        :type StarterBench: nba.nba.bin.enums.StarterBench
        :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all.
        :type VsConference: nba.nba.bin.enums.VsConference
        :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all.
        :type VsDivision: nba.nba.bin.enums.VsDivision
        :returns: Player bio stats and boxscore stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerbiostats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_clutch(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                      ClutchTime=enums.ClutchTime.mins5, AheadBehind=enums.AheadBehind.Default, PointDiff=100,
                      Gamescope=enums.GameScope.Blank, PlayerExperience=enums.PlayerExperience.Default, PlayerPosition=enums.PlayerPosition.Default,
                      StarterBench=enums.StarterBench.Default, MeasureType=enums.MeasureType.Default, per_mode=enums.PerMode.Default,
                      PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                      Outcome=enums.Outcome.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                      SeasonSegment=enums.SeasonSegment.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                      Opponentteam_id=enums.OpponentTeamID.Default, VsConference=enums.VsConference.Default,
                      VsDivision=enums.VsDivision.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                      LastNGames=enums.LastNGames.Default, College=enums.College.Default, Conference=enums.Conference.Default,
                      Country=enums.Country.Default, Division=enums.Division.Default, DraftPick=enums.DraftPick.Default,
                      DraftYear=enums.DraftYear.Default, team_id=enums.TeamID.Default, Height=enums.Height.Default,
                      Weight=enums.Weight.Default, PORound=enums.PORound.Default, ShotClockRange=enums.ShotClockRange.Default):
        """
        Player clutch stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param ClutchTime: Filter for stats occurring with less than this amount of time to play in the game. Default 5mins. Required.
        :type ClutchTime: nba.nba.bin.enums.ClutchTime
        :param AheadBehind: filter to only include when team is behind|ahead. Default includes all. Required
        :type AheadBehind: nba.nba.bin.enums.AheadBehind
        :param PointDiff: Absolute difference between teams for stats to be included. Required.
        :type PointDiff: int
        :param Gamescope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type Gamescope: nba.nba.bin.enums.GameScope
        :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type PlusMinus: nba.nba.bin.enums.PlusMinus
        :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
        :param Rank: whether to include stat ranks, Y|N. Default N. Required
        :type Rank: nba.nba.bin.enums.Rank
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :returns: Player clutch stats after applying all filters.
        :rtype: Dataframe
    
         """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerclutch'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_ptshot(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                      per_mode=enums.PerMode.Default, CloseDefDistRange=enums.CloseDefDistRange.Default,
                      DribbleRange=enums.DribbleRange.All, ShotClockRange=enums.ShotClockRange.Default, ShotDistRange='',
                      TouchTimeRange='', GeneralRange='', team_id=enums.TeamID.Default, College=enums.College.Default,
                      Conference=enums.Conference.Default, Country=enums.Country.Default, DateFrom=enums.DateFrom.Default,
                      DateTo=enums.DateTo.Default, Division=enums.Division.Default, DraftPick=enums.DraftPick.Default,
                      DraftYear=enums.DraftYear.Default, GameSegment=enums.GameSegment.Default, Height=enums.Height.Default,
                      Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Weight=enums.Weight.Default,
                      Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                      Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
                      PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default,
                      StarterBench=enums.StarterBench.Default, VsConference=enums.VsConference.Default,
                      VsDivision=enums.VsDivision.Default):
        """
        Player shot stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param DateFrom: Minimum date cutoff to include data from. Default '' returns all.
        :type DateFrom: nba.nba.bin.enums.DateFrom
        :param DateTo:  Maximum date cutoff to include data to. Default '' returns all.
        :type DateTo: nba.nba.bin.enums.DateTo
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param GameSegment: Filter to include only certain parts of games. Default '' includes entire games.
        :type GameSegment: nba.nba.bin.enums.GameSegment
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
        :type Period: nba.nba.bin.enums.Period
        :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games.
        :type LastNGames: nba.nba.bin.enums.LastNGames
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param Location: Filter for home or road games only. Default '' returns all.
        :type Location: nba.nba.bin.enums.Location
        :param Month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
        :type Month: nba.nba.bin.enums.Month
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
        :param Outcome: Filter to only include stats for won or lost games. Default '' returns all.
        :type Outcome nba.nba.bin.enums.Outcome
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param PlayerExperience: Filter to only include players of specific experience level. Default '' returns all.
        :type PlayerExperience: nba.nba.bin.enums.PlayerExperience
        :param PlayerPosition: Filter to only include players of certain position. Default '' returns all.
        :type PlayerPosition: nba.nba.bin.enums.PlayerPosition
        :param SeasonSegment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type SeasonSegment: nba.nba.bin.enums.SeasonSegment
        :param StarterBench: Filter to only include starts or bench. Default '' returns all.
        :type StarterBench: nba.nba.bin.enums.StarterBench
        :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all.
        :type VsConference: nba.nba.bin.enums.VsConference
        :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all.
        :type VsDivision: nba.nba.bin.enums.VsDivision
        :returns: Player shot stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerptshot'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_shotlocations(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                             per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                             PaceAdjust=enums.PaceAdjust.Default, Rank = enums.Rank.Default, DistanceRange=enums.DistanceRange.Default,
                             ShotClockRange=enums.ShotClockRange.Default, Gamescope=enums.GameScope.Blank,
                             team_id=enums.TeamID.Default, College=enums.College.Default, Conference=enums.Conference.Default,
                             Country=enums.Country.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                             Division=enums.Division.Default, DraftPick=enums.DraftPick.Default, DraftYear=enums.DraftYear.Default,
                             GameSegment=enums.GameSegment.Default, Height=enums.Height.Default, Period=enums.Period.Default,
                             LastNGames=enums.LastNGames.Default, Weight=enums.Weight.Default, Location=enums.Location.Default,
                             Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                             PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
                             PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default,
                             StarterBench=enums.StarterBench.Default, VsConference=enums.VsConference.Default,
                             VsDivision=enums.VsDivision.Default):
        """
        Player shot stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
        :param MeasureType: Type of stats to return. Default 'Base'. Required
        :type MeasureType: nba.nba.bin.enums.MeasureType
        :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type PlusMinus: nba.nba.bin.enums.PlusMinus
        :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
        :param Rank: whether to include stat ranks, Y|N. Default N. Required
        :type Rank: nba.nba.bin.enums.Rank
        :param DistanceRange: Filter shots to include by range buckets. Default '' includes all. Required.
        :type DistanceRange: nba.nba.bin.enums.DistanceRange
        :param Gamescope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type Gamescope: nba.nba.bin.enums.GameScope
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :returns: Player shot stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayershotlocations'
        r = self.request(endpoint, params)
        df = pd.DataFrame(data=r.get('resultSets').get('rowSet'),columns=r.get('resultSets').get('headers')[1].get('columnNames'))
        return df
    
    
    def player_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                     per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                     PaceAdjust=enums.PaceAdjust.Default, Rank = enums.Rank.Default, DistanceRange=enums.DistanceRange.Default,
                     ShotClockRange=enums.ShotClockRange.Default, Gamescope=enums.GameScope.Blank,
                     team_id=enums.TeamID.Default, College=enums.College.Default, Conference=enums.Conference.Default,
                     Country=enums.Country.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                     Division=enums.Division.Default, DraftPick=enums.DraftPick.Default, DraftYear=enums.DraftYear.Default,
                     GameSegment=enums.GameSegment.Default, Height=enums.Height.Default, Period=enums.Period.Default,
                     LastNGames=enums.LastNGames.Default, Weight=enums.Weight.Default, Location=enums.Location.Default,
                     Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                     PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
                     PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default,
                     StarterBench=enums.StarterBench.Default, VsConference=enums.VsConference.Default,
                     VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
        :param MeasureType: Type of stats to return. Default 'Base'. Required
        :type MeasureType: nba.nba.bin.enums.MeasureType
        :param PlusMinus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type PlusMinus: nba.nba.bin.enums.PlusMinus
        :param PaceAdjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type PaceAdjust: nba.nba.bin.enums.PaceAdjust
        :param Rank: whether to include stat ranks, Y|N. Default N. Required
        :type Rank: nba.nba.bin.enums.Rank
        :param Gamescope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type Gamescope: nba.nba.bin.enums.GameScope
        :param DistanceRange: Filter shots to include by range buckets. Default '' includes all. Required.
        :type DistanceRange: nba.nba.bin.enums.DistanceRange
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :returns: Player stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerstats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_ptdefend(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                        per_mode=enums.PerMode.Default, DefenseCategory=enums.DefenseCategory.Default, College=enums.College.Default,
                        Conference=enums.Conference.Default, Country=enums.Country.Default, DateFrom=enums.DateFrom.Default,
                        DateTo=enums.DateTo.Default, Division=enums.Division.Default, DraftPick=enums.DraftPick.Default,
                        DraftYear=enums.DraftYear.Default, Gamescope=enums.GameScope.Default, PlayerID=enums.TeamID.Default,
                        team_id=enums.TeamID.Default, GameSegment=enums.GameSegment.Default, Height=enums.Height.Default,
                        Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Weight=enums.Weight.Default,
                        Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                        Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
                        PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default,
                        ShotClockRange=enums.ShotClockRange.Default, StarterBench=enums.StarterBench.Default,
                        VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player defensive stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param PlayerExperience: Filter to only include players of specific experience level. Default '' returns all.
        :type PlayerExperience: nba.nba.bin.enums.PlayerExperience
        :param PlayerPosition: Filter to only include players of certain position. Default '' returns all.
        :type PlayerPosition: nba.nba.bin.enums.PlayerPosition
        :param StarterBench: Filter to only include starts or bench. Default '' returns all.
        :type StarterBench: nba.nba.bin.enums.StarterBench
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param PlayerID: ID of specific player to filter. Default 0, returns all.
        :type PlayerID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :returns: Player defensive stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashptdefend'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_ptstats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                       per_mode=enums.PerMode.Default, PtMeasureType=enums.PtMeasureType.ShootingEfficiency,
                       PlayerOrTeam=enums.PlayerOrTeam.Player, College=enums.College.Default, Conference=enums.Conference.Default,
                       Country=enums.Country.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                       Division=enums.Division.Default, DraftPick=enums.DraftPick.Default, DraftYear=enums.DraftYear.Default,
                       Gamescope=enums.GameScope.Blank, PlayerID=enums.TeamID.Default, team_id=enums.TeamID.Default,
                       GameSegment=enums.GameSegment.Default, Height=enums.Height.Default, Period=enums.Period.Default,
                       LastNGames=enums.LastNGames.Default, Weight=enums.Weight.Default, Location=enums.Location.Default,
                       Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                       PORound=enums.PORound.Default, PlayerExperience=enums.PlayerExperience.Default,
                       PlayerPosition=enums.PlayerPosition.Default, SeasonSegment=enums.SeasonSegment.Default,
                       ShotClockRange=enums.ShotClockRange.Default, StarterBench=enums.StarterBench.Default,
                       VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player scoring stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
        :param PtMeasureType: Filter the type of shots and stats returned. Default 'Efficiency' returns all. Required.
        :type PtMeasureType: nba.nba.bin.enums.PtMeasureType
        :param PlayerOrTeam: whether to return stats by player or team. Default 'Player'. Required.
        :type PlayerOrTeam: nba.nba.bin.enums.PlayerOrTeam
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type TeamID nba.nba.bin.enums.TeamID
        :param PlayerID: ID of specific player to filter. Default 0, returns all.
        :type PlayerID nba.nba.bin.enums.TeamID
        :param College: Filter for players attending specific college. Default '' returns all.
        :type College: nba.nba.bin.enums.College
        :param Conference: Filter for players from specific conference. Default '' returns all.
        :type Conference: nba.nba.bin.enums.Conference
        :param Country: Filter for players from specific country. Default '' returns all.
        :type Country: nba.nba.bin.enums.Country
        :param Division: Filter by specific division. Default '' returns all.
        :type Division: nba.nba.bin.enums.Division
        :param DraftPick: Filter by players pick in the draft. Default '' returns all.
        :type DraftPick: nba.nba.bin.enums.DraftPick
        :param DraftYear: Filter by year of the players draft. Default '' returns all.
        :type DraftYear: nba.nba.bin.enums.DraftYear
        :param Height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type Height: nba.nba.bin.enums.Height
        :param Weight: Filter by players weight in lbs. Default '' returns all.
        :type Weight: nba.nba.bin.enums.Weight
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :returns: Player scoring stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashptstats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_careerstats(self, PlayerID, idx_data, per_mode=enums.PerMode.Default):
        """
        Get career or season individual player stats breakdown.
    
        :param PlayerID: ID of the player for whom to get stats breakdown.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
        :returns:
        :rtype: Dataframe
    
        ========   ============================   ===============================================================
        idx_data              Name                                         Description
        ========   ============================   ===============================================================
            0       SeasonTotalsRegularSeason      Breakdown by season of players Regular Season box score stats.
            1       CareerTotalsRegularSeason      Players career Regular Season box score stats.
            2       SeasonTotalsPostSeason         Breakdown by season of players Post Season box score stats.
            3       CareerTotalsPostSeason         Players career Post Season box score stats.
            4       SeasonTotalsAllStarSeason      Breakdown by season of players All Star box score stats.
            5       CareerTotalsAllStarSeason      Players career All Star box score stats.
            6       SeasonTotalsCollegeSeason      Breakdown by season of players College box score stats.
            7       CareerTotalsCollegeSeason      Players career College box score stats.
            8       SeasonRankingsRegularSeason    Breakdown by season of players Regular Season ranking in box score stats.
            9       SeasonRankingsPostSeason       Players career Regular Season ranking in box score stats.
        ========   ============================   ===============================================================
    
        """
        endpoint = 'playercareerstats'
        params = {'PlayerID': PlayerID, 'PerMode': PerMode}
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def league_gamelog(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                       PlayerOrTeam=enums.PlayerOrTeam.Player[0], Sorter=enums.Stat.PTS, Direction=enums.Direction.Descending,
                       Counter=0, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default):
    
    
        """
        Get game logs sorted by specific stat.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param PlayerOrTeam: whether to return stats by player or team. Default 'P'. Required.
        :type PlayerOrTeam: nba.nba.bin.enums.PlayerOrTeam, first letter only
        :param Sorter: stat to sort players/teams logs by.
        :type Sorter: nba.nba.bin.enums.Stat
        :param Direction: direction to sort stat in. Default Descending.
        :type Direction: nba.nba.bin.enums.Direction
        :param Counter:
        :type Counter: int
        :param DateFrom: Minimum date cutoff to include data from. Default '' returns all.
        :type DateFrom: nba.nba.bin.enums.DateFrom
        :param DateTo:  Maximum date cutoff to include data to. Default '' returns all.
        :type DateTo: nba.nba.bin.enums.DateTo
        :returns: Game logs stats after applying all filters.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguegamelog'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_compare(self, PlayerID, VsPlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                       season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                       PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                       ShotClockRange=enums.ShotClockRange.Default, Conference=enums.Conference.Default, DateFrom=enums.DateFrom.Default,
                       DateTo=enums.DateTo.Default, Division=enums.Division.Default, GameSegment=enums.GameSegment.Default,
                       Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                       Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                       PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                       VsDivision=enums.VsDivision.Default):
        """
        Comparison of two players.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param VsPlayerID: Player ID for Player 2 in comparison.
        :type  VsPlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param PORound: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type PORound: nba.nba.bin.enums.PORound
        :param ShotClockRange: Filter to specific shot clock time windows. Default '' returns all.
        :type ShotClockRange: nba.nba.bin.enums.ShotClockRange
        :returns: Player stats comparison after applying all filters.
        :rtype: Dataframe
    
        ========   ================   ===============================================================
        idx_data         Name                               Description
        ========   ================   ===============================================================
            0       OverallCompare     Overall comparison of player 1 vs player 2.
            1       Individual         Individual player breakdowns.
        ========   ================   ===============================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playercompare'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_byclutch(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                        per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                        PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                        DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                        Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                        Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                        PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                        VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player clutch stats breakdown.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player clutch stats after applying all filters.
        :rtype: Dataframe
    
        ========   =======================================   ==============================================================
        idx_data                   Name                                            Description
        ========   =======================================   ==============================================================
            0       OverallPlayerDashboard                    Overall player clutch stats breakdown.
            1       Last5Min5PointPlayerDashboard             Players stats with time to play <= 5mins and point diff <= 5
            2       Last3Min5PointPlayerDashboard             Players stats with time to play <= 3mins and point diff <= 5
            3       Last1Min5PointPlayerDashboard             Players stats with time to play <= 1mins and point diff <= 5
            4       Last30Sec3PointPlayerDashboard            Players stats with time to play <= 30secs and point diff <= 3
            5       Last10Sec3PointPlayerDashboard            Players stats with time to play <= 10secs and point diff <= 3
            6       Last5MinPlusMinus5PointPlayerDashboard    Players stats with time to play <= 5mins or point diff <= 5
            7       Last3MinPlusMinus5PointPlayerDashboard    Players stats with time to play <= 3mins or point diff <= 5
            8       Last1MinPlusMinus5PointPlayerDashboard    Players stats with time to play <= 1mins or point diff <= 5
            9       Last30Sec3Point2PlayerDashboard           Players stats with time to play <= 30secs and point diff <= 2
            10      Last10Sec3Point2PlayerDashboard           Players stats with time to play <= 10secs and point diff <= 2
        ========   =======================================   ==============================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbyclutch'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_bygamesplits(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                            per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                            PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                            DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                            Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                            Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                            PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                            VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by score bucket|period|half or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ==============================   ====================================================================
        idx_data                   Name                                           Description
        ========   ==============================   ====================================================================
            0       OverallPlayerDashboard           Overall player stats with no splits.
            1       ByHalfPlayerDashboard            Player stats split by half in which they occurred.
            2       ByPeriodPlayerDashboard          Player stats split by period in which they occurred.
            3       ByScoreMarginPlayerDashboard     Player stats split by absolute point diff bucket when they occurred.
            4       ByActualMarginPlayerDashboard    Player stats split by actual point diff bucket when they occurred.
        ========   ==============================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbygamesplits'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def shotchart_detail(self, PlayerID, idx_data, GameID=enums.Default_Values.Blank, ContextMeasure=enums.ContextMeasure.FGA,
                         ClutchTime=enums.ClutchTime.Default, AheadBehind=enums.AheadBehind.Default, PointDiff=100,
                         StartPeriod=enums.Default_Values.Blank, EndPeriod=enums.Default_Values.Blank,
                         StartRange=enums.Default_Values.Blank, EndRange=enums.Default_Values.Blank,
                         league_id=enums.LeagueID.Default, season_type=enums.SeasonType.Default, DateFrom=enums.DateFrom.Default,
                         DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default, season=enums.Default_Values.Blank,
                         team_id=enums.TeamID.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                         Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                         Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                         VsDivision=enums.VsDivision.Default, PlayerPosition=enums.PlayerPosition.All,
                         RookieYear=enums.Default_Values.Blank):
        """
        Get x,y data location and further details of shots for a player in a specific game.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param GameID: ID of a specific game. Default '' returns all. Required.
        :type GameID: int
        :param ContextMeasure: Type of shot to get data for. Default FGA. Required.
        :type ContextMeasure: nba.nba.bin.enums.ContextMeasure
        :param ClutchTime: Filter for stats occurring with less than this amount of time to play in the game. Default 5mins. Required.
        :type ClutchTime: nba.nba.bin.enums.ClutchTime
        :param AheadBehind: filter to only include when team is behind|ahead. Default includes all. Required
        :type AheadBehind: nba.nba.bin.enums.AheadBehind
        :param PointDiff: Absolute difference between teams for stats to be included. Required.
        :type PointDiff: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Default '' returns all. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :param RookieYear: filter by the year in which the player was a rookie.
        :type RookierYear: str('%Y-%y')
        :returns: Player shot locations after applying all filters. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ==================   ====================================================================
        idx_data         Name                             Description
        ========   ==================   ====================================================================
            0       Shot_Chart_Detail    Individual shot breakdown.
            1       LeagueAverages       League average and totals by zone, area and range.
        ========   ==================   ====================================================================
    
    
        """
        params = clean_locals(locals())
        endpoint = 'shotchartdetail'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_bygeneralsplits(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                               per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                               PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                               DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                               Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                               Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                               PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                               VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by score bucket|period|half or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ==============================   ====================================================================
        idx_data              Name                                           Description
        ========   ==============================   ====================================================================
            0       OverallPlayerDashboard           Overall player stats with no splits.
            1       LocationPlayerDashboard          Player stats split by home|road location in which they occurred.
            2       WinsLossesPlayerDashboard        Player stats split by game result in which they occurred.
            3       MonthPlayerDashboard             Player stats split by month in which they occurred.
            4       PrePostAllStarPlayerDashboard    Player stats split by pre post all star break.
            5       StartingPosition                 Player stats split by whether player started or was on bench.
            6       DaysRestPlayerDashboard          Player stats split by no. days rest.
        ========   ==============================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbygeneralsplits'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_bylastngames(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                            season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                            PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                            ShotClockRange=enums.ShotClockRange.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                            GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                            Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                            Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                            VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by pre defined number of most recent games or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters in pervious N games or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ==========================   =======================================================
        idx_data              Name                            Description
        ========   ==========================   =======================================================
            0       OverallPlayerDashboard       Overall player stats with no splits.
            1       Last5PlayerDashboard         Player stats in most recent 5 games.
            2       Last10PlayerDashboard        Player stats in most recent 10 games.
            3       Last15PlayerDashboard        Player stats in most recent 15 games.
            4       Last20PlayerDashboard        Player stats in most recent 20 games.
            5       GameNumberPlayerDashboard    Player stats split by buckets of 10 most recent games.
        ========   ==========================   =======================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbylastngames'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_byopponent(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                          season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                          PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                          ShotClockRange=enums.ShotClockRange.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                          GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                          Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                          Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                          VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by opponent or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by conference|division|team or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ==============================   ====================================================================
        idx_data              Name                                           Description
        ========   ==============================   ====================================================================
            0       OverallPlayerDashboard           Overall player stats with no splits.
            1       ConferencePlayerDashboard        Player stats split by conference of team against whom they occurred.
            2       DivisionPlayerDashboard          Player stats split by division of team against whom they occurred.
            3       OpponentPlayerDashboard          Player stats split by team against whom they occurred.
        ========   ==============================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbyopponent'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_byshootingsplits(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                                season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                                PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                                ShotClockRange=enums.ShotClockRange.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                                GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                                Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                                Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                                VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by shot type, zone and distance or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by shot zone|type|distance|assist or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ==============================   ====================================================================
        idx_data              Name                                           Description
        ========   ==============================   ====================================================================
            0       OverallPlayerDashboard           Overall player stats with no splits.
            1       Shot5FTPlayerDashboard           Player stats split by shot distance as granular as 5ft range.
            2       Shot8FTPlayerDashboard           Player stats split by shots distance as granular as 8ft range.
            3       ShotAreaPlayerDashboard          Player stats split by shot area.
            4       AssitedShotPlayerDashboard       Player stats split by Assisted|Unassisted.
            5       ShotTypeSummaryPlayerDashboard   Player stats split by Shot Type.
            6       ShotTypePlayerDashboard          Player stats split by more granular shot type.
            7       AssistedBy                       Player stats split by player assisting.
        ========   ==============================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbyshootingsplits'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_byteamperformance(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                                 season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                                 PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                                 ShotClockRange=enums.ShotClockRange.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                                 GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                                 Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                                 Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                                 VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by team performance or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by points for|against|difference or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   =================================   ====================================================================
        idx_data                Name                                           Description
        ========   =================================   ====================================================================
            0       OverallPlayerDashboard              Overall player stats with no splits.
            1       ScoreDifferentialPlayerDashboard    Player stats split by games final score differential.
            2       PointsScoredPlayerDashboard         Player stats split by total points scored by players team in game.
            3       PontsAgainstPlayerDashboard         Player stats split by total points scored by opposing team in game.
        ========   =================================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbyteamperformance'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_byyear(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                      season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default,
                      PlusMinus=enums.PlusMinus.Default, PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default,
                      ShotClockRange=enums.ShotClockRange.Default, DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default,
                      GameSegment=enums.GameSegment.Default, Period=enums.Period.Default, LastNGames=enums.LastNGames.Default,
                      Location=enums.Location.Default, Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default,
                      Outcome=enums.Outcome.Default, PORound=enums.PORound.Default, SeasonSegment=enums.SeasonSegment.Default,
                      VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player stats breakdown by year or overall.
    
        :param PlayerID: player ID for Player 1 in comparison.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by season or overall. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ========================   ======================================
        idx_data           Name                          Description
        ========   ========================   ======================================
            0       OverallPlayerDashboard     Overall player stats with no splits.
            1       ByYearPlayerDashboard      Player stats split by season.
        ========   ========================   ======================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbyyearoveryear'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_passing(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                       season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default,
                       DateTo=enums.DateTo.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                       Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                       SeasonSegment=enums.SeasonSegment.Default, VsConference=enums.VsConference.Default,
                       VsDivision=enums.VsDivision.Default):
        """
        Player pass stats breakdown by received|made.
    
        :param PlayerID: player ID to retrieve data for.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
        :param VsConference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type VsConference: nba.nba.bin.enums.VsConference
        :param VsDivision: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type VsDivision: nba.nba.bin.enums.VsDivision
        :param LastNGames: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type LastNGames: nba.nba.bin.enums.LastNGames
        :returns: Player stats after applying all filters by passes made|received. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ===============   ==================================================
        idx_data        Name                           Description
        ========   ===============   ==================================================
            0       PassesMade        Breakdown of passes made by player thrown to.
            1       PassesReceived	  Breakdown of passes received by player thrown by.
        ========   ===============   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashptpass'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_rebounding(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                          season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default,
                          DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                          LastNGames=enums.LastNGames.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                          Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default,
                          VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player rebounding stats breakdown by shot|shot distance|rebound distance|contest or overall.
    
        :param PlayerID: player ID to retrieve data for.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by passes made|received. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   =======================   ========================================================
        idx_data            Name                                   Description
        ========   =======================   ========================================================
            0       OverallRebounding         Overall player rebounding stats..
            1       ShotTypeRebounding	      Player rebounding stats by shot type.
            2       NumContestedRebounding    Player rebounding stats by number of people contesting.
            3       ShotDistanceRebounding    Player rebounding stats by shot distance.
            4       RebDistanceRebounding     Player rebounding stats by rebound distance.
        ========   =======================   ========================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashptreb'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def player_shotdefense(self, PlayerID, league_id=enums.LeagueID.Default, season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default,
                           DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                           LastNGames=enums.LastNGames.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                           Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default,
                           VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player shot defense success stats breakdown when player is the defender of the shot.
    
        :param PlayerID: player ID to retrieve data for.
        :type PlayerID: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters by shot success.
        :rtype: Dataframe
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashptshotdefend'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    
    def player_shooting(self, PlayerID, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                        season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, DateFrom=enums.DateFrom.Default,
                        DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default, Period=enums.Period.Default,
                        LastNGames=enums.LastNGames.Default, Location=enums.Location.Default, Month=enums.Month.Default,
                        Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default, SeasonSegment=enums.SeasonSegment.Default,
                        VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player shot success stats breakdown.
    
        :param PlayerID: player ID to retrieve data for.
        :type PlayerID: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player shooting stats after applying all filters by shot success.
        :rtype: Dataframe
    
        ========   ================================   ========================================================
        idx_data            Name                                   Description
        ========   ================================   ========================================================
            0       Overall                            Overall player shooting stats..
            1       GeneralShooting	                   Player shooting stats by basic shot type.
            2       ShotClockShooting                  Player shooting stats by time on shotclock buckets.
            3       DribbleShooting                    Player shooting stats by number of dribbles taken.
            4       ClosestDefenderShooting            Player shooting stats by distance to closest defender.
            5       ClosestDefender10ftPlusShooting    Player shooting stats Defender > 10ft.
            6       TouchTimeShooting                  Player shooting stats by time touching ball buckets.
        ========   ================================   ========================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashptshots'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    
    def players_vs_players(self, Team1ID, vs_team_id, PlayerID1, VsPlayerID1, idx_data, PlayerID2=enums.Default_Values.Zero, PlayerID3=enums.Default_Values.Zero,
                           PlayerID4=enums.Default_Values.Zero, PlayerID5=enums.Default_Values.Zero, VsPlayerID2=enums.Default_Values.Zero,
                           VsPlayerID3=enums.Default_Values.Zero, VsPlayerID4=enums.Default_Values.Zero, VsPlayerID5=enums.Default_Values.Zero,
                           league_id=enums.LeagueID.Default, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                           per_mode=enums.PerMode.Default, MeasureType=enums.MeasureType.Default, PlusMinus=enums.PlusMinus.Default,
                           PaceAdjust=enums.PaceAdjust.Default, Rank=enums.Rank.Default, ShotClockRange=enums.ShotClockRange.Default,
                           DateFrom=enums.DateFrom.Default, DateTo=enums.DateTo.Default, GameSegment=enums.GameSegment.Default,
                           Period=enums.Period.Default, LastNGames=enums.LastNGames.Default, Location=enums.Location.Default,
                           Month=enums.Month.Default, Opponentteam_id=enums.OpponentTeamID.Default, Outcome=enums.Outcome.Default,
                           Conference=enums.Conference.Default, Division=enums.Division.Default, SeasonSegment=enums.SeasonSegment.Default,
                           VsConference=enums.VsConference.Default, VsDivision=enums.VsDivision.Default):
        """
        Player|Players stats breakdown individually or combined whilst other players are on|off court.
    
        :param Team1ID: Team ID of the base team in comparison. Required.
        :type Team1ID: int
        :param vs_team_id: Team ID of the comparative team. Required.
        :type vs_team_id: int
        :param PlayerID1: player ID for Player 1 in comparison. Required.
        :type PlayerID1: int
        :param VsPlayerID1: player ID for VsTeam Player 1 in comparison. Required.
        :type VsPlayerID1: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param PlayerID2: player ID for Player 2 in comparison. Default 0 will not include a second player.
        :type PlayerID2: int
        :param VsPlayerID2: player ID for VsTeam Player 2 in comparison. Default 0 will not include a second player.
        :type VsPlayerID2: int
        :param PlayerID3: player ID for Player 3 in comparison. Default 0 will not include a third player.
        :type PlayerID3: int
        :param VsPlayerID3: player ID for VsTeam Player 3 in comparison. Default 0 will not include a third player.
        :type VsPlayerID3: int
        :param PlayerID4: player ID for Player 4 in comparison. Default 0 will not include a fourth player.
        :type PlayerID4: int
        :param VsPlayerID4: player ID for VsTeam Player 4 in comparison. Default 0 will not include a fourth player.
        :type VsPlayerID4: int
        :param PlayerID5: player ID for Player 5 in comparison. Default 0 will not include a fifth player.
        :type PlayerID5: int
        :param VsPlayerID5: player ID for VsTeam Player 5 in comparison. Default 0 will not include a fifth player.
        :type VsPlayerID5: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.nba.bin.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.nba.bin.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.nba.bin.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.nba.bin.enums.PerMode
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
        :param Opponentteam_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type Opponentteam_id: nba.nba.bin.enums.TeamID
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
        :returns: Player stats after applying all filters either grouped or individually. Shown in idx_data table below.
        :rtype: Dataframe
    
        ========   ================   ================================================================================
        idx_data        Name                                           Description
        ========   ================   ================================================================================
            0       OverallCompare     Overall combined stats of all players split by Team.
            1       Combined           Team1 players combined stats while all Team2 Players were on|off court split.
            2       Individual         Team1 players individual stats while all Team2 Players were on|off court split.
        ========   ================   ================================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playersvsplayers'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
