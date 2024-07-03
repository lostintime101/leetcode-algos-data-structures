function minDifference(nums: number[]): number {

    let ans = Infinity;
    let poss = [[0, -4], [1, -3], [2, -2], [3, -1]];

    if(nums.length <= 3) {
        return 0;
    }

    nums.sort((a,b) => a-b);

    for(let p of poss){
        let start = p[0];
        let end =  p[1];

        let curr = nums[end + nums.length] - nums[start];
        ans = Math.min(curr, ans);

    }

    return ans

};