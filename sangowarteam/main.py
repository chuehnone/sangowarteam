import multiprocessing
from hero import Troop, Hero, TroopQuality, TroopType
from sangowarteam.battle import Result
from team import Team
from battle import simulate_battle


def worker(args):
    team1, team2, simulations = args
    local_results = {
        Result.DRAW.name: 0,
        Result.TEAM1_WIN.name: 0,
        Result.TEAM2_WIN.name: 0,
    }
    for _ in range(simulations):
        result = simulate_battle(team1, team2)
        local_results[result.name] += 1
    return local_results


def calculate_win_rate_parallel(team1, team2, total_simulations=10000, num_workers=4):
    simulations_per_worker = total_simulations // num_workers
    pool = multiprocessing.Pool(processes=num_workers)
    args = [(team1, team2, simulations_per_worker) for _ in range(num_workers)]
    results = pool.map(worker, args)
    pool.close()
    pool.join()

    final_results = {
        Result.DRAW.name: 0,
        Result.TEAM1_WIN.name: 0,
        Result.TEAM2_WIN.name: 0,
    }
    for res in results:
        for key in final_results:
            final_results[key] += res.get(key, 0)

    win_rate_team1 = (final_results[Result.TEAM1_WIN.name] / total_simulations) * 100
    win_rate_team2 = (final_results[Result.TEAM2_WIN.name] / total_simulations) * 100
    draw_rate = (final_results[Result.DRAW.name] / total_simulations) * 100
    return {team1.name: win_rate_team1, team2.name: win_rate_team2, "平手": draw_rate}


if __name__ == "__main__":
    # 定義隊伍1
    team1_heros = [
        Hero(
            "劉備",
            attack=115.63,
            defense=10.63,
            forces=100,
            speed=10.63,
            intelligence=10.63,
            troops=Troop(
                cavalry=TroopQuality.C,
                shield=TroopQuality.C,
                bows=TroopQuality.C,
                spears=TroopQuality.C,
            ),
        ),
        Hero(
            "關羽",
            attack=15.63,
            defense=10.63,
            forces=100,
            speed=10.63,
            intelligence=10.63,
            troops=Troop(
                cavalry=TroopQuality.C,
                shield=TroopQuality.C,
                bows=TroopQuality.C,
                spears=TroopQuality.C,
            ),
        ),
        Hero(
            "張飛",
            attack=15.63,
            defense=10.63,
            forces=100,
            speed=10.63,
            intelligence=10.63,
            troops=Troop(
                cavalry=TroopQuality.C,
                shield=TroopQuality.C,
                bows=TroopQuality.C,
                spears=TroopQuality.C,
            ),
        ),
    ]
    team1 = Team("蜀軍", team1_heros)
    for hero in team1.heros:
        hero.troops.set_current(TroopType.Bows)

    # 定義隊伍2
    team2_heros = [
        Hero(
            "曹操",
            attack=10,
            defense=10,
            forces=100,
            speed=10,
            intelligence=10,
            troops=Troop(
                cavalry=TroopQuality.C,
                shield=TroopQuality.C,
                bows=TroopQuality.C,
                spears=TroopQuality.C,
            ),
        ),
        Hero(
            "夏侯惇",
            attack=10,
            defense=10,
            forces=100,
            speed=10,
            intelligence=10,
            troops=Troop(
                cavalry=TroopQuality.C,
                shield=TroopQuality.C,
                bows=TroopQuality.C,
                spears=TroopQuality.C,
            ),
        ),
        Hero(
            "夏侯淵",
            attack=10,
            defense=10,
            forces=100,
            speed=10,
            intelligence=10,
            troops=Troop(
                cavalry=TroopQuality.C,
                shield=TroopQuality.C,
                bows=TroopQuality.C,
                spears=TroopQuality.C,
            ),
        ),
    ]
    team2 = Team("魏軍", team2_heros)
    for hero in team2.heros:
        hero.troops.set_current(TroopType.Cavalry)

    # 計算勝率
    win_rates = calculate_win_rate_parallel(
        team1, team2, total_simulations=1, num_workers=1
    )
    print(f"勝率結果：{win_rates}")
