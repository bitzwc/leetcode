
def twoSum(nums, target):
    result = set()
    nums_dist = {}
    for i in range(len(nums)):
        nums_dist[target-nums[i]] = i
    for i in range(len(nums)):
        if nums[i] in nums_dist.keys() and i != nums_dist[nums[i]]:
            result.add(i)
            result.add(nums_dist[nums[i]])
    return list(result)

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    print twoSum(nums, target)