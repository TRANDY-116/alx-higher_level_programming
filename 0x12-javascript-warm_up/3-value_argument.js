#!/usr/bin/node
/*
 * prints the first aruments passed to it
 */
const firstArg = process.argv[2];

// print messages based on argument passed first
if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
