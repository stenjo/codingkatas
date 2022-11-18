"use strict";
exports.__esModule = true;
var index_1 = require("../src/index");
describe('testing index file', function () {
    test('empty string should result in zero', function () {
        expect((0, index_1.add)('')).toBe(0);
    });
});
