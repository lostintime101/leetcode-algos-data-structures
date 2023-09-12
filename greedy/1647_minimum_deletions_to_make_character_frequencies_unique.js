
/*

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

*/

/**
 * @param {string} s
 * @return {number}
 */
var minDeletions = function(s) {

    let freq = new Array(26).fill(0);

    for (let i = 0; i < s.length; i++){

        var c = s.charAt(i);
        var index = c.charCodeAt(0) - 'a'.charCodeAt(0);
        freq[index]++;
    }

    freq.sort(function(a, b) {
    return a - b;
    });

    // console.log(freq)
    let ans = 0
    for (let i=freq.length-1; i>0; i--) {

        if (freq[i-1] === 0){break};

        while(freq[i-1] >= freq[i]){

            freq[i-1] -= 1
            ans += 1
            if (freq[i-1] === 0){break};
        }
    }
    // console.log(freq)
    return ans
};
