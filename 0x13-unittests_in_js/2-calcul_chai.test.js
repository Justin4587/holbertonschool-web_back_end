const expect = require('chai').expect;
const calculateNumber = require('./1-calcul');

describe('#calculateNumber()', function () {
  it('should calculate the number of digits', function () {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('', function () {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('', function () {
    expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
  });
  it('', function () {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('', function () {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
});
