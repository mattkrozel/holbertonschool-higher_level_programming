#!/usr/bin/node
const req = require('request');
const url = process.argv[2];
req(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    console.log(films.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
