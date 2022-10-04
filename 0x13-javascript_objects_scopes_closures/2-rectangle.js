#!/usr/bin/node
// JS script to define a class, initialize values if positive integer
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return this;
    }
  }
}
module.exports = Rectangle;
