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

function sumOfLeftLeaves(root: TreeNode | null): number {

    function dfs(node, left){

        if(!node){
            return 0;
        }
        if(!node.left && !node.right && left){
            return node.val;
        }
        return dfs(node.left, true) + dfs(node.right, false)
    }

    return dfs(root.left, true) + dfs(root.right, false)

};