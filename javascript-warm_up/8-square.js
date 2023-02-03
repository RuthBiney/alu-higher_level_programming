#!/usr/bin/node
const args = process.argv.slice(2);
// can a first argument be converted to an integer?
if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  const square = 'X'.repeat(parseInt(args[0]));
  for (let i = 0; i < args[0]; i++) {
    console.log(square);
  }
}
