export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  [Symbol.toPrimitive](word) {
    if (word === 'number') {
      return this._size;
    }
    if (word === 'string') {
      return this._location;
    }
    return this;
  }
}
