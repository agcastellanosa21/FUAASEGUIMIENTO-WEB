'use strict';

var WebService = function() {
    var messageDisplayed = false;

    /**
     * This method is used to obtain the locations of all the cars,
     * to later place them on the map. this function is called through an interval that runs every 10 seconds
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

    /**
     * Function to get the updated location and location history of the car
     * and add in the map, this function is called through an interval that runs every 10 seconds
     * @param plaque
     */
    var localizeCart = function(plaque) {
        $.ajax({
            type: 'GET',
            url: '/localization-detail/' + plaque,
            cache: false,
            success: function (response) {
                console.log(response);
                //Clear all markets on the map
                HereMap.removeAllMarkets();

                //Update localization for cart
                if(response.currentLocalization != null && response.currentLocalization != undefined) {
                    HereMap.addMarket(response.currentLocalization);
                }

                //It is verified that the location history is not empty
                if(response.localizationHistory != null && response.localizationHistory.length > 0) {
                    //The table showing location history is cleaned up
                    $('#localizations').empty();
                    //Each of the items in the location history is iterated
                    //and added to the table where the history is displayed
                    response.localizationHistory.forEach(function(value) {

                        $('#localizations')
                        .append(
                            "<tr>" +
                            "   <td class='text-left location-label' width='60%'>" +
                            "       <a class='text-decoration-none'>" + value.latitude + ", " + value.longitude + "</a>" +
                            "   </td>" +
                            "   <td class='text-right location-label' width='40%'>" + value.date.replace('T', ' ') + "</td>" +
                            "</tr>"
                        );
                    });
                }
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
        },

        localizeCart: function (plaque) {
            localizeCart(plaque);
        }
    }
}();