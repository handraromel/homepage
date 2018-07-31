function regular_map() {
    var var_location = new google.maps.LatLng(-0.81771, 100.3116333);

    var var_mapoptions = {
        center: var_location,
        zoom: 14
    };

    var var_map = new google.maps.Map(document.getElementById("map-container"),
        var_mapoptions);

    var var_marker = new google.maps.Marker({
        position: var_location,
        map: var_map,
        title: "Padang Sarai Permai"
    });
}

// Initialize maps
google.maps.event.addDomListener(window, 'load', regular_map);