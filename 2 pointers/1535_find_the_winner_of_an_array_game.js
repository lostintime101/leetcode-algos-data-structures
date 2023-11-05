/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var getWinner = function(arr, k) {

    let l = 0, r = 1
    let curr = 0, count = 0

    while(r < arr.length){

        if(arr[l] > arr[r]){
            count ++
            r ++
        } else {
            curr = r
            l = r
            r = l+1
            count = 1
        }
        // console.log(l,r,curr,count)
        if(count >= k) return arr[curr]
    }

    return arr[curr]
};