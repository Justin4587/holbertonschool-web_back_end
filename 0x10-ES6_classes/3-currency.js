export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  set code(acode) {
    this._code = acode;
  }

  get code() {
    return this._code;
  }

  set name(aname) {
    this._name = aname;
  }

  get name() {
    return this._name;
  }

  displayFullCurrency() {
    const lp = ' (';
    const rp = ')';
    const nam = this._name;
    const cod = this._code;
    return nam + lp + cod + rp;
  }
}
