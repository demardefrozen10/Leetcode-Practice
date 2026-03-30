class Solution:
    def isHappy(self, n: int) -> bool:
        original = n
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            temp = n
            num = 0
            while temp > 0:
                digit =  temp % 10
                num += pow(digit, 2)
                temp = temp // 10
            n = num
        

        if n == 1:
            return True
        return False
