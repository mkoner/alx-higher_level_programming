#!/usr/bin/node
// JS script that gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(process.argv[3], body, 'utf8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
