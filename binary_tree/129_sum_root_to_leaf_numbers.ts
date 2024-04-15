/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumNumbers(root: TreeNode | null): number {

    function dfs(node, curr){
        curr *= 10;
        curr += node.val

        if(!node.left && !node.right){
            return curr;
        }

        return ((node.left && dfs(node.left, curr)) || 0) + ((node.right && dfs(node.right, curr) || 0));
    }

    return dfs(root, 0)

};