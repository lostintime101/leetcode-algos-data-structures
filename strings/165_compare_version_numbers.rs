impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {

        let v1: Vec<i32> = version1.split('.').map(|s| s.parse().unwrap_or(0)).collect();
        let v2: Vec<i32> = version2.split('.').map(|s| s.parse().unwrap_or(0)).collect();

        let max_len = v1.len().max(v2.len());

        for i in 0..max_len {
            let num1 = v1.get(i).unwrap_or(&0);
            let num2 = v2.get(i).unwrap_or(&0);

            if num1 > num2 {
                return 1;
            } else if num1 < num2 {
                return -1;
            }
        }

        0
    }

}

// Old solution
// impl Solution {
//     pub fn compare_version(version1: String, version2: String) -> i32 {
//
//         let mut v1: Vec<&str> = version1.split('.').collect();
//         let mut v2: Vec<&str> = version2.split('.').collect();
//         let mut v1i: Vec<i32> = Vec::new();
//         let mut v2i: Vec<i32> = Vec::new();
//
//         for version in v1.iter() {
//             let v = version.parse().unwrap();
//             v1i.push(v);
//         }
//
//         for version in v2.iter() {
//             let v = version.parse().unwrap();
//             v2i.push(v);
//         }
//
//         while v1i.len() < v2i.len() {
//             v1i.push(0);
//         }
//
//         while v2i.len() < v1i.len() {
//             v2i.push(0);
//         }
//
//         for i in 0..v1i.len() {
//             if v1i[i] > v2i[i] {
//                 return 1;
//             }
//             if v1i[i] < v2i[i] {
//                 return -1;
//             }
//         }
//
//         0
//     }
// }