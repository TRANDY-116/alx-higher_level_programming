#!/usr/bin/node
/*
 * Write a script that prints x times “C is fun”
 */
const arg = process.argv[2];

// converting the arg to an integer
const intValue = parseInt(arg);

// the C is fun variable
const c = 'C is fun';

// checking the conversion
if (!isNaN(intValue)) {
	for (let i = 0; i < intValue; i++) {
		console.log(c);
	}
} else {
  console.log('Missing number of occurrences');
}
