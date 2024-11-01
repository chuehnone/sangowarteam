class Team:
    def __init__(self, name, heros):
        self.name = name
        self.heros = heros

    def is_defeated(self):
        return all(not hero.is_alive() for hero in self.heros)

    def get_alive_heros(self):
        return [hero for hero in self.heros if hero.is_alive()]
