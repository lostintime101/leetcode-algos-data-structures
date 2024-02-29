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

function isEvenOddTree(root: TreeNode | null): boolean {

    let prev = [root];
    let curr = [];
    if(root.val %2 !== 1){
        return false;
    }
    let odd = false;

    while(prev.length > 0){
        odd = !odd;
        let vals = [];
        for(let p of prev){

            if(p.left){
                curr.push(p.left)
            }
            if(p.right){
                curr.push(p.right)
            }
            vals.push(p.val)
        }

        if(odd == true){
            for(let i=0; i<vals.length-1; i++){
                if((vals[i] %2 !== 1) || (vals[i] >= vals[i+1])){
                    return false;
                }
            }
            if(vals[vals.length -1] %2 !== 1){
                return false
            }
        } else {
            for(let i=0; i<vals.length-1; i++){
                if((vals[i] %2 !== 0) || (vals[i] <= vals[i+1])){
                    return false;
                }
            }
            if(vals[vals.length -1] %2 !== 0){
                return false
            }
        }

        prev = curr;
        curr = [];

    }

    return true;

};