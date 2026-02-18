import sys
input = sys.stdin.readline

a,b = map(int, input().split())

sum = 0

def count(n):
  total = 0
  k = 0
  while (1 << k) <= n:
      period = 1 << (k + 1)
      ones_in_block = 1 << k
      full = (n + 1) // period
      rem  = (n + 1) %  period
      total += full * ones_in_block + max(0, rem - ones_in_block)
      k += 1
  return total

print(count(b)-count(a-1))