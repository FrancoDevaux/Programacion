let contador = 0;
const numero = document.getElementById("numero");
const sumar = document.getElementById("sumar");
const restar = document.getElementById("restar");
const reiniciar = document.getElementById("reiniciar");

sumar.addEventListener("click", () => {
    contador++;
    numero.textContent = contador;
});

restar.addEventListener("click", () => {
    contador--;
    numero.textContent = contador;
});

reiniciar.addEventListener("click", () => {
    contador = 0;
    numero.textContent = contador;
});
