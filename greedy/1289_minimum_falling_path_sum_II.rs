impl Solution {
    pub fn min_falling_path_sum(grid: Vec<Vec<i32>>) -> i32 {

        let mut new_grid = grid.clone();
        let mut left:i32 = 1_000_000_000;
        let mut right:i32 = 1_000_000_000;

        for row in 1.. grid.len() {
            for col in 0.. grid[0].len() {

                left = 1_000_000_000;
                right = 1_000_000_000;

                if col != 0 {
                    let left_slice = &new_grid[row - 1][..col];
                    left = *left_slice.iter().min().unwrap();
                }

                if col != grid[0].len()-1 {
                    let right_slice = &new_grid[row - 1][col+1..];
                    right = *right_slice.iter().min().unwrap();
                }

                new_grid[row][col] += i32::min(left, right);
            }
        }

        *new_grid.last().unwrap().iter().min().unwrap()

    }
}
