function numIslands(grid: string[][]): number {

    let ans = 0;
    const DIRS = [[0,1],[0,-1],[1,0],[-1,0]];
    const ROWS = grid.length;
    const COLS = grid[0].length;

    function check(r:number,c:number){
        let prev = [[r,c]];
        let curr = [];

        while(prev.length > 0){
            for(let[r,c] of prev){
                for(let[x,y] of DIRS){
                    let [dx,dy] = [r+x , c+y];
                    if(dx<0 || dy<0 || dx>=ROWS || dy>=COLS){
                        continue;
                    }
                    if(grid[dx][dy] === "1"){
                        grid[dx][dy] = "-1";
                        curr.push([dx,dy]);
                    }
                }

            }
            prev = curr;
            curr = [];
        }
    }

    for(let row=0; row<ROWS; row++){
        for(let col=0; col<COLS; col++){

            if(grid[row][col] === "1"){
                ans += 1;
                grid[row][col] = "-1";;
                check(row, col);
            }
        }
    }


    return ans;

};