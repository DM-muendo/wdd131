document.addEventListener('DOMContentLoaded', function () {
  const yearEl = document.getElementById('currentyear');
  const lastModifiedEl = document.getElementById('lastModified');
  const windChillEl = document.getElementById('wind-chill');

  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  if (lastModifiedEl) {
    lastModifiedEl.textContent = 'Last modified: ' + document.lastModified;
  }

  function calculateWindChill(temperature, windSpeed) {
    return 35.74 + 0.6215 * temperature - 35.75 * Math.pow(windSpeed, 0.16) + 0.4275 * temperature * Math.pow(windSpeed, 0.16);
  }

  const temperature = 40;
  const windSpeed = 10;

  if (windChillEl) {
    if (temperature <= 50 && windSpeed > 3) {
      windChillEl.textContent = calculateWindChill(temperature, windSpeed).toFixed(1) + '°F';
    } else {
      windChillEl.textContent = 'N/A';
    }
  }
});
