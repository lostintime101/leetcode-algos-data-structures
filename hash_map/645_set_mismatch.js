/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findErrorNums = function(nums) {

    let freq = {};

    for(let num of nums){
        freq[num] = (freq[num] || 0) + 1;
    }

    let ans = [0,0];

    for(let i=1; i<nums.length+1; i++){

        curr = (freq[i] || 0)
        if(curr === 0){
            ans[1] = i;
        }
        if(curr === 2){
            ans[0] = i;
        }
    }

    return ans;

};