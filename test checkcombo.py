from random import randint
import collections
import os
###################################################################################################################################
class Card:
    """
    The card class
    """
    def __init__(self, rankCard = "defaultRank", suitCard = "defaultSuit"):
        self.rank = rankCard
        self.suit = suitCard
#-----------------------------------------------------------------------------------------------------------------------------------        
    def printCard(self):
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
        return int(self.rank)
#-----------------------------------------------------------------------------------------------------------------------------------  
    def getSuit(self):
        return self.suit
###################################################################################################################################
class Deck:
    """
    The deck class
    """
    def __init__(self):
        self.ranks = ["14", "2", "3","14", "2", "3","14", "2", "3","14","14", "2", "3"]#, "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"] #11=Jack , 12=Queen, 13=King, 14=Ace
        self.suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        
        self.deckArray = [Card() for i in range(52)]            #Create array of cards

        for i in range(52):
            self.deckArray[i] = Card( self.ranks[int(i%13)] , self.suits[int(i/13)] )

        self.avaliCards = 52    #Remaining cards in deck
        self.deckTop = -1       #Set to -1 because of drawCardFromTop() method
#-----------------------------------------------------------------------------------------------------------------------------------  
    def shuffleDeck(self):
        for i in range(51):
            random = randint(0,51)
            tempCard = self.deckArray[i]
            self.deckArray[i] = self.deckArray[random]
            self.deckArray[random] = tempCard
#-----------------------------------------------------------------------------------------------------------------------------------  
    def printDeck(self):
        for i in range(self.avaliCards):
            print( self.deckArray[i].printCard() )
#-----------------------------------------------------------------------------------------------------------------------------------  
    def drawCardFromTop(self):
        topCard = self.deckArray[0]
        for self.deckTop in range(51):
            self.deckArray[self.deckTop] = self.deckArray[self.deckTop+1]
        self.avaliCards -= 1
        return topCard
###################################################################################################################################
class Player:
    """
    The player class
    """
    def __init__(self):
        self.hand = [Card for i in range(5)]
        self.handSize = 0
        self.handValue = 0
        self.score = 0
#-----------------------------------------------------------------------------------------------------------------------------------          
    def drawStartingHand(self, deckObject):
        for i in range(5):
            self.hand[self.handSize] = deckObject.drawCardFromTop()
            self.handSize += 1
#-----------------------------------------------------------------------------------------------------------------------------------          
    def printHand(self):
        for i in range(self.handSize):
            print(i+1,") ", self.hand[i].printCard(), sep="")
#-----------------------------------------------------------------------------------------------------------------------------------
    def printScore(self):
        print(self.score)
#-----------------------------------------------------------------------------------------------------------------------------------  
    def reDrawCard(self, deckObj): #Replace with a better user input prompt
        alreadySelected = []
        while(True):
            userInput = input("How many cards would you like to redraw? (0-5):")
            if userInput.isdigit() and int(userInput) >= 0 and int(userInput) <= 5:
                break
            else:
                print("Please input a valid number of cards")
        if userInput != 0:
            for i in range( int(userInput) ):
                while(True):
                    whichCardInput = input("Which card do you want to remove? (1-5):")
                    #Check if out of bounds or already selected
                    if int(whichCardInput) >= 1 and int(whichCardInput) <= 5 and (whichCardInput not in alreadySelected):
                        break
                    else:
                        print("Please input a valid card, (1-5 with no repeating numbers)")
                    
                self.hand[ int(whichCardInput)-1 ] = deckObj.drawCardFromTop()
                alreadySelected.extend(whichCardInput) #Add to list of cards already replaced
#-----------------------------------------------------------------------------------------------------------------------------------  
    def checkHandCombo(self):
        rankList = []
        
        for i in range(self.handSize):
            rankList.append(self.hand[i].getRank())
            
        counter = collections.Counter(rankList)
        rankList.sort()
        
        #Format = [Rank][frequency]        
        mostFreq = counter.most_common(1)[0][1]         #the most frequent one (or first card in "common-ified" list)
        secondMostFreq = counter.most_common(2)[1][1]   #the second most common
        freqRank = counter.most_common(2)[0][0]         #the rank of most freq
        secondFreqRank = counter.most_common(2)[1][0]   #the rank of 2nd most freq
        
        #Check for royalFlush/straightFlush/flush
        if(self.isFlush() == True):
            if(self.isStraight(rankList)):
                if(rankList[0] == 10):
                    print("ROYAL FLUSH")
                    return 1000000000
                else:
                    print("Straight Flush of: ", rankList[0], " to " , rankList[4], sep="")
                    return rankList[4] * 100000000
            else:
                print("Flush of: ", self.hand[0].getSuit(), "!")
                return rankList[4] * 100000

        #Check Straight
        if(self.isStraight(rankList)):
            print("Straight with a max of: ", rankList[4], "!", sep="")
            return rankList[4] * 10000
        #Check 4 Pair
        if(mostFreq == 4):
            print("Four of a kind of: ", self.printFace(freqRank), "'s!", sep="")
            return int(freqRank) * 10000000
        #Check Full House
        if(mostFreq == 3 and secondMostFreq == 2):
            print(counter.most_common())
            print("freqRank: ", freqRank, "2ndFreqRank: ", secondFreqRank)
            print("Full house of", self.print2Face(freqRank), " and ", self.print2Face(secondFreqRank), "'s!")
            return int(freqRank) * 1000000
        #Check 3 Pair
        if(mostFreq == 3):
            print("Three of a kind of", self.printFace(freqRank), "'s!")
            return int(freqRank) * 1000
        #Check 2 Pair
        if(mostFreq == secondMostFreq and secondMostFreq == 2):
            print(counter.most_common())
            print("freqRank: ", freqRank, "2ndFreqRank: ", secondFreqRank)
            print("Two pairs of", self.print2Face(freqRank), " and ", self.print2Face(secondFreqRank), "'s!")
            return int(freqRank) * 100
        #Check Pair
        if(mostFreq == 2):
            print("One Pair of", self.print2Face(freqRank), "'s!")
            return int(freqRank) * 10
        #Check HighCard
        if(mostFreq == 1):
            print("High Card of", self.printFace(rankList[4]), "'s!")
            return self.getMax()
#-----------------------------------------------------------------------------------------------------------------------------------  
    def isFlush(self):
        if(self.hand[0].getSuit() == self.hand[1].getSuit() == self.hand[2].getSuit() == self.hand[3].getSuit() == self.hand[4].getSuit()):
            return True
        else:
            return False
#-----------------------------------------------------------------------------------------------------------------------------------  
    def isStraight(self, rankList):
        if(rankList[0]+4 == rankList[1]+3 == rankList[2]+2 == rankList[3]+1 == rankList[4]):
            return True
        else:
            return False
#-----------------------------------------------------------------------------------------------------------------------------------  
    def getMax(self): #Get the highCard in a hand
        theMax = -1
        for i in range(self.handSize):
            if(theMax < self.hand[i].getRank()):
                theMax = self.hand[i].getRank()
        return theMax
#-----------------------------------------------------------------------------------------------------------------------------------
    def printFace(self, theRank):
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
    def print2Face(self, theRank):
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
    """
    The game class
    """
    #add score system, maybe player rotations and shit
    def __init__(self):
        self.playerNum = self.intro()
        self.startGame()
#-----------------------------------------------------------------------------------------------------------------------------------
    def clearScreen(self):
        print("\n" * 100)
#-----------------------------------------------------------------------------------------------------------------------------------    
    def intro(self):
        print("WELCOME TO 5 CARD POKER")
        while(True):
            self.startGame(2)
#-----------------------------------------------------------------------------------------------------------------------------------
    def startGame(self, playerNum):
        if(playerNum == 2):
            self.twoPlayerGame()
        if(playerNum == 3):
            self.threePlayerGame()
        if(playerNum == 4):
            self.fourPlayerGame()
#-----------------------------------------------------------------------------------------------------------------------------------
    def twoPlayerGame(self):
        print("twoplayer game#################################")
        theDeck = Deck()
        theDeck.shuffleDeck()
        
        player1 = Player()
        player2 = Player()
        
        player1.drawStartingHand(theDeck)
        player2.drawStartingHand(theDeck)

        #input("Player 1's Turn, please press enter to continue..")
        #self.clearScreen()

        player1.printHand()
        player1.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player1.printHand()

        #input("Please press enter to finish turn")
        #self.clearScreen()
        #input("Player 2's Turn, please press enter to continue..")
        print("player2")
        player2.printHand()
        player2.reDrawCard(theDeck)
        print("----------------------------------------------------")
        print("Your redrawn hand:")
        player2.printHand()

        #player2.score = 5 #just testing lol
        #sweet it works
        
        #input("Please press enter to showdown..")
        #self.clearScreen()
        print("Player 1 has: ")
        p1Score = player1.checkHandCombo()
        print("Player 2 has: ")
        p2Score = player2.checkHandCombo()
        theWinner = self.showDown(p1Score, p2Score)
        self.winScreen(theWinner, player1, player2)
#-----------------------------------------------------------------------------------------------------------------------------------
    def threePlayerGame(self):
        print("three")
#-----------------------------------------------------------------------------------------------------------------------------------
    def fourPlayerGame(self):
        print("four")
#-----------------------------------------------------------------------------------------------------------------------------------
    def showDown(self, p1Score=0, p2Score=0, p3Score=0, p4Score=0):
        scoreList = [p1Score, p2Score, p3Score, p4Score]
        theMax = scoreList.index(max(scoreList))
        if( len(scoreList) != len(set(scoreList)) ): #If there is a tie
            for i in range(len(scoreList)):
                if(i != theMax and scoreList[i] == scoreList[theMax]):
                    return None
        return theMax
#-----------------------------------------------------------------------------------------------------------------------------------
    def winScreen(self, theWinner, player1=Player(), player2=Player(), player3=Player(), player4=Player()):
        if(theWinner == 0):
            print("Player 1 Wins!")
            player1.score += 1
        if(theWinner == 1):
            print("Player 2 Wins!")
            player2.score += 1
            player2.printScore()
        if(theWinner == 2):
            print("Player 3 Wins!")
            player3.score += 1
        if(theWinner == 3):
            print("Player 4 Wins!")
            player4.score += 1
        if(theWinner == None):
            print("Tie! No winner will be awarded")
###################################################################################################################################
def main():
    theGame = Game()


main()

