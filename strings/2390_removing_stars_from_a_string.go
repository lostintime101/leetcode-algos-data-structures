func removeStars(s string) string {

    stack := []rune{}
    ans := ""

    for _, r := range s {

        if r != '*' {
            stack = append(stack, r)
        } else if len(stack) > 0 {
            stack = stack[:len(stack)-1]
        }
    }

    ans = string(stack)

    return ans

}