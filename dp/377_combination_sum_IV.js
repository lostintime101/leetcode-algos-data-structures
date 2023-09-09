/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {

    let dp = {0: 1}

    for(let i=1; i<=target; i++){
        dp[i] = 0
        for(let num of nums){
            dp[i] += dp[i-num] || 0;
        }
    }
    return dp[target]

};

const assert = require('assert');

function runTests() {
    // Test cases
    const testCases = [
        { nums: [1, 2, 3], target: 4, expected: 7 },
        { nums: [9], target: 3, expected: 0 },
        { nums: [1, 2, 3], target: 32, expected: 181997601 },
        { nums: [], target: 10, expected: 0 },
    ];

    testCases.forEach((testCase, index) => {
        const { nums, target, expected } = testCase;
        const result = combinationSum4(nums, target);
        assert.strictEqual(result, expected, `Test case ${index + 1} failed`);
    });

    console.log('All test cases passed!');
}

runTests();
