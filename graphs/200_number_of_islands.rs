impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {

        let mut ans:i32 = 0;
        let DIRS: [[i32;2];4]= [[1,0],[-1,0],[0,1],[0,-1]];

        for row in 0.. grid.len() {
            for col in 0.. grid[0].len() {
                if grid[row][col] == '1' {
                    ans += 1;
                    grid[row][col] = '2';
                    check(&mut grid, row, col, &DIRS);
                }
            }
        }

        ans
    }
}

pub fn check(grid: &mut Vec<Vec<char>>, r: usize, c: usize, dirs: &[[i32;2];4]){

    let mut prev = Vec::new();
    let mut curr = Vec::new();
    prev.push([r as i32,c as i32]);

    while !prev.is_empty() {
        for [r,c] in prev {
            for [x,y] in dirs {
                let [dx,dy] = [r+x, c+y];
                if dx < 0 || dy < 0 || dx >= grid.len() as i32 || dy >= grid[0].len() as i32 {
                    continue;
                }
                if grid[dx as usize][dy as usize] == '1' {
                    grid[dx as usize][dy as usize] = '2';
                    curr.push([dx,dy]);
                }
            }
        }

        prev = curr.clone();
        curr = Vec::new();
    }

}