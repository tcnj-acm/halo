    new WOW().init();

(function ($) {

   'use strict';

    /*
     * ----------------------------------------------------------------------------------------
     *  SMOTH SCROOL JS
     * ----------------------------------------------------------------------------------------
     */

    $('a.smoth-scroll').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top - 50
        }, 1000);
        e.preventDefault();
    });



    /* ==========================================================================
      COUNTER UP 
 ========================================================================== */

    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });

    $('.carousel').carousel({
      interval: 8000
    });
    
    /* Closes the Responsive Menu on Menu Item Click*/
    $('.navbar-collapse .navbar-nav a').on('click', function () {
        $('.navbar-toggler:visible').click();
    });
    /*END MENU JS*/

    
    /* ----------------------------------------------------------- */
    /*  Fixed header
    /* ----------------------------------------------------------- */


    $(window).on('scroll', function () {
        if ($(window).scrollTop() > 650) {
            $('.site-navigation,.trans-navigation').addClass('header-white');
        } else {
            $('.site-navigation,.trans-navigation').removeClass('header-white');
        }



    });


    /* ==========================================================================
      SCROLL SPY
 ========================================================================== */

    $('body').scrollspy({
        target: '.navbar-collapse',
        offset: 195
    });

})(window.jQuery);
const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
const firstDate = new Date("3/22/2022");
const secondDate = new Date();

const diffDays = Math.round(Math.abs((firstDate - secondDate) / oneDay));
document.getElementById("countdown").innerHTML = diffDays

