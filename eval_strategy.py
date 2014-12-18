#!/bin/python

from __future__ import division
from itertools import permutations, combinations, combinations_with_replacement
from math import factorial

def validate_user_choices(user_choices):
    for choice in user_choices:
        if len(choice) != user_choices / 2:
            return False
    return True

# user_choices is an array of boxes each user will open
# we generate all possible arrangements of boxes and calculate the percentage of times the strategy will succeed
def eval_strategy(user_choices, debug=False):
    num_boxes = len(user_choices)
    win_count = 0

    if debug: print user_choices
    for arrangement in permutations(range(num_boxes)):
        if eval_arrangement(user_choices, arrangement, debug):
            win_count += 1

    return win_count / factorial(num_boxes)

# for each box's user, checks if the user is planning to open that box
def eval_arrangement(user_choices, arrangement, debug=False):
    if debug: print "arrangement: "+str(arrangement),
    for box_number, user_number in enumerate(arrangement):
        boxes_for_user = user_choices[user_number]
        if box_number not in boxes_for_user:
            if debug: print "failed"
            return False
    if debug: print "succeeded"
    return True


def test_eval_arrangement():
    example_user_choices = [ [0], [1] ]
    example_arrangement = [0, 1]
    print "expect True"
    print eval_arrangement(example_user_choices, example_arrangement)
    failing_arrangement = [1, 0]
    print "expect False"
    print eval_arrangement(example_user_choices, failing_arrangement)

def test_eval_strategy():
    example_user_choices = [ [0], [1] ]
    print "expect .5"
    print eval_strategy(example_user_choices, True)

def some_junk():
    # conjecture: every pair of users needs to have the minimum overlap
    # user 0 and 1 split half, user 2 and 3 split half, but each pair don't worry about each other
    four_person_strategy_1 = [ [0, 1], [2, 3], [0, 1], [2, 3] ] # so this won't lose all the time but won't be awesome
    print eval_strategy(four_person_strategy_1, True)
    four_person_strategy_2 = [ [0, 1], [2, 3], [0, 3], [1, 2] ] # this will be better than strategy 1 because no two users have the exact same choices [WRONG]
    print eval_strategy(four_person_strategy_2, True)
    #and strategy 2 is half as good as 1, because there were only 2 box arragements that will match, while strat 1 matched 4
    four_person_strategy_3 = [ [0, 1], [2, 3], [0, 2], [1, 3] ] 
    print eval_strategy(four_person_strategy_3, True)

# note that 6 boxes have 177100 strategies
def generate_all_strategies(count):
    all_available_choices = combinations(range(count), count // 2)
    return combinations_with_replacement(all_available_choices, count)

def find_winning_strategies(count):
    winners = []
    best_score = 0
    for strat in list(generate_all_strategies(count)):
        score = eval_strategy(strat)
        if score > best_score:
            winners = [strat]
            best_score = score
        elif score == best_score:
            winners.append(strat)
        print str(strat)+": "+str(eval_strategy(strat))
    
    print "best score: "+str(best_score)
    print "winners:"+str(winners)
    for w in winners:
        print w

find_winning_strategies(4)

