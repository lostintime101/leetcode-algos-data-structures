/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function(s, t) {

    let new_s = []
    let new_t = []

    for(let i=0; i<s.length ;i++){
        if(s[i] === "#"){
            if(new_s) new_s.pop()
        }
        else {
            new_s.push(s[i])
        }
    }

    for(let i=0; i<t.length ;i++){
        if(t[i] === "#"){
            if(new_t) new_t.pop()
        }
        else {
            new_t.push(t[i])
        }
    }

    return JSON.stringify(new_s) === JSON.stringify(new_t)

};