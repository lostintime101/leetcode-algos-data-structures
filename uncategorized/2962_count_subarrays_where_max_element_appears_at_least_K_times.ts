function countSubarrays(nums: number[], k: number): number {

    let N = nums.length
    let mx = Math.max(...nums);
    let start = 0, count = 0, ans = 0;

    for(let end = 0; end < N; end++){
        if(nums[end] == mx){
            count ++;
        };

        while(count >= k && start <= end){
            ans += N - end;
            if(nums[start] == mx){
                count --;
            };
            start ++;
        };
    };

    return ans;

};