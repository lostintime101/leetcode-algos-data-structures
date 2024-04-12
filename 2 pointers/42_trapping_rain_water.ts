function trap(height: number[]): number {


    let N = height.length, ans = 0;
    let bigL = new Array(N).fill(0), bigR = new Array(N).fill(0);

    let prev = 0;
    for(let i=0; i<N; i++){
        bigL[i] = Math.max(prev, height[i]);
        prev = bigL[i];
    }

    prev = 0;
    for(let i=N-1; i>-1; i--){
        bigR[i] = Math.max(prev, height[i]);
        prev = bigR[i];
    }

    for(let i=0; i<N; i++){
        ans += (Math.min(bigL[i], bigR[i]) - height[i]);
    }

    return ans;

};