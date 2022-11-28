const $ = window.$;
$(document).ready(() => { 
  $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', (res) => {
    $('DIV#hello').html(`<p>${res.hello}</p>`)
});
});
