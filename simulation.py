import soldiers

class one_fight():
    soldier1 = ""
    soldier2 = ""

    def define_soldiers(self, soldier1_dict, soldier2_dict):
        self.soldier1 = ""
        self.soldier1 = soldiers.soldier()
        self.soldier1.set_stats(soldier1_dict)
        self.soldier2 = ""
        self.soldier2 = soldiers.soldier()
        self.soldier2.set_stats(soldier2_dict)
        return 0

    def simulation_step(self):
        #result: 0 - all alive, 1 - 1st died, 2 - 2nd died
        if not self.soldier1.attack_enemy(self.soldier2):
            return 2
        if not self.soldier2.attack_enemy(self.soldier1):
            return 1
        return 0

    def simulate(self, soldier1_dict, soldier2_dict):
        #result: 1 - 1st died (2nd win), 2 - 2nd died (1st win)
        self.define_soldiers(soldier1_dict, soldier2_dict)
        result = 0
        while result == 0:
            result = simulation_step()
        return result