#!/usr/bin/node
// JS script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const allMovies = JSON.parse(body).results;
    const movies = allMovies.filter(movie => movie.characters.includes('https://swapi-api.hbtn.io/api/people/18/'));
    if (movies.length > 0) {
      console.log(movies.length);
    } else {
      console.log(0);
    }
  }
});
