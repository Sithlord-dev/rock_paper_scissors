# Rock paper scissors game!

A little program to play Rock, Paper, Scissors with 4 different bots : 

`cyril` : Pretty dumb, will always play a set of moves regardless of what you play.
`christal` : a bit smarter than cyril, sniffs glue but also analyses your last move and try to guess on that.
`lana` : Smart, always carry TEC-nines and will somehow analyse your moves and try to deduce your most frequent out of the last 10 moves.
`dr_krieger` : Smartest bot, definitely willing to beat you.

and an `AI_player` that beats the four of them.

The `play` function takes four arguments:
- two players to play against each other (the players are actually functions)
- the number of games to play in the match
- an optional argument to see a log of each game. Set it to `True` to see these messages.

```py
play(player1, player2, num_games[, verbose])
```

You can play against one of four bots, or against their boss. You can also play against a random player.
Here is an example where Cyril plays against a random player:

```py
play(cyril, random_player, 1000)
```
