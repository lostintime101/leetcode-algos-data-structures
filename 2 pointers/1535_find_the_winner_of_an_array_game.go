func getWinner(arr []int, k int) int {

    l := 0
    r := 1
    curr := 0
    count := 0

    for r < len(arr) {

        if arr[l] > arr[r] {
            r ++
            count ++
        } else {
            l = r
            curr = r
            r = r+1
            count = 1
        }

        if count >= k {
            return arr[curr]
        }
    }

    return arr[curr]
}