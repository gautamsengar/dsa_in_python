class Solution:
 def fib(self,num):
  self.num= num
  if self.num==0 or self.num==1:
   return num
  else:
   return self.fib(num-1)+self.fib(num-2)
answer=Solution()
print(answer.fib(6))

# Time Complexity: O(2^n)

# Space Complexity: O(n)
 