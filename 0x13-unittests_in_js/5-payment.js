const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  const text = 'The total is: ';
  console.log(text + total);
}

module.exports = sendPaymentRequestToApi;
