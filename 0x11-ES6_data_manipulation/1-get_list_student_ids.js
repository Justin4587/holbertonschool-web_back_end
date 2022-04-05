export default function getListStudentIds(stuff) {
  try {
    return stuff.map((stuffmap) => stuffmap.id);
  } catch (E) {
    return [];
  }
}
