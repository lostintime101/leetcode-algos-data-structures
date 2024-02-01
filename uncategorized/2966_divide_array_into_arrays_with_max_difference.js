/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[][]}
 */
var divideArray = function(nums, k) {

    nums.sort((a,b) => a - b);
    let ans = [];
    let curr = [];

    for(let i=0; i<nums.length; i++){

        curr.push(nums[i]);

        // console.log(curr)

        if(i%3 === 2){
            if(curr[2] - curr[0] > k){
                return [];
            }
            ans.push(curr);
            curr = [];
        }

    };

    return ans;

};