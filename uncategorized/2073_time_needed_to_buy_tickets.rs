impl Solution {
    pub fn time_required_to_buy(tickets: Vec<i32>, k: i32) -> i32 {

        let mut ans:i32 = 0;
        let k = k as usize;

        for (i,v) in tickets.iter().enumerate() {
            if i <= k {
                ans += i32::min(*v, tickets[k]);
            } else {
                ans += i32::min(*v, tickets[k]-1);
            }
        }

        ans
    }
}