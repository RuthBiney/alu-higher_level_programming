#!/usr/bin/node
// Class rectangle that defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (w == null || h == null) return null;
    if (w <= null || h <= null) return null;
    this.width = w;
    this.height = h;
  }
}
module.exports = Rectangle;
