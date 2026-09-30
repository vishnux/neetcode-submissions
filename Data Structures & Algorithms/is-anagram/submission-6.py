class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # set_s = set(s)
        # set_t = set(t)
        # y = "racecar"
        # dict_s = dict(y)

        # if set_s == set_t and len(s) == len(t):
        #     #print(dict_s)
        #     print(set_s)
        #     print(set_t)
        #     print(len(s))
        #     print(len(t))
        #     return True
        from collections import Counter
        dict_s = Counter(s)
        print(dict_s)
        dict_t = Counter(t)
        print(dict_t)

        if dict_s == dict_t:
            return True
        return False