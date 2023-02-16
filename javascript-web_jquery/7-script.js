#!/usr/bin/node
// javascript that fetches the character name
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data)  {
    $('div#character').text(data.name);
  });
