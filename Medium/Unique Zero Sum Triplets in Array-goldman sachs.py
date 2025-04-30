def find_triplets(nums):
    nums.sort()
    triplets = set()
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
                
    return [list(triplet) for triplet in triplets]