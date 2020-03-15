import modules.nhl.data
import modules.nhl.team
import modules.logger
from typing import List

def get_games(season: int) -> List[str]:
    season_data = modules.nhl.data.get_schedule(season)

    games_list = []

    for date in season_data['dates']:
        for game in date['games']:
            games_list.append(game['gamePk'])

    return games_list

def get_team_games(season: int, team: str) -> List[str]:
    season_data = modules.nhl.data.get_schedule(season)
    team = modules.nhl.data.get_team(team)

    games_list = []

    for date in season_data['dates']:
        for game in date['games']:
            if game['teams']['away']['team']['id'] == team['id']:
                games_list.append(game['gamePk'])
            if game['teams']['home']['team']['id'] == team['id']:
                games_list.append(game['gamePk'])

    return games_list