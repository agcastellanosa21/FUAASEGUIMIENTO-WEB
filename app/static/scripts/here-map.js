'use strict';

var HereMap = function() {

    var platform;
    var defaultLayers;
    var map;
    var ui;
    var behavior;

    var addMarket = function(localization) {
        // Showing a default Marker on the Map
        const marker = new H.map.Marker({
            lat: localization.latitude,
            lng: localization.longitude
        });

        map.addObject(marker);
    }

    return {
        init: function(zoom) {
            platform = new H.service.Platform({
                'apikey': 'V0R3EObBSStxnX5MgnFl6p76Ip0KMus2VQCZm66HvUQ'
            });

            defaultLayers = platform.createDefaultLayers();

            const lat = '6.152448';
	        const lng = '-75.622995';

	        map = new H.Map(
            document.getElementById('mapContainer'),
            defaultLayers.vector.normal.map,
            {
                zoom: zoom,
                center: { lat: lat, lng: lng }
            });

            window.addEventListener('resize', () => map.getViewPort().resize());
            ui = H.ui.UI.createDefault(map, defaultLayers);
            behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
        },

        addMarket: function(localization) {
            addMarket(localization);
        },

        removeAllMarkets: function() {
            map.removeObjects(map.getObjects ());
        }
    }

}();