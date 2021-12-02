# process
with open('inputs/1.txt') as f:
    lines = f.readlines()
    nums = [int(line.strip()) for line in lines]

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

def getWindow(idx):
  return nums[idx] + nums[idx+1] + nums[idx+2]

part2count = 0
for index, num in enumerate(nums):
    if index == len(nums) - 3:
      break
    currentWindow = getWindow(index)
    nextWindow = getWindow(index+1)
    if nextWindow  > currentWindow:
      part2count += 1
print('part 2:', part2count)

# Your puzzle answer was 1395
