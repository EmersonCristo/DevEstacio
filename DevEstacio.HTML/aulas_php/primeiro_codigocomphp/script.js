function buscarDados(){
    fetch('dados.php')
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultado').innerHTML =   `Nome: ${data.nome}, Idade: ${data.idade}`;
        })
        .catch(error => console.error("Erro", error));
}