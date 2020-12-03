from collections import defaultdict
# returns index of 

def two_sum(numbers, target):
    indecies = []
    known = {}
    for idx, num in enumerate(numbers):
        for k in known:
            if num + k == target:
                return [known[k], idx]
        known[num] = idx
    return indecies

print(two_sum([1,2,2], 4))
