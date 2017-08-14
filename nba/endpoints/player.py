
import pandas as pd

from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Player(BaseEndpoint):
    
    def all_ranked_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                         season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                         stat_category=enums.Stat.PTS, scope=enums.Scope.Default, active_flag=True):
        """
        Player ranked stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param stat_category: stat to rank players by. Default 'PTS'. Required.
        :type stat_category: nba.enums.Stat
        :param scope: defines the type of players to include. Default 'S' returns all. Required.
        :type scope: nba.enums.Scope
        :param active_flag: whether to only include active players. Default True.
        :returns: players ranked by stat specified.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leagueleaders'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSet')
        return df

    def all_player_bios(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                        season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                        team_id=enums.TeamID.Default, college=enums.College.Default,
                        conference=enums.Conference.Default, country=enums.Country.Default,
                        date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default, division=enums.Division.Default,
                        draft_pick=enums.DraftPick.Default, draft_year=enums.DraftYear.Default,
                        game_segment=enums.GameSegment.Default, height=enums.Height.Default,
                        period=enums.Period.Default, last_n_games=enums.LastNGames.Default, weight=enums.Weight.Default,
                        location=enums.Location.Default, month=enums.Month.Default,
                        opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                        po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default,
                        player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                        shot_clock_range=enums.ShotClockRange.Default, starter_bench=enums.StarterBench.Default,
                        vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player bio data and stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param date_from: Minimum date cutoff to include data from. Default '' returns all.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all.
        :type date_to: nba.enums.DateTo
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param draft_pick: Filter by players pick in the draft. Default '' returns all.
        :type draft_pick: nba.enums.DraftPick
        :param draft_year: Filter by year of the players draft. Default '' returns all.
        :type draft_year: nba.enums.DraftYear
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type height: nba.enums.Height
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games.
        :type last_n_games: nba.enums.LastNGames
        :param weight: Filter by players weight in lbs. Default '' returns all.
        :type weight: nba.enums.Weight
        :param location: Filter for home or road games only. Default '' returns all.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
        :type month: nba.enums.Month
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all.
        :type opponent_team_id: nba.enums.TeamID
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all.
        :type outcome: nba.enums.Outcome
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: nba.enums.PlayerPosition
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type season_segment: nba.enums.SeasonSegment
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: nba.enums.StarterBench
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all.
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all.
        :type vs_division: nba.enums.VsDivision
        :returns: Player bio stats and boxscore stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerbiostats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def all_clutch_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                         season_type=enums.SeasonType.Default, clutch_time=enums.ClutchTime.mins5,
                         ahead_behind=enums.AheadBehind.Default, point_diff=100, game_scope=enums.GameScope.Blank,
                         player_experience=enums.PlayerExperience.Default, player_position=enums.PlayerPosition.Default,
                         starter_bench=enums.StarterBench.Default, measure_type=enums.MeasureType.Default,
                         per_mode=enums.PerMode.Default, plus_minus=enums.PlusMinus.Default,
                         pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default, outcome=enums.Outcome.Default,
                         location=enums.Location.Default, month=enums.Month.Default,
                         season_segment=enums.SeasonSegment.Default, date_from=enums.DateFrom.Default,
                         date_to=enums.DateTo.Default, opponent_team_id=enums.OpponentTeamID.Default,
                         vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default,
                         game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                         last_n_games=enums.LastNGames.Default, college=enums.College.Default,
                         conference=enums.Conference.Default, country=enums.Country.Default,
                         division=enums.Division.Default, draft_pick=enums.DraftPick.Default,
                         draft_year=enums.DraftYear.Default, team_id=enums.TeamID.Default, height=enums.Height.Default,
                         weight=enums.Weight.Default, po_round=enums.PORound.Default,
                         shot_clock_range=enums.ShotClockRange.Default):
        """
        Player clutch stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param clutch_time: Filter for stats occurring with less than this amount of time to play in the game. Default 5mins. Required.
        :type clutch_time: nba.enums.ClutchTime
        :param ahead_behind: filter to only include when team is behind|ahead. Default includes all. Required
        :type ahead_behind: nba.enums.AheadBehind
        :param point_diff: Absolute difference between teams for stats to be included. Required.
        :type point_diff: int
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type game_scope: nba.enums.GameScope
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all. Required.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all. Required.
        :type player_position: nba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all. Required
        :type starter_bench: nba.enums.StarterBench
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param draft_pick: Filter by players pick in the draft. Default '' returns all.
        :type draft_pick: nba.enums.DraftPick
        :param draft_year: Filter by year of the players draft. Default '' returns all.
        :type draft_year: nba.enums.DraftYear
        :param height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type height: nba.enums.Height
        :param weight: Filter by players weight in lbs. Default '' returns all.
        :type weight: nba.enums.Weight
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player clutch stats after applying all filters.
        :rtype: DataFrame
    
         """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerclutch'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def all_shot_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                       season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                       close_def_dist_range=enums.CloseDefDistRange.Default, dribble_range=enums.DribbleRange.All,
                       shot_clock_range=enums.ShotClockRange.Default, touch_time_range='', general_range='',
                       team_id=enums.TeamID.Default, college=enums.College.Default, conference=enums.Conference.Default,
                       country=enums.Country.Default, date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                       division=enums.Division.Default, draft_pick=enums.DraftPick.Default,
                       draft_year=enums.DraftYear.Default, game_segment=enums.GameSegment.Default,
                       height=enums.Height.Default, period=enums.Period.Default, last_n_games=enums.LastNGames.Default,
                       weight=enums.Weight.Default, location=enums.Location.Default, month=enums.Month.Default,
                       opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                       po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default,
                       player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                       starter_bench=enums.StarterBench.Default, vs_conference=enums.VsConference.Default,
                       vs_division=enums.VsDivision.Default):
        """
        Player shot stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param close_def_dist_range: Filter stats to include of shots with specific closest defender range. Default '' returns all.
        :type close_def_dist_range: nba.enums.CloseDefDistRange
        :param dribble_range: Filter stats to include only shots where specific no. of dribbles occured. Default '' returns all.
        :type dribble_range: nba.enums.DribbleRange
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :param touch_time_range: Filter by how long ball is held prior to shot. Default '' returns all.
        :type touch_time_range: unsure.
        :param general_range: No idea what this does.
        :type general_range: unsure.
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param date_from: Minimum date cutoff to include data from. Default '' returns all.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all.
        :type date_to: nba.enums.DateTo
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param draft_pick: Filter by players pick in the draft. Default '' returns all.
        :type draft_pick: nba.enums.DraftPick
        :param draft_year: Filter by year of the players draft. Default '' returns all.
        :type draft_year: nba.enums.DraftYear
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type height: nba.enums.Height
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games.
        :type last_n_games: nba.enums.LastNGames
        :param weight: Filter by players weight in lbs. Default '' returns all.
        :type weight: nba.enums.Weight
        :param location: Filter for home or road games only. Default '' returns all.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
        :type month: nba.enums.Month
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all.
        :type opponent_team_id: nba.enums.TeamID
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all.
        :type outcome: nba.enums.Outcome
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: nba.enums.PlayerPosition
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type season_segment: nba.enums.SeasonSegment
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: nba.enums.StarterBench
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all.
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all.
        :type vs_division: nba.enums.VsDivision
        :returns: Player shot stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayerptshot'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def all_shot_locations(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                           measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                           pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                           distance_range=enums.DistanceRange.Default, shot_clock_range=enums.ShotClockRange.Default,
                           game_scope=enums.GameScope.Blank, team_id=enums.TeamID.Default,
                           college=enums.College.Default, conference=enums.Conference.Default,
                           country=enums.Country.Default, date_from=enums.DateFrom.Default,
                           date_to=enums.DateTo.Default, division=enums.Division.Default,
                           draft_pick=enums.DraftPick.Default, draft_year=enums.DraftYear.Default,
                           game_segment=enums.GameSegment.Default, height=enums.Height.Default,
                           period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                           weight=enums.Weight.Default, location=enums.Location.Default, month=enums.Month.Default,
                           opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                           po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default,
                           player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                           starter_bench=enums.StarterBench.Default, vs_conference=enums.VsConference.Default,
                           vs_division=enums.VsDivision.Default):
        """
        Player shot stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param distance_range: Filter shots to include by range buckets. Default '' includes all. Required.
        :type distance_range: nba.enums.DistanceRange
        :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type game_scope: nba.enums.GameScope
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all. Required.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all. Required.
        :type player_position: nba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all. Required
        :type starter_bench: nba.enums.StarterBench
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param draft_pick: Filter by players pick in the draft. Default '' returns all.
        :type draft_pick: nba.enums.DraftPick
        :param draft_year: Filter by year of the players draft. Default '' returns all.
        :type draft_year: nba.enums.DraftYear
        :param height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type height: nba.enums.Height
        :param weight: Filter by players weight in lbs. Default '' returns all.
        :type weight: nba.enums.Weight
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player shot stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashplayershotlocations'
        r = self.request(endpoint, params)
        df = pd.DataFrame(
            data=r.get('resultSets').get('rowSet'), columns=r.get('resultSets').get('headers')[1].get('columnNames')
        )
        return df
    
    def all_raw_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                      season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                      measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                      pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                      distance_range=enums.DistanceRange.Default, shot_clock_range=enums.ShotClockRange.Default,
                      game_scope=enums.GameScope.Blank, team_id=enums.TeamID.Default, college=enums.College.Default,
                      conference=enums.Conference.Default, country=enums.Country.Default,
                      date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default, division=enums.Division.Default,
                      draft_pick=enums.DraftPick.Default, draft_year=enums.DraftYear.Default,
                      game_segment=enums.GameSegment.Default, height=enums.Height.Default,
                      last_n_games=enums.LastNGames.Default, weight=enums.Weight.Default,
                      location=enums.Location.Default, month=enums.Month.Default, period=enums.Period.AllQuarters,
                      opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                      po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default,
                      player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                      starter_bench=enums.StarterBench.Default, vs_conference=enums.VsConference.Default,
                      vs_division=enums.VsDivision.Default):
            """
            Player stats breakdown.
        
            :param league_id: ID of the league to get data for. Default 00. Required.
            :type league_id: nba.enums.LeagueID
            :param season: Season to get players from. Required.
            :type season: nba.enums.Season
            :param season_type: part of season to pull data from. Required.
            :type season_type: nba.enums.SeasonType
            :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
            :type per_mode: nba.enums.PerMode
            :param measure_type: Type of stats to return. Default 'Base'. Required
            :type measure_type: nba.enums.MeasureType
            :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
            :type plus_minus: nba.enums.PlusMinus
            :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
            :type pace_adjust: nba.enums.PaceAdjust
            :param rank: whether to include stat ranks, Y|N. Default N. Required
            :type rank: nba.enums.Rank
            :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
            :type game_scope: nba.enums.GameScope
            :param distance_range: Filter shots to include by range buckets. Default '' includes all. Required.
            :type distance_range: nba.enums.DistanceRange
            :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
            :type outcome: nba.enums.Outcome
            :param location: Filter for home or road games only. Default '' returns all. Required.
            :type location: nba.enums.Location
            :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
            :type month: nba.enums.Month
            :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
            :type season_segment: nba.enums.SeasonSegment
            :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
            :type date_from: nba.enums.DateFrom
            :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
            :type date_to: nba.enums.DateTo
            :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
            :type opponent_team_id: nba.enums.TeamID
            :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
            :type vs_conference: nba.enums.VsConference
            :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
            :type vs_division: nba.enums.VsDivision
            :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
            :type game_segment: nba.enums.GameSegment
            :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
            :type period: nba.enums.Period
            :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
            :type last_n_games: nba.enums.LastNGames
            :param player_experience: Filter to only include players of specific experience level. Default '' returns all. Required.
            :type player_experience: nba.enums.PlayerExperience
            :param player_position: Filter to only include players of certain position. Default '' returns all. Required.
            :type player_position: nba.enums.PlayerPosition
            :param starter_bench: Filter to only include starts or bench. Default '' returns all. Required
            :type starter_bench: nba.enums.StarterBench
            :param team_id: ID of specific team to filter. Default 0, returns all.
            :type team_id: nba.enums.TeamID
            :param college: Filter for players attending specific college. Default '' returns all.
            :type college: nba.enums.College
            :param conference: Filter for players from specific conference. Default '' returns all.
            :type conference: nba.enums.Conference
            :param country: Filter for players from specific country. Default '' returns all.
            :type country: nba.enums.Country
            :param division: Filter by specific division. Default '' returns all.
            :type division: nba.enums.Division
            :param draft_pick: Filter by players pick in the draft. Default '' returns all.
            :type draft_pick: nba.enums.DraftPick
            :param draft_year: Filter by year of the players draft. Default '' returns all.
            :type draft_year: nba.enums.DraftYear
            :param height: Filter by players height (doesn't appear to work). Default '' returns all.
            :type height: nba.enums.Height
            :param weight: Filter by players weight in lbs. Default '' returns all.
            :type weight: nba.enums.Weight
            :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
            :type po_round: nba.enums.PORound
            :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
            :type shot_clock_range: nba.enums.ShotClockRange
            :returns: Player stats after applying all filters.
            :rtype: DataFrame
        
            """
            params = clean_locals(locals())
            endpoint = 'leaguedashplayerstats'
            r = self.request(endpoint, params)
            df = self.process_response(r, 0, 'resultSets')
            return df

    def all_defensive_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                            season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                            defense_category=enums.DefenseCategory.Default, college=enums.College.Default,
                            conference=enums.Conference.Default, country=enums.Country.Default,
                            date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                            division=enums.Division.Default, draft_pick=enums.DraftPick.Default,
                            draft_year=enums.DraftYear.Default, game_scope=enums.GameScope.Default,
                            player_id=enums.TeamID.Default, team_id=enums.TeamID.Default,
                            game_segment=enums.GameSegment.Default, height=enums.Height.Default,
                            period=enums.Period.Default, last_n_games=enums.LastNGames.Default,
                            weight=enums.Weight.Default, location=enums.Location.Default, month=enums.Month.Default,
                            opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                            po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default,
                            player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                            shot_clock_range=enums.ShotClockRange.Default, starter_bench=enums.StarterBench.Default,
                            vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player defensive stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param defense_category: Filter to include only defense of shots from specific distance bucket. Default 'Overall' returns all. Required.
        :type defense_category: nba.enums.DefenseCategory
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all.
        :type date_to: nba.enums.DateTo
        :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type game_scope: nba.enums.GameScope
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all.
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games.
        :type last_n_games: nba.enums.LastNGames
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: nba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: nba.enums.StarterBench
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param player_id: ID of specific player to filter. Default 0, returns all.
        :type player_id: nba.enums.TeamID
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param draft_pick: Filter by players pick in the draft. Default '' returns all.
        :type draft_pick: nba.enums.DraftPick
        :param draft_year: Filter by year of the players draft. Default '' returns all.
        :type draft_year: nba.enums.DraftYear
        :param height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type height: nba.enums.Height
        :param weight: Filter by players weight in lbs. Default '' returns all.
        :type weight: nba.enums.Weight
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player defensive stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashptdefend'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def all_scoring_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                          season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                          pt_measure_type=enums.PtMeasureType.ShootingEfficiency,
                          player_or_team=enums.PlayerOrTeam.Player, college=enums.College.Default,
                          conference=enums.Conference.Default, country=enums.Country.Default,
                          date_from=enums.DateFrom.Default, draft_pick=enums.DraftPick.Default,
                          date_to=enums.DateTo.Default, division=enums.Division.Default,
                          draft_year=enums.DraftYear.Default, game_scope=enums.GameScope.Blank,
                          player_id=enums.TeamID.Default, team_id=enums.TeamID.Default,
                          game_segment=enums.GameSegment.Default, height=enums.Height.Default,
                          period=enums.Period.Default, last_n_games=enums.LastNGames.Default,
                          weight=enums.Weight.Default, month=enums.Month.Default, location=enums.Location.Default,
                          opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                          po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default,
                          player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                          shot_clock_range=enums.ShotClockRange.Default, starter_bench=enums.StarterBench.Default,
                          vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player scoring stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param pt_measure_type: Filter the type of shots and stats returned. Default 'Efficiency' returns all. Required.
        :type pt_measure_type: nba.enums.PtMeasureType
        :param player_or_team: whether to return stats by player or team. Default 'Player'. Required.
        :type player_or_team: nba.enums.PlayerOrTeam
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type game_scope: nba.enums.GameScope
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all. Required.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all. Required.
        :type player_position: nba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all. Required
        :type starter_bench: nba.enums.StarterBench
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param player_id: ID of specific player to filter. Default 0, returns all.
        :type player_id: nba.enums.TeamID
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param draft_pick: Filter by players pick in the draft. Default '' returns all.
        :type draft_pick: nba.enums.DraftPick
        :param draft_year: Filter by year of the players draft. Default '' returns all.
        :type draft_year: nba.enums.DraftYear
        :param height: Filter by players height (doesn't appear to work). Default '' returns all.
        :type height: nba.enums.Height
        :param weight: Filter by players weight in lbs. Default '' returns all.
        :type weight: nba.enums.Weight
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player scoring stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashptstats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def individual_career_stats(self, player_id, idx_data, per_mode=enums.PerMode.Default):
        """
        Get career or season individual player stats breakdown.
    
        :param player_id: ID of the player for whom to get stats breakdown.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :returns:
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'playercareerstats'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    def player_game_logs(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                         season_type=enums.SeasonType.Default, player_or_team=enums.PlayerOrTeam.Player[0],
                         sorter=enums.Stat.PTS, direction=enums.Direction.Descending, counter=0,
                         date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default):
        """
        Get game logs sorted by specific stat.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param player_or_team: whether to return stats by player or team. Default 'P'. Required.
        :type player_or_team: nba.enums.PlayerOrTeam, first letter only
        :param sorter: stat to sort players/teams logs by.
        :type sorter: nba.enums.Stat
        :param direction: direction to sort stat in. Default Descending.
        :type direction: nba.enums.Direction
        :param counter:
        :type counter: int
        :param date_from: Minimum date cutoff to include data from. Default '' returns all.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all.
        :type date_to: nba.enums.DateTo
        :returns: Game logs stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguegamelog'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def player_compare(self, player_id_list, vs_player_id_list, idx_data, league_id=enums.LeagueID.Default,
                       season=enums.Season.Default, season_type=enums.SeasonType.Default,
                       per_mode=enums.PerMode.Default, measure_type=enums.MeasureType.Default,
                       plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                       rank=enums.Rank.Default, shot_clock_range=enums.ShotClockRange.Default,
                       conference=enums.Conference.Default, date_from=enums.DateFrom.Default,
                       date_to=enums.DateTo.Default, division=enums.Division.Default, month=enums.Month.Default,
                       game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                       last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                       opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                       po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default,
                       vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Comparison of two players.
    
        :param player_id_list: player ID for Player 1 in comparison.
        :type player_id_list: int
        :param vs_player_id_list: Player ID for Player 2 in comparison.
        :type vs_player_id_list: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats comparison after applying all filters.
        :rtype: DataFrame
    
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
    
    def individual_clutch_stats(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                season=enums.Season.Default, season_type=enums.SeasonType.Default,
                                per_mode=enums.PerMode.Default, measure_type=enums.MeasureType.Default,
                                plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                                rank=enums.Rank.Default, location=enums.Location.Default,
                                shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default,
                                date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                                period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                                month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                outcome=enums.Outcome.Default, po_round=enums.PORound.Default,
                                season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default,
                                vs_division=enums.VsDivision.Default):
        """
        Player clutch stats breakdown.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player clutch stats after applying all filters.
        :rtype: DataFrame
    
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
    
    def individual_game_splits(self, player_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default, 
                               season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, 
                               measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default, 
                               pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default, 
                               shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default, 
                               date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default, 
                               period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                               location=enums.Location.Default, month=enums.Month.Default,
                               opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default, 
                               po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default, 
                               vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by score bucket|period|half or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_shot_chart(self, player_id, idx_data, game_id=enums.Default_Values.Blank, 
                              context_measure=enums.ContextMeasure.FGA, clutch_time=enums.ClutchTime.Default, 
                              ahead_behind=enums.AheadBehind.Default, point_diff=100, 
                              start_period=enums.Period.Default, end_period=enums.Period.Default,
                              start_range=enums.Default_Values.Blank, end_range=enums.Default_Values.Blank, 
                              league_id=enums.LeagueID.Default, season_type=enums.SeasonType.Default, 
                              date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default, 
                              game_segment=enums.GameSegment.Default, season=enums.Default_Values.Blank, 
                              team_id=enums.TeamID.Default, period=enums.Period.AllQuarters, month=enums.Month.Default,
                              last_n_games=enums.LastNGames.Default, location=enums.Location.Default, 
                              opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default, 
                              season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default, 
                              vs_division=enums.VsDivision.Default, player_position=enums.PlayerPosition.All,
                              rookie_year=enums.Default_Values.Blank):
        """
        Get x,y data location and further details of shots for a player in a specific game.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param game_id: ID of a specific game. Default '' returns all. Required.
        :type game_id: int
        :param context_measure: Type of shot to get data for. Default FGA. Required.
        :type context_measure: nba.enums.ContextMeasure
        :param clutch_time: Filter for stats occurring with less than this amount of time to play in the game. Default 5mins. Required.
        :type clutch_time: nba.enums.ClutchTime
        :param ahead_behind: filter to only include when team is behind|ahead. Default includes all. Required
        :type ahead_behind: nba.enums.AheadBehind
        :param point_diff: Absolute difference between teams for stats to be included. Required.
        :type point_diff: int
        :param start_period: filter shots to only those taken after a specified quarter. Default includes all quarters.
        :type start_period: nba.enums.Period
        :param end_period: filter shots to only those taken before a specified quarter. Default includes all quarters.
        :type end_period: nba.enums.Period
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Default '' returns all. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param player_position: filter for when player was playing in a specific position.
        :type player_position: nba.enums.PlayerPosition
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param rookie_year: filter by the year in which the player was a rookie.
        :type rookie_year: str('%Y-%y')
        :returns: Player shot locations after applying all filters. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_breakdown(self, player_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                             season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                             measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                             pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                             shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default,
                             date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                             period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                             location=enums.Location.Default, month=enums.Month.Default,
                             opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                             po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default,
                             vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by score bucket|period|half or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_recent_games(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                season=enums.Season.Default, season_type=enums.SeasonType.Default,
                                per_mode=enums.PerMode.Default, measure_type=enums.MeasureType.Default,
                                plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                                rank=enums.Rank.Default, shot_clock_range=enums.ShotClockRange.Default,
                                date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                                game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                                last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                                month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                outcome=enums.Outcome.Default, po_round=enums.PORound.Default,
                                season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default,
                                vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by pre defined number of most recent games or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters in pervious N games or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_by_opponent(self, player_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                               season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                               measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                               pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                               shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default,
                               date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                               period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                               location=enums.Location.Default, month=enums.Month.Default,
                               opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                               po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default,
                               vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by opponent or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by conference|division|team or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_by_shot_type(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                season=enums.Season.Default, season_type=enums.SeasonType.Default,
                                per_mode=enums.PerMode.Default, measure_type=enums.MeasureType.Default,
                                plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                                rank=enums.Rank.Default, shot_clock_range=enums.ShotClockRange.Default,
                                date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                                game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                                last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                                month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                outcome=enums.Outcome.Default, po_round=enums.PORound.Default,
                                season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default,
                                vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by shot type, zone and distance or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by shot zone|type|distance|assist or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_by_performance(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                  season=enums.Season.Default, season_type=enums.SeasonType.Default,
                                  per_mode=enums.PerMode.Default, measure_type=enums.MeasureType.Default,
                                  plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                                  rank=enums.Rank.Default, shot_clock_range=enums.ShotClockRange.Default,
                                  date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                                  game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                                  last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                                  month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                  outcome=enums.Outcome.Default, po_round=enums.PORound.Default,
                                  season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default,
                                  vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by team performance or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by points for|against|difference or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
        ========   =================================   ====================================================================
        idx_data                Name                                           Description
        ========   =================================   ====================================================================
            0       OverallPlayerDashboard              Overall player stats with no splits.
            1       ScoreDifferentialPlayerDashboard    Player stats split by games final score differential.
            2       PointsScoredPlayerDashboard         Player stats split by total points scored by players team in game.
            3       PointsAgainstPlayerDashboard        Player stats split by total points scored by opposing team in game.
        ========   =================================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashboardbyteamperformance'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df
    
    def individual_by_year(self, player_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                           measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                           pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                           shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default,
                           date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                           period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                           location=enums.Location.Default, month=enums.Month.Default,
                           opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                           po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default,
                           vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player stats breakdown by year or overall.
    
        :param player_id: player ID for Player 1 in comparison.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by season or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_passing_stats(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                 season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                                 season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                                 date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                                 last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                                 month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                 outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                                 vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player pass stats breakdown by received|made.
    
        :param player_id: player ID to retrieve data for.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :returns: Player stats after applying all filters by passes made|received. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_rebounding_stats(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                    season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                                    season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                                    date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                                    game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                                    last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                                    month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                    outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                                    vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player rebounding stats breakdown by shot|shot distance|rebound distance|contest or overall.
    
        :param player_id: player ID to retrieve data for.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :returns: Player stats after applying all filters by passes made|received. Shown in idx_data table below.
        :rtype: DataFrame
    
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
    
    def individual_shot_defense_stats(self, player_id, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                                      team_id=enums.Default_Values.Zero, season_type=enums.SeasonType.Default,
                                      per_mode=enums.PerMode.Default, date_from=enums.DateFrom.Default,
                                      date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                                      period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                                      location=enums.Location.Default, month=enums.Month.Default,
                                      opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                                      season_segment=enums.SeasonSegment.Default,
                                      vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player shot defense success stats breakdown when player is the defender of the shot.
    
        :param player_id: player ID to retrieve data for.
        :type player_id: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters by shot success.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'playerdashptshotdefend'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df
    
    def individual_shooting_stats(self, player_id, idx_data, league_id=enums.LeagueID.Default,
                                  season=enums.Season.Default, team_id=enums.Default_Values.Zero,
                                  season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                                  date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                                  game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                                  last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                                  month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                                  outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                                  vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Player shot success stats breakdown.
    
        :param player_id: player ID to retrieve data for.
        :type player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param team_id: ID of the team to filter for. Default 0 returns all. Required.
        :type team_id: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :returns: Player shooting stats after applying all filters by shot success.
        :rtype: DataFrame
    
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
    
    def players_vs_players(self, player_team_id, vs_team_id, player_id_1, vs_player_id_1, idx_data,
                           player_id_2=enums.Default_Values.Zero, player_id_3=enums.Default_Values.Zero,
                           player_id_4=enums.Default_Values.Zero, player_id_5=enums.Default_Values.Zero,
                           vs_player_id_2=enums.Default_Values.Zero, vs_player_id_3=enums.Default_Values.Zero,
                           vs_player_id_4=enums.Default_Values.Zero, vs_player_id_5=enums.Default_Values.Zero,
                           league_id=enums.LeagueID.Default, season=enums.Season.Default,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                           measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                           pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                           shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default,
                           date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                           period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                           location=enums.Location.Default, month=enums.Month.Default,
                           opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                           conference=enums.Conference.Default, division=enums.Division.Default,
                           season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default,
                           vs_division=enums.VsDivision.Default):
        """
        Player|Players stats breakdown individually or combined whilst other players are on|off court.
    
        :param player_team_id: Team ID of the base team in comparison. Required.
        :type player_team_id: int
        :param vs_team_id: Team ID of the comparative team. Required.
        :type vs_team_id: int
        :param player_id_1: player ID for Player 1 in comparison. Required.
        :type player_id_1: int
        :param vs_player_id_1: player ID for VsTeam Player 1 in comparison. Required.
        :type vs_player_id_1: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param player_id_2: player ID for Player 2 in comparison. Default 0 will not include a second player.
        :type player_id_2: int
        :param vs_player_id_2: player ID for VsTeam Player 2 in comparison. Default 0 will not include a second player.
        :type vs_player_id_2: int
        :param player_id_3: player ID for Player 3 in comparison. Default 0 will not include a third player.
        :type player_id_3: int
        :param vs_player_id_3: player ID for VsTeam Player 3 in comparison. Default 0 will not include a third player.
        :type vs_player_id_3: int
        :param player_id_4: player ID for Player 4 in comparison. Default 0 will not include a fourth player.
        :type player_id_4: int
        :param vs_player_id_4: player ID for VsTeam Player 4 in comparison. Default 0 will not include a fourth player.
        :type vs_player_id_4: int
        :param player_id_5: player ID for Player 5 in comparison. Default 0 will not include a fifth player.
        :type player_id_5: int
        :param vs_player_id_5: player ID for VsTeam Player 5 in comparison. Default 0 will not include a fifth player.
        :type vs_player_id_5: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :param plus_minus: whether to have stats as PlusMinus, Y|N. Default N. Required.
        :type plus_minus: nba.enums.PlusMinus
        :param pace_adjust: whether to have stats as adjusted for pace, Y|N. Default N. Required.
        :type pace_adjust: nba.enums.PaceAdjust
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
        :param outcome: Filter to only include stats for won or lost games. Default '' returns all. Required.
        :type outcome: nba.enums.Outcome
        :param location: Filter for home or road games only. Default '' returns all. Required.
        :type location: nba.enums.Location
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all. Required.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all. Required
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :param opponent_team_id: Filter to only include stats for games against a specific team. Default 0 returns all. Required.
        :type opponent_team_id: nba.enums.TeamID
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all. Required
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all. Required.
        :type vs_division: nba.enums.VsDivision
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Player stats after applying all filters either grouped or individually. Shown in idx_data table below.
        :rtype: DataFrame
    
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

    def all_by_play_type(self, category=enums.PlayType.Default, names=enums.SynergyName.Offense, q=2504502,
                         season=enums.Season.Current.split('-')[0], season_type=enums.SynergySeasonType.Regular):
        """
        Breakdown of players stats on a specific play type, play types defined by synergy data.

        :param category: Play type to get stats for. Required.
        :type category: nba.enums.PlayType
        :param names: specify whether to get offensive or defensive stats for players on the specified play type. Required.
        :type names: nba.enums.SynergyName
        :param q: appears to have no effect but is required.
        :type q: int
        :param season: Season to get stats from. Required.
        :type season: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SynergySeasonType
        :return: play type player stats
        :rtype: DataFrame
        """
        params = clean_locals(locals())
        url = r'http://stats-prod.nba.com/wp-json/statscms/v1/synergy/player/'
        r = self.request(None, params, request_url=url)
        df = pd.DataFrame(r.get('results', []))
        return df
