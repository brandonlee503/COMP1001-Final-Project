###
#5 Card Poker
#Brandon Lee
"""
===Program Design===
The program consists of an implementation of the game "5 Card Poker", utilizing classes.
The program utilizes a deck class to create an array of Card objects in order to simulate a
realistic gaming environment with factors such as luck as well as skill.  The program uses
other modules as well as built in modules to check for winnings hands.  The game is designed
to entertain a maximum of four players.

===Amount of Effort===
I believe that I put in a good amount of work.  Making a working program with classes in python
was a bit new to me and took longer than I had initially expected.  However, this did provide me
with a lot of knowledge on how classes can be utilized and how powerful OO programming can be
with Python.  Ultimately, I would say I put in a good amount of work into making this game
as my project was not modeled towards any other existing program, but completely designed from
the ground up.
"""

#---Description---
#This program is my implementation of the game "Poker" which utilizes the standard ruleset of the 5 Hand variant.
#The goal of poker is to obtain a better hand than your opponents through strategy and luck by redrawing cards.
#This game supports multiplayer from 2 to 4 players per match.

#---Application Directions (How to Play)---
#1) Start off by inputting total number of players, to which game will initiate
#2) A fresh deck will be shuffled and the game will commence with Player 1's turn,
#   which will progress to Player 2, Player 3, and Player 4.
#3) Player 1 will be able to initiate their turn by viewing their hand and respectively
#   choosing how many and which cards to discard and redraw from the deck.
#4) Player 1 will redraw any cards selected and the new hand will be displayed.
#5) Player 1's turn ends and repeat steps 3 and 4 for all the other players.
#6) Once all players have ended their turns, all players show their hands and the
#   player with the best hand wins.
#7) The winner will get +1 point added to their score and the game offers players to continue playing.
#8) Once users decide to finish game, scores are added up and displayed onto a text file.

#---Poker Hand Rankings--
#1) Royal Flush
#2) Straight Flush
#3) Four of a Kind
#4) Full House
#5) Flush
#6) Straight
#7) Three of a Kind
#8) Two Pair
#9) One Pair
#10)High Card

#---Module Citations---
# Random Library - Used for randint in shuffling and in AI
# Collections Library - Used for checking winning hand combos
###
Here's a sample session to show how to use this module.
At the moment, this is the only documentation.

The Basics
----------

Playing the game is simple:

   >>> Please enter the number of players(1-4), or 5 for hand rankings, or '0' to quit: 

Just enter the number of players you want to initiate the game.

  >>> 2

Once the player count information has been inputted, just follow the instructions printed on screen.

  >>>	===TWO PLAYER GAME===
  >>> Player 1's Turn, please press enter to continue..

As the game progresses, just simply keep on following the instructional prompts.

  >>> 1) 10 of Hearts
  >>> 2) Ace of Spades
  >>> 3) 8 of Diamonds
  >>> 4) Queen of Spades
  >>> 5) 7 of Clubs

  >>> How many cards would you like to redraw? (0-5): 1
  >>> Which card do you want to remove? (1-5): 4
----------------------------------------------------
  >>> Your redrawn hand:
  >>> 1) 10 of Hearts
  >>> 2) Ace of Spades
  >>> 3) 8 of Diamonds
  >>> 4) 9 of Spades
  >>> 5) 7 of Clubs
  >>> Please press enter to finish turn

Allow for other players to do the same, switching screens each time each players's turn begins.  Notice
as all the players begin to finish their turns, a message pops up indicating to enter showdown, an environment
which checks player hands to see which is the best.

  >>> Please press enter to showdown..

The checkHandCombo() method takes in the Player's hand and evaluates the number of pairs or any other
form of combo that is apparent in poker, this method utilizes collections as well as lists to sort out the
possible winning hands each player may have and ultimately delivers the result of the winning player.
See above for possible hands.

#Finally here is the Poker project:

from random import randint
import collections
###################################################################################################################################
class Card:
    """The card class - Stores card suit and rank.  Also able to print cards too."""
    def __init__(self, rankCard = "defaultRank", suitCard = "defaultSuit"):
        self.rank = rankCard
        self.suit = suitCard
#-----------------------------------------------------------------------------------------------------------------------------------        
    def printCard(self):
        """Print rank and suit of the card."""
        #Check if face card, if so print the face
        if(self.rank == "11"):
            self.cardString = "Jack" + " of " + self.suit
        elif(self.rank == "12"):
            self.cardString = "Queen" + " of " + self.suit
        elif(self.rank == "13"):
            self.cardString = "King" + " of " + self.suit
        elif(self.rank == "14"):
            self.cardString = "Ace" + " of " + self.suit
        else:
            self.cardString = self.rank + " of " + self.suit
            
        return(self.cardString)
#-----------------------------------------------------------------------------------------------------------------------------------  
    def getRank(self):
        """Obtain the card's rank."""
        return int(self.rank)
#-----------------------------------------------------------------------------------------------------------------------------------  
    def getSuit(self):
        """Obtain the card's suit."""
        return self.suit
###################################################################################################################################
class Deck:
    """The Deck Class - Stores array of cards.  Also able to draw, print, and shuffle."""
    def __init__(self):
        #Initilize range of ranks and suits of all the cards in the deck
        #11=Jack , 12=Queen, 13=King, 14=Ace
        self.ranks = ["14", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        self.suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

        #Create array of cards
        self.deckArray = [Card() for i in range(52)]
        #Fill the deck array
        for i in range(52):
            self.deckArray[i] = Card( self.ranks[int(i%13)] , self.suits[int(i/13)] )
        #Set remaining cards in deck
        self.avaliCards = 52
        #Initilize as -1 because of drawCardFromTop() method
        self.deckTop = -1
#-----------------------------------------------------------------------------------------------------------------------------------  
    def shuffleDeck(self):
        """Randomizes the deck"""
        #For each card in the deck, swap it with another random card
        for i in range(51):
            random = randint(0,51)
            tempCard = self.deckArray[i]
            self.deckArray[i] = self.deckArray[random]
            self.deckArray[random] = tempCard
#-----------------------------------------------------------------------------------------------------------------------------------  
    def printDeck(self):
        """Prints the deck"""
        for i in range(self.avaliCards):
            print( self.deckArray[i].printCard() )
#-----------------------------------------------------------------------------------------------------------------------------------  
    def drawCardFromTop(self):
        """Draws card from top of the deck"""
        #Find the top card in the deck
        topCard = self.deckArray[0]
        #For each card after top card, move it up one
        for self.deckTop in range(51):
            self.deckArray[self.deckTop] = self.deckArray[self.deckTop+1]
        self.avaliCards -= 1
        return topCard
###################################################################################################################################
class Player:
    """The Player Class - Stores and prints player's hand, able to draw cards from deck and check poker hand rankings."""
    def __init__(self):
        self.hand = [Card for i in range(5)]
        self.handSize = 0
        self.handValue = 0
#-----------------------------------------------------------------------------------------------------------------------------------          
    def drawStartingHand(self, deckObject):
        """Draws the player's starting hand of five cards."""
        for i in range(5):
            self.hand[self.handSize] = deckObject.drawCardFromTop()
            self.handSize += 1
#-----------------------------------------------------------------------------------------------------------------------------------          
    def printHand(self):
        """Prints the player's hand of cards."""
        for i in range(self.handSize):
            print(i+1,") ", self.hand[i].printCard(), sep="")
#-----------------------------------------------------------------------------------------------------------------------------------  
    def reDrawCard(self, deckObj):
        """Prompts user to re-draw any cards during turn."""
        alreadySelected = []
        #Prompt user with loop to check for errors
        while(True):
            userInput = input("How many cards would you like to redraw? (0-5):")
            if(userInput.isdigit() and int(userInput) >= 0 and int(userInput) <= 5):
                break
            else:
                print("Please input a valid number of cards")
        if(userInput != 0):
            for i in range( int(userInput) ):
                #Check if out of bounds or already selected
                while(True):
                    whichCardInput = input("Which card do you want to remove? (1-5):")
                    if(whichCardInput.isdigit() and int(whichCardInput) >= 1 and int(whichCardInput) <= 5 and (whichCardInput not in alreadySelected)):
                        break
                    else:
                        print("Please input a valid card, (1-5 with no repeating numbers)")
                    
                self.hand[ int(whichCardInput)-1 ] = deckObj.drawCardFromTop()
                #Add to list of cards already replaced
                alreadySelected.extend(whichCardInput)
#-----------------------------------------------------------------------------------------------------------------------------------  
    def reDrawCardAI(self, deckObj):
        """Prompts AI to re-draw any cards during turn."""
        alreadySelected = []
        #Prompt AI with loop to check for errors
        while(True):
            input("How many cards would you like to redraw? (0-5):")
            userInput = randint(0,5)
            print(userInput)
            if(int(userInput) >= 0 and int(userInput) <= 5):
                break
            else:
                print("Please input a valid number of cards")
        if(userInput != 0):
            for i in range( int(userInput) ):
                #Check if out of bounds or already selected
                while(True):
                    input("Which card do you want to remove? (1-5):")
                    whichCardInput = randint(1,5)
                    print(whichCardInput)
                    if(int(whichCardInput) >= 1 and int(whichCardInput) <= 5 and (str(whichCardInput) not in alreadySelected)):
                        break
                    else:
                        print("Please input a valid card, (1-5 with no repeating numbers)")
                    
                self.hand[ int(whichCardInput)-1 ] = deckObj.drawCardFromTop()
                #Add to list of cards already replaced
                alreadySelected.extend(str(whichCardInput))
#-----------------------------------------------------------------------------------------------------------------------------------  
    def checkHandCombo(self):
        """Checks player's hand for possible poker hands and returns their respective value."""
        #Create and fill list for rank checking
        rankList = []
        
        for i in range(self.handSize):
            rankList.append(self.hand[i].getRank())

        #Utilize counter module for easy counting of pairs
        counter = collections.Counter(rankList)
        #Sort the list for checking straights
        rankList.sort()

        #Format = [Rank][frequency]
        mostFreq = counter.most_common(1)[0][1]         #Frequency of the most frequent card in hand
        secondMostFreq = counter.most_common(2)[1][1]   #Frequency of the 2nd most frequent card in hand
        freqRank = counter.most_common(2)[0][0]         #Most frequent card's rank
        secondFreqRank = counter.most_common(2)[1][0]   #2nd most frequent card's rank

        #Check 4 Pair
        if(mostFreq == 4):
            print("Four of a kind of ", self.printFace(freqRank), "'s!", sep="")
            return int(freqRank) * 10000000
        #Check Full House
        if(mostFreq == 3 and secondMostFreq == 2):
            print("Full House of ", self.print2Faces(freqRank), " and ", self.print2Faces(secondFreqRank), "'s!", sep="")
            return int(freqRank) * 1000000 + int(secondFreqRank)
        #Check for Royal Flush | Straight Flush | Flush
        if(self.isFlush() == True):
            if(self.isStraight(rankList)):
                if(rankList[0] == 10):
                    print("ROYAL FLUSH")
                    return 1000000000
                else:
                    print("Straight Flush of ", rankList[0], " to " , rankList[4], sep="")
                    return rankList[4] * 100000000
            else:
                print("Flush of ", self.hand[0].getSuit(), "!", sep="")
                return rankList[4] * 100000
        #Check Straight
        if(self.isStraight(rankList)):
            print("Straight with a max of ", rankList[4], "!", sep="")
            return rankList[4] * 10000
        #Check 3 Pair
        if(mostFreq == 3):
            print("Three of a kind of ", self.printFace(freqRank), "'s!", sep="")
            return int(freqRank) * 1000
        #Check 2 Pairs
        if(mostFreq == secondMostFreq and secondMostFreq == 2):
            print("Two pairs of ", self.print2Faces(freqRank), " and ", self.print2Faces(secondFreqRank), "'s!", sep="")
            return int(freqRank) * 100 + int(secondFreqRank)
        #Check Pair
        if(mostFreq == 2):
            print("Pair of ", self.print2Faces(freqRank), "'s!", sep="")
            return int(freqRank) * 10
        #Check HighCard
        if(mostFreq == 1):
            print("High Card of ", self.printFace(rankList[4]), "'s!", sep="")
            return self.getMax()
#-----------------------------------------------------------------------------------------------------------------------------------  
    def isFlush(self):
        """Check if hand is a flush, returns boolean."""
        if(self.hand[0].getSuit() == self.hand[1].getSuit() == self.hand[2].getSuit() == self.hand[3].getSuit() == self.hand[4].getSuit()):
            return True
        else:
            return False
#-----------------------------------------------------------------------------------------------------------------------------------  
    def isStraight(self, rankList):
        """Check if hand is a straight, returns boolean."""
        if(rankList[0]+4 == rankList[1]+3 == rankList[2]+2 == rankList[3]+1 == rankList[4]):
            return True
        else:
            return False
#-----------------------------------------------------------------------------------------------------------------------------------  
    def getMax(self):
        """Get the highCard in a hand."""
        theMax = -1
        for i in range(self.handSize):
            if(theMax < self.hand[i].getRank()):
                theMax = self.hand[i].getRank()
        return theMax
#-----------------------------------------------------------------------------------------------------------------------------------
    def printFace(self, theRank):
        """Print the max value in the hand."""
        if(self.getMax() == 11):
            theRank = "Jack"
        elif(self.getMax() == 12):
            theRank = "Queen"
        elif(self.getMax() == 13):
            theRank = "King"
        elif(self.getMax() == 14):
            theRank = "Ace"
        return theRank
#-----------------------------------------------------------------------------------------------------------------------------------
    def print2Faces(self, theRank):
        """Prints 2nd most signifigant value for Full House or Two Pair."""
        if(theRank == 11):
            theRank = "Jack"
        elif(theRank == 12):
            theRank = "Queen"
        elif(theRank == 13):
            theRank = "King"
        elif(theRank == 14):
            theRank = "Ace"
        return theRank
###################################################################################################################################
class Game:
    """The Game Class - Stores player scores and starts the game depending on number of players."""
    def __init__(self):
        #Initilize all player scores
        self.player1score = 0
        self.player2score = 0
        self.player3score = 0
        self.player4score = 0
        self.playerNum = self.intro()
#-----------------------------------------------------------------------------------------------------------------------------------
    def clearScreen(self):
        """Clears the screen."""
        print("\n" * 100)
#-----------------------------------------------------------------------------------------------------------------------------------    
    def intro(self):
        """Introduction/Instructions on how to play '5 Card Poker' Also prompts user for number of players and executes game."""
        
        print("     WELCOME TO 5 CARD POKER")
        print("\t===HOW TO PLAY===")
        print("\t---Description---")
        print("This program is my implementation of the game 'Poker' which utilizes the standard ruleset of the 5 Hand variant.")
        print("The goal of poker is to obtain a better hand than your opponents through strategy and luck by redrawing cards.")
        print("This game supports multiplayer from 2 to 4 players per match.")
        print("")
        while(True):
            playerNum = input("Please enter the number of players(1-4), or 5 for hand rankings, or '0' to quit: ")
            if(playerNum.isdigit() and playerNum =="5"):
                print("\t---Hand Rankings---")
                print("01) Royal Flush")
                print("02) Straight Flush")
                print("03) Four of a Kind")
                print("04) Full House")
                print("05) Flush")
                print("06) Straight")
                print("07) Three of a Kind")
                print("08) Two Pair")
                print("09) One Pair")
                print("10) High Card")
            if(playerNum.isdigit() and playerNum == "1" or playerNum == "2" or playerNum == "3" or playerNum == "4"):
                self.startGame(int(playerNum))
            if(playerNum.isdigit() and playerNum == "0"):
                print("    ***Thanks for Playing!***")
                print("Your scores will be displayed in pokerScores.txt!")
                scoreFile = open("pokerScores.txt", "w")
                content1 = "Poker Scores:\nPlayer 1 Score: " + str(self.player1score) + "\nPlayer 2 Score: " + str(self.player2score)
                content2 = "\nPlayer 3 Score: " + str(self.player3score) + "\nPlayer 4 Score: " + str(self.player4score)
                content3 = content1 + content2
                scoreFile.write(content3)
                return
            else:
                print("Your input was not valid.")           
#-----------------------------------------------------------------------------------------------------------------------------------
    def startGame(self, playerNum):
        """Initiates game according to the number of players."""
        if(playerNum == 1):
            self.onePlayerGame()
            return
        if(playerNum == 2):
            self.twoPlayerGame()
            return
        if(playerNum == 3):
            self.threePlayerGame()
            return
        if(playerNum == 4):
            self.fourPlayerGame()
            return
#-----------------------------------------------------------------------------------------------------------------------------------
    def onePlayerGame(self):
        """One player Round."""
        print("\t===ONE PLAYER GAME VS EASY AI===")

        #Create and shuffle deck
        theDeck = Deck()
        theDeck.shuffleDeck()

        #Initilize players
        player1 = Player()
        player2 = Player()

        #Draw cards
        player1.drawStartingHand(theDeck)
        player2.drawStartingHand(theDeck)

        #Player 1's turn
        input("Player 1's Turn, please press enter to continue..")
        self.clearScreen()
        player1.printHand()
        player1.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player1.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 2's Turn
        input("Player 2's Turn (AI), please press enter to continue..")
        player2.printHand()
        player2.reDrawCardAI(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player2.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #End Round
        input("Please press enter to showdown..")
        self.clearScreen()
        print("Player 1 has: ", end="")
        p1Score = player1.checkHandCombo()
        print("Player 2 has: ", end="")
        p2Score = player2.checkHandCombo()
        theWinner = self.showDown(p1Score, p2Score)
        self.winScreen(theWinner)
        return
#-----------------------------------------------------------------------------------------------------------------------------------
    def twoPlayerGame(self):
        """Standard Two Player Round."""
        print("\t===TWO PLAYER GAME===")
        #Create and shuffle deck
        theDeck = Deck()
        theDeck.shuffleDeck()

        #Initilize players
        player1 = Player()
        player2 = Player()

        #Draw cards
        player1.drawStartingHand(theDeck)
        player2.drawStartingHand(theDeck)

        #Player 1's turn
        input("Player 1's Turn, please press enter to continue..")
        self.clearScreen()
        player1.printHand()
        player1.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player1.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 2's Turn
        input("Player 2's Turn, please press enter to continue..")
        player2.printHand()
        player2.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player2.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #End Round
        input("Please press enter to showdown..")
        self.clearScreen()
        print("Player 1 has: ", end="")
        p1Score = player1.checkHandCombo()
        print("Player 2 has: ", end="")
        p2Score = player2.checkHandCombo()
        theWinner = self.showDown(p1Score, p2Score)
        self.winScreen(theWinner)
        return
#-----------------------------------------------------------------------------------------------------------------------------------
    def threePlayerGame(self):
        """Standard Three Player Round."""
        print("\t===THREE PLAYER GAME===")
        #Create and shuffle deck
        theDeck = Deck()
        theDeck.shuffleDeck()

        #Initilize players
        player1 = Player()
        player2 = Player()
        player3 = Player()

        #Draw cards
        player1.drawStartingHand(theDeck)
        player2.drawStartingHand(theDeck)
        player3.drawStartingHand(theDeck)

        #Player 1's turn
        input("Player 1's Turn, please press enter to continue..")
        self.clearScreen()
        player1.printHand()
        player1.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player1.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 2's Turn
        input("Player 2's Turn, please press enter to continue..")
        player2.printHand()
        player2.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player2.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 3's Turn
        input("Player 3's Turn, please press enter to continue..")
        player3.printHand()
        player3.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player3.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #End Round
        input("Please press enter to showdown..")
        self.clearScreen()
        print("Player 1 has: ", end="")
        p1Score = player1.checkHandCombo()
        print("Player 2 has: ", end="")
        p2Score = player2.checkHandCombo()
        print("Player 3 has: ", end="")
        p3Score = player3.checkHandCombo()
        theWinner = self.showDown(p1Score, p2Score, p3Score)
        self.winScreen(theWinner)
        return
#-----------------------------------------------------------------------------------------------------------------------------------
    def fourPlayerGame(self):
        """Standard Four Player Round."""
        print("\t===FOUR PLAYER GAME===")
        #Create and shuffle deck
        theDeck = Deck()
        theDeck.shuffleDeck()

        #Initilize players
        player1 = Player()
        player2 = Player()
        player3 = Player()
        player4 = Player()

        #Draw cards
        player1.drawStartingHand(theDeck)
        player2.drawStartingHand(theDeck)
        player3.drawStartingHand(theDeck)
        player4.drawStartingHand(theDeck)

        #Player 1's turn
        input("Player 1's Turn, please press enter to continue..")
        self.clearScreen()
        player1.printHand()
        player1.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player1.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 2's Turn
        input("Player 2's Turn, please press enter to continue..")
        player2.printHand()
        player2.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player2.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 3's Turn
        input("Player 3's Turn, please press enter to continue..")
        player3.printHand()
        player3.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player3.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #Player 4's Turn
        input("Player 4's Turn, please press enter to continue..")
        player4.printHand()
        player4.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player4.printHand()
        input("Please press enter to finish turn")
        self.clearScreen()

        #End Round
        input("Please press enter to showdown..")
        self.clearScreen()
        print("Player 1 has: ", end="")
        p1Score = player1.checkHandCombo()
        print("Player 2 has: ", end="")
        p2Score = player2.checkHandCombo()
        print("Player 3 has: ", end="")
        p3Score = player3.checkHandCombo()
        print("Player 4 has: ", end="")
        p4Score = player4.checkHandCombo()
        theWinner = self.showDown(p1Score, p2Score, p3Score, p4Score)
        self.winScreen(theWinner)
        return
#-----------------------------------------------------------------------------------------------------------------------------------
    def showDown(self, p1Score=0, p2Score=0, p3Score=0, p4Score=0):
        """Determines winner of the round and checks for any ties as well."""
        scoreList = [p1Score, p2Score, p3Score, p4Score]
        theMax = scoreList.index(max(scoreList))
        #Check if there is a tie
        if( len(scoreList) != len(set(scoreList)) ):
            for i in range(len(scoreList)):
                if(i != theMax and scoreList[i] == scoreList[theMax]):
                    return None
        return theMax
#-----------------------------------------------------------------------------------------------------------------------------------
    def winScreen(self, theWinner):
        """Prints winner and adds score."""
        if(theWinner == 0):
            self.player1score += 1
            print("Player 1 Wins! Total Score is: ", self.player1score)
        if(theWinner == 1):
            self.player2score += 1
            print("Player 2 Wins! Total Score is: ", self.player2score) 
        if(theWinner == 2):
            self.player3score += 1
            print("Player 3 Wins! Total Score is: ", self.player3score)
        if(theWinner == 3):
            self.player4score += 1
            print("Player 4 Wins! Total Score is: ", self.player4score)
        if(theWinner == None):
            print("Tie! No winner will be awarded")
        return
###################################################################################################################################
def main():
    theGame = Game()

main()
