class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False # if lengths are not same, it is not an anagram. 
            #It also makes the next step safe to proceed since edge cases where lengths are 
            #different are already checked. 
        
        count_s, count_t = {}, {}
        
        # s = 'aab' # first case dry run
        for i in range(len(s)):                 # i = 0 ; len(s) = 3
            if s[i] in count_s:                 # s[0] = 'a' count_s = {} 
                count_s[s[i]] += 1              # a is not in {}
            else:
                count_s[s[i]] = 1               # so we are assigning value of a to 1. 
            # t = 'aab' ; let's take i = 2 for example sake for dry run 
            if t[i] in count_t:                 # t[2] = a, count_t = {a:1}
                count_t[t[i]] += 1              # since a is already in count_t as key, 
            else:                               # we add 1 to count of a in count_t
                count_t[t[i]] = 1               # count_t = {a:2}

            #finally we check if the counts of both dictionaries are same. if same, it means they are anagrams
        if count_s == count_t:
            return True
        else: 
            return False

        