// Problem: https://leetcode.com/problems/valid-palindrome/submissions/875748375/

const isPalindrome = function(s) {
    const regex = /[a-z\d]/g
    const formattedString = s.toLowerCase().match(regex) || []
    return formattedString.join('') === formattedString.reverse().join('')
};
