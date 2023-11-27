/**
* @param {number} n
* @return {number}
*/
var knightDialer = function(n) {

    const MOD = 10**9 + 7

    const nextMoves = {
        0: [4,6],
        1: [6,8],
        2: [7,9],
        3: [4,8],
        4: [0,3,9],
        5: [],
        6: [0,1,7],
        7: [2,6],
        8: [1,3],
        9: [2,4]
    }

    let prev = [1,1,1,1,1,1,1,1,1,1]
    let curr = [0,0,0,0,0,0,0,0,0,0]

    for(let _=0; _<n-1; _++){

        for(p in prev){
            for(val of nextMoves[p]){
                curr[val] += prev[p] % MOD
            }
        }
        prev = curr
        curr = [0,0,0,0,0,0,0,0,0,0]

    }
    return prev.reduce((a,b) => a+b) % MOD
};