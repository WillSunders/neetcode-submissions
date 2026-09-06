class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        pad = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz",
        }
        out, word = [],[]
        
        def dfs(index: int):
            if index == len(digits):
                out.append("".join(word))
                return
            print(pad[digits[index]])
            for s in pad[digits[index]]:
                word.append(s)
                dfs(index + 1)
                word.pop()
        dfs(0)
        return out