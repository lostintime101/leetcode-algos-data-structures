/**
 * @param {number} n
 * @param {number[]} left
 * @param {number[]} right
 * @return {number}
 */
var getLastMoment = function(n, left, right) {

    let leftMax = (Math.max(... left) || 0)
    let rightMax = (Math.max(... right.map((num) => n-num)) || 0)
    return Math.max(leftMax, rightMax)

};