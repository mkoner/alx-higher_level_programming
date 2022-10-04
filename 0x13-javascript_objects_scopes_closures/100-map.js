#!/usr/bin/node
const data = require('./100-data').list;
const mapped = data.map(function (value, index) { return value * index; });
console.log(data);
console.log(mapped);
