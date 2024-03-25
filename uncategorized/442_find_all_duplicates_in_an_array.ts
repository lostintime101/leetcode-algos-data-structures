function findDuplicates(nums: number[]): number[] {

    let ans = [];
    let N = nums.length;

    for(let i=0; i<N; i++){
        let curr = nums[i];
        if(curr < 0){
            curr *= -1;
        };
        curr -= 1;
        if(nums[curr] < 0){
            ans.push(curr + 1);
        } else {
            nums[curr] = nums[curr] * -1;
        }
    };

    return ans;

};