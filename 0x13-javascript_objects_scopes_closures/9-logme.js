#!/usr/bin/node

// Prints number of args already printed and new arg value.

let numOfArgs = 0;
exports.logMe = function (item) {
  console.log(`${numOfArgs}: ${item}`);
  numOfArgs++;
};
