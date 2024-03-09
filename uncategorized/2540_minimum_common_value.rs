impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {

        let (mut a, mut b): (usize, usize) = (0,0);

        while a < nums1.len() && b < nums2.len() {
            if nums1[a] == nums2[b] {
                return nums1[a];
            } else if nums1[a] > nums2[b] {
                b += 1;
            } else {
                a += 1;
            }
        }

        -1
    }
}