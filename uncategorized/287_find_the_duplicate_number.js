/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {

    let curr = 0;
    let numsSet = new Set();

    for( let num of nums ) {
        let oldCurr = curr;
        numsSet.add(num);
        curr = numsSet.size;
        if ( oldCurr === curr) return num;
    }
};