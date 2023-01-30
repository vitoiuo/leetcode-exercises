// https://leetcode.com/problems/same-tree/submissions/875734201/

const isSameTree = function(p, q) {
    return JSON.stringify(p) === JSON.stringify(q) 
};
