import pytest
from sangowarteam.hero import Hero, Troop, TroopQuality, TroopType
from sangowarteam.team import Team


@pytest.fixture
def setup_teams():
    # Define heroes for team1
    team1_heros = [
        Hero(
            "Hero1",
            attack=50,
            defense=30,
            forces=10000,
            speed=20,
            intelligence=80,
            troops=Troop(
                cavalry=TroopQuality.S,
                shield=TroopQuality.A,
                bows=TroopQuality.B,
                spears=TroopQuality.C,
            ),
        ),
        Hero(
            "Hero2",
            attack=50,
            defense=30,
            forces=10000,
            speed=20,
            intelligence=80,
            troops=Troop(
                cavalry=TroopQuality.S,
                shield=TroopQuality.A,
                bows=TroopQuality.B,
                spears=TroopQuality.C,
            ),
        ),
    ]
    team1 = Team("Team1", team1_heros)

    # Define heroes for team2
    team2_heros = [
        Hero(
            "Hero3",
            attack=50,
            defense=30,
            forces=10000,
            speed=20,
            intelligence=80,
            troops=Troop(
                cavalry=TroopQuality.S,
                shield=TroopQuality.A,
                bows=TroopQuality.B,
                spears=TroopQuality.C,
            ),
        ),
        Hero(
            "Hero4",
            attack=50,
            defense=30,
            forces=10000,
            speed=20,
            intelligence=80,
            troops=Troop(
                cavalry=TroopQuality.S,
                shield=TroopQuality.A,
                bows=TroopQuality.B,
                spears=TroopQuality.C,
            ),
        ),
    ]
    team2 = Team("Team2", team2_heros)

    return team1, team2


def test_is_defeated(setup_teams):
    team1, team2 = setup_teams

    # Initially, no team should be defeated
    assert not team1.is_defeated()
    assert not team2.is_defeated()

    # Simulate all heroes in team1 being defeated
    for hero in team1.heros:
        hero.current_forces = 0

    assert team1.is_defeated()
    assert not team2.is_defeated()


def test_get_alive_heros(setup_teams):
    team1, team2 = setup_teams

    # Initially, all heroes should be alive
    assert len(team1.get_alive_heros()) == len(team1.heros)
    assert len(team2.get_alive_heros()) == len(team2.heros)

    # Simulate some heroes being defeated
    team1.heros[0].current_forces = 0

    assert len(team1.get_alive_heros()) == len(team1.heros) - 1
    assert len(team2.get_alive_heros()) == len(team2.heros)
