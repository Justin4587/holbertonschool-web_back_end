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

describe('cart', () => {
  const path200 = 'http://localhost:7865/cart/12';
  const path404 = 'http://localhost:7865/cart/notnum';

  it('', (done) => {
    request(path200, function (err, res, body) {
      (res.statusCode).should.equal(200);
      done();
    })
  })

  it('', (done) => {
    request(path404, function (err, res, body) {
      (res.statusCode).should.equal(404);
      done();
    })
  })

  it('', done => {
    request(path200, function (err, res, body) {
      (body).should.equal('Payment methods for cart 12');
      done();
    })
  })

  it('', done => {
    request(path404, function (err, res, body) {
      (body).should.equal('Not a number');
      done();
    })
  })
})
