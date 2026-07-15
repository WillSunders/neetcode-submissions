class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            temp = "".join(sorted(word))
            if not temp in anagrams:
                anagrams[temp] = [word]
            else:
                anagrams[temp].append(word)
        return list(anagrams.values())