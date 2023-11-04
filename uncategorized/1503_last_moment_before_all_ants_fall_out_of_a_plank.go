func getLastMoment(n int, left []int, right []int) int {

 leftMax := 0
 rightMax := 0

 for _, num := range left {
    if leftMax < num {
        leftMax = num
    }
 }

 for _, num := range right {
     if rightMax < n-num {
         rightMax = n-num
     }
 }

ans := 0
 if ans < leftMax {
     ans = leftMax
 }
 if ans < rightMax {
     ans = rightMax
 }

 return ans
}