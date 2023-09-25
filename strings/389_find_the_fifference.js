/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {

    let sCounter = new Map();
    let tCounter = new Map();

    for (let char of s){

        if (sCounter.has(char)) {
            sCounter.set(char, sCounter.get(char) + 1);
        } else {
            sCounter.set(char, 1);
        }
    }

    for (let char of t){

        if (tCounter.has(char)) {
            tCounter.set(char, tCounter.get(char) + 1);
        } else {
            tCounter.set(char, 1);
        }
    }

    // console.log(sCounter, tCounter)

    for (let [key, value] of tCounter.entries()) {
    if (!sCounter.has(key) || tCounter.get(key) !== sCounter.get(key)) {
        return key;
    }
    }

};