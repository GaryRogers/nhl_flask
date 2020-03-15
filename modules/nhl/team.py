import modules.nhl.data

def get_team_id(abbreviation: str) -> int:
    return modules.nhl.data.get_team(abbreviation)['id']

def get_team_abbreviation(id: int) -> str:
    return modules.nhl.data.get_team_by_id(id)['abbreviation']