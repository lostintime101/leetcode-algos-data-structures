impl Solution {
    pub fn island_perimeter(grid: Vec<Vec<i32>>) -> i32 {

        let mut ans:i32 = 0;

        fn check(grid: &Vec<Vec<i32>>, i:i32, j:i32) -> i32 {
            let mut ret:i32 = 0;
            let dirs:[[i32; 2]; 4] = [[0,1],[0,-1],[1,0],[-1,0]];
            for [x,y] in dirs.iter() {
                let [dx] = [i+x];
                let [dy] = [j+y];
                if dx == -1 || dy == -1 || dx == grid.len() as i32 || dy == grid[0].len() as i32 {
                    ret += 1;
                } else if grid[dx as usize][dy as usize] == 0 {
                    ret += 1;
                }
            }
            ret
        }

        for (i,row) in grid.iter().enumerate() {
            for (j,col) in row.iter().enumerate() {
                if *col == 1 {
                    ans += check(&grid, i as i32,j as i32);
                }
            }
        }

        ans
    }
}