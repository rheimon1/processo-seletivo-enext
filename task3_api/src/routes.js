const express = require('express');
const fs = require('fs')

  const routes = express.Router()

  routes.get('/games/:id', (request, response) => {
  const {
    id
  } = request.params;
  let result_game = '';

  const obj = JSON.parse(fs.readFileSync('parser.json', 'utf8'));

  for (let game in obj) {
    if (obj[game].id == id) {
      result_game = obj[game];
    } else {
      continue;
    }
  }

  if (!result_game) {
    return response.json({
      error: 'Jogo não encontrado!'
    });
  } else
    return response.json(result_game)
});

module.exports = routes
