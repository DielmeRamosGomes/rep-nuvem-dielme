function MeuBotao() {

    function handleClick() {
        const img = document.createElement('img');
        img.src = '/src/react/imagens/react.png'; // Substitua pela URL da sua imagem
        document.body.appendChild(img);
    }

    return (
        <button id="botao" onClick={handleClick}>Clique aqui para aparecer uma imagem</button>
    );
}



