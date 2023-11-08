func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {

    xLimit := int(math.Abs(float64(sx - fx)))
    yLimit := int(math.Abs(float64(sy - fy)))
    limit := int(math.Max(float64(xLimit), float64(yLimit)))

    return t >= limit && !(t == 1 && limit == 0)

}