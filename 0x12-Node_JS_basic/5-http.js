const http = require('http');
const countStudents = require('./3-read_file_async.js');
const __CSV = process.argv.slice;
const CSV = __CSV[0]

const hostname = '127.0.0.1';
const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  const { url } = req;

  if (url === '/') {
    res.write('Hello Holberton School!');
  } else if (url === '/students'){
    res.write('This is the list of our students\n');
    try {
      const students = await countStudents(CSV);
      console.log(students);
      res.end(students);
    } catch (E) {
      res.end(E.message);
    }
    
  }

  res.end('Hello Holberton School!');
});
app.listen(port, hostname);
module.exports = app;
