// Problem: https://leetcode.com/problems/number-of-1-bits/description/

var hammingWeight = function(n) {
    const binaryArray = n.toString().split('')
    const numberOfOneBit = binaryArray.filter(e => e === '1').length
    return numberOfOneBit
};

hammingWeight(00000000000000000000000000001011)
