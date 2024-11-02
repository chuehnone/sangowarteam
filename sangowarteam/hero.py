import random
from enum import Enum


class TroopType(Enum):
    # Cavalry (騎兵), Shield (盾兵), Bows (弓兵), Spears (槍兵)
    Cavalry = 1
    Shield = 2
    Bows = 3
    Spears = 4


class TroopQuality(Enum):
    # S: 1.2, A: 1, B: 0.85, C: 0.7
    S = 1.2
    A = 1
    B = 0.85
    C = 0.7


class Troop:
    # 兵種適性
    def __init__(
        self,
        cavalry: TroopQuality,
        shield: TroopQuality,
        bows: TroopQuality,
        spears: TroopQuality,
    ):
        self.current_troop_type = None
        self.troops = {
            TroopType.Cavalry: cavalry,
            TroopType.Shield: shield,
            TroopType.Bows: bows,
            TroopType.Spears: spears,
        }

    def set_current(self, troop_type: TroopType):
        self.current_troop_type = troop_type

    def get_troop_rate(self):
        return self.troops.get(self.current_troop_type).value

    # 屬性相剋 1.1 vs 0.85
    def compare_troop_rate(self, target_troop):
        strong = 1.1
        weak = 0.85
        general = 1
        target_troop_type = target_troop.current_troop_type
        match target_troop_type:
            case TroopType.Cavalry:
                if self.current_troop_type == TroopType.Spears:
                    return strong
                elif self.current_troop_type == TroopType.Shield:
                    return weak
            case TroopType.Shield:
                if self.current_troop_type == TroopType.Bows:
                    return weak
                elif self.current_troop_type == TroopType.Cavalry:
                    return strong
            case TroopType.Bows:
                if self.current_troop_type == TroopType.Spears:
                    return weak
                elif self.current_troop_type == TroopType.Shield:
                    return strong
            case TroopType.Spears:
                if self.current_troop_type == TroopType.Cavalry:
                    return weak
                elif self.current_troop_type == TroopType.Bows:
                    return strong
        return general


class Hero:
    # 武將
    # Forces (兵數) , Attack, Defense (統率), Speed, Intelligence, Troops (兵種)
    def __init__(
        self, name, forces, attack, defense, speed, intelligence, troops: Troop
    ):
        self.name = name
        self.current_forces = forces
        self.max_forces = forces
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.intelligence = intelligence
        self.troops = troops

    def is_alive(self):
        return self.current_forces > 0

    def attack_target(self, target):
        if not self.is_alive() or not target.is_alive():
            return

        forces_random_weight = random.uniform(0.01, 0.05)
        base_attribute_weight = random.uniform(0.01, 0.1)
        min_damage = random.randint(5, 15)

        damage = 0
        base_damage = (
            self.attack
            * self.troops.get_troop_rate()
            * self.troops.compare_troop_rate(target.troops)
        ) - (target.defense * target.troops.get_troop_rate())

        if base_damage > 0:
            damage = (
                base_damage * (1 + base_attribute_weight)
                + self.current_forces * forces_random_weight
            )
        damage = max(min_damage, int(damage))

        target.current_forces -= damage
        print(
            f"{self.name} attack {target.name} with {damage} damage, {target.name} remaining forces: {target.current_forces}"
        )
