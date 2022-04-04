export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw Error('cannot divide by 0');
  }
  try {
    const answer = numerator / denominator;
    return answer;
  } catch (Error) {
    return Error;
  }
}
