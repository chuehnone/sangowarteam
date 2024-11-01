import random
from enum import Enum


class Result(Enum):
    DRAW = 0
    TEAM1_WIN = 1
    TEAM2_WIN = -1


def simulate_battle(team1, team2):
    # 初始化雙方生命值
    for hero in team1.heros + team2.heros:
        hero.current_forces = hero.max_forces

    # 最大回合數
    max_count = 8
    count = 0

    while not team1.is_defeated() and not team2.is_defeated():
        # 獲取所有存活的單位
        alive_team1 = team1.get_alive_heros()
        alive_team2 = team2.get_alive_heros()
        all_heros = alive_team1 + alive_team2

        # 按速度排序，速度高的先行動
        all_heros.sort(key=lambda x: x.speed, reverse=True)

        for hero in all_heros:
            if not hero.is_alive():
                continue
            if hero in team1.heros:
                enemies = team2.get_alive_heros()
                if not enemies:
                    break
                target = random.choice(enemies)
                hero.attack_target(target)
            else:
                enemies = team1.get_alive_heros()
                if not enemies:
                    break
                target = random.choice(enemies)
                hero.attack_target(target)
        count += 1
        if count >= max_count:
            break
    if team1.is_defeated() == team2.is_defeated():
        return Result.DRAW
    elif team2.is_defeated():
        return Result.TEAM1_WIN
    else:
        return Result.TEAM2_WIN
