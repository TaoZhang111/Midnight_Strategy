
import random
class Strategy5: 
    
    def __init__(self, score: int = 20):
        self._keep = []
        self._target_score = score

    # choose all the dice we want
    def choose(self, input):
         have_pick = False
        
        # check the max dice available
        while(len(input) > 0):
            curr_max = max(input)
            
            # if all 6, 1, and 4 are presented and we need, we pick all of them.
            while 6 in input:
                if 4 not in self._keep and 4 in input:
                    self._keep.append(4)
                    have_pick = True
                    input.remove(4)              
                        
                if 1 not in self._keep and 1 in input:
                    self._keep.append(1)
                    have_pick = True
                    input.remove(1)
                   
                self._keep.append(6)
                have_pick = True
                input.remove(6)
                # if we've pick too many 6 but not 4 and 1 yet when we have 3 dice, we 
                # stop picking 6 more. 
                if len(self._keep) > 3 and ((4 or 1) not in self._keep):
                    break
            # check if need 4
            if 4 not in self._keep and 4 in input:
                self._keep.append(4)
                have_pick = True
                input.remove(4)
                # print('add 4')
            
            # check if need 1
            if 1 not in self._keep and 1 in input:
                self._keep.append(1)
                have_pick = True
                input.remove(1)
                # print('add 1')
            
            # check if what we get is already larger than the target score. 
            if (4 and 1 in self._keep) and (self.score()+sum(input)> self._target_score):
                for num in input:
                    self._keep.append(num)
                    input.remove(num)
                # print('we are all good')
                break
            else: 
                    
                if have_pick == True:
                    break
                else:
                    curr_max = max(input)
                    # print("curr_max:" + str(curr_max))
                    self._keep.append(curr_max)
                    input.remove(curr_max)
                    break
                
    # check the current score
    def score(self):
        have_4 = False
        have_1 = False
        result = 0
        if 1 in self._keep:
            have_1 = True
        if 4 in self._keep:
            have_4 = True
            
        if have_1 and have_4:
            return sum(self._keep) - 5
        else:
            return 0
