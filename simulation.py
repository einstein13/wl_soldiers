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