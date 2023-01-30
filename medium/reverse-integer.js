//Problem: https://leetcode.com/problems/reverse-integer/submissions/877514980/

const reverse = function(x) {
    const regex = /^[-](\d+)/g
    let number = (x).toString()
    let reversedNumber
    const rangeStart = (-2)**31
    let rangeEnd = 2**31-1

    if (!regex.test(number)) {
        reversedNumber = +number.split('').reverse().join('')
    }
    else {
        number = number.match(regex)[0]
        reversedNumber = +(number[0] + number.slice(1, number.length).split('').reverse().join(''))
    }

    return (rangeEnd >= reversedNumber && reversedNumber >= rangeStart) ? reversedNumber : 0
};
