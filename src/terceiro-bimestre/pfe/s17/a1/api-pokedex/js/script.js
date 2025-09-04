const btnBuscarPokemon = document.querySelector('#btn-pokemon');
const inputNomePokemon = document.querySelector('#nome-pokemon');
const idPokemon = document.querySelector('#id-resposta');
const nomePokemon = document.querySelector('#nome-resposta');
const pesoPokemon = document.querySelector('#peso-resposta');
const alturaPokemon = document.querySelector('#altura-resposta');
const imgPokemon = document.querySelector('#img-resposta');
const div = document.querySelector('#form-resposta');

let url_base = 'https://pokeapi.co/api/v2/pokemon/';
btnBuscarPokemon.addEventListener('click', buscarPokemon);

function limparUI() {
    div.classList.add('hidden');
    idPokemon.innerText = '';
    nomePokemon.innerText = '';
    pesoPokemon.innerText = '';
    alturaPokemon.innerText = '';
    imgPokemon.src = '';
}

async function buscarPokemon() {
    limparUI();
    let nome = inputNomePokemon.value.trim().toLowerCase();
    if (nome === '') {
        idPokemon.innerText = 'Por favor, digite um nome de um Pokémon'
        return;
    }
    try {
        let url_completa = url_base + nome;
        const response = await fetch(url_completa);

        if (!response.ok) {
            throw new Error('Pokémon não encontrado');
        }

        const data = await response.json();
        alert(data.name);
        idPokemon.innerText = data.id;
        nomePokemon.innerText = data.name;
        pesoPokemon.innerText = data.weight / 10;
        alturaPokemon.innerText = data.height / 10;

        const imagemUrl = data.sprites.front_default || 'https://via.placeholder.com/150';
        imgPokemon.src = imagemUrl;
        
        div.classList.remove('hidden');

    } catch (error) {
        console.error('Erro ao buscar pokémon', error);
    }
}
