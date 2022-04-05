export default function updateStudentGradeByCity(students, city, newGrades) {
  let wierd = 'N/A';
  const filtStu = students.filter((student) => student.location === city);
  const newerGrades = filtStu.map((student) => {
    const newGrade = newGrades.filter((thing) => thing.studentId === student.id);
    if (newGrade[0]) {
      wierd = newGrade[0].grade;
    }
    return { ...student, wierd };
  });
  return newerGrades;
}
