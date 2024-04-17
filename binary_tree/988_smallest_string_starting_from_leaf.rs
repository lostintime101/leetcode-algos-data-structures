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
    pub fn smallest_from_leaf(root: Option<Rc<RefCell<TreeNode>>>) -> String {

        let mut ans = String::new();

        pub fn traverse(node: Option<Rc<RefCell<TreeNode>>>, mut curr:String, ans:&mut String) {

            if let Some(node) = node {

                let node_b = node.borrow();

                curr = ((node_b.val as u8 + 97) as char).to_string() + &curr;

                if node_b.left.is_none() && node_b.right.is_none() {
                    if ans.is_empty() || curr < *ans {
                        *ans = curr.clone();
                    }
                }

                if node_b.left.is_some() {
                    traverse(node_b.left.clone(), curr.clone(), ans);
                }

                if node_b.right.is_some() {
                    traverse(node_b.right.clone(), curr.clone(), ans);
                }
            }
        }

        traverse(root, String::new(), &mut ans);

        ans

    }
}