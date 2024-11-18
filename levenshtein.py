def distance(word1, word2):
  dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

  for i in range(len(word1) + 1):
      for j in range(len(word2) + 1):
          if i == 0:
              dp[j][0] = j
          elif j == 0:
              dp[0][i] = i
          elif word1[i-1] == word2[j-1]:
              dp[j][i] = dp[j-1][i-1]
          else:
              dp[j][i] = 1 + min(
                  dp[j-1][i-1], dp[j][i-1], dp[j-1][i]
              )

  return dp[len(word2)][len(word1)]
