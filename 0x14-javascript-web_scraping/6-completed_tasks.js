#!/usr/bin/node
// JS  script that computes the number of tasks completed by user id

const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body);
    let grouped = {};
    results.forEach(result => {
      const uid = result.userId;
      if (!(uid in grouped)) {
        grouped[uid] = {};
        grouped[uid] = 0;
      }
      if (result.completed) {
        grouped[uid]++;
      }
    });
    console.log(grouped);
  }
});
