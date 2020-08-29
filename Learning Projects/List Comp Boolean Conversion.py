from random import randint

nums = [randint(0, 5) for x in range(10)]

print(nums)

nums = [x%2 == 0 for x in nums]

print(nums)