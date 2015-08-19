# COMP1001-Final-Project
My final project for this course, 5 card poker!

Written in Python 3.4

## Description
This program is my implementation of the game "Poker" which utilizes the standard ruleset of the 5 Hand variant.
The goal of poker is to obtain a better hand than your opponents through strategy and luck by redrawing cards.
This game supports multiplayer from 2 to 4 players per match.

## How to Play
1. Start off by inputting total number of players, to which game will initiate
2. A fresh deck will be shuffled and the game will commence with Player 1's turn, which will progress to Player 2, Player 3, and Player 4.
3. Player 1 will be able to initiate their turn by viewing their hand and respectively choosing how many and which cards to discard and redraw from the deck.
4. Player 1 will redraw any cards selected and the new hand will be displayed.
5. Player 1's turn ends and repeat steps 3 and 4 for all the other players.
6. Once all players have ended their turns, all players show their hands and the player with the best hand wins.
7. The winner will get +1 point added to their score and the game offers players to continue playing.
8. Once users decide to finish game, scores are added up and displayed onto a text file.

## Poker Hand Rankings
1. Royal Flush
2. Straight Flush
3. Four of a Kind
4. Full House
5. Flush
6. Straight
7. Three of a Kind
8. Two Pair
9. One Pair
10. High Card

## Mockup

Playing the game is simple:
```
$ Please enter the number of players(1-4), or 5 for hand rankings, or '0' to quit: 
```

Just enter the number of players you want to initiate the game.
```
$ 2
```

Once the player count information has been inputted, just follow the instructions printed on screen.
```
===TWO PLAYER GAME===
$ Player 1's Turn, please press enter to continue..
```

As the game progresses, just simply keep on following the instructional prompts.
```
$ 1) 10 of Hearts
$ 2) Ace of Spades
$ 3) 8 of Diamonds
$ 4) Queen of Spades
$ 5) 7 of Clubs
$ How many cards would you like to redraw? (0-5): 1
$ Which card do you want to remove? (1-5): 4
----------------------------------------------------
$ Your redrawn hand:
$ 1) 10 of Hearts
$ 2) Ace of Spades
$ 3) 8 of Diamonds
$ 4) 9 of Spades
$ 5) 7 of Clubs
$ Please press enter to finish turn
```

Allow for other players to do the same, switching screens each time each players's turn begins.  Notice
as all the players begin to finish their turns, a message pops up indicating to enter showdown, an environment
which checks player hands to see which is the best.
```
  >>> Please press enter to showdown..
```

The checkHandCombo() method takes in the Player's hand and evaluates the number of pairs or any other
form of combo that is apparent in poker, this method utilizes collections as well as lists to sort out the
possible winning hands each player may have and ultimately delivers the result of the winning player.
See above for possible hands.

## Module Citations
Random Library - Used for randint in shuffling and in AI
Collections Library - Used for checking winning hand combos

