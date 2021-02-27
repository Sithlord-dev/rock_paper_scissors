# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago.
# It is not a very good player so you will need to change the code to pass the challenge.
import numpy as np

# ideal response:
perfect_ans = {"P": "S", "R": "P", "S": "R"}
# reset variable
AI_moves = ["R"]
opp_history = []
strategy = [0, 0, 0, 0]
AI_strategy_guess = ["", "", "", ""]
opp_guess = ["", "", "", ""]
AI_play_order = {}
opp_play_order = {}


def AI_player(prev_play):
    if prev_play in ["R", "P", "S"]:
        opp_history.append(prev_play)
        for i in range(0, 4):
            if opp_guess[i] == prev_play:
                strategy[i] += 1
    else:
        reset()

    # Strategies:

    # guess on the last move
    if len(AI_moves) > 0:
        last_play = AI_moves[-1]
        opp_guess[0] = perfect_ans[last_play]
        AI_strategy_guess[0] = perfect_ans[opp_guess[0]]
    # guess on the most frequent move of the last 10 moves
    last_10_moves = AI_moves[-10:]
    if len(last_10_moves) > 0:
        most_frequent_move = max(set(last_10_moves), key=last_10_moves.count)
        opp_guess[1] = perfect_ans[most_frequent_move]
        AI_strategy_guess[1] = perfect_ans[opp_guess[1]]
    # guess on opp move patterns
    if len(opp_history) >= 3:
        opp_guess[2] = predict_move(opp_history, 3, opp_play_order)
        AI_strategy_guess[2] = perfect_ans[opp_guess[2]]
    # guess on opp's counter-pattern-prediction
    if len(AI_moves) >= 2:
        opp_guess[3] = perfect_ans[predict_move(AI_moves, 2, AI_play_order)]
        AI_strategy_guess[3] = perfect_ans[opp_guess[3]]

    best_strategy = np.argmax(strategy)
    guess = AI_strategy_guess[best_strategy]
    if guess == "":
        guess = "S"
    AI_moves.append(guess)
    return guess


def predict_move(history, n, play_order):
    """ Predict the next move according to a history and play order """
    if "".join(history[-n:]) in play_order.keys():
        play_order["".join(history[-n:])] += 1
    else:
        play_order["".join(history[-n:])] = 1
    possible = ["".join(history[-(n - 1):]) + k for k in ["R", "P", "S"]]
    for pm in possible:
        if pm not in play_order.keys():
            play_order[pm] = 0
    predict = max(possible, key=lambda key: play_order[key])
    return predict[-1]


def reset():
    global AI_moves, opp_history, strategy, opp_guess, AI_strategy_guess, opp_play_order, AI_play_order
    AI_moves = ["R"]
    opp_history.clear()
    strategy = [0, 0, 0, 0]
    opp_guess = ["", "", "", ""]
    AI_strategy_guess = ["", "", "", ""]
    opp_play_order = {}
    AI_play_order = {}

