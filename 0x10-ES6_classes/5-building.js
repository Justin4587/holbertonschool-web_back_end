export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    if (this.constructor !== Building && this.evacuationWarningMessage === undefined) {
      throw Error('Class extending Building must overide evacuationWarningMessage');
    }
  }

  get sqft() {
    return this._sqft;
  }
}
