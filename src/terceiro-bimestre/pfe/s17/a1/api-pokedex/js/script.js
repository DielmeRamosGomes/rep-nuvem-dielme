const btnBuscarPokemon = document.querySelector('#btn-pokemon');
const inputNomePokemon = document.querySelector('#nome-pokemon');
const idPokemon = document.querySelector('#id-resposta');
const nomePokemon = document.querySelector('#nome-resposta');
const pesoPokemon = document.querySelector('#peso-resposta');
const alturaPokemon = document.querySelector('#altura-resposta');
const imgPokemon = document.querySelector('#img-resposta');

let url_base = 'https://pokeapi.co/api/v2/pokemon/';
btnBuscarPokemon.addEventListener('click', () => {
    buscarPokemon();
});

async function buscarPokemon() {
    let nome = inputNomePokemon.value.trim().toLowerCase();
    let url_completa = url_base + nome;

    fetch(url_completa)
        .then(response => {
            if (!response.ok) {
                throw new Error('Pokémon não encontrado');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            idPokemon.innerText = data.id;
            nomePokemon.innerText = data.name;
            pesoPokemon.innerText = data.weight / 10;
            alturaPokemon.innerText = data.height / 10;
            imgPokemon.src = data.sprites.front_default;
        })
        .catch(error => {
            console.error('Erro ao buscar o Pokémon:', error);
            idPokemon.innerText = 'Não encontrado';
            nomePokemon.innerText = '';
            pesoPokemon.innerText = '';
            alturaPokemon.innerText = '';
            imgPokemon.src = '';
        });
}
