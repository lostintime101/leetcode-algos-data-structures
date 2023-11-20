/**
 * @param {string[]} garbage
 * @param {number[]} travel
 * @return {number}
 */
var garbageCollection = function(garbage, travel) {

    let time = 0
    let Gi = 0, Pi = 0, Mi = 0

    for(let i=garbage.length-1; i>-1; i--){

        time += garbage[i].length
        if(Gi === 0 && garbage[i].includes("G")) Gi = i
        if(Pi === 0 && garbage[i].includes("P")) Pi = i
        if(Mi === 0 && garbage[i].includes("M")) Mi = i

    }
    const G = travel.slice(0, Gi).reduce((total, current) => total + current, 0)
    const P = travel.slice(0, Pi).reduce((total, current) => total + current, 0)
    const M = travel.slice(0, Mi).reduce((total, current) => total + current, 0)

    return time + G + P + M

};