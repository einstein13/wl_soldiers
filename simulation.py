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
            result = self.simulation_step()
        return result

class main_simulation():
    soldier1_wins = 0
    soldier2_wins = 0
    
    def simulate(self, soldier1_dict, soldier2_dict, number_of_fights):
        self.soldier1_wins = 0
        self.soldier2_wins = 0
        figth = ""
        itr = 0
        while itr < number_of_fights:
            itr += 1
            figth = ""
            figth = one_fight()
            result = figth.simulate(soldier1_dict, soldier2_dict)
            if result == 1:
                self.soldier2_wins += 1
            elif result == 2:
                self.soldier1_wins += 1
        return 1.0 * self.soldier1_wins / number_of_fights

class statistics():
    result_matrix = []
    dictionaries_list = []
    
    def add_soldiers_definitions(self, dictionary_or_list):
        if isinstance(dictionary_or_list, dict):
            self.dictionaries_list.append(dictionary_or_list)
            return 0
        for element in dictionary_or_list:
            self.dictionaries_list.append(element)
        return 0

    def construct_result_matrix(self):
        length = len(self.dictionaries_list)
        self.result_matrix = []
        for itr1 in range(length):
            self.result_matrix.append([])
            for itr2 in range(length):
                self.result_matrix[itr1].append(0.0)
        return 0

    def simulate_one(self, soldier1, soldier2, number_of_fights):
        simulation = main_simulation()
        dict1 = self.dictionaries_list[soldier1]
        dict2 = self.dictionaries_list[soldier2]
        result = 100.0*simulation.simulate(dict1, dict2, number_of_fights)
        self.result_matrix[soldier1][soldier2] = result
        return result

    def simulate_all(self, number_of_fights):
        length = len(self.dictionaries_list)
        self.construct_result_matrix()
        for itr1 in range(length):
            for itr2 in range(length):
                res = self.simulate_one(itr1, itr2, number_of_fights)
                print(str(self.dictionaries_list[itr1]['name'])+" vs. "+str(self.dictionaries_list[itr2]['name'])+"\t"+str(res)+"%")
        return 0

    def print_results(self):
        length = len(self.dictionaries_list)
        for itr1 in range(length):
            for itr2 in range(length):
                print(str(itr1)+"\t"+str(itr2)+"\t"+str(self.result_matrix[itr1][itr2]))
        return 0