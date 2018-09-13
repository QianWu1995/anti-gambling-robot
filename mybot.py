# -*- coding: utf-8 -*-
from pdbot import PDBot
import random
class realNiggaBot(PDBot):
    def __init__(self):
        self.init()
    

    def init(self):
        self.numberOfDefect = 0
        self.numberOfCooperate = 0
        self.counter = 8
        self.p = 1


    def get_play(self):
        
        myplay = "take 1"
        if(self.counter == 4):
            return myplay
        if(self.counter >= 1):
            ##use first 4 rounds to fool the opponent
            self.counter -= 1
            return "give 2"
        else:
            if(self.numberOfCooperate >= self.numberOfDefect):
                return "give 2"
            else:
                return "take 1"


   
    def make_play(self,opponent_play):
        if(opponent_play == "take 1"):
            self.numberOfDefect += 1
        else:
            self.numberOfCooperate += 1
        return
class realNiggaBot123(PDBot):
    def __init__(self):
        self.init()
    

    def init(self):

        self.counter = 1



    def get_play(self):
        
        myplay = "take 1"
        if(self.counter%3 == 1 or self.counter%2 == 2):
            return "give 2"
        if(self.counter%3 == 0):
            return "take 1"


   
    def make_play(self,opponent_play):
        self.counter += 1
        return

class realNiggaBot2(PDBot):
    def __init__(self):
        self.init()
    

    def init(self):
        self.numberOfDefect = 0
        self.numberOfCooperate = 0
        self.counter = 4
        self.p = 1


    def get_play(self):
        
        myplay = "give 2"
        if(self.counter <= 2):
            ##use first 4 rounds to fool the opponent
            self.counter -= 1
            return "give 2"
        else:
            return "take 1"


   
    def make_play(self,opponent_play):
        self.counter += 1
        return  

class testBot(PDBot):
    def __init__(self):
        self.init()
    
    # maintain a list of opponent's reactions
    def init(self):
        self.oppo = []

    def get_play(self):
        # set initial utility value as 0.7,1.0,0.0,0.2
        # testBot's first play is "take 1"
        myplay = "take 1"
        if len(self.oppo) != 0:
            # calculate the degree of selfishness
            count_take = self.oppo.count("take 1")
            p_take = 1.0 * count_take / len(self.oppo)
            #print p_take
            # p_take > (1-p_take) means the opponent is more selfish
            # so testBot believes her opponent is more likely to "take 1" in the next round
            if p_take > (1-p_take):
                # choose the action with the maximum utility value
                if 0.0*(1-p_take) > 0.2*p_take:
                    myplay = "give 2"
                else:
                    myplay = "take 1"
            # p_take <= (1-p_take) means the opponent is more cooperative
            # so testBot believes her opponent is more likely to "give 2" in the next round
            else:
                # maximize utility
                if 0.4*(1-p_take) > 1.0*p_take:
                    myplay = "give 2"
                else:
                    myplay = "take 1"

        return myplay
   
    def make_play(self,opponent_play):
        # record the opponent's reactions
        self.oppo.append(opponent_play)
        return

class testBot2(PDBot):
    def __init__(self):
        self.init()

    def init(self):
        self.allnumber = 0
        self.numberOfDefect = 0

    def get_play(self):
        
        myplay = "take 1"
        if(random.random() < 0.2):
            return "take 1"
        if self.allnumber != 0:
            
            if(self.allnumber == 0):
                p_take = 0
            else:
                p_take = self.numberOfDefect/self.allnumber

            
            
            if p_take > (1-p_take):
                myplay = "take 1"
            
            else:
                if 0.5*(1-p_take) > 1.0*p_take:
                    myplay = "give 2"
                else:
                    myplay = "take 1"

        return myplay
   
    def make_play(self,opponent_play):
        
        if(opponent_play == "take 1"):
            self.numberOfDefect += 1
        self.allnumber += 1
        return

class AwesomeBot(PDBot):
    #can add a constructor to set up any state you need
    def __init__(self):
        #initialise
        #tit-for-tat always starts with cooperation
        self.other_last_play="give 2"


    def init(self):
        self.other_last_play="give 2"
    #get_play is a function that takes no arguments
    #and returns one of the two strings "give 2" or "take 1" 
    #denoting the next play your agent will take in the game
    def get_play(self):
        #tit-for-tat always returns the other's last play
        #return self.other_last_play
        #almost-tit-for-tat
        if random.random() < 0.9:
            myplay = self.other_last_play
        else:
            if random.random() > 0.5:
                myplay =  "give 2"
            else:
                myplay =  "take 1"
        #you may also want to store myplay here, although awesomebot doesn't need this
        self.my_last_play = myplay

        return myplay

    #make_play is a function that takes a single string argument
    #that is either "give 2" or "take 1" denoting the opponent's
    #last play in the game    
    def make_play(self,opponent_play):
        #store for next round
        self.other_last_play = opponent_play
        return

if __name__ == "__main__":
    

    testBot = AwesomeBot()
    real_nigga = testBot2()
    iteration = 0
    testBotScore = 0
    real_niggaScore = 0
    testBot.init()
    real_nigga.init()

    while iteration < 18:
        
        testBotAction = testBot.get_play()

        real_niggaAction = real_nigga.get_play()

        testBot.make_play(real_niggaAction)
        real_nigga.make_play(testBotAction)

        #print "pd-bot's action is to: ",agent_action


        if testBotAction == "give 2" and real_niggaAction == "give 2":
            real_niggaScore += 2
            testBotScore += 2
        if testBotAction == "give 2" and real_niggaAction == "take 1":
            real_niggaScore += 3
        if testBotAction == "take 1" and real_niggaAction == "take 1":
            real_niggaScore += 1
            testBotScore += 1
        if testBotAction == "take 1" and real_niggaAction == "give 2":
            testBotScore += 3
        print "your score:    ",real_niggaScore
        print "pd-bots score: ",testBotScore

        iteration += 1
    print "your score:    ",real_niggaScore
    print "pd-bots score: ",testBotScore
