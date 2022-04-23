import { createClient } from 'redis';

(async () => {
  const client = createClient();
  console.log('working');
  client.on('error', async (err) => {
    const Error = err;
    const mess = 'Redis Client not connected to the server:';
    const message = mess + Error;
    console.log(message);
  });

  client.on('connect', async () => {
    console.log('Redis client connected to the server');
  });
})();
