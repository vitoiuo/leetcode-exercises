// Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

const lengthOfLongestSubstring = function(s) {
    let largestSubstring = 0
    s.split('').forEach((e,index, array) => {
        let substring = e
        let count = 1
        while (!substring.includes(array[index+count]) && array[index+count]) {
            substring+=array[index+count]
            count+=1
        }
        if (substring.length > largestSubstring) {
            largestSubstring = substring.length 
            s.replace(substring, '')
        }
    })
    return largestSubstring
};