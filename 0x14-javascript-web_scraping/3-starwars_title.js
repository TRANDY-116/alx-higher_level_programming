#!/usr/bin/node
const request = require('request');
const starWarsId = process.argv[2];
const movieUri = 'https://swapi-api.alx-tools.com/api/films/'.concat(starWarsId);

request(movieUri, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
