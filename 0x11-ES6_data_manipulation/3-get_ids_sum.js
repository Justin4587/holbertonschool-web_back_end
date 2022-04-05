const getStudentIdsSum = (list) => list.reduce((item, num) => item + num.id, 0);
export default getStudentIdsSum;
