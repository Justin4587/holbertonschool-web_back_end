export default function getStudentsByLocation(studentList, city) {
  const notEmpty =  studentList.filter((thing) => thing.location === city);
  return notEmpty;
}
