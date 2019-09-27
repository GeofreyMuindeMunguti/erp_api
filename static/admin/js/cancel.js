(function($) {
    'use strict';
    $(function() {
        $('.cancel-link').on('click', function(e) {
            e.preventDefault();
            if (window.location.search.indexOf('&_popup=1') === -1) {
<<<<<<< HEAD
                window.history.back(); // Go back if not a popup.
=======
                window.history.back();  // Go back if not a popup.
>>>>>>> 90696d15faae8c0cb87a9190e0c1cc49f55b9f6c
            } else {
                window.close(); // Otherwise, close the popup.
            }
        });
    });
})(django.jQuery);
