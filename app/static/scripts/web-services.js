'use strict';

var WebService = function() {
    var messageDisplayed = false;

    /**
     * This method is used to obtain the locations of all the cars,
     * to later place them on the map. This function is called through an interval that runs every 10 seconds
     */
    var localizeAllCarts = function() {
        $.ajax({
            type: 'GET',
            url: '/localizations',
            cache: false,
            success: function (response) {
                //Clear all markets on the map
                HereMap.removeAllMarkets();

                //Check if the list of locations is empty and
                //if the message has already been displayed
                if(response.length <= 0 && !messageDisplayed) {
                    //Show informational message
                    toastr.info('No hay ubicaciones disponibles.');
                    //The flag is updated to true, so as not to show the message again
                    messageDisplayed = true;
                    return;
                }

                //Update localization for all carts
                response.forEach(function (localization) {
                    HereMap.addMarket(localization);
                });
            },
            error: function (exception) {
                console.error(exception);
                //We verify that the error message has not been displayed
                if(!messageDisplayed) {
                    //Show error message
                    toastr.error('Error al obtener las ubicaciones de los vehículos.');
                    //The flag is updated to true, so as not to show the message again
                    messageDisplayed = true;
                }
            }
        });
    }

    return {
        localizeAllCarts: function() {
            localizeAllCarts();
        }
    }
}();