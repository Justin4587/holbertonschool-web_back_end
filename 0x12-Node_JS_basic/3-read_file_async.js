const fs = require('fs');

async function countStudents(path) {
  let data;
  try {
    data = await fs.promises.readFile(path, 'utf8');
  } catch (E) {
    throw new Error('Cannot load the database');
  }
  
  let strngs = data.toString().split('\n');
  strngs = strngs.filter((strng) => strng !== '');
  strngs.shift();
  const total = strngs.length;
  console.log('Number of students: ' + total);

  const csStudents = strngs.filter((strng) => strng.endsWith('CS')).map((strng) => {
    const namesCs = strng.split(',');
    return namesCs[0];
  });

  const cs = 'Number of students in CS: ';
  const cs1 = csStudents.length;
  const cs2 = '. List: ';
  const cs3 = csStudents.join(', ');
  console.log(cs + cs1 + cs2 + cs3);

  
  const sweStudents = strngs.filter((strng) => strng.endsWith('SWE')).map((strng) => {
    const namesSwe = strng.split(',');
    return namesSwe[0];
  });

  const sw = 'Number of students in SWE: ';
  const sw1 = sweStudents.length;
  const sw2 = '. List: ';
  const sw3 = sweStudents.join(', ');
  console.log(sw + sw1 + sw2 + sw3);
};

module.exports = countStudents;
