#!/usr/bin/env python3

import modules.config
import modules.secrets
import modules.logger
import modules.nhl.season
import modules.nhl.game
import json

logger = modules.logger.get()

#logger.info('this is a message')
#logger.warning('This is a warning')
#logger.error('This is an error')

#try:
#    raise ValueError('This is an exception')
#except Exception as ex:
#    logger.exception(ex)


#season = modules.nhl.download.get_schedule(20192020)
#game = modules.nhl.download.get_game(2019020001)

team_games = modules.nhl.season.get_team_games(20192020,'bos')

game = modules.nhl.game.get(team_games[0])
home_team = modules.nhl.game.home_team(team_games[0], True)

print(home_team)