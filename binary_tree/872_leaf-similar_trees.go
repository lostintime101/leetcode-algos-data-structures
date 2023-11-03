/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func dfs(node *TreeNode, leaves *[]int) {

    if node == nil {
        return
    }

    if node.Left == nil && node.Right == nil {
        *leaves = append(*leaves, node.Val)
    }

    if node.Left != nil {
        dfs(node.Left, leaves)
    }
    if node.Right != nil {
        dfs(node.Right, leaves)
    }
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {

    leaves1 := []int{}
    leaves2 := []int{}

    dfs(root1, &leaves1)
    dfs(root2, &leaves2)

    if len(leaves1) != len(leaves2) {
        return false
    }

    for i := 0; i < len(leaves1); i++ {
        if leaves1[i] != leaves2[i] {
            return false
        }
    }

    // fmt.Println("Leaves 1:")
    for _, val := range leaves1 {
        fmt.Println(val)
    }

    // fmt.Println("Leaves 2:")
    for _, val := range leaves2 {
        fmt.Println(val)
    }

    return true

}