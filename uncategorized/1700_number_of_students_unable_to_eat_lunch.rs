impl Solution {
    pub fn count_students(students: Vec<i32>, sandwiches: Vec<i32>) -> i32 {

        let mut squ:i32 = students.iter().sum();
        let mut cir:i32 = students.len() as i32 - squ;

        for (i,v) in sandwiches.iter().enumerate() {
            if *v == 1 {
                squ -= 1;
            } else {
                cir -= 1;
            }

            if squ < 0 || cir < 0 {
                return (sandwiches.len() - i) as i32
            }
        }

        0

    }
}
