/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findLeastNumOfUniqueInts = function(arr, k) {

    let freq = {};

    for(let a of arr){
        freq[a] = (freq[a] || 0) + 1;
    }

    let vals = [];

    for(let k of Object.keys(freq)){
        vals.push(freq[k]);
    }

    vals.sort((a,b) => a - b);

    let remove = 0;
    for(let v of vals){
        if(v <= k){
            k -= v;
            remove ++
        } else {
            break
        }
    }

    return vals.length - remove

};