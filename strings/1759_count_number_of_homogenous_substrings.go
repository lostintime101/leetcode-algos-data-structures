func countHomogenous(s string) int {

    MOD := int(math.Pow(10, 9)) + 7
    ret := 0
    count := 1
    prev := 'A'

    for _, i := range s{

        if i == prev {
            count = count + 1
        } else {
            count = 1
        }

        prev = i
        ret = ret + count
    }

    return ret % MOD

}