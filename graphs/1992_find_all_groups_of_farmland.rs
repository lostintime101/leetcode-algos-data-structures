impl Solution {
    pub fn find_farmland(mut land: Vec<Vec<i32>>) -> Vec<Vec<i32>> {

        let mut ans = Vec::new();
        let ROWS:usize = land.len();
        let COLS:usize = land[0].len();
        let DIRS:[[i32; 2];4] = [[1,0],[-1,0],[0,1],[0,-1]];

        for row in 0.. ROWS {
            for col in 0.. COLS {
                if land[row][col] == 1 {
                    land[row][col] = -1;
                    let mut start = Vec::from([row as i32,col as i32]);
                    start.extend(Solution::check(&mut land, row, col));
                    ans.push(start);
                }
            }
        }

        ans

    }

    pub fn check(land: &mut Vec<Vec<i32>>, r: usize, c: usize) -> Vec<i32> {
        let mut prev = Vec::from([[r as i32,c as i32]]);
        let mut curr = Vec::new();
        let mut end:[i32; 2] = [r as i32,c as i32];
        let ROWS:i32 = land.len() as i32;
        let COLS:i32 = land[0].len() as i32;
        let DIRS:[[i32; 2];4] = [[1,0],[-1,0],[0,1],[0,-1]];

        while !prev.is_empty() {
            for [r,c] in prev.iter() {
                for [x,y] in DIRS.iter() {
                    let [dx,dy] = [r+x, c+y];
                    if dx < 0 || dy < 0 || dx >= ROWS || dy >= COLS {
                        continue;
                    }
                    if land[dx as usize][dy as usize] == 1 {
                       land[dx as usize][dy as usize] = -1;
                        curr.push([dx,dy]);
                        end = [i32::max(dx,end[0]), i32::max(dy,end[1])];
                    }
                }
            }
            std::mem::swap(&mut prev, &mut curr);
            curr.clear();
        }
        end.to_vec()
    }
}