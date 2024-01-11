
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
use std::{cmp, rc::Rc, cell::RefCell};

impl Solution {
    pub fn max_ancestor_diff(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {

        if let Some(root) = root {
            let mut ans:i32 = 0;
            let val = root.borrow().val;

            let mut queue = vec![(root, val, val)];

            while queue.len() > 0 {

                let (node, mut min_v, mut max_v) = queue.pop().unwrap();
                let node = node.borrow();

                max_v = i32::max(max_v, node.val);
                min_v = i32::min(min_v, node.val);
                ans = i32::max(ans, max_v - min_v);

                if let Some(mut left) = node.left.clone() {
                    queue.push((left, min_v, max_v));
                } else {}

                if let Some(mut right) = node.right.clone() {
                    queue.push((right, min_v, max_v));
                } else {}
            }

            ans

        } else {
            0
        }
    }
}