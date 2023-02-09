#!/usr/bin/node
const url = process.argv.slice(2)[0];
const request = require('request');
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const parsedData = JSON.parse(body);
    const results = parsedData.results;
    let counter = 0;
    results.forEach(result => {
      result.characters.forEach(characterUrl => {
	if (characterUrl.includes('18')) {
          counter++;
	}
      });
    });
    console.log(counter);
  }
});
