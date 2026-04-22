# 1.sequential search (linear search)









# limear search

# def linear_search(nums, target):
#     for i in range(len(nums)):
#         if nums[i] == target:
#             return i
#     return -1
# li = list(map(int,input().split()))
# target = int(input())
# print(linear_search(li, target))

#binary search

def Bnary_search(nums, target):
    low,high = 0,len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

li = list(map(int,input().split()))
target = int(input())
print(Bnary_search(li, target))


