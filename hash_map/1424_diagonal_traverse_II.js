/**
 * @param {number[][]} nums
 * @return {number[]}
 */
var findDiagonalOrder = function(nums) {

    const mapping = {}
    let mx = 0
    for(let r=0; r<nums.length; r++){
        for(let c=0; c<nums[r].length; c++){
            if (!mapping[r+c]) mapping[r+c] = [];
            mapping[r+c].push(nums[r][c])
            mx = Math.max(mx, r+c)
        }
    }

    let ans = []
    let count = 0

    for(let i=0; i<=mx; i++){
        curr = mapping[i]
        for(let j=curr.length-1; j>-1; j--){
            ans.push(curr[j])
        }
    }

    return ans

};