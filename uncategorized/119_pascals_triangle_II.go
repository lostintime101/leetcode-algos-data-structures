func getRow(rowIndex int) []int {

    if rowIndex == 0 {
        return []int{1}
    }
    row := 0
    prev := []int{1}

    for {

        row ++
        curr := []int{1}

        for i:= 0 ; i < len(prev)-1 ; i++ {
            curr = append(curr, prev[i]+prev[i+1])
        }
        curr = append(curr, 1)

        if row == rowIndex {
            return curr
        }

        prev = curr
    }

}