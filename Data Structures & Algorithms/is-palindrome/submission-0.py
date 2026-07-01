class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s= s.lower().replace(" ", "")
        for ch in "?.!/,:;'-":
            s = s.replace(ch, "")

        array1 = []
        array2 = []
        char = 0
        while char < len(s):
            array1.append(s[char])
            char += 1

        char2 = len(s) -1
        while char2 >= 0:
            array2.append(s[char2])
            char2 -= 1


        if array1 == array2:
            return True

        else:
            return False

