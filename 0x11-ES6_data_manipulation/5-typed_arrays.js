export default function createInt8TypedArray(length, position, value) {
  const buf = new ArrayBuffer(length);
  const view = new DataView(buf);

  try {
    view.setInt8(position, value);
    return view;
  } catch (E) {
    throw Error('Position outside range');
  }
}
