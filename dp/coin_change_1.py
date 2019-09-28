class Solution:
    """
    Compute the fewest number of coins that you need to make up that amount.
    """
    def coin_change_backtrack(self, coins, amount):
        ans = []
        indent = 0
        self._helper_bt(amount, coins, [], ans, indent)
        print('amount: {}, coins: {}, coins needed: {}, coins: {}'.format(amount, coins, len(ans[0]), ans))
        
        return len(ans[0]) if ans else -1

    def _helper_bt(self, amount, coins, curr_set, ans, indent):
        #print(' '*indent, 'curr_set={}'.format(curr_set))
        if amount==0:
            if not ans:
                ans.append(list(curr_set))
                return
            if len(curr_set) < len(ans[0]):
                ans.pop()
                ans.append(curr_set)
                return
        for i, c in enumerate(coins):
            if amount - c >= 0:
                self._helper_bt(amount - c, coins, curr_set + [c], ans, indent + 2)
        return

    def coin_change_dp_top_down(self, coins, amount):
        if amount==0:  return 0
        # tracks mininum coins needed for amount [0, amount]
        dp = [-1 for x in range(amount+1)]
        self._helper_dp_top_down(coins, amount, dp, 0)
        #print('amount: {}, coins: {}, coins needed: {}'.format(amount, coins, dp[amount]))
        print('dp = {}, len={}'.format(dp, dp[amount]))
        return dp[amount]
    
    def _helper_dp_top_down(self, coins, amount, dp, indent):
        if amount==0:
            #print(' '*indent + 'amount: {}'.format(amount))
            return 0
        if dp[amount] != -1:
            #print('reading dp[{}] = {}'.format(amount, dp[amount]))
            return dp[amount]
        min_val = -1
        for c in coins:
            if c > amount:
                continue
            ret = self._helper_dp_top_down(coins, amount - c, dp, indent+8)
            if ret != -1:
                if min_val==-1 or ret < min_val:
                    min_val = ret + 1
        #min_val = -1 if min_val==-1 else min_val + 1
        #print('update dp[{}] = {}'.format(amount, min_val))
        dp[amount] = min_val
        return dp[amount]

    def coin_change_dp_bottom_up(self, coins, amount):
        dp = [0] + [-1 for x in range(amount)]
        for i in range(1,len(dp)):
            min_ways = -1
            ways = -1
            print('amount:', i)
            for c in coins:
                print('\tchoosing {}'.format(c))
                if c > i:
                    print('\t\tnegative')
                    continue
                if dp[i-c] != -1:
                    ways = 1 + dp[i-c]
                    print('\t\tupdating ways to {}'.format(ways))
                if min_ways == -1 or (min_ways != -1 and ways < min_ways):
                    min_ways = ways
                    print('\t\tupdating min_ways to {}'.format(ways))
            print('\tsetting dp[{}] = {}'.format(i, min_ways))
            dp[i] = min_ways
        return dp[amount]        

        


coins = [1,2,5]
amount =  40
# very slow
#Solution().coin_change_backtrack(coins, amount)

# faster but hits TLE
#Solution().coin_change_dp_top_down(coins, amount)

# Ultra fast
Solution().coin_change_dp_bottom_up(coins, amount)
