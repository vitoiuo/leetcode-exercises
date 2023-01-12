// https://leetcode.com/problems/same-tree/description/

const isSameTree = function(p, q) {
    return JSON.stringify(p) === JSON.stringify(q) 
};
