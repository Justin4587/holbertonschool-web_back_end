const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('#calculateNumber()', function () {
  it('should return  4 when calculateNumber is passed 1 and 3', function () {
    assert.strictEqual(calculateNumber(1, 3), 4);
  });
});
