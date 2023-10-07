document.addEventListener("DOMContentLoaded", function () {
    const getWeatherButton = document.getElementById("get-weather-button");
    const cityNameInput = document.getElementById("city-name-input");
    const weatherCard = document.getElementById("weather-card");

    getWeatherButton.addEventListener("click", function (e) {
        e.preventDefault();

        const cityName = cityNameInput.value;

        fetch(`/buscar_ciudad?city=${cityName}`)
            .then((response) => response.json())
            .then((data) => {
                if (data && !data.error) {
                    // Los datos están disponibles y no hay errores
                    const weather = data;

                    // Actualizar la "CARD 2" con los datos obtenidos
                    weatherCard.querySelector(".temp").textContent = `${weather.temp}°C`;
                    weatherCard.querySelector(".card-category").textContent = weather.name;
                    weatherCard.querySelector(".humidity").textContent = `${weather.humidity}%`;
                    weatherCard.querySelector(".weather").textContent = weather.weather;
                } else if (data && data.error) {
                    // Se encontró un error en la respuesta
                    console.error("Error al obtener datos del clima:", data.error);
                    alert("Los datos climáticos no están disponibles para la ciudad ingresada.");
                } else {
                    // Error genérico, por ejemplo, si no se puede conectar con el servidor
                    console.error("Error al obtener datos del clima");
                    alert("No se pudo obtener la información del clima para la ciudad ingresada.");
                }
            })
            .catch((error) => {
                // Error en la solicitud
                console.error("Error al obtener datos del clima:", error);
                alert("No se pudo obtener la información del clima para la ciudad ingresada.");
            });
    });
});
