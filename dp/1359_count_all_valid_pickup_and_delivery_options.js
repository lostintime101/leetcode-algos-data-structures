/**
 * @param {number} n
 * @return {number}
 */
var countOrders = function(n) {

    factors = {0: 0}
    for(let i=1; i < (n*2)+2 ; i++){
        factors[i] = factors[i-1] + i
    }

    let curr = 0
    let positions = 0
    let dp = Array(n).fill(0);
    dp[0] = 1

    while( curr !== n-1 ) {

        curr ++
        positions = (curr*2) + 1
        dp[curr] = (factors[positions] * dp[curr-1]) % (1e9 + 7)

    }

    return dp[dp.length -1];

};


const assert = require('chai').assert;

// Import the countOrders function here

describe('countOrders', function() {
    it('should return 1 when n is 1', function() {
        assert.equal(countOrders(1), 1);
    });

    it('should return 6 when n is 2', function() {
        assert.equal(countOrders(2), 6);
    });

    it('should return 90 when n is 3', function() {
        assert.equal(countOrders(3), 90);
    });

    it('should return 2520 when n is 4', function() {
        assert.equal(countOrders(4), 2520);
    });

    it('should return 113400 when n is 5', function() {
        assert.equal(countOrders(5), 113400);
    });
});
