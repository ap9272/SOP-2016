from post_polarity import post_polarity
from get_data import data
from get_max import get_max
import matplotlib.pyplot as plt

import sys

#print negative_words

incorrect = 0
correct = 0

i=0
# positive_pheromone.append(pheromone_initial)
# negative_pheromone.append(pheromone_initial)
# positive_heuristic.append(heuristic_initial)
# negative_heuristic.append(heuristic_initial)

# max_favorite_count = get_max(data['favorite_count'])
# max_retweet_count = get_max(data['retweet_count'])
# max_user_followers_count = get_max(data['user_followers_count'])

weight_post = 1
weight_fav_count = 1
weight_retweet_count = 1
weight_follow_count = 1

positive_pheromone = []
negative_pheromone = []
positive_heuristic = []
negative_heuristic = []
ants_decision = []

def initialize_arrays(pheromone_initial,heuristic_initial):

	global positive_pheromone,negative_pheromone,positive_heuristic,negative_heuristic,ants_decision

	positive_pheromone = [pheromone_initial]*(len(data)+1)
	negative_pheromone = [pheromone_initial]*(len(data)+1)
	positive_heuristic = [heuristic_initial]*(len(data)+1)
	negative_heuristic = [heuristic_initial]*(len(data)+1)
	ants_decision = [0]*len(data)



def ACO(record, pheromone_initial,pheromone_update,heuristic_initial,heuristic_update,evaporation):


	#ants_decision.append(0)
	global i, positive_pheromone,negative_pheromone,positive_heuristic,negative_heuristic,ants_decision,correct,incorrect

	# positive_pheromone.append(pheromone_initial)
	# negative_pheromone.append(pheromone_initial)
	# positive_heuristic.append(heuristic_initial)
	# negative_heuristic.append(heuristic_initial)
	# ants_decision.append(0)

	
	positive_pheromone[i+1] = positive_pheromone[i]
	negative_pheromone[i+1] = negative_pheromone[i]
	positive_heuristic[i+1] = positive_heuristic[i]
	negative_heuristic[i+1] = negative_heuristic[i]

	if ((positive_heuristic[i]*positive_pheromone[i]) - (negative_heuristic[i]*negative_pheromone[i]) > 0):
		ants_decision[i] = 1
	elif ((positive_heuristic[i]*positive_pheromone[i]) - (negative_heuristic[i]*negative_pheromone[i]) < 0):
		ants_decision[i] = -1
	else:
		ants_decision[i] = 0

	#if (data['sentiment'][msg_no] == 0):
	#	prediction = -1
	#elif (data['sentiment'][msg_no] == 2):
	#	prediction = 0
	#else:
	#	prediction = 1

	prediction = post_polarity(record['post'])

	# favorite_count_value = record['favorite_count']/max_favorite_count
	# retweet_count_value = record['retweet_count']/max_retweet_count
	# user_followers_count_value = record['user_followers_count']/max_user_followers_count

	if (prediction != 0):
		if (prediction == 1):
			positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
		else:
			negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update

		if (ants_decision[i] == prediction):
			if (prediction == 1):
				positive_heuristic[i+1] = positive_heuristic[i] + heuristic_update
			else:
				negative_heuristic[i+1] = negative_heuristic[i] + heuristic_update
		elif (ants_decision[i] == 1 and prediction == -1):
			positive_heuristic[i+1] = positive_heuristic[i] - heuristic_update
		elif (ants_decision[i] == -1 and prediction == 1):
			negative_heuristic[i+1] = negative_heuristic[i] - heuristic_update
		elif (ants_decision[i] == 0):
			positive_heuristic[i+1] = positive_heuristic[i] - heuristic_update
			negative_heuristic[i+1] = negative_heuristic[i] - heuristic_update


		# if (ants_decision[i] == prediction):
		# 	if (ants_decision[i] == 1):
		# 		# print "ph updated"
		# 		positive_heuristic[i+1] = positive_heuristic[i] + heuristic_update
		# 		positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
		# 	elif (ants_decision[i] == -1):
		# 		# print "nh updated"
		# 		negative_heuristic[i+1] = negative_heuristic[i] + heuristic_update
		# 		negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update
		# else:
		# 	if (ants_decision[i] == 1):
		# 		# print "ph downgraded"
		# 		positive_heuristic[i+1] = positive_heuristic[i] - heuristic_update
		# 		#negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update
		# 	elif (ants_decision[i] == -1):
		# 		# print "nh downgraded"
		# 		negative_heuristic[i+1] = negative_heuristic[i] - heuristic_update
		# 		#positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
		# 	elif (prediction  == 1):
		# 		# print "pp updated"
		# 		positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
		# 		positive_heuristic[i+1] = positive_heuristic[i] + heuristic_update
		# 		# print positive_pheromone[i+1]
		# 	elif (prediction == -1):
		# 		# print "np updated"
		# 		negative_heuristic[i+1] = negative_heuristic[i] + heuristic_update
		# 		negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update

	positive_pheromone[i+1] = positive_pheromone[i+1]*evaporation
	negative_pheromone[i+1] = negative_pheromone[i+1]*evaporation

	if ( (positive_pheromone[i+1] < pheromone_initial) and (negative_pheromone[i+1] < pheromone_initial)):
		positive_pheromone[i+1] = negative_pheromone[i+1] = pheromone_initial


	# print "pp" + str(positive_pheromone)
	# print "np" + str(negative_pheromone)
	# print "ph" + str(positive_heuristic)
	# print "nh" + str(negative_heuristic)
	# print "ad" + str(ants_decision)
	
	i = i+1;

	#final_prediction = (positive_heuristic[-1]*positive_pheromone[-1]) - (negative_heuristic[-1]*negative_pheromone[-1])

	# print "pp" + str(positive_pheromone)
	# print "np" + str(negative_pheromone)
	# print "ph" + str(positive_heuristic)
	# print "nh" + str(negative_heuristic)
	# print "ad" + str(ants_decision)
	# #print final_prediction
	# print ""
	correct = 50
	incorrect = -50
	#return final_prediction

# print ACO(["i","love","ant","colony","optimization"])

def test(record):
	global i,positive_pheromone,negative_pheromone,positive_heuristic,negative_heuristic
	global correct,incorrect

	if ((positive_heuristic[i]*positive_pheromone[i]) - (negative_heuristic[i]*negative_pheromone[i]) > 0):
		ants_decision[i] = 1
	elif ((positive_heuristic[i]*positive_pheromone[i]) - (negative_heuristic[i]*negative_pheromone[i]) < 0):
		ants_decision[i] = -1
	else:
		ants_decision[i] = 0


	prediction = post_polarity(record['post'])

	# favorite_count_value = record['favorite_count']/max_favorite_count
	# retweet_count_value = record['retweet_count']/max_retweet_count
	# user_followers_count_value = record['user_followers_count']/max_user_followers_count

	if (prediction != 0):
		if (ants_decision[i] == prediction):
			# if (ants_decision[i] == 1):
			# 	# print "ph updated"
			# 	positive_heuristic[i+1] = positive_heuristic[i] + heuristic_update
			# 	positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
			# elif (ants_decision[i] == -1):
			# 	# print "nh updated"
			# 	negative_heuristic[i+1] = negative_heuristic[i] + heuristic_update
			# 	negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update
			correct = correct + 1
		else:
		# 	if (ants_decision[i] == 1):
		# 		# print "ph downgraded"
		# 		positive_heuristic[i+1] = positive_heuristic[i] - heuristic_update
		# 		#negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update
		# 	elif (ants_decision[i] == -1):
		# 		# print "nh downgraded"
		# 		negative_heuristic[i+1] = negative_heuristic[i] - heuristic_update
		# 		#positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
		# 	elif (prediction  == 1):
		# 		# print "pp updated"
		# 		positive_pheromone[i+1] = positive_pheromone[i] + pheromone_update
		# 		positive_heuristic[i+1] = positive_heuristic[i] + heuristic_update
		# 		# print positive_pheromone[i+1]
		# 	elif (prediction == -1):
		# 		# print "np updated"
		# 		negative_heuristic[i+1] = negative_heuristic[i] + heuristic_update
		# 		negative_pheromone[i+1] = negative_pheromone[i] + pheromone_update
			incorrect = incorrect + 1

	# print "prediction : " + str(prediction) + " ants_decision : " + str(ants_decision[i]) + ", heuristics : " + str(positive_heuristic[i]) + "," + str(positive_pheromone[i])
	i = i + 1



def result_after_iteration():
	global i
	# print (positive_heuristic[i]*positive_pheromone[i]) - (negative_heuristic[i]*negative_pheromone[i])
	i=0 		


def result(pi_index,pu_index,hi_index,hu_index,e_index):
	global i,correct,incorrect

	# print "pp" + str(positive_pheromone)
	# print "np" + str(negative_pheromone)
	# print "ph" + str(positive_heuristic)
	# print "nh" + str(negative_heuristic)
	# print "ad" + str(ants_decision)
	#print final_prediction
	# print "Correct : " + str(correct) + " Incorrect : " + str(incorrect)
	print "Correct = " + str(correct) + ", Incorrect = " + str(incorrect) + ", Accuracy = " + str(float(correct) * 100 / (correct + incorrect) )
	correct = incorrect = i = 0

def print_graph():
	# print positive_pheromone
	temp_list = range(len(positive_pheromone)/10)
	list_len = len(negative_heuristic)/10
	plt.plot(negative_heuristic)
	plt.xlim(0, list_len)
	plt.ylabel('negative heuristic amount')
	plt.show()