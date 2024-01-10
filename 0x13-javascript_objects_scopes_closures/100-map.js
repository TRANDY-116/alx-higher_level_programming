#!/usr/bin/node

// Scripts that imports an array and computes a new array

const entry = require('./100-data.js');
const oldList = entry.list;
const newList = oldList.map((val, indx) => val * indx);

console.log(oldList);
console.log(newList);
