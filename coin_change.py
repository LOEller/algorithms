class Solution:
    def change(self, amount: int, coins) -> int:
        """
        if amount < 0 or len(coins) == 0:
            return 0

        if amount == 0:
            return 1

        return self.change(amount, coins[1:]) + self.change(amount - coins[0], coins)
        """

        dp = [[0 for _ in range(len(coins))] for _ in range(amount+1)]

        for i in range(amount+1):
            for j in range(len(coins)):
                if i == 0:
                    dp[i][j] = 1
                    continue

                coin = coins[j]

                left_val = dp[i][j-1] if j-1 >= 0 else 0
                up_val = dp[i-coin][j] if i-coin >= 0 else 0
                dp[i][j] = left_val + up_val

        print(dp)
        return dp[amount][len(coins)-1]


if __name__ == "__main__":
  solution = Solution()

  result = solution.change(3, [1, 2])
  print(result)
