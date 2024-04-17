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

function smallestFromLeaf(root: TreeNode | null): string {

    let ans = null;

    function traverse(node: TreeNode|null, curr: string){

        curr = String.fromCharCode(97 + node.val) + curr;

        if(!node.left && !node.right){
            if(!ans || ans > curr){
                ans = curr;
            }
        }

        if(node.left){
            traverse(node.left, curr);
        }
        if(node.right){
            traverse(node.right, curr);
        }
    }

    traverse(root, "")

    return ans

};