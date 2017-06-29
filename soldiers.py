import stats
import random

class soldier():
    attack_min = 0.0
    attack_max = 0.0
    defense = 0.0
    evade = 0.0
    health = 0.0
    tribe = 0

    def set_tirbe(self, tribe_name):
        if tribe_name == "barbarians" or tribe_name == "Barbarians":
            self.tribe = 1
        elif tribe_name == "empire" or tribe_name == "Empire":
            self.tribe = 2
        elif tribe_name == "atlanteans" or tribe_name == "Atlanteans":
            self.tribe = 3
        elif tribe_name == "frisians" or tribe_name == "Frisians":
            self.tribe = 4
        return 0

    def set_stats(self, dict):
        if not "tribe" in dict.keys():
            return 0
        self.set_tirbe(dict['tribe'])
        if "attack" in dict.keys():
            self.attack_min = stats.get_min_attack(self.tribe, dict['attack'])
            self.attack_max = stats.get_max_attack(self.tribe, dict['attack'])
        if "defense" in dict.keys():
            self.defense = stats.get_defense(self.tribe, dict['defense'])
        if "evade" in dict.keys():
            self.evade = stats.get_evade(self.tribe, dict['evade'])
        if "health" in dict.keys():
            self.health = stats.get_health(self.tribe, dict['health'])
        return 0

    def is_alive(self):
        return self.health > 0

    def form_attack(self):
        return random.randint(self.attack_min*1000, self.attack_max*1000)/1000.0

    def form_defence(self, attack):
        # return: True - still alive, False - killed
        rand_evade = random.uniform(0.0, 1.0)
        if rand_evade > self.evade:
            return True
        self.health -= attack * self.defense
        if self.is_alive():
            return True
        self.health = 0.0
        return False

    def attack_enemy(self, enemy_soldier):
        attack_force = self.form_attack()
        return enemy_soldier.form_defence(attack_force)