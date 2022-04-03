export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(aamount) {
    this._amount = aamount;
  }

  get amount() {
    return this._amount;
  }

  set currency(acurrency) {
    this._currency = acurrency;
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    // const lp = ' (';
    // const rp = ')';
    const amo = this._amount;
    const spce = ' ';
    // const cur = this._currency;
    const fuck = this.currency.displayFullCurrency();
    return amo + spce + fuck;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
