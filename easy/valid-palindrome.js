// Problem: https://leetcode.com/problems/valid-palindrome/

const isPalindrome = function(s) {
    const regex = /[a-z\d]/g
    const formattedString = s.toLowerCase().match(regex) || []
    return formattedString.join('') === formattedString.reverse().join('')
};
