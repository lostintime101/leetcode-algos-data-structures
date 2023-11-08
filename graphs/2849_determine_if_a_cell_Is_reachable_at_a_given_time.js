/**
 * @param {number} sx
 * @param {number} sy
 * @param {number} fx
 * @param {number} fy
 * @param {number} t
 * @return {boolean}
 */
var isReachableAtTime = function(sx, sy, fx, fy, t) {

    const limit = Math.max(Math.abs(sx - fx), Math.abs(sy - fy))

    return t >= limit && !(limit == 0 && t == 1)

};