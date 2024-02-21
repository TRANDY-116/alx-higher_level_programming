#!/usr/bin/node
const request = require('request');
const starWarsId = process.argv[2];
const characterId = '18';
let number = 0;

request(starWarsId, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body).results.forEach((movie) => {
      movie.characters.forEach((chars) => {
        if (chars.includes(characterId)) {
          number++;
        }
      });
    });
    console.log(number);
  }
});
