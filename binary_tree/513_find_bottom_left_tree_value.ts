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

function findBottomLeftValue(root: TreeNode | null): number {

    let prev = [root];
    let curr = [];
    let ans = null;

    while(prev.length != 0){
        ans = prev[0].val;
        for(let p of prev){
            if(p.left){
                curr.push(p.left)
            }
            if(p.right){
                curr.push(p.right)
            }
        }
        prev = curr;
        curr = [];
    }

    return ans;

};