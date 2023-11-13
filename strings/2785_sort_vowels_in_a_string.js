/**
 * @param {string} s
 * @return {string}
 */
var sortVowels = function(s) {

    const vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    const vowelsFound = [], placesFound = []

    s = Array.from(s)

    for(let i=0; i<s.length; i++){
        if(vowels.includes(s[i])){
            vowelsFound.push(s[i].charCodeAt(0))
            placesFound.push(i)
        }
    }

    vowelsFound.sort((a,b) => a - b)

    for(let i=0; i<placesFound.length; i++){
        s[placesFound[i]] = String.fromCharCode(vowelsFound[i])
    }

    return s.join("")

};