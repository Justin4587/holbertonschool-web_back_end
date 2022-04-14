const sinon = require('sinon');
const should = require('chai').should();
const sendPaymentRequestToApi = require('./5-payment');

describe('#sendPaymentRequestToApi()', function () {
  let spy;

  beforeEach(function() {
    spy = sinon.spy(console, 'log');
  });

  afterEach(function() {
    spy.calledOnce.should.be.true;
    spy.restore();
  });

  it('should bring my life validation', function () {
    sendPaymentRequestToApi(100, 20);
    spy.calledWith('The total is: 120').should.equal(true);
  });

  it('should bring my life validation', function () {
    sendPaymentRequestToApi(10, 10);
    spy.calledWith('The total is: 20').should.equal(true);
  });
});
