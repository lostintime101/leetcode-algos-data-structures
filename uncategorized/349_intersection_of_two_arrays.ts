function intersection(nums1: number[], nums2: number[]): number[] {

    let counter1 = {};
    let ans = [];

    for(let num of nums1){
        counter1[num] = (counter1[num] || 0) + 1;
    };

    for(let num of nums2){
        if(counter1[num] > 0){
            counter1[num] = 0;
            ans.push(num);
        }
    };

    return ans;

};