import soldiers

def round(number, points):
    base = 10**points
    bigger = number*base
    if bigger - int(bigger) >= 0.5:
        bigger += 1
    return 1.0 * int(bigger)/base

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
        result = [result, self.soldier1.health, self.soldier2.health]
        return result


class main_simulation():
    soldier1_wins = 0
    soldier2_wins = 0
    attackers_healt = 0.0
    defenders_healts = 0.0
    
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
            if result[0] == 1:
                self.soldier2_wins += 1
            elif result[0] == 2:
                self.soldier1_wins += 1
            self.attackers_healt += result[1]
            self.defenders_healts += result[2]
        soldiers = one_fight()
        soldiers.define_soldiers(soldier1_dict, soldier2_dict)

        stat_1 = 1.0 * self.soldier1_wins / number_of_fights
        stat_2 = 0.0
        if self.attackers_healt > 0.0:
            stat_2 = self.attackers_healt / number_of_fights / soldiers.soldier1.health
        stat_3 = 0.0
        if self.defenders_healts > 0.0:
            stat_3 = self.defenders_healts / number_of_fights / soldiers.soldier2.health

        result = [stat_1, stat_2, stat_3]
        return result

class statistics():
    result_matrix = []
    attackers_healts = []
    defenders_healts = []
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
            self.attackers_healts.append([])
            self.defenders_healts.append([])
            for itr2 in range(length):
                self.result_matrix[itr1].append(0.0)
                self.attackers_healts[itr1].append(0.0)
                self.defenders_healts[itr1].append(0.0)
        return 0

    def simulate_one(self, soldier1, soldier2, number_of_fights):
        simulation = main_simulation()
        dict1 = self.dictionaries_list[soldier1]
        dict2 = self.dictionaries_list[soldier2]
        result = simulation.simulate(dict1, dict2, number_of_fights)
        result = [x * 100 for x in result]
        self.result_matrix[soldier1][soldier2] = result[0]
        self.attackers_healts[soldier1][soldier2] = result[1]
        self.defenders_healts[soldier1][soldier2] = result[2]
        return result

    def simulate_all(self, number_of_fights):
        length = len(self.dictionaries_list)
        self.construct_result_matrix()
        for itr1 in range(length):
            for itr2 in range(length):
                res = self.simulate_one(itr1, itr2, number_of_fights)
                string = str(self.dictionaries_list[itr1]['name'])
                string += " vs. "
                string += str(self.dictionaries_list[itr2]['name'])
                string += "\t"+str(res[0])+"%"
                string += "\tAT_hp="+str(round(res[1],4))+"%"
                string += "\tDF_hp="+str(round(res[2],4))+"%"
                print(string)
        return 0

    def markdown_table(self, matrix):
        length = len(self.dictionaries_list)
        string = "| vs."
        for itr1 in range(length):
            string += " | "+self.dictionaries_list[itr1]['name']
        string += " |\n"
        for itr1 in range(-1, length):
            string += "| --- "
        string += "|\n"
        for itr1 in range(length):
            for itr2 in range(-1,length):
                if itr2 == -1:
                    string += "| " + self.dictionaries_list[itr1]['name']
                else:
                    string += " | " + str(round(matrix[itr1][itr2],1)) + "%"
            string += " |\n"
        return string

    def print_results(self):
        string = "Battles win:\n"
        string += self.markdown_table(self.result_matrix)
        string += "\nAttackers health:\n"
        string += self.markdown_table(self.attackers_healts)
        string += "\nDefenders health:\n"
        string += self.markdown_table(self.defenders_healts)
        print("\n"+string)
        file = open("out.txt","w")
        file.write(string)
        file.close()
        return 0