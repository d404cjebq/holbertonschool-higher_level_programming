#!/usr/bin/node
fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    document.querySelector('#hello').textContent = data.hello;
  })
  .catch(function (error) {
    console.error('Error fetching hello:', error);
  });
  