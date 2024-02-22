impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {

        let mut trusts: Vec<i32> = vec![0; n as usize];
        let mut is_trusted: Vec<i32> = vec![0; n as usize];

        for t in trust {
            let (truster, trusted) = (t[0] as usize - 1, t[1] as usize - 1);
            trusts[truster] = 1;
            is_trusted[trusted] += 1;
        }

        for i in 0.. n as usize {
            if trusts[i] == 0 && is_trusted[i] == n-1 {
                return (i+1) as i32;
            }
        }

        -1
    }
}