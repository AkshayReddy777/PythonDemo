
def sort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]



nums = [1,22,100,2,65,35,82,2]

sort(nums)
print(nums)