    
    var platform = new H.service.Platform({
        'apikey': '{1NH8ekgHy9tHhU6MhlXdJ2DTWCpzjchGvYBxPCtboc4}'
        });
        // Obtain the default map types from the platform object:
        var defaultLayers = platform.createDefaultLayers();
    
        // Instantiate (and display) a map object:
        var map = new H.Map(
            document.getElementById('mapContainer'),
            defaultLayers.raster.normal.map,
            {
                zoom: 11,
                center: { lat: 51.5, lng: 0.011 }
            });
            
            const ui = H.ui.UI.createDefault(map, defaultLayers);
            // The behavior variable implements default interactions for pan/zoom (also on touch devices).
            const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
            // Enable dynamic resizing of the map, based on the current size of the enclosing container
            window.addEventListener('resize', () => map.getViewPort().resize());
            
            /**
            * Returns an instance of H.map.Icon to style the markers
            * @param {number|string} id An identifier that will be displayed as marker label
            *
            * @return {H.map.Icon}
            */
            function getMarkerIcon(id) {
                const svgCircle = `<svg width="30" height="30" version="1.1" xmlns="http://www.w3.org/2000/svg">
                              <g id="marker">
                                <circle cx="15" cy="15" r="20" fill="#0099D8" stroke="#0099D8" stroke-width="4" />
                                <text x="50%" y="50%" text-anchor="middle" fill="#FFFFFF" font-family="Arial, sans-serif" font-size="12px" dy=".3em">${id}</text>
                              </g></svg>`;
                return new H.map.Icon(svgCircle, {
                    anchor: {
                        x: 10,
                        y: 10
                    }
                });
            }
    
            /**
            * Create an instance of H.map.Marker and add it to the map
            *
            * @param {object} position  An object with 'lat' and 'lng' properties defining the position of the marker
            * @param {string|number} id An identifier that will be displayed as marker label
            * @return {H.map.Marker} The instance of the marker that was created
            */
            function addMarker(position, id) {
            const marker = new H.map.Marker(position, {
                data: {
                    id
                },
                icon: getMarkerIcon(id),
            });
    
            map.addObject(marker);
            return marker;
            }
    
    
            const destination = {
                lat: 51.54257,
                lng: -0.01196,
            }; // Mind London
    
            const destinationMarker = addMarker(destination, 'Mind');