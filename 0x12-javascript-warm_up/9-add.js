#!/usr/bin/node
/*
 * function that add two integer
 */
function add (a, b) {
  console.log(a + b);
}

// Retrieve command-line arguments
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Check if both arguments are provided
if (arg1 !== undefined && arg2 !== undefined) {
  // Convert arguments to integers
  const a = parseInt(arg1);
  const b = parseInt(arg2);

  // Check if conversion is successful
  if (!isNaN(a) && !isNaN(b)) {
    add(a, b);
  } else {
    console.log('NaN');
  }
} else {
  console.log('NaN');
}
