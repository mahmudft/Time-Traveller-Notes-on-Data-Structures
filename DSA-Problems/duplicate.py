"""
Given array if it contains the same entry at least twice return True else false

[1,2,3,4,3] => True

[1,2,3] => False

"""



def findduplicate(arr):
    counter = {}
    
    for x in arr:
        if counter.get(x) is None:
            counter[x] = 1
        else:
            return True
    return False