from Strategy_3 import Strategy3
# Strategy4 is a player2 strategy and will deal with 3 cases of player1's score.
class Strategy4:
    # initialize the strategy4 and defined sel._keep to record keeped number, self._turns to record the turns
    # defined the self._score_compare to record the player1's score. If player1's score is between 16(exclusive) and 20(inclusive)
    # it will use strategy4
    def __init__(self, score:int = 20) -> None:
        if score > 16 and score <= 20:
            self._strategy = Strategy3()
            self._keep = self._strategy._keep
            self._turns = self._strategy._turns
            self._score_compare = score
        else: 
            self._keep = []
            self._score_compare = score
            self._turns = 0
    
    # find max number of input list
    def find_max(self,lst):
        max_value = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
        return max_value
    
    #choosing number when player1's score is less or equal to 16
    def below16(self, input):
        add = len(self._keep)
        if 1 in input:
            if 1 not in self._keep:
                self._keep.append(1)
        if 4 in input:
            if 4 not in self._keep:
                self._keep.append(4)
        if 1 in self._keep and 4 in self._keep:
            if 5 in input:
                count = input.count(5)
                for i in range(count):
                    self._keep.append(5)
            if 6 in input:
                count = input.count(6)
                for i in range(count):
                    self._keep.append(6)
        if add == len(self._keep):
            max = self.find_max(input)
            self._keep.append(max)
            
    #choosing number when player's score is between 16(exclusive) and 20(inclusive)
    def above16(self, input):
        self._strategy.choose(input)
    
    #choosing number when player's score is above 20(inclusive)
    def above20(self, input):
        add = len(self._keep)
        if self._turns == 1 or self._turns == 2 or self._turns == 3:
            if 6 in input:
                count = input.count(6)
                num = len(self._keep)
                max = 3-num
                if count > max:
                    count = max
                for i in range(count):
                    self._keep.append(6)
            elif 4 in input or 1 in input:
                if 4 in input:
                    if 4 not in self._keep:
                        self._keep.append(4)
                if 1 in input:
                    if 1 not in self._keep:
                        self._keep.append(1)
            else:
                max = self.find_max(input)
                self._keep.append(max)
                
            if add == len(self._keep):
                max = self.find_max(input)
                self._keep.append(max)
        elif self._turns == 4:
            if 1 in self._keep or 4 in self._keep:
                self._turns = 3
                self.above20(input)
                self._turns +=1
            else:
                if 1 in input or 4 in input:
                    if 1 in input:
                        self._keep.append(1)
                    if 4 in input:
                        self._keep.append(4)
                else:
                    max = self.find_max(input)
                    self._keep.append(max)
        else:
            if 1 in input:
               if 1 not in self._keep:
                    self._keep.append(1)
            if 4 in input:
                if 4 not in self._keep:
                    self._keep.append(4)
            if add == len(self._keep):
                max = self.find_max(input)
                self._keep.append(max)
                
    #the main choosing method according to player1's score
    def choose(self, input):
        self._turns += 1
        if self._score_compare <= 16:
            self.below16(input)
        elif self._score_compare > 16 and self._score_compare <= 20:
            self.above16(input)
        else:
            self.above20(input)

    # find the final score
    def score(self):
        score = 0
        if 1 not in self._keep or 4 not in self._keep:
            return 0
        self._keep.remove(1)
        self._keep.remove(4)
        for i in self._keep:
                score += i
        return score
