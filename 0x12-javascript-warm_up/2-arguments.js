#!/usr/bin/node
const argL = process.argv.length

if (argL < 3) {
  console.log('No argument')
} else if (argL === 3) {
  console.log('Arguement found')
} else {
  console.log('Argument Found')
}
