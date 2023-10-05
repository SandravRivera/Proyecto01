document.addEventListener("DOMContentLoaded", function () {
    const getWeatherButton = document.getElementById("get-weather-button");
    let weatherCache = {};

    getWeatherButton.addEventListener("click", function (e) {
        e.preventDefault();

        const cityNameInput = document.getElementById("city-name-input");
        const cityName = cityNameInput.value;

        // Comprobar si los datos ya están en caché
        const cachedWeatherData = getCachedWeatherData(cityName);
        if (cachedWeatherData) {
            updateWeatherCard(cachedWeatherData);
        } else {
            // Realizar una solicitud AJAX a la función Python
            fetch(`/buscar_ciudad?city=${cityName}`)
                .then((response) => response.json())
                .then((data) => {
                    if (data && data.name && data.temp && data.humidity && data.wind) {
                        // Almacenar los datos en caché
                        cacheWeatherData(cityName, data);

                        // Actualizar la "CARD 2" con los datos obtenidos de la API
                        updateWeatherCard(data);
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

    function cacheWeatherData(cityName, data) {
        // Almacenar los datos en caché en el objeto weatherCache
        weatherCache[cityName] = data;
    }

    function getCachedWeatherData(cityName) {
        // Obtener los datos en caché desde el objeto weatherCache
        return weatherCache[cityName];
    }

    function updateWeatherCard(data) {
        const weatherCard = document.getElementById("weather-card");

        // Actualizar la "CARD 2" con los datos obtenidos de la API
        weatherCard.querySelector(".temp").textContent = `${data.temp}°C`;
        weatherCard.querySelector(".card-category").textContent = data.name;
        weatherCard.querySelector(".humidity").textContent = `${data.humidity}%`;
        weatherCard.querySelector(".wind").textContent = `${data.wind} km/h`;
    }
});
