from Strategy_3 import Strategy3
class Strategy4_explore:
    def __init__(self, score, low, high) -> None:
        self._low = low
        self._high = high
        if score > self._low and score <= self._high:
            self._strategy = Strategy3()
            self._keep = self._strategy._keep
            self._turns = self._strategy._turns
            self._score_compare = score
        else: 
            self._keep = []
            self._score_compare = score
            self._turns = 0
    
    def find_max(self,lst):
        max_value = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
        return max_value
        
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

    def above16(self, input):
        self._strategy.choose(input)
    
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
                
        
    def choose(self, input):
        self._turns += 1
        if self._score_compare <= self._low:
            self.below16(input)
        elif self._score_compare > self._low and self._score_compare <= self._high:
            self.above16(input)
        else:
            self.above20(input)


    def score(self):
        score = 0
        if 1 not in self._keep or 4 not in self._keep:
            return 0
        self._keep.remove(1)
        self._keep.remove(4)
        for i in self._keep:
                score += i
        return score