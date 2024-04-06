function minRemoveToMakeValid(s: string): string {

    let ends = 0, opened = 0;
    let ans = "";

    for(let l of s){
        if(l === ")"){
            ends ++;
        }
    }

    for(let l of s){

        if(l === "("){
            if(ends < 1){
                continue
            } else {
                ends -= 1;
                opened += 1;
            }
        }
        if(l === ")"){
            if(opened < 1){
                ends -= 1
                continue
            } else {
                opened -= 1;
            }
        }

        ans += l;
    }

    return ans;

};