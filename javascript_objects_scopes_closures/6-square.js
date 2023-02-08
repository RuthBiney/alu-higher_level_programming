#!/usr/bin/node
//Class square that defines a square and inherit from square
const previousSquare = require('./5-square');
class Square extends previousSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
	console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
