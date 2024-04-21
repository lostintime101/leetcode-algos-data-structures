function validPath(n: number, edges: number[][], source: number, destination: number): boolean {

    let seen = new Array(n).fill(false);
    let mapp = {};

    for(let [a,b] of edges){

        let currA = (mapp[a] || []);
        currA.push(b);
        mapp[a] = currA;
        let currB = (mapp[b] || []);
        currB.push(a);
        mapp[b] = currB;
    }

    let prev = [source];
    let curr = [];

    while(prev.length != 0){

        for(let p of prev){
            if(p === destination){
                return true;
            }
            if(seen[p] == true){
                continue;
            } else {
                seen[p] = true;
            }

            curr.push(... mapp[p]);
        }

        prev = curr;
        curr = [];
    }

    return false;

};