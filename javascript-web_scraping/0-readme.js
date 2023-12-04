#!/usr/bin/node

const fp = process.argv[2];
const fs = require('fs');
fs.readFile(fp, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
