const nombre = document.getElementById("nombre");
const error = document.getElementById("errornombre");
const enviar = document.querySelector("#enviar");

enviar.addEventListener("click", (evento) => {
    evento.preventDefault();
    if (nombre.value.trim() === "") {
        error.textContent = "El campo nombre es obligatorio";
        error.classList.add("error");
    } else {
        error.classList.remove("error");
        alert("Éxito");
    }
});
