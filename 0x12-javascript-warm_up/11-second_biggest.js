#!/usr/bin/node
const process = require('process');
const nums = process.argv.slice(2).map((x) => {
  return parseInt(x);
});

if (nums.length <= 1) {
  console.log(0);
} else {
  console.log(nums.sort((a, b) => {
    return b - a;
  })[1]);
}
