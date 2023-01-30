// Problem: https://leetcode.com/problems/number-of-1-bits/submissions/875141636/

var hammingWeight = function(n) {
    const binaryArray = n.toString().split('')
    const numberOfOneBit = binaryArray.filter(e => e === '1').length
    return numberOfOneBit
};

