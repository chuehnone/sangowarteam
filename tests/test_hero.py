import pytest
from sangowarteam.hero import TroopType, TroopQuality, Troop, Hero


@pytest.fixture
def setup_troops():
    troop1 = Troop(TroopQuality.A, TroopQuality.B, TroopQuality.C, TroopQuality.S)
    troop2 = Troop(TroopQuality.B, TroopQuality.S, TroopQuality.A, TroopQuality.C)
    return troop1, troop2


def test_compare_troop_rate_cavalry_vs_spears(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Cavalry)
    troop2.set_current(TroopType.Spears)
    assert troop1.compare_troop_rate(troop2) == 0.85


def test_compare_troop_rate_cavalry_vs_shield(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Cavalry)
    troop2.set_current(TroopType.Shield)
    assert troop1.compare_troop_rate(troop2) == 1.1


def test_compare_troop_rate_shield_vs_bows(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Shield)
    troop2.set_current(TroopType.Bows)
    assert troop1.compare_troop_rate(troop2) == 1.1


def test_compare_troop_rate_shield_vs_cavalry(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Shield)
    troop2.set_current(TroopType.Cavalry)
    assert troop1.compare_troop_rate(troop2) == 0.85


def test_compare_troop_rate_bows_vs_spears(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Bows)
    troop2.set_current(TroopType.Spears)
    assert troop1.compare_troop_rate(troop2) == 1.1


def test_compare_troop_rate_bows_vs_shield(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Bows)
    troop2.set_current(TroopType.Shield)
    assert troop1.compare_troop_rate(troop2) == 0.85


def test_compare_troop_rate_spears_vs_cavalry(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Spears)
    troop2.set_current(TroopType.Cavalry)
    assert troop1.compare_troop_rate(troop2) == 1.1


def test_compare_troop_rate_spears_vs_bows(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Spears)
    troop2.set_current(TroopType.Bows)
    assert troop1.compare_troop_rate(troop2) == 0.85


def test_compare_troop_rate_general(setup_troops):
    troop1, troop2 = setup_troops
    troop1.set_current(TroopType.Cavalry)
    troop2.set_current(TroopType.Cavalry)
    assert troop1.compare_troop_rate(troop2) == 1


@pytest.fixture
def setup_heroes():
    troop1 = Troop(TroopQuality.A, TroopQuality.B, TroopQuality.C, TroopQuality.S)
    troop2 = Troop(TroopQuality.B, TroopQuality.S, TroopQuality.A, TroopQuality.C)
    hero1 = Hero("Hero1", 100, 50, 30, 20, 10, troop1)
    hero2 = Hero("Hero2", 100, 40, 25, 15, 5, troop2)
    return hero1, hero2


def test_attack_target(setup_heroes):
    hero1, hero2 = setup_heroes
    hero1.troops.set_current(TroopType.Cavalry)
    hero2.troops.set_current(TroopType.Spears)
    hero1.attack_target(hero2)
    assert hero2.current_forces == 100 - int(50 * 1 * 0.85 - 25 * 0.7)
