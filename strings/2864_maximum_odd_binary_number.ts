function maximumOddBinaryNumber(s: string): string {

    let ans = "";
    let first = true;

    for(let c of s){
        if(c === "1"){
            if(first){
                first = false;
            } else {
                ans += "1"
            }
        }
    }

    let zeros = s.length - ans.length -1;
    ans += "0".repeat(zeros);
    ans += "1"

    return ans;

};