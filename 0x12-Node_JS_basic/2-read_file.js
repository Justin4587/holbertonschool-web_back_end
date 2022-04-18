const fs = require('fs');
var { parse } = require('csv-parse');
const total = 'Number of students: ';
let clone = [];
var parser = parse({ skip_empty_lines: true }, function (err, student) {
  let students = [];
  students.push(student);
  let totalnum = students[0].length - 1;
  console.log(total + totalnum);
  clone = [ ...students ];

  for (let i = 0; i < students[0].length; i++) {
    console.log(students[0][i][0]);
    console.log(students[0].length);
    //console.log(clone[0][i][i]);
  }
  console.log(clone[0][0][0]);
  console.log(clone[0][0][1]); console.log(clone[0][0][0]);
  console.log(clone[0][2][0]);
});

function countStudents(path) {

  try {
    fs.createReadStream(path).pipe(parser);
    //console.log(parser);
  } catch (E) {
    throw Error('Cannot load the database');
  }
}

//console.log(clone);

module.exports = countStudents;
