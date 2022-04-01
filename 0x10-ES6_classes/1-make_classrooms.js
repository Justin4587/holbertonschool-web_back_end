import ClassRoom from './0-classroom';

// return array.map((item) => new ClassRoom(item))
export default function InitializeRooms() {
  return [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
}
