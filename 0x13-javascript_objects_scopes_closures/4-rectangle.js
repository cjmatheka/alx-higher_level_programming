#!/usr/bin/node

// defining the rectangle class
class Rectangle {
  constructor (w, h) {
    if ((w > 0 && Number.isInteger(w)) && (h > 0 && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    } else {
      // Create an empty object if w or h is invalid
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};

module.exports = Rectangle;
