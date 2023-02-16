#!/usr/bin/node
//javascript that fetches from a url
$('document').ready(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
      $('div#hello').text(data.hello);
    });
});
