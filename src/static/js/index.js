document.addEventListener("DOMContentLoaded", function() {
    const getWeatherButton = document.getElementById("get-weather-button");
    const cityNameInput = document.getElementById("city-name-input");
    const weatherCard = document.getElementById("weather-card");

    window.onload = function() {
        cityNameInput.value = '';
      };

    getWeatherButton.addEventListener("click", function (e) {
        e.preventDefault();
        const cityName = cityNameInput.value;

        fetch(`/buscar_ciudad?city=${cityName}`)
            .then((response) => response.json())
            .then((data) => {
                if ("error" in data) {
                    console.error("Error al obtener datos del clima:", data.error);
                    alert(data.error);
                } else {
                    // Actualizar la "CARD 2" con los datos obtenidos
                    weatherCard.querySelector(".temp").textContent = `${data.temp}°C`;
                    weatherCard.querySelector(".name").textContent = data.name;
                    weatherCard.querySelector(".humidity").textContent = `${data.humidity}%`;
                    weatherCard.querySelector(".weather").textContent = data.weather;
                }
            })
            .catch((error) => {
                console.error("Error al obtener datos del clima:", error);
                alert("No se pudo obtener la información del clima para la ciudad ingresada.");
            });
    });
});
