import random


def play(player1, player2, num_games, verbose=False):
    """ Function that takes players for argument and the desired number of games, and return the winning rate of the
    first player """
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"P1_win": 0, "P2_win": 0, "Tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["Tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["P1_win"] += 1
            winner = "Player 1 wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["P2_win"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1: {} | Player 2: {}\n {}\n".format(p1_play, p2_play, winner))

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['P1_win'] + results['P2_win']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['P1_win'] / games_won * 100

    print("Final results:", results)
    print("Player 1 win rate: {:.2f}%".format(win_rate))

    return win_rate


def cyril(prev_play, count=[0]):
    """ Pretty dumb, will always play a set of moves regardless of what you play """
    count[0] += 1
    choices = ["P", "S", "S", "R", "P"]
    return choices[count[0] % len(choices)]


def christal(prev_opp_play):
    """ a bit smarter than cyril, sniffs glue but also analyses your last move and try to guess on that """
    if prev_opp_play == '':
        prev_opp_play = "R"
    perfect_ans = {'P': 'S', 'R': 'P', 'S': 'R'}
    return perfect_ans[prev_opp_play]


def lana(prev_opp_play, opp_history=list()):
    """ Smart, always carry TEC-nines and will somehow analyse your moves and try to deduce your most frequent out of
    the last 10 moves """
    opp_history.append(prev_opp_play)
    last_ten = opp_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    perfect_ans = {'P': 'S', 'R': 'P', 'S': 'R'}
    return perfect_ans[most_frequent]


def dr_krieger(prev_opp_play,
               opp_history=list(),
               play_order=[{"RR": 0, "RP": 0, "RS": 0, "PR": 0, "PP": 0, "PS": 0, "SR": 0, "SP": 0, "SS": 0, }]):
    """" Smartest bot, definitely willing to beat you """
    if not prev_opp_play:
        prev_opp_play = 'R'
    opp_history.append(prev_opp_play)

    last_two = "".join(opp_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opp_play + "R",
        prev_opp_play + "P",
        prev_opp_play + "S",
    ]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    perfect_ans = {'P': 'S', 'R': 'P', 'S': 'R'}
    return perfect_ans[prediction]


def human(prev_opp_play):
    """ Us, humans"""
    while True:
        inp = input("[R]ock, [P]aper, [S]cissors? ")
        if inp in ["R", "P", "S"]:
            print(inp)
            move = inp
            break
        else:
            print("I did not understand that, can you try again?")
            continue
    return move


def random_player(prev_opp_play):
    """ random player for test """
    return random.choice(['R', 'P', 'S'])
