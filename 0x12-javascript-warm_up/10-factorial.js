#!/usr/bin/node
const process = require('process');
function factorial (a) {
  if (a >= 1) {
    return a * factorial(a - 1);
  } else {
    return 1;
  }
}
const number = parseInt(process.argv[2]);
console.log(factorial(number));
