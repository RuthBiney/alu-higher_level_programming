#!/usr/bin/node
const args = process.argv.slice(2);

function factorial (num) {
  if (num < 1) {
    return 1;
  }
  return num * factorial(num - 1);
}

const num = parseInt(args[0]);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
