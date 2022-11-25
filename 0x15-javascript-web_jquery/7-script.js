const $ = window.$;
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', (res) => {
  $('DIV#character').html(`<p>${res.name}</p>`);
});
