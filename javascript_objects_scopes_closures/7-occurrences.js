#!/usr/bin/node
//A function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  list.forEach(element => {
    if (element === searchElement) {
      occurences++;
    }
  });
  return occurences;
};
