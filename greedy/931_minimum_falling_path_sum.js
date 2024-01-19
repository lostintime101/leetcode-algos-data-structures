/**
 * @param {number[][]} matrix
 * @return {number}
 */
var minFallingPathSum = function(matrix) {

    let ROWS = matrix.length;
    let COLS = matrix[0].length;

    for(let row = 1; row< ROWS; row++){
        for(let col =0; col<COLS; col++){

            let left = Infinity, right = Infinity, center = Infinity;
            center = matrix[row-1][col];

            if(col !== 0){
                left = matrix[row-1][col-1]
            }
            if(col !== COLS-1){
                right = matrix[row-1][col+1]
            }

            matrix[row][col] += Math.min(left, right, center);

        }
        // console.log(matrix)
    }

    return Math.min(... matrix[matrix.length-1])

};