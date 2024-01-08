#!/usr/bin/node
/*
 * computes and prints a factorial
 */
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const arg = process.argv[2];

const n = parseInt(arg);

// Check if the conversion is successful
if (!isNaN(n)) {
  // Calculate and print the factorial
  const result = factorial(n);
  console.log(`${result}`);
} else {
  console.log('1');
}
