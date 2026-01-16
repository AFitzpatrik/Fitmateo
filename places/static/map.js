const map = L.map('map').setView([50.0755, 14.4378], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

fetch('/api/places/')
    .then(response => response.json())
    .then(data => {
        data.forEach(place => {
            const marker = L.marker([place.latitude, place.longitude]).addTo(map);

            marker.bindPopup(`
                <strong>${place.name}</strong><br>
                ${place.description || ''}<br><br>
                ⭐ ${place.average_rating} / 5<br>
                Recenze: ${place.reviews_count}
            `);
        });
    });
