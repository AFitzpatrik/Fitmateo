console.log('map.js loaded');

/* =========================
   CSRF
========================= */
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie) {
        document.cookie.split(';').forEach(cookie => {
            const c = cookie.trim();
            if (c.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(c.slice(name.length + 1));
            }
        });
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

/* =========================
   MAP INIT
========================= */
const map = L.map('map').setView([50.0755, 14.4378], 12);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap'
}).addTo(map);

/* =========================
   MARKER ICONS
========================= */
const markerIcons = {
    kickbox: L.icon({ iconUrl: '/static/markers/KB.svg', iconSize: [40, 60], iconAnchor: [20, 60] }),
    box: L.icon({ iconUrl: '/static/markers/BOX.svg', iconSize: [40, 60], iconAnchor: [20, 60] }),
    mma: L.icon({ iconUrl: '/static/markers/MMA.svg', iconSize: [40, 60], iconAnchor: [20, 60] }),
    muaythai: L.icon({ iconUrl: '/static/markers/MT.svg', iconSize: [40, 60], iconAnchor: [20, 60] }),
    bodybuilding: L.icon({ iconUrl: '/static/markers/BB.svg', iconSize: [40, 60], iconAnchor: [20, 60] }),
    fitness: L.icon({ iconUrl: '/static/markers/FITNESS.svg', iconSize: [40, 60], iconAnchor: [20, 60] }),
};

function getMarkerIcon(type) {
    return markerIcons[type] || markerIcons.fitness;
}

/* =========================
   LOAD PLACES
========================= */
fetch('/api/places/')
    .then(res => res.json())
    .then(data => {
        data.forEach(place => {
            L.marker(
                [place.latitude, place.longitude],
                { icon: getMarkerIcon(place.place_type) }
            )
            .addTo(map)
            .bindPopup(`
                <strong>${place.name}</strong><br>
                ${place.description || ''}
            `);
        });
    });

/* =========================
   ADD PLACE
========================= */
let clickedLat = null;
let clickedLng = null;

map.on('click', function (e) {
    clickedLat = e.latlng.lat.toFixed(6);
    clickedLng = e.latlng.lng.toFixed(6);

    L.popup()
        .setLatLng(e.latlng)
        .setContent(`
            <div style="width:240px">
                <label>Název</label><br>
                <input id="place-name" style="width:100%"><br><br>

                <label>Popis</label><br>
                <textarea id="place-desc" rows="3" style="width:100%"></textarea><br><br>

                <label>Typ místa</label><br>
                <select id="place-type" style="width:100%">
                    <option value="fitness">Fitness</option>
                    <option value="bodybuilding">Bodybuilding</option>
                    <option value="box">Box</option>
                    <option value="kickbox">Kickbox</option>
                    <option value="mma">MMA</option>
                    <option value="muaythai">Muay Thai</option>
                </select><br><br>

                <label>Obrázek</label><br>
                <input id="place-image" type="file"><br><br>

                <label>Tagy</label><br>
                <input id="place-tags" placeholder="#mma #sparring" style="width:100%"><br><br>

                <button id="save-place">Uložit</button>
            </div>
        `)
        .openOn(map);
});

map.on('popupopen', function () {
    const btn = document.getElementById('save-place');
    if (!btn) return;

    btn.onclick = function () {
        const name = document.getElementById('place-name').value.trim();
        if (!name) {
            alert('Vyplň název');
            return;
        }

        const formData = new FormData();
        formData.append('name', name);
        formData.append('description', document.getElementById('place-desc').value);
        formData.append('place_type', document.getElementById('place-type').value);
        formData.append('latitude', clickedLat);
        formData.append('longitude', clickedLng);

        const image = document.getElementById('place-image').files[0];
        if (image) {
            formData.append('image', image);
        }

        document.getElementById('place-tags').value
            .split(' ')
            .map(t => t.replace('#', '').trim())
            .filter(Boolean)
            .slice(0, 10)
            .forEach(tag => formData.append('tags[]', tag));

        fetch('/api/places/create/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: formData
        })
        .then(res => {
            if (!res.ok) throw new Error();
            return res.json();
        })
        .then(place => {
            L.marker(
                [clickedLat, clickedLng],
                { icon: getMarkerIcon(place.place_type) }
            )
            .addTo(map)
            .bindPopup(`
                <strong>${place.name}</strong><br>
                ${place.description || ''}
            `);

            map.closePopup();
        })
        .catch(() => {
            alert('Chyba při ukládání místa');
        });
    };
});
