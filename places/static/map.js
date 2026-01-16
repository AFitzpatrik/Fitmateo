console.log('map.js loaded');

document.addEventListener('DOMContentLoaded', function () {

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
            iconUrl: '/static/markers/kickbox.svg',
            iconSize: [40, 60],
            iconAnchor: [20, 60],
            popupAnchor: [0, -60],
        }),
        box: L.icon({
            iconUrl: '/static/markers/box.svg',
            iconSize: [40, 60],
            iconAnchor: [20, 60],
            popupAnchor: [0, -60],
        }),
        mma: L.icon({
            iconUrl: '/static/markers/mma.svg',
            iconSize: [40, 60],
            iconAnchor: [20, 60],
            popupAnchor: [0, -60],
        }),
        muaythai: L.icon({
            iconUrl: '/static/markers/muaythai.svg',
            iconSize: [40, 60],
            iconAnchor: [20, 60],
            popupAnchor: [0, -60],
        }),
        bodybuilding: L.icon({
            iconUrl: '/static/markers/bodybuilding.svg',
            iconSize: [40, 60],
            iconAnchor: [20, 60],
            popupAnchor: [0, -60],
        }),
        fitness: L.icon({
            iconUrl: '/static/markers/fitness.svg',
            iconSize: [40, 60],
            iconAnchor: [20, 60],
            popupAnchor: [0, -60],
        }),
    };

    function getMarkerIcon(placeType) {
        return markerIcons[placeType] || markerIcons.fitness;
    }


    /* =========================
       STARS
    ========================= */

    function renderStars(rating) {
        const fullStars = Math.floor(rating);
        const halfStar = rating % 1 !== 0;
        const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);

        let stars = '';
        for (let i = 0; i < fullStars; i++) stars += '⭐';
        if (halfStar) stars += '✩';
        for (let i = 0; i < emptyStars; i++) stars += '☆';

        return stars;
    }


    /* =========================
       LOAD PLACES
    ========================= */

    function loadPlaces() {
        fetch('/api/places/')
            .then(res => res.json())
            .then(data => {
                data.forEach(place => {
                    const marker = L.marker(
                        [place.latitude, place.longitude],
                        { icon: getMarkerIcon(place.place_type) }
                    ).addTo(map);

                    marker.bindPopup(`
                        <strong>${place.name}</strong><br>
                        ${place.description || ''}<br><br>
                        ${renderStars(place.average_rating)}<br>
                        <small>${place.average_rating} / 5 · ${place.reviews_count} recenzí</small>
                    `);
                });
            });
    }

    loadPlaces();


    /* =========================
       ADD PLACE BY CLICK
    ========================= */

    map.on('click', function (e) {
        const lat = Number(e.latlng.lat.toFixed(6));
        const lng = Number(e.latlng.lng.toFixed(6));

        const name = prompt('Název místa');
        if (!name) return;

        const description = prompt('Popis místa') || '';

        const placeType = prompt(
            'Typ místa:\n' +
            'kickbox / box / mma / muaythai / bodybuilding / fitness'
        );
        if (!placeType) return;

        fetch('/api/places/create/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name,
                description,
                latitude: lat,
                longitude: lng,
                place_type: placeType
            })
        })
        .then(res => res.json())
        .then(place => {
            const marker = L.marker(
                [place.latitude, place.longitude],
                { icon: getMarkerIcon(place.place_type) }
            ).addTo(map);

            marker.bindPopup(`
                <strong>${place.name}</strong><br>
                ${place.description || ''}<br><br>
                ⭐ 0 / 5<br>
                <small>0 recenzí</small>
            `).openPopup();
        });
    });

});
