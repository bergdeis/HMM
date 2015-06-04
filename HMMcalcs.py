hidden = [[.6, .4],[.5, .5]]
observable = [[.2, .3, .5],[.6, .3, .1]]
initial_prob = [.5, .5]

cold = [['c', 'c', 'c', 'c'],['c', 'c', 'c', 'h'],['c', 'c', 'h', 'c'],
        ['c', 'c', 'h', 'h'],['c' ,'h', 'c', 'c'], ['c', 'h', 'c', 'h'],
        ['c', 'h', 'h', 'c'],['c', 'h', 'h', 'h']]

hot = list()

"""hot is the same as cold, but 'h's and 'c's are reversed"""
for sequence in cold:
	temp = list()
	for state in sequence:
		if state == 'c':
			temp.append('h')
		else:
			temp.append('c')
	hot.append(temp)

state_sequences = hot + cold

new_sequence = list()
for sequence in state_sequences:
	temp = list()
	for state in sequence:
		if state == 'c':
			temp.append(1)
		else:
			temp.append(0)
	new_sequence.append(temp)

"I decided to change 'c' and 'h' to 0 and 1 respectively to index my lists more easily"""
"""
>>> new_sequence
[[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 0, 1, 1], [0, 1, 0, 0],
[0, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0],
[1, 1, 0, 1], [1, 1, 0, 0], [1, 0, 1, 1], [1, 0, 1, 0], [1, 0, 0, 1],
[1, 0, 0, 0]]
"""
state_sequences = new_sequence

"""determines probability for each state_sequence"""
for sequence in state_sequences:
	initial = sequence[0]
	prev = initial
	prob = initial_prob[initial]
	prob *= observable[initial][0]
	count = 1
	for state in sequence[1:]:
		prob *= hidden[prev][state]
		if count == 1:
			prob *= observable[state][1]
		if count == 2:
			prob *= observable[state][2]
		if count == 3:
			prob *= observable[state][0]
		count += 1	
		prev = state
	print str(sequence) + ': ' + str(prob)
	

"Forward Algorithm"""
def state_score(current, sequence, hidden, observable):
	if len(sequence) == 0:
		return current
	else:
		"""obser corresponds to the observation state's indeces in observable"""
		obser = 0
		if sequence[0] == 'm':
			obser = 1
		elif sequence[0] == 'b':
			obser = 2

		h = (current[0] * hidden[1][1] * observable[1][obser]) + (current[1] * hidden[1][0] * observable[1][obser])
		c = (current[1] * hidden[0][0] * observable[0][obser]) + (current[0] * hidden[0][1] * observable[0][obser])
		print [h,c]
		return state_score([h,c], sequence[1:], hidden, observable)

"""I started with the alpha_1 already calculated because that is a slightly
different calculation"""
alpha_one = [current[0] + initial_prob[1] * observable[1][0], current[1] + initial_prob[0] * observable[0][0]]
"""
>>> alpha_one
[0.3, 0.1]
>>> final_scores = state_score(alpha_one, ['m', 'b', 'g'], hidden, observable)
[0.06, 0.05399999999999999]
[0.0057, 0.028199999999999996]
[0.010169999999999998, 0.00384]
>>> final_score = final_scores[0] + final_scores[1]
>>> final_score
0.014009999999999998
"""

"""Viterbi Algorithm"""
def viterbi(current, sequence, hidden):
	if len(sequence) == 0:
		return current
	else:
		h = current[0] * max(current[0] * hidden[1][1], current[1] * hidden[1][0])
 		c = current[1] * max(current[0] * hidden[0][1], current[1] * hidden[0][0])
 		print [h,c]
 		return viterbi([h,c], sequence[1:], hidden)
"""
>>> score = viterbi(alpha_one, ['m', 'b', 'g'], hidden)
[0.045, 0.012]
[0.0010125, 0.000216]
[5.125781249999999e-07, 8.747999999999999e-08]
"""

