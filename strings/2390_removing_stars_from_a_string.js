/**
 * @param {string} s
 * @return {string}
 */
var removeStars = function(s) {

    const stack = []

    for(l of s) {
        if(l === "*") stack.pop()
        else stack.push(l)
    }

    return stack.join("")
};