#!/usr/bin/node

let fp = process.argv[2];
let fs = require('fs');
fs.readFile(fp, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.tostring());
  }
});
