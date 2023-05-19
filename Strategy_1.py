# create a strategy1
class Strategy1:
    # initialized the self._keep to record the number
    def __init__(self) -> None:
        self._keep = []
    
    # find the max number of input list
    def find_max(self,lst):
        max_value = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
        return max_value
    
    # keep all the 6 in input list
    def absorb6(self,list1):
        num = list1.count(6)
        new_items = [6] * num
        if len(self._keep) + num > 6:
            new_items = new_items[:6-len(self._keep)]
        self._keep.extend(new_items)

    #keep one 5 in the input list
    def absorb5(self, list1):
        count = list1.count(5)
        new_items = [5] * count
        if len(self._keep) + count > 6:
            new_items = new_items[:6-len(self._keep)]
        self._keep.extend(new_items)

    # choosing the number from input list
    def choose(self, input):
        count = len(self._keep)
        if len(self._keep) < 6:
            if 4 in input:
                if 4 not in self._keep:
                    self._keep.append(4)
        if len(self._keep) < 6:
            if 1 in input:
                if 1 not in self._keep:
                    self._keep.append(1)
        if len(self._keep) < 6:
            self.absorb6(input)
        if len(self._keep) < 6:
            self.absorb5(input)
        if len(self._keep) == count:
            max = self.find_max(input)
            self._keep.append(max)
        return self._keep
    
    # get the final score
    def score(self):
        score = 0
        if 1 not in self._keep or 4 not in self._keep:
            return 0
        self._keep.remove(1)
        self._keep.remove(4)
        for i in self._keep:
                score += i
        return score
