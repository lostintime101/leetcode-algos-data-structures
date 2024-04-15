// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {

        pub fn dfs(node: Option<Rc<RefCell<TreeNode>>>, mut curr: i32) -> i32 {

            if let Some(node) = node {

                let node_b = node.borrow();

                curr *= 10;
                curr += node_b.val;

                if node_b.left.is_none() && node_b.right.is_none() {
                    return curr;
                }

                let left_val = if let Some(left) = &node_b.left {
                    dfs(Some(left.clone()), curr)
                } else {
                    0
                };

                let right_val = if let Some(right) = &node_b.right {
                    dfs(Some(right.clone()), curr)
                } else {
                    0
                };

                left_val + right_val

            } else {
                0
            }
        }

        dfs(root, 0)

    }
}