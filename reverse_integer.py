class Solution:
    def reverse(self, x: int) -> int:
        reverse = 0
        negative = False
        if x<0:
            x = -1 * x
            negative = True
        while x:
            remainder = x % 10
            reverse = reverse * 10 + remainder
            x = x//10
        if negative:
            reverse = -1 * reverse
        if reverse < (2**31 -1) and reverse > (-(2**31)):
            return reverse
        else:
            return 0
