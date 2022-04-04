export default function guardrail(mathFunction) {
  const queue = [];

  try {
    queue.push(mathFunction());
  } catch (Error) {
    queue.push(Error.toString());
  }

  queue.push('Guardrail was processed');
  return queue;
}
