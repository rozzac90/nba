
import requests
import pandas as pd

from nba import enums
from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Team(BaseEndpoint):

    def all_raw_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default, 
                      season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default, 
                      measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default, 
                      pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default, 
                      shot_clock_range=enums.ShotClockRange.Default, game_scope=enums.GameScope.Blank, 
                      team_id=enums.TeamID.Default, college=enums.College.Default, conference=enums.Conference.Default, 
                      country=enums.Country.Default, date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default, 
                      division=enums.Division.Default, game_segment=enums.GameSegment.Default, 
                      period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                      location=enums.Location.Default, month=enums.Month.Default, 
                      opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default, 
                      po_round=enums.PORound.Default, player_experience=enums.PlayerExperience.Default, 
                      player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default, 
                      starter_bench=enums.StarterBench.Default, vs_conference=enums.VsConference.Default, 
                      vs_division=enums.VsDivision.Default):
        """
        Team stats breakdown.
    
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
        :param college: Filter for players attending specific college. Default '' returns all.
        :type college: nba.enums.College
        :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type game_scope: nba.enums.GameScope
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
        :param player_experience: Filter to only include players of specific experience level. Default '' returns all.
        :type player_experience: nba.enums.PlayerExperience
        :param player_position: Filter to only include players of certain position. Default '' returns all.
        :type player_position: nba.enums.PlayerPosition
        :param starter_bench: Filter to only include starts or bench. Default '' returns all.
        :type starter_bench: nba.enums.StarterBench
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param country: Filter for players from specific country. Default '' returns all.
        :type country: nba.enums.Country
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Team stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashteamstats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def team_lineups(self, team_id, game_id=enums.Default_Values.Blank, season=enums.Season.Default,
                     season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                     group_quantity=enums.GroupQuantity.Default, measure_type=enums.MeasureType.Default,
                     plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                     date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                     game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters, outcome=enums.Outcome.Default,
                     last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                     month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                     season_segment=enums.SeasonSegment.Default, conference=enums.Conference.Default,
                     division=enums.Division.Default, vs_conference=enums.VsConference.Default,
                     vs_division=enums.VsDivision.Default):
        """
        Top 250 team lineup combinations of specified group quantity, by minutes played descending.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param game_id: Filter for specific game. Default '' returns all.
        :type: game_id: int
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param group_quantity: no. of players to group into ranking. Default 5. Required.
        :type group_quantity: int
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
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
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
        :param vs_conference: Filter to only include only teams from specific conference. Default '' returns all.
        :type vs_conference: nba.enums.VsConference
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Team lineup combinations of GroupQuantity, ranked by StatCategory after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'teamdashlineups'
        r = self.request(endpoint, params)
        df = self.process_response(r, 1, 'resultSets')
        return df

    def all_team_lineups(self, season=enums.Season.Default, season_type=enums.SeasonType.Default,
                         per_mode=enums.PerMode.Default, group_quantity=enums.GroupQuantity.Default,
                         measure_type=enums.MeasureType.Default, team_id=enums.TeamID.Default,
                         plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                         rank=enums.Rank.Default, date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                         game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                         last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                         month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                         outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                         conference=enums.Conference.Default, division=enums.Division.Default,
                         vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Top 250 team lineup combinations of specified group quantity, ranked by stat category.
    
        :param season: Season to get players from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :param group_quantity: no. of players to group into ranking. Default 5. Required.
        :type group_quantity: int
        :param measure_type: Type of stats to return. Default 'Base'. Required
        :type measure_type: nba.enums.MeasureType
        :type team_id: filter for specific team. Default 0 returns all.
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
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param vs_conference: Filter to only include only teams from specific conference. Default '' returns all.
        :type vs_conference: nba.enums.VsConference
        :returns: Team lineup combinations of GroupQuantity, ranked by StatCategory after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashlineups'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def all_shot_locations(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                           measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                           pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                           distance_range=enums.DistanceRange.Zone, shot_clock_range=enums.ShotClockRange.Default,
                           game_scope=enums.GameScope.Blank, team_id=enums.TeamID.Default,
                           conference=enums.Conference.Default, date_from=enums.DateFrom.Default,
                           date_to=enums.DateTo.Default, division=enums.Division.Default,
                           game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                           last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                           month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                           outcome=enums.Outcome.Default, po_round=enums.PORound.Default,
                           player_experience=enums.PlayerExperience.Default, starter_bench=enums.StarterBench.Default,
                           player_position=enums.PlayerPosition.Default, season_segment=enums.SeasonSegment.Default,
                           vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team shot stats breakdown, default broken down by shot category.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams stats from. Required.
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
        :param distance_range: Filter shots to include by range buckets. Default by zone. Required.
        :type distance_range: nba.enums.DistanceRange
        :param rank: whether to include stat ranks, Y|N. Default N. Required
        :type rank: nba.enums.Rank
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
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: team shot stats by shot category after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashteamshotlocations'
        r = self.request(endpoint, params)
        df = pd.DataFrame(
            data=r.get('resultSets').get('rowSet'), columns=r.get('resultSets').get('headers')[1].get('columnNames')
        )
        return df

    def all_shot_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                       season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                       close_def_dist_range=enums.CloseDefDistRange.Default, dribble_range=enums.DribbleRange.All,
                       shot_clock_range=enums.ShotClockRange.Default, shot_dist_range=enums.Default_Values.Blank,
                       touch_time_range=enums.Default_Values.Blank, general_range=enums.Default_Values.Blank,
                       team_id=enums.TeamID.Default, conference=enums.Conference.Default,
                       date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default, division=enums.Division.Default,
                       game_segment=enums.GameSegment.Default, period=enums.Period.Default,
                       last_n_games=enums.LastNGames.Default, po_round=enums.PORound.Default,
                       location=enums.Location.Default, month=enums.Month.Default,
                       opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                       season_segment=enums.SeasonSegment.Default, vs_conference=enums.VsConference.Default,
                       vs_division=enums.VsDivision.Default):
        """
        Team shot stats breakdown.
    
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
        :param shot_dist_range: Filter stats to include only shots in specified distance range. Default '' returns all.
        :type shot_dist_range: unsure.
        :param touch_time_range: Filter by how long ball is held prior to shot. Default '' returns all.
        :type touch_time_range: unsure.
        :param general_range: No idea what this does.
        :type general_range: unsure.
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param date_from: Minimum date cutoff to include data from. Default '' returns all.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all.
        :type date_to: nba.enums.DateTo
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games.
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games.
        :type last_n_games: nba.enums.LastNGames
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
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type season_segment: nba.enums.SeasonSegment
        :param vs_conference: Filter to only include stats for games against specific conference. Default '' returns all.
        :type vs_conference: nba.enums.VsConference
        :param vs_division: Filter to only include stats for games against specific division. Default '' returns all.
        :type vs_division: nba.enums.VsDivision
        :returns: Team shot stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashteamptshot'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def all_defensive_stats(self, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                            season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                            defense_category=enums.DefenseCategory.Default, conference=enums.Conference.Default,
                            date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                            division=enums.Division.Default, game_scope=enums.GameScope.Default,
                            team_id=enums.TeamID.Default, game_segment=enums.GameSegment.Default,
                            period=enums.Period.AllQuarters, last_n_games=enums.LastNGames.Default,
                            location=enums.Location.Default, month=enums.Month.Default,
                            opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                            po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default,
                            vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team defensive stats breakdown.
    
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
        :param game_scope: Filter for games to include, Last 10 or Yesterday accepted. Default '' returns all. Required
        :type game_scope: nba.enums.GameScope
        :param month: Filter for games occurring in a specific month (relative to season start). Default 0 returns all.
        :type month: nba.enums.Month
        :param season_segment: Filter to only include stats from Post/Pre all star break. Default '' returns all.
        :type season_segment: nba.enums.SeasonSegment
        :param date_from: Minimum date cutoff to include data from. Default '' returns all.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all.
        :type date_to: nba.enums.DateTo
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
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :returns: Team defensive stats after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'leaguedashptdefend'
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
                         last_n_games=enums.LastNGames.Default, conference=enums.Conference.Default,
                         division=enums.Division.Default, team_id=enums.TeamID.Default, po_round=enums.PORound.Default,
                         shot_clock_range=enums.ShotClockRange.Default):
        """
        Team clutch stats breakdown.
    
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams data from. Required.
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
        :param conference: Filter for players from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param po_round: Filter to only include stats for specific playoff round games. Default '' returns all.
        :type po_round: nba.enums.PORound
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Team clutch stats after applying all filters.
        :rtype: DataFrame
    
         """
        params = clean_locals(locals())
        endpoint = 'leaguedashteamclutch'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def team_passing_stats(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                           date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                           last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                           month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                           outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                           vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team pass stats breakdown by received|made.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get team data from. Required.
        :type season: nba.enums.Season
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
        :returns: Team stats after applying all filters by passes made|received. Shown in idx_data table below.
        :rtype: DataFrame
    
        ========   ===============   ==================================================
        idx_data        Name                           Description
        ========   ===============   ==================================================
            0       PassesMade        Breakdown of passes made by player thrown by.
            1       PassesReceived	  Breakdown of passes received by player thrown to.
        ========   ===============   ==================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'teamdashptpass'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_rebounding_stats(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                              season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                              date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                              game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                              last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                              month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                              outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                              vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team rebounding stats breakdown by shot|shot distance|rebound distance|contest or overall.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
        :type season: nba.enums.Season
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
        :returns: Team stats after applying all filters by passes made|received. Shown in idx_data table below.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamdashptreb'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_shooting_stats(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                            season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                            date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                            game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                            last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                            month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                            outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                            vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team shot success stats breakdown.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams data from. Required.
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
        :returns: Team shooting stats after applying all filters by shot success.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamdashptshots'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_vs_player(self, team_id, vs_player_id, idx_data, league_id=enums.LeagueID.Default,
                       season=enums.Season.Default, season_type=enums.SeasonType.Default,
                       per_mode=enums.PerMode.Default, measure_type=enums.MeasureType.Default,
                       plus_minus=enums.PlusMinus.Default, pace_adjust=enums.PaceAdjust.Default,
                       rank=enums.Rank.Default, shot_clock_range=enums.ShotClockRange.Default,
                       date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                       game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                       last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                       month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                       outcome=enums.Outcome.Default, conference=enums.Conference.Default,
                       division=enums.Division.Default, season_segment=enums.SeasonSegment.Default,
                       vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team stats breakdown vs specific player by player on|off court, shot distance and shot area.
    
        :param team_id: Team ID of the base team in comparison. Required.
        :type team_id: int
        :param vs_player_id: player ID for comparison. Required.
        :type vs_player_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams data from. Required.
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
        :param conference: Filter for teams from specific conference. Default '' returns all.
        :type conference: nba.enums.Conference
        :param division: Filter by specific division. Default '' returns all.
        :type division: nba.enums.Division
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :param shot_clock_range: Filter to specific shot clock time windows. Default '' returns all.
        :type shot_clock_range: nba.enums.ShotClockRange
        :returns: Team stats after applying all filters. Shown in idx_data table below.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamvsplayer'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_clutch_stats(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team clutch stats breakdown.
    
        :param team_id: Team to get stats for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Team clutch stats after applying all filters.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamdashboardbyclutch'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_game_splits(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team stats breakdown by score bucket|period|half or overall.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams data from. Required.
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
        :returns: Team stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamdashboardbygamesplits'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_breakdown(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team stats breakdown by score bucket|period|half or overall.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Teams stats after applying all filters by score bucket|period|half or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamdashboardbygeneralsplits'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_recent_games(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team stats breakdown by pre defined number of most recent games or overall.
    
        :param team_id: Team for which to retrieve data.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Team stats after applying all filters in previous N games or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
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
        params = clean_locals(locals())
        endpoint = 'teamdashboardbylastngames'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_by_opponent(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team stats breakdown by opponent or overall.
    
        :param team_id: Team for which to retrieve data.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Team stats after applying all filters by conference|division|team or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
        ========   =========================   ====================================================================
        idx_data              Name                                      Description
        ========   =========================   ====================================================================
            0       OverallTeamDashboard        Overall Team stats with no splits.
            1       ConferenceTeamDashboard     Team stats split by conference of team against whom they occurred.
            2       DivisionTeamDashboard       Team stats split by division of team against whom they occurred.
            3       OpponentTeamDashboard       Team stats split by team against whom they occurred.
        ========   =========================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'teamdashboardbyopponent'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_by_shot_type(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team stats breakdown by shot type, zone and distance or overall.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Team stats after applying all filters by shot zone|type|distance|assist or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
        ========   ==============================   ====================================================================
        idx_data              Name                                           Description
        ========   ==============================   ====================================================================
            0       OverallTeamDashboard             Overall Team stats with no splits.
            1       Shot5FTTeamDashboard             Team stats split by shot distance as granular as 5ft range.
            2       Shot8FTTeamDashboard             Team stats split by shots distance as granular as 8ft range.
            3       ShotAreaTeamDashboard            Team stats split by shot area.
            4       AssitedShotTeamDashboard         Team stats split by Assisted|Unassisted.
            5       ShotTypeTeamDashboard            Team stats split by more granular shot type.
            6       AssistedBy                       Team stats split by Team assisting.
        ========   ==============================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'teamdashboardbyshootingsplits'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_by_performance(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
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
        Team stats breakdown by team performance or overall.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Team stats after applying all filters by points for|against|difference or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
        ========   =================================   ====================================================================
        idx_data                Name                                           Description
        ========   =================================   ====================================================================
            0       OverallTeamDashboard                Overall Team stats with no splits.
            1       ScoreDifferentialTeamDashboard      Team stats split by games final score differential.
            2       PointsScoredTeamDashboard           Team stats split by total points scored by Teams team in game.
            3       PontsAgainstTeamDashboard           Team stats split by total points scored by opposing team in game.
        ========   =================================   ====================================================================
    
        """
        params = clean_locals(locals())
        endpoint = 'teamdashboardbyteamperformance'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_by_year(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                     season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                     measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                     pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default, period=enums.Period.AllQuarters,
                     shot_clock_range=enums.ShotClockRange.Default, date_from=enums.DateFrom.Default,
                     date_to=enums.DateTo.Default, game_segment=enums.GameSegment.Default,
                     last_n_games=enums.LastNGames.Default, location=enums.Location.Default, month=enums.Month.Default,
                     opponent_team_id=enums.OpponentTeamID.Default, outcome=enums.Outcome.Default,
                     po_round=enums.PORound.Default, season_segment=enums.SeasonSegment.Default,
                     vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team stats breakdown by year or overall.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season: Season to get teams from. Required.
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
        :returns: Team stats after applying all filters by season or overall. Shown in idx_data table below.
        :rtype: DataFrame
    
        ========   ========================   ======================================
        idx_data           Name                          Description
        ========   ========================   ======================================
            0       OverallTeamDashboard     Overall Team stats with no splits.
            1       ByYearTeamDashboard      Team stats split by season.
        ========   ========================   ======================================
    
        """
        params = clean_locals(locals())
        endpoint = 'teamdashboardbyyearoveryear'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def team_by_season(self, team_id, league_id=enums.LeagueID.Default, season_type=enums.SeasonType.Default,
                       per_mode=enums.PerMode.Default):
        """
        Team stats breakdown by season.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param league_id: ID of the league to get data for. Default 00. Required.
        :type league_id: nba.enums.LeagueID
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param per_mode: grouping of stat data. Totals or PerGame accepted. Required.
        :type per_mode: nba.enums.PerMode
        :returns: Team stats after applying all filters by season.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'teamyearbyyearstats'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def team_game_logs(self, team_id, season=enums.Season.Current, season_type=enums.SeasonType.Default,
                       date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default):
        """
        Team game logs.
    
        :param team_id: Team to retrieve data for.
        :type team_id: int
        :param season: Season to get teams from. Required.
        :type season: nba.enums.Season
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SeasonType
        :param date_from: Minimum date cutoff to include data from. Default '' returns all. Required.
        :type date_from: nba.enums.DateFrom
        :param date_to:  Maximum date cutoff to include data to. Default '' returns all. Required.
        :type date_to: nba.enums.DateTo
        :returns: Team game logs after applying all filters.
        :rtype: DataFrame
    
        """
        params = clean_locals(locals())
        endpoint = 'teamgamelog'
        r = self.request(endpoint, params)
        df = self.process_response(r, 0, 'resultSets')
        return df

    def team_player_on_off(self, team_id, idx_data, league_id=enums.LeagueID.Default, season=enums.Season.Default,
                           season_type=enums.SeasonType.Default, per_mode=enums.PerMode.Default,
                           measure_type=enums.MeasureType.Default, plus_minus=enums.PlusMinus.Default,
                           pace_adjust=enums.PaceAdjust.Default, rank=enums.Rank.Default,
                           date_from=enums.DateFrom.Default, date_to=enums.DateTo.Default,
                           game_segment=enums.GameSegment.Default, period=enums.Period.AllQuarters,
                           last_n_games=enums.LastNGames.Default, location=enums.Location.Default,
                           month=enums.Month.Default, opponent_team_id=enums.OpponentTeamID.Default,
                           outcome=enums.Outcome.Default, season_segment=enums.SeasonSegment.Default,
                           vs_conference=enums.VsConference.Default, vs_division=enums.VsDivision.Default):
        """
        Team stats details breakdown by player when on|off court.
    
        :param team_id: ID of specific team to filter. Default 0, returns all.
        :type team_id: nba.enums.TeamID
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
        :param game_segment: Filter to include only certain parts of games. Default '' includes entire games.
        :type game_segment: nba.enums.GameSegment
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
        :param period: Filter stats for only those pertaining to a certain period of games. Default '' includes entire games. Required
        :type period: nba.enums.Period
        :param last_n_games: Filter stats for only those occurring in the last n games. Default '' includes entire games. Required.
        :type last_n_games: nba.enums.LastNGames
        :returns: Team stats details breakdown by player when on|off court..
        :rtype: DataFrame
    
        ========   ======================================   =============================================
        idx_data                  Name                                      Description
        ========   ======================================   =============================================
            0       OverallTeamPlayerOnOffDetails            Overall Team stats with no splits.
            1       PlayersOnCourtTeamPlayerOnOffDetails     Team stats by player when they are on court.
            2       PlayersOffCourtTeamPlayerOnOffDetails    Team stats by player when they are on court.
        ========   ======================================   =============================================
    
        """
        params = clean_locals(locals())
        endpoint = 'teamplayeronoffdetails'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def franchise_history(self, idx_data, league_id=enums.LeagueID.Default):
        """
        Breakdown of each franchise's record in the NBA.

        :param idx_data: the index to retrieve data from json.
        :type idx_data: int
        :param league_id: define league to look at, nba.
        :type league_id: nba.enums.LeagueID
        :returns: franchise information.
        :rtype: DataFrame

        ========   =================   ==================================================
        idx_data          Name                        Description
        ========   =================   ==================================================
            0       FranchiseHistory   Win/Loss Record and Titles Info for franchises.
            1       DefunctTeams       Franchises no longer in NBA.
        ========   =================   ==================================================

        """
        params = clean_locals(locals())
        endpoint = 'franchisehistory'
        r = self.request(endpoint, params)
        df = self.process_response(r, idx_data, 'resultSets')
        return df

    def all_by_play_type(self, category=enums.PlayType.Default, names=enums.SynergyName.Offense, q=2504502,
                         season=enums.Season.Current.split('-')[0], season_type=enums.SynergySeasonType.Regular):
        """
        Breakdown of teams stats on a specific play type, play types defined by synergy data.
        
        :param category: Play type to get stats for. Required.
        :type category: nba.enums.PlayType
        :param names: specify whether to get offensive or defensive stats for teams on the specified play type. Required.
        :type names: nba.enums.SynergyName
        :param q: appears to have no effect but is required.
        :type q: int
        :param season: Season to get stats from. Required.
        :type season: int
        :param season_type: part of season to pull data from. Required.
        :type season_type: nba.enums.SynergySeasonType
        :return: play type team stats
        :rtype: DataFrame
        """
        params = clean_locals(locals())
        url = r'http://stats-prod.nba.com/wp-json/statscms/v1/synergy/team/'
        r = self.request(None, params, request_url=url)
        df = pd.DataFrame(r.get('results', []))
        return df
