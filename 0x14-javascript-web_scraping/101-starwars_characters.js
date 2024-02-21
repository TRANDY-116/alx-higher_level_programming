#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  process.exit(1);
}

const starWarsURL = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(starWarsURL, function (err, res, body) {
  if (err) {
    console.error('Error', err);
    return;
  }
  const filmData = JSON.parse(body);
  const characters = filmData.characters;
  function printCharacterNames (index) {
    if (index >= characters.length) {
      return;
    }

    request(characters[index], function (error, response, charBody) {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      printCharacterNames(index + 1);
    });
  }
  printCharacterNames(0);
});
