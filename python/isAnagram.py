def IsAnagram(s,t):
    ''' 
	IsAnagram(s,t) checks if two letters are anagrams or not
	IsAnagram: Str, Str -> Bool
	'''
    if len(s)!= len(t):
        return False
    count = {}
    for letter in s:
        count[letter] = count.get(letter,0) + 1
    for letter in t:
        if letter not in count:
            return False
        count[letter] = count[letter] - 1
    for letter in count:
        if count[letter] != 0:
            return False
    return True
    
IsAnagram("carrace","racecar") 
print(IsAnagram("jam","jar"))
