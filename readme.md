# NHL Flask

Python modules that provide helper functions for dealing with NHL API data. The modules also cache API data locally so that you aren't hitting the NHL API all the time when looking up keys or games that you're working with.

Eventually I'll put together a Flask/Vue.js app that'll give all this a nice UI.

[NHL API Documentation](https://gitlab.com/dword4/nhlapi/-/tree/master)

## Modules

### `modules.nhl.data`

Functions to pull down data from NHL API, or serve up data cached in a local data directory. Used by other modules for data access.

#### `get_schedule(season)`

#### `get_game(game_id)`

#### `get_teams()`

#### `get_team(abbreviation)`

#### `get_team_by_id(team_id)`

### `modules.nhl.game`

#### `get(game_id)`

Get the raw game data as provided by the NHL API

#### `home_team(game_id, details)`

Get the home team abbreviation, or the entire team object if details = True

#### `away_team(game_id, details)`

Get the away team abbreviation, or the entire team object if details = True

#### `faceoffs(game_id)`

#### `hits(game_id)`

#### `giveaways(game_id)`

#### `takeaways(game_id)`

#### `goals(game_id)`

#### `shots(game_id)`

#### `missed_shots(game_id)`

#### `penalties(game_id)`

#### `fights(game_id)`

#### `blocked_shots(game_id)`