// Definir los colores disponibles
const colors = ["red", "blue", "yellow", "purple", "green"];

// Obtener el botón y agregarle el evento de clic
const changeColorBtn = document.getElementById("changeColorBtn");

changeColorBtn.addEventListener("click", () => {
    // Elegir un color aleatorio de la lista
    const randomColor = colors[Math.floor(Math.random() * colors.length)];
    
    // Cambiar el color de fondo del body
    document.body.style.backgroundColor = randomColor;
});
