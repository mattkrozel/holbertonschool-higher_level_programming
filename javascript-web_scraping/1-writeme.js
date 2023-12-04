#!/usr/bin/node
const fs = require('fs');
const fp = process.argv[2];
const content = process.argv[3];
fs.writeFile(fp, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});