/**
 * @param {string} colors
 * @return {boolean}
 */
var winnerOfGame = function(colors) {

    let plays = { "A": 0, "B": 0}
    let curr = colors[0]
    let streak = 1

    for (let i=1; i<colors.length; i++){

        if (colors[i] === curr){
            streak ++;
        }
        else {
            curr = colors[i]
            streak = 1;
        }

        if (streak > 2){
            plays[curr] ++;
        }
    }

    return plays["A"] > plays["B"]
};