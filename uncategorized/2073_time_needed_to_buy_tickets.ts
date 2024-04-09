function timeRequiredToBuy(tickets: number[], k: number): number {

    let ans = 0;

    for(let [i,v] of tickets.entries()){
        if(i <= k){
            ans += Math.min(v,tickets[k]);
        } else {
            ans += Math.min(v,tickets[k]-1);
        }
    }

    return ans;

};