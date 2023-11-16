/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {

    return dfs(root, 0)

}

func dfs(node *TreeNode, depth int) int {

    if node == nil {
        return depth
    }

    leftDepth := dfs(node.Left, depth+1)
    rightDepth := dfs(node.Right, depth+1)

    if leftDepth > rightDepth {
        return leftDepth
    } else {
        return rightDepth
    }

}