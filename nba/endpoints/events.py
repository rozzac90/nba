
import pandas as pd

from nba.utils import clean_locals
from nba.endpoints.baseendpoint import BaseEndpoint


class Events(BaseEndpoint):

    def get_moments(self, game_id, event_id):
        """
        ***Blocked Cannot Access***
        Get location moments for each player throughout a single game event.
    
        :param game_id: ID of the game to get location data from.
        :type game_id: str
        :param event_id: ID of specific game event.
        :type event_id: int
        :returns: location data for each snapshot in the event.
        :rtype: DataFrame
    
        """
        raise DeprecationWarning('This endpoint has been closed to public access')
        endpoint = 'locations_getmoments'
        params = clean_locals(locals())
        r = self.request(endpoint, params)
        if len(r) > 0:
            try:
                headers = ["TeamID", "PlayerID", "x_loc", "y_loc", "Radius",
                           "MomentID", "GameClock", "ShotClock", "EventID"]
                player_moments = []
                moments = r['moments']
                for moment in moments:
                    for player in moment[5]:
                        player.extend((moments.index(moment), moment[2], moment[3], event_id))
                        player_moments.append(player)
                df = pd.DataFrame(player_moments, columns=headers)
            except:
                df = pd.DataFrame()
        else:
            df = pd.DataFrame()
        return df

    def get_all_moments(self, game_id, limit):
        """
        ***Blocked Cannot Access***
        Get location moments for all events IDs up to set limit.
    
        :param game_id: ID of the game to get location data from.
        :type game_id: str
        :param limit: depth to iterate through game events.
        :type limit: int
        :returns: location moments for all players for each event up to limit.
        :rtype: Dataframe
    
        """
        raise DeprecationWarning('This endpoint has been closed to public access')
        endpoint = 'locations_getmoments'
        df = pd.DataFrame()
        for i in range(1, int(limit)):
            params = {'GameID': game_id, 'EventID': str(i)}
            r = self.request(endpoint, params)
            if len(r) > 0:
                try:
                    headers = ["TeamID", "PlayerID", "x_loc", "y_loc", "Radius",
                               "MomentID", "GameClock", "ShotClock", "EventID"]
                    player_moments = []
                    moments = r['moments']
                    for moment in moments:
                        for player in moment[5]:
                            player.extend((moments.index(moment), moment[2], moment[3], i))
                            player_moments.append(player)
                    temp = pd.DataFrame(player_moments, columns=headers)
                    df = pd.concat([df, temp])
                except:
                    continue
            else:
                continue
        return df
