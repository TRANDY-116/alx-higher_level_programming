#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const object = process.argv[3];

fs.writeFile(filePath, object, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
});
