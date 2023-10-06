document.addEventListener("DOMContentLoaded", function () {
    const getWeatherButton = document.getElementById("get-weather-button");
    const cityNameInput = document.getElementById("city-name-input");
    const weatherCard = document.getElementById("weather-card");

    getWeatherButton.addEventListener("click", function (e) {
        e.preventDefault();
        const cityName = cityNameInput.value;

        fetch(`/searchWeatherWith_NameOfCity?city=${cityName}`)
            .then((response) => response.json())
            .then((data) => {
                if (data && data.weather) {
                    const weather = data.weather;
                    // Actualizar la "CARD 2" con los datos obtenidos
                    weatherCard.querySelector(".temp").textContent = `${weather.temp}°C`;
                    weatherCard.querySelector(".card-category").textContent = weather.name;
                    weatherCard.querySelector(".humidity").textContent = `${weather.humidity}%`;
                    weatherCard.querySelector(".weather").textContent = weather.weather;
                } else {
                    console.error("Datos faltantes en la respuesta de la API de OpenWeather");
                    alert("Los datos climáticos no están disponibles para la ciudad ingresada.");
                }
            })
            .catch((error) => {
                console.error("Error al obtener datos del clima:", error);
                alert("No se pudo obtener la información del clima para la ciudad ingresada.");
            });
    });
});
