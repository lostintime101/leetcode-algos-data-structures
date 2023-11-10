/**
 * @param {number[][]} adjacentPairs
 * @return {number[]}
 */
var restoreArray = function(adjacentPairs) {
    const neighbors = {};

    for (pair of adjacentPairs) {
        if (!neighbors[pair[0]]) neighbors[pair[0]] = [pair[1]];
        else neighbors[pair[0]].push(pair[1]);

        if (!neighbors[pair[1]]) neighbors[pair[1]] = [pair[0]];
        else neighbors[pair[1]].push(pair[0]);
    }

    const ret = new Array(Object.keys(neighbors).length).fill(0);

    for (key of Object.keys(neighbors)) {
        if (neighbors[key].length === 1) {
            ret[0] = parseInt(key);
            ret[1] = neighbors[key][0];
            break;
        }
    }

    for (let i = 2; i < ret.length; i++) {
        if (neighbors[ret[i-1]][0] === ret[i-2]) {
            ret[i] = neighbors[ret[i-1]][1];
        } else {
            ret[i] = neighbors[ret[i-1]][0];
        }
    }

    return ret;
};
