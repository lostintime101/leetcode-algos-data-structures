func backspaceCompare(s string, t string) bool {

    newS := []rune{}
    newT := []rune{}

    for _, char := range s {
        if char == '#' {
            if len(newS) > 0 {
                newS = newS[:len(newS)-1]
            }
        } else {
            newS = append(newS, char)
        }
    }

    for _, char := range t {
        if char == '#' {
            if len(newT) > 0 {
                newT = newT[:len(newT)-1]
            }
        } else {
            newT = append(newT, char)
        }
    }

    return string(newS) == string(newT)
}