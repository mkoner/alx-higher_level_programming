const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', (res) => {
  const films = res.results;
  $.each(films, (key, value) => {
    $('UL#list_movies').append(`<li>${value.title}</li>`);
  });
});
