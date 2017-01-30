import simulation

#example soldiers

#Barbarians
bar0 = {'name':'bar_00', 'tribe':'barbarians', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
bar2 = {'name':'bar_02', 'tribe':'barbarians', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
bar7 = {'name':'bar_07', 'tribe':'barbarians', 'attack':3, 'defense':0, 'evade':2, 'health':2} #promoted only for iron
bar9 = {'name':'bar_09', 'tribe':'barbarians', 'attack':5, 'defense':0, 'evade':2, 'health':2} #without last promotion
bar10 = {'name':'bar_10', 'tribe':'barbarians', 'attack':5, 'defense':0, 'evade':2, 'health':3} #fully promoted soldier

#Empire
emp0 = {'name':'emp_00', 'tribe':'empire', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
emp2 = {'name':'emp_02', 'tribe':'empire', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
emp7 = {'name':'emp_07', 'tribe':'empire', 'attack':2, 'defense':0, 'evade':2, 'health':3} #promoted only for iron
emp9 = {'name':'emp_09', 'tribe':'empire', 'attack':4, 'defense':0, 'evade':2, 'health':3} #without last promotion
emp10 = {'name':'emp_10', 'tribe':'empire', 'attack':4, 'defense':0, 'evade':2, 'health':4} #fully promoted soldier

#Atlanteans
atl0 = {'name':'atl_00', 'tribe':'atlanteans', 'attack':0, 'defense':0, 'evade':0, 'health':0} #not promoted soldier
atl2 = {'name':'atl_02', 'tribe':'atlanteans', 'attack':0, 'defense':0, 'evade':2, 'health':0} #promoted only for food
atl7 = {'name':'atl_07', 'tribe':'atlanteans', 'attack':2, 'defense':1, 'evade':2, 'health':0} #promoted only for iron
atl9 = {'name':'atl_09', 'tribe':'atlanteans', 'attack':4, 'defense':1, 'evade':2, 'health':1} #without last promotion
atl10 = {'name':'atl_10', 'tribe':'atlanteans', 'attack':4, 'defense':2, 'evade':2, 'health':1} #fully promoted soldier

list_to_test = [bar0, bar2, bar7, bar10, emp0, emp2, emp7, emp10, atl0, atl2, atl7, atl10]
list_to_test = [bar9, bar10, emp9, emp10, atl9, atl10]
#list_to_test = [bar10, emp10, atl10]
number_of_tests = 10**6
number_of_tests = 10**5

stats = simulation.statistics()
stats.add_soldiers_definitions(list_to_test)
stats.simulate_all(number_of_tests)
stats.print_results()