/**
 * @param {number[]} nums
 * @param {number[]} l
 * @param {number[]} r
 * @return {boolean[]}
 */
var checkArithmeticSubarrays = function(nums, l, r) {
    const ans = []
    for(let i=0; i<l.length; i++){
        let curr = nums.slice(l[i], r[i]+1);
        curr = curr.sort((a,b) => (a - b))

        let curr_diff = 0, flag = true

        for(let j=1; j<curr.length; j++){

            if(j===1) curr_diff = curr[j] - curr[j-1]
            else {
                if(curr[j] - curr[j-1] !== curr_diff) flag = false
            }
        }
        ans.push(flag)
    }
    return ans
};