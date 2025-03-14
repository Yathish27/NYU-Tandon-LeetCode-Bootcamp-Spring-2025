class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  
        if not s:
            return 0

        sign = 1
        index = 0
        result = 0

      
        if s[index] in ('-', '+'):
            sign = -1 if s[index] == '-' else 1
            index += 1

        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1

            if sign * result >= 2**31 - 1:
                return 2**31 - 1
            if sign * result <= -2**31:
                return -2**31

        return sign * result
