#!/usr/bin/node
// prints the first argument
const ArgC = []
let ind
process.argv.forEach((val, index) => {
  ArgC[index] = `${val}`
  ind = `${index}`
})
if (ind < 2) {
  console.log('No argument')
} else {
  console.log(ArgC[2])
}
