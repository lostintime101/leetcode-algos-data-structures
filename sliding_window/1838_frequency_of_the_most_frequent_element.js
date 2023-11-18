/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxFrequency = function(nums, k) {

    nums = nums.sort((a,b) => a - b)

    let l = 0, r = 1
    let curr_k = 0, highest = 1

    while(r < nums.length){

        curr_k += (nums[r] - nums[r-1]) * (r-l)

        while(curr_k > k){
            curr_k -= (nums[r] - nums[l])
            l ++
        }

        highest = Math.max(highest, (r+1)-l)
        r ++
    }

    return highest

};
