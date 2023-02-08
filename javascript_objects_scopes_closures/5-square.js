#!/usr/bin/node
const Rectangle = require('./4-rectangle');
//A class square that defines a square and inherit from rectangle
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
