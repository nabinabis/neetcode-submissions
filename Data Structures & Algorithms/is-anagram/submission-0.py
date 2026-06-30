class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
    #put both strings into a set , and if theres a single letter different then return false
        seen1 = {}
        for char in s:
            if char in seen1:
                seen1[char] += 1
            else:
                seen1[char] = 1

        seen2 = {}

        for char in t:
            if char in seen2:
                seen2[char] += 1
            else:
                seen2[char] = 1

        if seen1 == seen2:
            return True
        else:
            return False
