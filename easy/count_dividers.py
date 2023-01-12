# Problem: https://leetcode.com/problems/count-the-digits-that-divide-a-number/

def countDigits(num):
    division_count=0
    num_digits=list(str(num))
    for number in range(1, int(max(num_digits))+1):
        if (num % number == 0 and str(number) in num_digits):
            division_count+=num_digits.count(str(number))
    return division_count
