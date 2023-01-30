// Problem: https://leetcode.com/problems/maximum-score-words-formed-by-letters/submissions/876874922/

const maximumGap = function(nums) {
    if (!nums.length) {
        return 0
    }
    let maxGap = 0
    nums.sort((a,b) => a-b).forEach((element, index, array) => {
        const gap = array[index+1] ? array[index+1] - element : 0
        if (gap > maxGap) {
            return maxGap = gap
        }
    });

    return maxGap
};
