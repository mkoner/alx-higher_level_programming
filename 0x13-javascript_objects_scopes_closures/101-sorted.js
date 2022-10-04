#!/usr/bin/node
const data = require('./101-data').dict;
const sorted = {};

Object.keys(data).forEach(key => {
  if (sorted[data[key]] === undefined) sorted[data[key]] = [];
  sorted[data[key]].push(key);
}
);
console.log(sorted);
