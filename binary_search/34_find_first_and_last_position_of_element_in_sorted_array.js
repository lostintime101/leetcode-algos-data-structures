/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {

    let l = 0
    let r = nums.length - 1
    let found = false
    let mid

    while(l <= r){

        mid = Math.floor((l+r) / 2)

        if(nums[mid] === target){
            found = true
            break
        }
        else if(nums[mid] > target) r = mid -1
        else l = mid + 1

    }

    if(!found) return [-1, -1]

    let left = mid
    let right = mid

    while((0 <= left-1) && (nums[left-1] === target)) left -= 1
    while((nums.length-1 >= right+1) && (nums[right+1] === target)) right += 1

    return [left, right]

};