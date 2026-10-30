class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sublist = {}
        # for str in strs:
        #     sorted_str = "".join(sorted(str))
        #     print(sorted_str)
        #     if str not in anagram_sublist:
        #         anagram_sublist[sorted_str] = []   
        #         print(anagram_sublist)
        #     anagram_sublist[sorted_str].append(str)
        #     print(anagram_sublist)

        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str not in anagram_sublist:
                anagram_sublist[sorted_str] = []   
            anagram_sublist[sorted_str].append(str)


        res = anagram_sublist.values()
        #print(res)
        return list(res)   