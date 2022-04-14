const should = require('chai').should();
const request = require('request');

describe('index', () => {
  const path = 'http://localhost:7865';

  it(''  , (done) => {
    request(path, function (err, res, body) {
      (res.statusCode).should.equal(200);
      done();
    });
  });

  it('', (done) => {
    request(path, function (err, res, body) {
      (body).should.equal('Welcome to the payment system');
      done();
    })
  })
})
