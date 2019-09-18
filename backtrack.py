from typing import List

'''
# return all answers that form a valid square
'''

class Solution:
    def __init__(self):
        self.all_ans = []
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # run backtracking since max word len is 5 chars
        print('input - {}'.format(words))
        self.bt(words, [])
        return self.all_ans
            
    def bt(self, words, curr_ans):
        #print('words = {},    curr_ans = {}'.format(words, curr_ans))
        if curr_ans and len(curr_ans) == len(curr_ans[0]):
            if self.checkValid(curr_ans):
                #print('Found one solution {}'.format(curr_ans))
                self.all_ans.append(curr_ans)
                #if curr_ans not in all_ans:
            return
        for i,word in enumerate(words):
            #if word not in curr_ans:
            # very imp!! pass new list !
            self.bt(words[:i] + words[i+1:], curr_ans + [words[i]])
        return
        
    def checkValid(self, w):
        # A sequence of words forms a valid word square if the kth row 
        # and column read the exact same string, 
        # where 0 ≤ k < max(numRows, numColumns).
        #print('#####')
        for i in range(len(w)):
            if w[i] != self.get_col(w, i):
                #print('False: i={} r-{}, c-{}'.format(i, w[i], self.get_col(w, i)))
                return False
        #print('True: ans={}'.format(w))
        return True
                
                
    
    def get_col(self, w, col):
        cols = [x[col] for x in w]
        return ''.join(cols)

words = ["area","ball","lady","lead"]
sol = Solution()
print('output - {}'.format(sol.wordSquares(words)))


