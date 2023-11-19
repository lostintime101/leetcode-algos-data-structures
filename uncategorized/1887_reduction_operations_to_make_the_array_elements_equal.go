func reductionOperations(nums []int) int {

    sort.Ints(nums)

    ans := 0

    for i :=len(nums)-2; i>-1; i-- {
        if nums[i] != nums[i+1] {
            ans += len(nums) - (i+1)
        }
    }

    return ans

}