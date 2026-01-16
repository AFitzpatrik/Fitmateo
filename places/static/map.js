console.log('map.js loaded');

/* =========================
   MAP INIT
========================= */

const map = L.map('map').setView([50.0755, 14.4378], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);


/* =========================
   SVG ICONS
========================= */

const markerIcons = {
    kickbox: L.icon({
        iconUrl: '/static/markers/KB.svg',
        iconSize: [40, 60],
        iconAnchor: [20, 60],
    }),
    box: L.icon({
        iconUrl: '/static/markers/BOX.svg',
        iconSize: [40, 60],
        iconAnchor: [20, 60],
    }),
    mma: L.icon({
        iconUrl: '/static/markers/MMA.svg',
        iconSize: [40, 60],
        iconAnchor: [20, 60],
    }),
    muaythai: L.icon({
        iconUrl: '/static/markers/MT.svg',
        iconSize: [40, 60],
        iconAnchor: [20, 60],
    }),
    bodybuilding: L.icon({
        iconUrl: '/static/markers/BB.svg',
        iconSize: [40, 60],
        iconAnchor: [20, 60],
    }),
    fitness: L.icon({
        iconUrl: '/static/markers/FITNESS.svg',
        iconSize: [40, 60],
        iconAnchor: [20, 60],
    }),
};

function getMarkerIcon(type) {
    return markerIcons[type] || markerIcons.fitness;
}


/* =========================
   LOAD PLACES
========================= */

fetch('/api/places/')
    .then(r => r.json())
    .then(data => {
        data.forEach(place => {
            L.marker(
                [place.latitude, place.longitude],
                { icon: getMarkerIcon(place.place_type) }
            )
            .addTo(map)
            .bindPopup(`<strong>${place.name}</strong><br>${place.description || ''}`);
        });
    });


/* =========================
   ADD PLACE
========================= */

map.on('click', function (e) {

    const lat = e.latlng.lat;
    const lng = e.latlng.lng;

    const html = `
        <div id="popup-form">
            <label>Název</label><br>
            <input id="name"><br><br>

            <label>Popis</label><br>
            <textarea id="desc"></textarea><br><br>

            <label>Typ místa</label><br>
            <select id="type">
                <option value="fitness">Fitness</option>
                <option value="bodybuilding">Bodybuilding</option>
                <option value="box">Box</option>
                <option value="kickbox">Kickbox</option>
                <option value="mma">MMA</option>
                <option value="muaythai">Muay Thai</option>
            </select><br><br>

            <button id="save">Uložit</button>
        </div>
    `;

    L.popup()
        .setLatLng(e.latlng)
        .setContent(html)
        .openOn(map);

    // ⬇️ TADY JE KLÍČ
    setTimeout(() => {

        const btn = document.getElementById('save');
        const form = document.getElementById('popup-form');

        // zabráníme klikům padat na mapu
        L.DomEvent.disableClickPropagation(form);

        btn.onclick = function (ev) {
            ev.preventDefault();
            ev.stopPropagation();

            const name = document.getElementById('name').value.trim();
            const desc = document.getElementById('desc').value.trim();
            const type = document.getElementById('type').value;

            if (!name) {
                alert('Vyplň název');
                return;
            }

            fetch('/api/places/create/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    name,
                    description: desc,
                    latitude: lat,
                    longitude: lng,
                    place_type: type
                })
            })
            .then(r => {
                console.log('POST STATUS', r.status);
                return r.json();
            })
            .then(place => {
                L.marker(
                    [place.latitude, place.longitude],
                    { icon: getMarkerIcon(place.place_type) }
                )
                .addTo(map)
                .bindPopup(`<strong>${place.name}</strong><br>${place.description}`)
                .openPopup();

                map.closePopup();
            })
            .catch(err => {
                console.error(err);
                alert('Chyba při ukládání');
            });
        };

    }, 0);
});
