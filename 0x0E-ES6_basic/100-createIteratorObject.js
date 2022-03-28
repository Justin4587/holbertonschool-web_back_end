const createIteratorObject = (report) => {
  const { allEmployees } = (report);
  const array = [];

  for (const key of Object.keys(allEmployees)) {
    array.push(...allEmployees[key]);
  }
  return array;
};

export default createIteratorObject;
