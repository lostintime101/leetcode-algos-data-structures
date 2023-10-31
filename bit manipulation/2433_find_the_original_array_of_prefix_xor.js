/**
 * @param {number[]} pref
 * @return {number[]}
 */
var findArray = function(pref) {

    const ans = [... pref]

    for(let i=1; i<pref.length; i++){
        ans[i] = pref[i-1] ^ pref[i]
    }

    return ans

};