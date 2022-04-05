export default function updateStudentGradeByCity(students, city, newGrades) {
  let grade = 'N/A';
  const filtStu = students.filter((student) => student.location === city);
  const newerGrades = filtStu.map((student) => {
    const newGrade = newGrades.filter((thing) => thing.studentId === student.id);
    if (newGrade[0]) {
      grade = newGrade[0].grade;
    }
    return { ...student, grade };
  });
  return newerGrades;
}
