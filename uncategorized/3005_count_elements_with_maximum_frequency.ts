function maxFrequencyElements(nums: number[]): number {

    let counts = {};
    let mx = 0;
    let ans = 0;

    for(let num of nums){
        counts[num] = (counts[num] || 0) + 1;
        mx = Math.max(mx, counts[num]);
    }

    for(let v of Object.values(counts)){
        if(v === mx){
            ans += v;
        }
    }

    return ans;
};