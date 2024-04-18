function islandPerimeter(grid: number[][]): number {

    let ans = 0;
    let ROWS = grid.length;
    let COLS = grid[0].length;
    let dirs = [[-1,0],[1,0],[0,-1],[0,1]];

    function check(r:number, c:number): number{

        let ret = 0;
        for(let [x,y] of dirs){

            let [dx,dy] = [r+x, c+y];
            if(dx === -1 || dx === ROWS || dy === -1 || dy === COLS || grid[dx][dy] === 0){
                ret += 1;
            }
        }
        return ret;
    };

    for(let row=0; row<ROWS; row++){
        for(let col=0; col<COLS; col++){
            if(grid[row][col] === 1){
                ans += check(row,col);
            }
        }
    }

    return ans;

};