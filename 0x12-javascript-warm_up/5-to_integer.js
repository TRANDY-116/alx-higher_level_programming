#!/usr/bin/node
/*
 * script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
 *
 * If the argument can’t be converted to an integer, print “Not a number”
 */
const arg = process.argv[2];

// converting the arg to an integer
const intValue = parseInt(arg);

// Check if the conversion was successful
if (!isNaN(intValue)) {
  console.log('My number: ' + intValue);
} else {
  console.log('Not a number');
}
