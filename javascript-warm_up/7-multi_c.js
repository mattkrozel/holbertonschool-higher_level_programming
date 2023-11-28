#!/usr/bin/node

const num = process.argv[2];
if (!isNaN(parseInt(process.argv[2]))) {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
