import os
import json
import requests
import modules.config
import modules.logger
from typing import List

config = modules.config.get()
logger = modules.logger.get()


def _get_data(key: int, file_type: str, url: str) -> dict:
    try:
        return_object = None

        file = '{0}/{1}_{2}.json'.format(config['data']['directory'], key, file_type)
        abs_path = os.path.abspath(file)
        
        if os.path.isfile(abs_path):
            logger.debug('Returning {0} {1} data from file {2}'.format(key, file_type, abs_path))
            with open(abs_path) as f:
                return_object = json.load(f)
                f.close()
                return return_object

        result = requests.get(url)

        if result.status_code == requests.codes.ok:
            return_object = result.json()
            with open(abs_path, 'w') as f:
                logger.debug('Saving {0} {1} data to file {2}'.format(key, file_type, abs_path))
                json.dump(return_object, f)
                f.close()

            return return_object
        
        raise ValueError('API call returned status code {0}'.format(result.status_code))
    except Exception as ex:
        logger.exception(ex)


def get_schedule(season: int) -> dict:
    try:
        url = '{0}/schedule?season={1}&gameType=R'.format(config['api']['nhl']['base_url'], season)

        return _get_data(season, 'season', url)
    except Exception as ex:
        logger.exception(ex)


def get_game(game_id: int) -> dict:
    try:
        url = '{0}/game/{1}/feed/live'.format(config['api']['nhl']['base_url'], game_id)

        return _get_data(game_id, 'game', url)
    except Exception as ex:
        logger.exception(ex)
        

def get_team(abbreviation: str) -> dict:
    try:
        team_list = get_teams()
        
        for team in team_list['teams']:
            if team['abbreviation'].lower() == abbreviation.lower():
                return_team = team

        return return_team
    except Exception as ex:
        logger.exception(ex)


def get_team_by_id(id: int) -> dict:
    try:
        team_list = get_teams()
        
        for team in team_list['teams']:
            if team['id'] == id:
                return_team = team

        return return_team
    except Exception as ex:
        logger.exception(ex)
    

def get_teams() -> List[dict]:
    try:
        url = '{0}/teams/'.format(config['api']['nhl']['base_url'])
        
        return _get_data(0, 'teams', url)
    except Exception as ex:
        logger.exception(ex)