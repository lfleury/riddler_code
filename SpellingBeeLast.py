import numpy as np
from collections import Counter

results = []

# configure the overall number of simulations and a counter variable and iterate through that number of simulations
num_simulations = 100000
simulation = 1

# create a list of people along with their probability of getting any given word
while simulation <= num_simulations:
    contestants = [
        {'name': 'person 10', 'probability': .90},
        {'name': 'person 9', 'probability': .91},
        {'name': 'person 8', 'probability': .92},
        {'name': 'person 7', 'probability': .93},
        {'name': 'person 6', 'probability': .94},
        {'name': 'person 5', 'probability': .95},
        {'name': 'person 4', 'probability': .96},
        {'name': 'person 3', 'probability': .97},
        {'name': 'person 2', 'probability': .98},
        {'name': 'person 1', 'probability': .99}
    ]
	
	# iterate through different rounds until there is only a single contestant left
    round_num = 1

    while len(contestants) > 1:
		# create empty list to store contestants as they answer wrong
        failed_contestants = []
		# iterate through each contestant in above list
        for contestant in contestants:
			# get probability value from the contestant's dictionary
            succeed_probability = contestant['probability']
			# generate either 0 (wrong answer) or 1 (right answer) based on the probability of success. 
			# np.random.choice params are : 2 (list with 2 elements, 0 and 1), 1 (number of tries to generate), and p[probability of element 0, probability of element 1])
            response = np.random.choice(2, 1, p=[1 - succeed_probability, succeed_probability])[0]
			# if the contestant answers incorrectly, add them to the failed_contestants list
            if response == 0:
                failed_contestants.append(contestant)
		# in the situation where we generated 0 for every one of the remaining contestants, the last one is the only remaining individual by default, so the person who answers last wins by default because everyone else was eliminated already
        if len(failed_contestants) == len(contestants):
            # remove the contestant from the list of failed contestants who went last (i.e. the others failed before them and they won by being the last inidividual standing)
            failed_contestants.remove(failed_contestants[len(failed_contestants) - 1])
		# remove anyone who answered wrong from the contestants list, so the subsequent loop only contains individuals who answered correctly in the prior round
        for failed_contestant in failed_contestants:
            contestants.remove(failed_contestant)
		# increment round counter variable
        round_num = round_num + 1
	# append winning contestant's name to the results list, which contains the winner from an individual simulation.
    results.append(contestants[0]['name'])
	# log every 1000 simulations to the console to track progress
    if simulation % 1000 == 0:
        print('simulation {0} completed'.format(simulation))
	# increment simulation counter variable, then loop
    simulation = simulation + 1

# store a dictionary of the number of times each contestant won. 
results = Counter(results)

print(results)
# Counter({'person 1': 52426, 'person 2': 21571, 'person 3': 10893, 'person 4': 5978, 'person 5': 3639, 'person 6': 2154, 'person 7': 1418, 'person 8': 940, 'person 9': 587, 'person 10': 394})

# order of this is relatively random, it just orders by whoever won first on the first few simulations. I manually reordered mine. 
print('contestant    wins    probability')
for key, value in results.items():
    print(key, value, value/num_simulations)
	
# contestant    wins    probability
# person 1 		52426 	0.52426
# person 2 		21571 	0.21571
# person 3 		10893 	0.10893
# person 4 		5978 	0.05978
# person 5 		3639 	0.03639
# person 6 		2154 	0.02154
# person 7 		1418 	0.01418
# person 8 		940 	0.0094
# person 9 		587 	0.00587
# person 10 	394 	0.00394

