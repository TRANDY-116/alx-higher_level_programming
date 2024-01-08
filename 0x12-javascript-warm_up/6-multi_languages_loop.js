#!/usr/bin/node
/*
 * Write a script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
 *
 * The first line: “C is fun”
 * The second line: “Python is cool”
 * The third line: “JavaScript is amazing”
 * You must use console.log(...) to print all output
 */
const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

for (let i = 0; i < lines.length; i++) {
  console.log(lines[i]);
}
