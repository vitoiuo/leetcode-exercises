//Problem: https://leetcode.com/problems/palindrome-number/submissions/877459936/

const isPalindrome = function(x) {
    if (x < 0) {
        return false
    }
    const number = (x).toString()
    const reverseNumber = number.split('').reverse().join('')

    return number === reverseNumber
};
