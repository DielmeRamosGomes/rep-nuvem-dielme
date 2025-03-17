const pokemonList = document.getElementById('pokemon-list');

async function fetchPokemon(id) {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`);
    const data = await response.json();
    return data;
}

async function displayPokemon(id) {
    const pokemon = await fetchPokemon(id);

    const card = document.createElement('div');
    card.classList.add('pokemon-card');

    const name = document.createElement('h2');
    name.textContent = pokemon.name;

    const image = document.createElement('img');
    image.src = pokemon.sprites.front_default;

    card.appendChild(name);
    card.appendChild(image);
    pokemonList.appendChild(card);
}

// Exibe os primeiros 10 Pokémons (você pode ajustar este número)
for (let i = 1; i <= 10; i++) {
    displayPokemon(i);
}

 // http://127.0.0.1:5500/src/index.html







