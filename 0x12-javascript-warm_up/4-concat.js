#!/usr/bin/node
/*
 * a script that prints two arguments passed to it, in the following format: “ is ”
 */
const firstArg = process.argv[2];
const secondArg = process.argv[3];

// Print the fist argument + is + second argument
console.log(firstArg + ' is ' + secondArg);
