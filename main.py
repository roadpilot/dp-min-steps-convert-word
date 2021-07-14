# given two words, find min number of steps to convert word1 to word2. you can only insert, delete, and replace a char each step

# RECURSIVE SOLUTION
def rec(word1, word2, i, j):
  if i == len(word1):
    return len(word2)-j
  if j == len(word2):
    return len(word1)-1

  if word1[i] == word2[j]: # letters match in both words
    match = 0 + rec(word1, word2, i+1, j+1)
    return match

  insert = 1 + rec(word1, word2, i+1, j)
  delete = 1 + rec(word1, word2, i, j+1)
  replace = 1 + rec(word1, word2, i+1, j+1)

  return min(insert, delete, replace)  

# MEMOIZED SOLUTION
def memo_rec(word1, word2, i, j, memo):
  if i == len(word1):
    return len(word2)-j
  if j == len(word2):
    return len(word1)-1

  key = (i,j)
  if key in memo:
    return memo[key]

  if word1[i] == word2[j]: # letters match in both words
    match = 0 + memo_rec(word1, word2, i+1, j+1, memo)
    return match

  insert = 1 + memo_rec(word1, word2, i+1, j, memo)
  delete = 1 + memo_rec(word1, word2, i, j+1, memo)
  replace = 1 + memo_rec(word1, word2, i+1, j+1, memo)

  memo[key] = min(insert, delete, replace) 
  return memo[key]

print(rec("cat","dog",0,0))
print(memo_rec("doubt","rise",0,0,{}))