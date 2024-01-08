#!/usr/bin/node
/*
 * Notifiies if arguments are passed
 */

const numArg = process.argv.length - 2; // minus 2 to exclude the argument itself

// Print messages based on number of arguments
if (numArg === 0) {
  console.log('No argument');
} else if (numArg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
