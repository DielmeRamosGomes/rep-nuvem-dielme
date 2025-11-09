document.querySelectorAll('.image').forEach(image => {
    image.addEventListener('click', () => {
        // Alterna a cor de fundo da imagem clicada
        image.style.backgroundColor = image.style.backgroundColor === 'rgb(255, 99, 71)' ? '#ddd' : 'rgb(255, 99, 71)';
    });
});
