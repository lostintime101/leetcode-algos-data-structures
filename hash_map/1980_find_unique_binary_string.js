/**
 * @param {string[]} nums
 * @return {string}
 */
var findDifferentBinaryString = function(nums) {

    const hashMap = {}
    for(num of nums) hashMap[num] = true

    const n = nums[0].length

    for(let i=(2**n)-1; i>-1; i--){

        let base = i.toString(2).split('')
        let front = Array(n - base.length).fill("0")

        front = [... front, ... base]

        if(!hashMap[front.join("")]) return front.join("")
    }

};