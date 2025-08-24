const imagenPrincipal = document.getElementById("imagen-principal");
const miniaturas = document.querySelectorAll(".miniatura");

// A cada Imagen le hacemos un evento de clic
miniaturas.forEach((miniatura) => {
    miniatura.addEventListener("click", () => {
        // Hago clic en la imagen y cambiaria
        imagenPrincipal.src = miniatura.src;
    });
});
