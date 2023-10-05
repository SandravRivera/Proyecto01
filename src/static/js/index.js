document.addEventListener("DOMContentLoaded", function () {
    const getWeatherButton = document.getElementById("get-weather-button");

    getWeatherButton.addEventListener("click", function (e) {
        e.preventDefault();

        const cityName = input.value; 
        updateWeather(cityName); 
    });

    // Función para obtener y mostrar el clima
    function updateWeather(cityName) {
        const weatherCard = document.getElementById("weather-card");

        // Realizar una solicitud AJAX a la función Python
        fetch(`/buscar_ciudad?city=${cityName}`)
            .then((response) => response.json())
            .then((data) => {
                // Actualizar la "CARD 2" con los datos obtenidos de la API
                weatherCard.querySelector(".temp").textContent = `${data.temp}°C`;
                weatherCard.querySelector(".card-category").textContent = data.name;
                weatherCard.querySelector(".humidity").textContent = `${data.humidity}%`;
                weatherCard.querySelector(".wind").textContent = `${data.wind} km/h`;
            })
            .catch((error) => {
                console.error("Error al obtener datos del clima:", error);
                alert("No se pudo obtener la información del clima para la ciudad ingresada.");
            });
    }
});
