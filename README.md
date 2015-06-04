# HMM
HMM and POS tagging HW

1.1: Enumerate all of the possible hidden state sequences and compute 
P(X1, X2, X3, X4, O1 = G, O2 = M, O3 = B, O4 = G) for each.
=P(initial_state)SUM(P(O))SUM(P(X))

0 = C, 1 = H
[0, 0, 0, 0]: 0.000648
[0, 0, 0, 1]: 0.001296
[0, 0, 1, 0]: 7.2e-05
[0, 0, 1, 1]: 0.000216
[0, 1, 0, 0]: 0.00036
[0, 1, 0, 1]: 0.00072
[0, 1, 1, 0]: 6e-05
[0, 1, 1, 1]: 0.00018
[1, 1, 1, 1]: 0.000675
[1, 1, 1, 0]: 0.000225
[1, 1, 0, 1]: 0.0027
[1, 1, 0, 0]: 0.00135
[1, 0, 1, 1]: 0.00054
[1, 0, 1, 0]: 0.00018
[1, 0, 0, 1]: 0.00324
[1, 0, 0, 0]: 0.00162
total prob = 0.014082

1.2: alphai(t) represents the probability of the most likely state at any index on the HMM.

1.3: Run forward algorithm to compute the sum of the scores of all possible hidden state sequences.
Alpha(x): [hot, cold]
Alpha(1): [0.3, 0.1]
Alpha(2): [0.06, 0.05399999999999999]
Alpha(3): [0.0057, 0.028199999999999996]
Alpha(4): [0.010169999999999998, 0.00384]
Final score: 0.014009999999999998

1.4: alphai(x) is the probability of the most probable path to state i at position x.

1.5: Run Viterbi algorithm to compute the score of the best hidden state sequence.

Score of best hidden state sequence: 5.125781249999999e-07

2.1: 
(Pierre NNP) (Vinken NNP), (61 CD) (years NNS) (old JJ), (will MD) (repowentate  VB) (the DT) (krowen  NN) (as  IN) (a DT) (nonexecutive JJ) (director NN) (Nov. NNP) (29 CD). 
‘Vinken’ is tagged at a proper noun because it is capitalized and not beginning a sentence. It also comes after another proper noun, which is a common trend because first and last names come right after each other. 
‘repowentate’ is tagged at a verb because it directly follows a modal verb.
‘krownen’ is tagged as a noun because it directly follows a determiner.
2.2:
(Every DT) (time NN) (I PRP) (fire VB) (a DT) (linguist NN), (the DT) (performance NN) (of IN) (speech JJ) (recognizer NN) (is VB) (on IN) (fire NN). 
The first occurrence of ‘fire’ is tagged as a verb because ‘I’ is a complete NP. Since there is also an NP (‘a linguist’) following ‘fire’, the English grammar would probably not find it to be an NN also.
The second occurrence of ‘fire’ is a noun because it is following an IN, and probably in a PP. The possible verb tag for ‘fire’ would not make sense in this environment.
2.3:
(Colorless JJ) (green JJ) (ideas NNS) (sleep VB) (okletinely RB). 
‘okletinely’ is tagged as an adverb because I am familiar with the example that has ‘furiously’ instead. English grammar would allow ‘okletinely’ to be an NN as well, but a POS tagger would statistically determine which part of speech ‘oketinely’ would be.
2.4:
(The DT) (landlord NN) (marks VB) (where WDT) (the DT) (tenants NN) (left VBD) (the DT) (marks NN). 
The first occurrence of ‘marks’ follows a complete NP. ‘marks’ is either a verb or a noun, it is most likely a verb in this environment. 
The second occurrence of ‘marks’ directly follows a determine, which would make it a noun since there is no adjective reading of the word. 
