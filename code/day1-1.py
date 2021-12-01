# process
nums = []
with open('day1-1-input.txt') as f:
    lines = f.readlines()
    for line in lines:
      nums.append(int(line.strip()))


# part 1
part1count = 0
for index, num in enumerate(nums):
    number = num
    if index < len(nums) - 1:
      nextNum = nums[index+1]
    if nextNum > num:
      part1count += 1
print('part 1:', part1count)

# Your puzzle answer was 1451.

# part 2

def validIndex(idx):
  if idx < len(nums):
    return True
  return False

def getWindow(idx):
  sum = 0
  if validIndex(idx):
    sum += nums[idx]
  if validIndex(idx+1):
    sum += nums[idx+1]
  if validIndex(idx+2):
    sum += nums[idx+2]
  return sum

part2count = 0
for index, num in enumerate(nums):
    if index == len(nums) - 3:
      break
    currentWindow =0
    nextWindow = 0
    currentWindow = getWindow(index)
    nextWindow = getWindow(index+1)
    if nextWindow  > currentWindow:
      part2count += 1
print('part 2:', part2count)

# Your puzzle answer was 1395
