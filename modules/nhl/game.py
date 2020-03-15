import modules.nhl.data

def get(game_id: int) -> dict:
    return modules.nhl.data.get_game(game_id)

def home_team(game_id: int, details: bool = False) -> dict:
    game = get(game_id)
    if details:
        return game['gameData']['teams']['home']
    
    return game['gameData']['teams']['home']['abbreviation']

def away_team(game_id: int, details: bool = False) -> dict:
    game = get(game_id)
    if details:
        return game['gameData']['teams']['away']
    
    return game['gameData']['teams']['away']['abbreviation']