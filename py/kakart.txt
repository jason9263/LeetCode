"""
We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order, and no URL was visited more than once per person.

Write a function that takes two users' browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

Sample input:

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]

Sample output:

findContiguousHistory(user0, user1) => ["/pink", "/register", "/orange"]
findContiguousHistory(user0, user2) => [] (empty)
findContiguousHistory(user0, user0) => ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
findContiguousHistory(user2, user1) => ["a"] 
findContiguousHistory(user5, user2) => ["a"]
findContiguousHistory(user3, user4) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user4, user3) => ["/plum", "/blue", "/tan", "/red"]
findContiguousHistory(user3, user6) => ["/tan", "/red", "/amber"]

n: length of the first user's browsing history
m: length of the second user's browsing history

"""

user0 = ["/start", "/green", "/blue", "/pink", "/register", "/orange", "/one/two"]
user1 = ["/start", "/pink", "/register", "/orange", "/red", "a"]
user2 = ["a", "/one", "/two"]
user3 = ["/pink", "/orange", "/yellow", "/plum", "/blue", "/tan", "/red", "/amber", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow", "/BritishRacingGreen"]
user4 = ["/pink", "/orange", "/amber", "/BritishRacingGreen", "/plum", "/blue", "/tan", "/red", "/lavender", "/HotRodPink", "/CornflowerBlue", "/LightGoldenRodYellow"]
user5 = ["a"]
user6 = ["/pink","/orange","/six","/plum","/seven","/tan","/red", "/amber"]


#LCS dp longest common subsqesce. hints
# ans = 
# cur =
# start , end 


# f(i, j). # a(0, i) and b(o, j) longest common continuous substring
# a[i] == b[j] --> a[i-1]. b[j-1] + 1

# ans = max(ans,  a[i-1]. b[j-1] + 1)
# stard
# end 
# tmpres = A[i - ans: i + 1]

# a[i] != b[j] =  a[i-1] b[j-1]


# return ans


def solution(a, b):
  if not a or not b or len(a) == 0 or len(b) == 0:
    return []
  dp = [[0] * (len(a) + 1)] * (len(b) + 1)
  ans = []
  ans_len = 0
  for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
      if a[i-1] == b[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
        if ans_len < dp[i][j]:
          ans = a[i - dp[i][j]:(i + 1)]
          ans_len = dp[i][j]
      else:
        print(i, j, len(a), len(b))
        dp[i][j] = dp[i-1][j-1] 

  print(ans)



solution(user0, user1)



# Note: built-in functions like the Python difflib module should not be used as solutions to this problem
# from collections import defaultdict


# def solution(counts):
#   if not counts or len(counts) == 0:
#     return []

#   dic = defaultdict(int)

#   for click in counts:
#     cnt, clickString = click.split(',')
#     # count of click
#     cnt = int(cnt)
#     c_list = clickString.split('.')
#     tmp = []
#     # genrate the short domain and log domain name 
#     for i in range(len(c_list) - 1, -1, -1):
#       tmp = [c_list[i]] + tmp
#       dic[".".join(tmp)] = dic[".".join(tmp)] + cnt


#   ans = []
#   for k, v in dic.items():
#     tmp = str(k) + ":            " + str(v)
#     ans.append( tmp )
#     print(tmp)
#   return ans


# print(len(solution(counts)))


