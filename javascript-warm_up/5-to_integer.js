#!/usr/bin/node
const args = process.argv.slice(2);
// Can first argument be converted to integer?
if (isNaN(parseInt(args[0]))) {
console.log('Not a number');
} else {
console.log('My number: ' + Number(args[0]));
}
