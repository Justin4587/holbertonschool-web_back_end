const sinon = require('sinon');
const Utils = require('./utils');
const should = require('chai').should();
const sendPaymentRequestToApi = require('./3-payment');

describe('#sendPaymentRequestToApi()', function () {
  it('should bring my life validation', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    sendPaymentRequestToApi(100, 20);
    spy.calledWith('SUM', 100, 20).should.equal(true);
    spy.restore();
  })
})
