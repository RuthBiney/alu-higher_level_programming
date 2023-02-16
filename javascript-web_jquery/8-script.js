#!/usr/bin/node
//javascript that fetches and list title
$.get('https://swapi-api.tools.com/api/films/?format=json', function (data) {
    $('ul#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
  });
