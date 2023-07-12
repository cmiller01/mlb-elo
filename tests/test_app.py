from mlb_elo.data import get_teams

def test_get_teams():
    teams = get_teams()
    assert len(teams) > 5
    assert isinstance(teams, tuple)