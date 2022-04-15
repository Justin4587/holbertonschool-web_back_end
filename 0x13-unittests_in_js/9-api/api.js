const express = require('express');
const app = express();
const port = 7865;

app.get('/', (req, res) => {
  res.status(200).send('Welcome to the payment system');
});

app.listen(port, () => {
  console.log('API available on localhost port: ' + port);
});

app.get('/cart/:id', (req, res) => {
  const { id } = req.params;
  console.log(parseInt(id))
  if (isNaN(parseInt(id))) {
    res.status(404).send('Not a number');
  } else {
    res.status(200).send('Payment methods for cart ' + id);
  }
})
