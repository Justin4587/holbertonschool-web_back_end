const sinon = require('sinon');
const Utils = require('./utils');
const should = require('chai').should();
const sendPaymentRequestToApi = require('./3-payment');

describe('#sendPaymentRequestToApi()', function () {
  it('should bring my life validation', function () {
    const spy = sinon.spy(console, 'log');
    const stubby = sinon.stub(Utils, 'calculateNumber');
    stubby.returns(10);
    sendPaymentRequestToApi(100, 20);
    spy.calledWith('The total is: 10').should.equal(true);
    stubby.calledWith('SUM', 100, 20).should.equal(true);
    stubby.alwaysReturned(10).should.equal(true);
    spy.restore();
    stubby.restore();
  })
})
