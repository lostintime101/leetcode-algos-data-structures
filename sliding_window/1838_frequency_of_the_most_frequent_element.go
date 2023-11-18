func maxFrequency(nums []int, k int) int {

    sort.Ints(nums)

    l := 0
    r := 1
    curr_k := 0
    highest := 1

    for r < len(nums) {

        curr_k += (nums[r] - nums[r-1]) * (r-l)

        for curr_k > k {
            curr_k -= (nums[r] - nums[l])
            l ++
        }

        highest = max(highest, (r+1)-l)
        r ++
    }

    return highest

}