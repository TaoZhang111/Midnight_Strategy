class Strategy3:
    def __init__(self):
        self._keep = []
        self._turns = 0
    
    def find_max(self,lst):
        max_value = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
        return max_value
    
    def keep5_6(self, input, num):
        if 6 in input:
            count = input.count(6)
            if count > num:
                count = num
            for i in range(count):
                self._keep.append(6)
            return True
        elif 5 in input:
            self._keep.append(5)
            return True
        return False
    
    def turn1_2(self, input):
        if self._turns == 1:
            if self.keep5_6(input, 2):
                return self._keep
        elif self._turns == 2:
            if self.keep5_6(input, 1):
                return self._keep
        elif 4 in input or 1 in input:
            if 4 not in self._keep:
                self._keep.append(4)
                return self._keep
            if 1 not in self._keep:
                self._keep.append(1)
                return self._keep
        max = self.find_max(input)
        self._keep.append(max)
        return self._keep
            
    
    def turn3(self, input):
        if 4 in self._keep and 1 in self._keep:
            if self.keep5_6(input, 4):
                return self._keep
            max = self.find_max(input)
            self._keep.append(max)
            return self._keep
        if 4 in self._keep or 1 in self._keep:
            if self.keep5_6(input,1):
                return self._keep
            elif 4 in input:
                if 4 not in self._keep:
                    self._keep.append(4)
                    return self._keep
                else:
                    max = self.find_max(input)
                    self._keep.append(max)
                    return self._keep
            elif 1 in input:
                if 1 not in self._keep:
                    self._keep.append(1)
                    return self._keep
                else:
                    max = self.find_max(input)
                    self._keep.append(max)
                    return self._keep
        elif 4 not in self._keep and 1 not in self._keep:
            if 4 in input or 1 in input:
                if 4 in input:
                    self._keep.append(4)
                if 1 in input:
                    self._keep.append(1)
            else:
                max = self.find_max(input)
                self._keep.append(max)
    
    
    def turn4_5(self, input):
        if 4 in self._keep and 1 in self._keep:
            if self.keep5_6(input, 4):
                return self._keep
            max = self.find_max(input)
            self._keep.append(max)
            return self._keep
        else:
            if 4 in input or 1 in input:
                if 4 in input:
                    if 4 not in self._keep:
                        self._keep.append(4)
                if 1 in input:
                    if 1 not in self._keep:
                        self._keep.append(1)
            else:
                max = self.find_max(input)
                self._keep.append(max)
            return self._keep
    
        
    def choose(self, input):
        self._turns = len(self._keep)+1
        if self._turns == 1 or self._turns == 2:
            self.turn1_2(input)
        elif self._turns == 3:
            self.turn3(input)
        else:
            self.turn4_5(input)
        return self._keep


    def score(self):
        score = 0
        if 1 not in self._keep or 4 not in self._keep:
            return 0
        self._keep.remove(1)
        self._keep.remove(4)
        for i in self._keep:
                score += i
        return score