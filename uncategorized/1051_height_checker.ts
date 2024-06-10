function heightChecker(heights: number[]): number {

    let sorted_heights = [... heights];
    sorted_heights.sort((a,b) => a-b);

    // console.log(sorted_heights, heights);
    let ans = 0;

    for(let i=0; i<heights.length; i++){
        if(sorted_heights[i] != heights[i]){
            ans += 1;
        }
    }

    return ans;

};