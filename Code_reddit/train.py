from get_data import data
from ACO import ACO,result,result_after_iteration,test,print_graph,initialize_arrays
from get_constants import pheromone_initial_array, pheromone_update_array, heuristic_initial_array, heuristic_update_array, evaporation_array
import sys

correct = 0
incorrect = 0

for pi_index in pheromone_initial_array:
	for pu_index in pheromone_update_array:
		for hi_index in heuristic_initial_array:
			for hu_index in heuristic_update_array:
				for e_index in evaporation_array:
					# start loop

					# print pheromone_initial_array
					# pi_index = 0.001
					# pu_index = 0.5
					# hi_index = 0
					# hu_index = 0.3
					# e_index = 0.8

					# sys.stdout.write(str(pi_index) + "," + str(pu_index) + "," + str(hi_index) + "," + str(hu_index) + "," + str(e_index) + ",")
					initialize_arrays(pi_index,hi_index)
					print "Training"

					for j in range(9):
						for i in range(j,len(data),10):
							#prediction = 
							ACO(data.iloc[i], pi_index,pu_index,hi_index,hu_index,e_index)

							

							#print prediction
							# if prediction == data['sentiment'][i]:
							#     correct += 1
							# else:
							#     incorrect += 1

							#print str(correct) + "," + str(incorrect)

						result_after_iteration()
						
					print_graph()


					print "Testing"
					for i in range(9,len(data),10):
						test(data.iloc[i])

					result(pi_index,pu_index,hi_index,hu_index,e_index)
					#end loop