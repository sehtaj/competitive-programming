#groupAnagrams: List[str] -> List[List[str]]

#Time: O(n * mlogm) where n is the number of strings in the input list and m is the length of the longest string in the input list
#Space: O(n) where n is the number of strings in the input list
def groupAnagrams(strs):
   
    hp = {}

    for item in strs:
        sortedItem = ''.join(sorted(item)) 

        if sortedItem in hp:
            hp[sortedItem].append(item) 
        else:
            hp[sortedItem] = [item] 
    retval = []

    for key in hp:
        retval.append(hp[key])  

    return retval

# Edge Cases

#groupAnagrams([])

#groupAnagrams(["a"])

#groupAnagrams(["abc", "bca", "bac", "cab", "cba", "acb"])

#groupAnagrams(["aa", "bb", "cc"])  

#groupAnagrams(["ab", "ba", "abc", "bac", "cba", "dog", "god"])