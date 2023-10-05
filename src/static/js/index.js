document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".search");
    const input = document.querySelector("input");
    const weatherCard = document.getElementById("weather-card");

    form.addEventListener("submit", async function (e) {
        e.preventDefault();

        const cityName = input.value;

        try {
            const response = await fetch(`/buscar_ciudad?city=${cityName}`);
            const data = await response.json();

            // Actualizar la "CARD 2" con los datos obtenidos de la API
            weatherCard.querySelector(".temp").textContent = `${data.temp}°C`;
            weatherCard.querySelector(".card-category").textContent = data.name;
            weatherCard.querySelector(".humidity").textContent = `${data.humidity}%`;
            weatherCard.querySelector(".wind").textContent = `${data.wind} km/h`;

        } catch (error) {
            console.error("Error al obtener datos del clima:", error);
            alert("No se pudo obtener la información del clima para la ciudad ingresada.");
        }
    });
});
