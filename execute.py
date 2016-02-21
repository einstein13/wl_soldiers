import simulation

#example soldiers

#Barbarians
bar0 = {'name':'bar_00', 'tribe':'barbarians', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
bar2 = {'name':'bar_02', 'tribe':'barbarians', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
bar7 = {'name':'bar_07', 'tribe':'barbarians', 'attack':3, 'defense':0, 'evade':2, 'health':2} #promoted only for iron
bar10 = {'name':'bar_10', 'tribe':'barbarians', 'attack':5, 'defense':0, 'evade':2, 'health':3} #fully promoted soldier

#Empire
emp0 = {'name':'emp_00', 'tribe':'empire', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
emp2 = {'name':'emp_00', 'tribe':'empire', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
emp7 = {'name':'emp_00', 'tribe':'empire', 'attack':2, 'defense':0, 'evade':2, 'health':3} #promoted only for iron
emp10 = {'name':'emp_10', 'tribe':'empire', 'attack':4, 'defense':0, 'evade':2, 'health':4} #fully promoted soldier

#Atlanteans
atl0 = {'name':'atl_00', 'tribe':'atlanteans', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
atl2 = {'name':'atl_00', 'tribe':'atlanteans', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
atl7 = {'name':'atl_00', 'tribe':'atlanteans', 'attack':2, 'defense':1, 'evade':2, 'health':0} #promoted only for iron
atl10 = {'name':'atl_10', 'tribe':'atlanteans', 'attack':4, 'defense':2, 'evade':2, 'health':1} #fully promoted soldier

list_to_test = [bar10, emp10, atl10]
number_of_tests = 10000

stats = simulation.statistics()
stats.add_soldiers_definitions(list_to_test)
stats.simulate_all(number_of_tests)
stats.print_results()