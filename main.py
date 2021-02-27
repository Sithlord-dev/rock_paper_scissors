from game import play, cyril, christal, lana, dr_krieger, human, random_player
from AI_player import AI_player


# play(AI_player, cyril, 1000)
# play(AI_player, christal, 1000)
# play(AI_player, lana, 1000)
# play(AI_player, dr_krieger, 1000)

# Play interactively against one of the bots:
play(human, cyril, 20, verbose=True)

# Play against a bot that plays randomly:
# play(cyril, dr_krieger, 100000)

