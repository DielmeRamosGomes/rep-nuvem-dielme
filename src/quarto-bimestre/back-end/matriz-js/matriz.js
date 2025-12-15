
function criarMatriz(dim_linha, dim_coluna) {
    let matriz = [];
    for (let i = 0; i < dim_linha; i++) {
        matriz[i] = [];
        for (let j = 0; j < dim_coluna; j++) {
            matriz[i][j] = 0;
        }
    }
    return matriz;
}

function imprimeMatriz(dim_linha, dim_coluna, matriz) {
    for (let i = 0; i < dim_linha; i++) {
        let row = "";
        for (let j = 0; j < dim_coluna; j++) {
            row += matriz[i][j] + " ";
        }
        console.log(row);
    }
}

//imprimeMatriz(5, 5, criarMatriz(5, 5));

function matrizAleatoria(dim_linha, dim_coluna) {
    let matriz = criarMatriz(dim_linha, dim_coluna);
    for (let i = 0; i < dim_linha; i++) {
        for (let j = 0; j < dim_coluna; j++) {
            matriz[i][j] = Math.floor(Math.random() * 10);
        }
    }
    return matriz;
}

let matriz = matrizAleatoria(5, 5);
imprimeMatriz(5, 5, matriz);



