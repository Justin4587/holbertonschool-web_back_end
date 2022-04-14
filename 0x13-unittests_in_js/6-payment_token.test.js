const sinon = require('sinon');
const should = require('chai').should();
const getPaymentTokenFromAPI = require('./6-payment_token');

describe.only('#getPaymentTokenFromAPI', () => {
  it('should do nothing if no token is provided', () => {
    getPaymentTokenFromAPI(true).then(token => {
      token.data.should.equal('Successful response from the API');
      done();
    })
  })
})
