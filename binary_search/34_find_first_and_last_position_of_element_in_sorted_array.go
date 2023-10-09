func searchRange(nums []int, target int) []int {

    l, r, mid := 0, len(nums)-1, 0
    found := false

    for l <= r {
        mid = (l+r) / 2

        if nums[mid] == target {
            found = true
            break
        } else if nums[mid] < target {
            l = mid + 1
        } else {
            r = mid - 1
        }
    }

    if !found {
        return []int{-1,-1}
    }

    left, right := mid, mid

    for left > 0 && nums[left-1] == target {
        left --
    }

    for right < len(nums)-1 && nums[right+1] == target {
        right ++
    }

    return []int{left, right}
}