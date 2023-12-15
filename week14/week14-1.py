class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns = set()

        for a,b in paths: #先循一次，先檢查a
            notAns.add(a) #出發點不是答案

        for a,b in paths: #第二輪看一下b
            if b not in notAns: #b不再出發哩，就是答案
                return b #b不是，不是答案