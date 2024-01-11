/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxAncestorDiff = function(root) {

    let prev = [[root, root.val, root.val]];
    let curr = [];
    let ans = 0;

    while(prev.length > 0){

        for(let p of prev){
            [node, mi, ma] = p;
            ma = Math.max(ma, node.val);
            mi = Math.min(mi, node.val);
            ans = Math.max(ma-mi, ans);
            if(node.left != null){
                curr.push([node.left, mi, ma]);
            }
            if(node.right != null){
                curr.push([node.right, mi, ma]);
            }
        }

        prev = curr;
        curr = [];

    }

    return ans

};