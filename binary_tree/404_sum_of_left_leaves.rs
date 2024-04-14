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
    pub fn sum_of_left_leaves(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {

        pub fn dfs(node: Option<Rc<RefCell<TreeNode>>>, left: bool) -> i32 {
            match node {
                None => 0,
                Some(node) => {
                    let borrow_node = node.borrow();
                    if left && borrow_node.left.is_none() && borrow_node.right.is_none() {
                        borrow_node.val
                    } else {
                        dfs(borrow_node.left.clone(), true) + dfs(borrow_node.right.clone(), false)
                    }
                }
            }
        }

        if let Some(our_root) = root {
            let borrow_root = our_root.borrow();
            dfs(borrow_root.left.clone(), true) + dfs(borrow_root.right.clone(), false)
        } else {
            0
        }
    }
}