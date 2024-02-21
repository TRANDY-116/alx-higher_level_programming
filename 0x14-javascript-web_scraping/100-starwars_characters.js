#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
  process.exit(1);
}

const starWarsId = `https://swapi-api.hbtn.io/api/films/${url}`;

request(starWarsId, function (err, res, body) {
  if (err) {
    console.log(err);
    return;
  }
  const characters = JSON.parse(body).characters;

  for (let i = 0; i < characters.length; ++i) {
    request(characters[i], function (error, response, _body) {
      if (error) {
        console.log(error);
        return;
      }
      console.log(JSON.parse(_body).name);
    });
  }
});
