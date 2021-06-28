def sum_prime(nums):
  print (nums)
  sum = 0
  for number in nums:
    if int(number) % 2 != 0:
      sum = sum + int(number)

  return sum
  
  

nums = input()
nums = nums[1:-1].split(",")
 
print(sum_prime(nums))
