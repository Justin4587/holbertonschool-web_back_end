const taskBlock = (trueOrFalse) => {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    let task = true;
    let task2 = false;
    if (task) {
      task2 = false;
    }
    if (task2) {
      task = true;
    }
  }

  return [task, task2];
};

export default taskBlock;
