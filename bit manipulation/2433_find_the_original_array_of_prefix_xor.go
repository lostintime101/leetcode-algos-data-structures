func findArray(pref []int) []int {

    ans := make([]int, len(pref))
    copy(ans, pref)

    for i :=1; i<len(pref); i++ {

        ans[i] = pref[i-1] ^ pref[i]
    }

    return ans

}