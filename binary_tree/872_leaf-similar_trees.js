/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {boolean}
 */
var leafSimilar = function(root1, root2) {

    const leaves1 = []
    const leaves2 = []

    function dfs(node, leaves){

        if(!node.left && !node.right) {
            leaves.push(node.val)
            return
        }
        if(node.left) dfs(node.left, leaves)
        if(node.right) dfs(node.right, leaves)
    }

    dfs(root1, leaves1)
    const half = leaves1.length
    dfs(root2, leaves2)

    if(leaves1.length != leaves2.length) return false

    for(let i=0; i<leaves1.length ;i++){
        if(leaves1[i] != leaves2[i]) return false
    }

    return true

};