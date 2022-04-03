import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  set floors(floors) {
    this._floors = floors;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    const left = 'Evacuate slowly the ';
    const num = this._floors;
    const right = ' floors';
    return left + num + right;
  }
}
