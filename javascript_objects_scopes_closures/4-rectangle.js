#!/usr/bin/node
// Class rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w == null || h == null) return null;
    if (w <= 0 || h <= 0) return null;
    this.width = w;
    this.height = h;
  }

  print () {
    const width = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(width);
    }
  }

  rotate () {
    const val = this.width;
    this.width = this.height;
    this.height = val;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
