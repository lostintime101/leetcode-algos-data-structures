impl Solution {
    pub fn largest_local(grid: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

        // NEW
        let mut new_grid: Vec<Vec<i32>> = vec![Vec::new(); grid.len()-2];

        for row in 0.. grid.len()-2 {
            for col in 0.. grid.len()-2 {

                let mut mx = 0;

                for x in 0.. 3 {
                    for y in 0.. 3 {
                        mx = i32::max(mx, grid[row+x][col+y]);
                    }
                }

                new_grid[row].push(mx);
            }
        }

        new_grid
        // OLD
        // let mut new_grid: Vec<Vec<i32>> = vec![vec![0; grid.len()-2]; grid.len()-2];

        // for row in 0.. new_grid.len() {
        //     for col in 0.. new_grid[0].len() {

        //         new_grid[row][col] = [
        //             grid[row][col],
        //             grid[row][col+1],
        //             grid[row][col+2],
        //             grid[row+1][col],
        //             grid[row+1][col+1],
        //             grid[row+1][col+2],
        //             grid[row+2][col],
        //             grid[row+2][col+1],
        //             grid[row+2][col+2]
        //             ]
        //             .iter()
        //             .copied()
        //             .max()
        //             .unwrap()
        //     }
        // }

        // new_grid
    }
}