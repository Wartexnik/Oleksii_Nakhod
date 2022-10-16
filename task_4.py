def count_pairs(arr, target):
    """
    Counts pairs of numbers which sum to target in an array.
    
    Iterate once though the array, putting new elements in a dictionary,
    increasing the count of old elements, and increasing the count of
    pairs if complementary number exists in a dictionary.
    
    O(N) complexity.
    """
    count = 0
    hashmap = {}
    for el in arr:
        if target - el in hashmap:
            count += hashmap[target - el]
        if el in hashmap:
            hashmap[el] += 1
        else:
            hashmap[el] = 1
    return count