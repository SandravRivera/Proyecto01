const weatherIcon = document.querySelector(".weather-icon");
const weatherValue = "{{ data.weather[0].main }}";  

const weatherImageMap = {
    "Clouds": "clouds.png",
    "Clear": "clear.png",
    "Rain": "rain.png",
    "Drizzle": "rain.png",
    "Mist": "mist.png",
    "Haze": "mist.png",
    "Thunderstorm": "thunderstorm.png",
    "Snow": "snow.png",
  };

if (weatherImageMap.hasOwnProperty(weatherValue)) {
    weatherIcon.src = `../static/assets/${weatherImageMap[weatherValue]}`;
} else {
    weatherIcon.src = "../static/assets/else.png";
}