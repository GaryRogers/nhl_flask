import modules.nhl.data
from typing import List

def _events(game_id: int, eventTypeId: str) -> List['dict']:
    game = get(game_id)

    return_list = []

    for play in game['liveData']['plays']['allPlays']:
        if play['result']['eventTypeId'].lower() == eventTypeId.lower():
            return_list.append(play)

    return return_list    


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


def faceoffs(game_id: int) -> List[dict]:
    return _events(game_id, 'FACEOFF')


def hits(game_id: int) -> List[dict]:
    return _events(game_id, 'HIT')


def giveaways(game_id: int) -> List[dict]:
    return _events(game_id, 'GIVEAWAY')


def takeaways(game_id: int) -> List[dict]:
    return _events(game_id, 'TAKEAWAY')


def goals(game_id: int) -> List[dict]:
    return _events(game_id, 'GOAL')


def shots(game_id: int) -> List[dict]:
    return _events(game_id, 'SHOT')


def missed_shots(game_id: int) -> List[dict]:
    return _events(game_id, 'MISSED_SHOT')


def penalties(game_id: int) -> List[dict]:
    return _events(game_id, 'PENALTY')


def fights(game_id: int) -> List[dict]:
    return _events(game_id, 'FIGHT')


def blocked_shots(game_id: int) -> List[dict]:
    return _events(game_id, 'BLOCKED_SHOT')

