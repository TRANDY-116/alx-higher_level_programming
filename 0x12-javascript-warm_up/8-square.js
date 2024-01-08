#!/usr/bin/node
/*
 * script that prints a square
 */
const arg = process.argv[2];

// convert the arg to an integer
const size = parseInt(arg);

// Checking conversiom
if (!isNaN(size)) {
  // outer loop for rows
  for (let i = 0; i < size; i++) {
    let row = '';

    for (let j = 0; j < size; j++) {
      row += 'X';
    }

    console.log(row);
  }
} else {
  console.log('Missing size');
}
