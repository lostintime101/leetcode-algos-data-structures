function findMaxK(nums: number[]): number {

    let possible = {};

    for(let num of nums){
        possible[num] = true;
        if(!possible[num*-1]){
            possible[num*-1] = false;
        }
    }

    let ans = -1;

    for(let num of nums){
        if(possible[num] === true && possible[num*-1] === true){
            ans = Math.max(ans, num);
        }
    }

    return ans;

};