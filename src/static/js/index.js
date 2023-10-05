document.addEventListener("DOMContentLoaded", function () {
    const getWeatherButton = document.getElementById("get-weather-button");

    getWeatherButton.addEventListener("click", function (e) {
        e.preventDefault(); 

        // Obtener el valor ingresado en el campo de búsqueda o la ciudad deseada
        const cityNameInput = document.getElementById("city-name-input"); 
        const cityName = cityNameInput.value;

        updateWeather(cityName); 
    });


    function updateWeather(cityName) {
        const weatherCard = document.getElementById("weather-card");

        // Realizar una solicitud AJAX a la función Python
        fetch(`/buscar_ciudad?city=${cityName}`)
            .then((response) => response.json())
            .then((data) => {
                if (data && data.name && data.temp && data.humidity && data.wind) {
                    // Actualizar la "CARD 2" con los datos obtenidos de la API
                    weatherCard.querySelector(".temp").textContent = `${data.temp}°C`;
                    weatherCard.querySelector(".card-category").textContent = data.name;
                    weatherCard.querySelector(".humidity").textContent = `${data.humidity}%`;
                    weatherCard.querySelector(".wind").textContent = `${data.wind} km/h`;
                } else {
                    console.error("Datos faltantes en la respuesta de la API de OpenWeather");
                    alert("Los datos climáticos no están disponibles para la ciudad ingresada.");
                }
            })
            .catch((error) => {
                console.error("Error al obtener datos del clima:", error);
                alert("No se pudo obtener la información del clima para la ciudad ingresada.");
            });
    }
});
