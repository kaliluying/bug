/***************************************************************************************************************
||||||||||||||||||||||||||||        CUSTOM SCRIPT FOR ASSURANCE            |||||||||||||||||||||||||||||||||||||
****************************************************************************************************************
||||||||||||||||||||||||||||              TABLE OF CONTENT                  ||||||||||||||||||||||||||||||||||||
****************************************************************************************************************
****************************************************************************************************************
01. Preloader
02. Sticky header
03. mainmenu 
04. Revolution slider
05. scoll to Top
06. Testimonial Slider
07. Sponser Slider
08. Accordion
09. Fact counter 
10. Prealoder
11. Select Dropdown
12. ContactFormValidation


****************************************************************************************************************
||||||||||||||||||||||||||||            End TABLE OF CONTENT                ||||||||||||||||||||||||||||||||||||
****************************************************************************************************************/
"use strict";
        
/*=================== Sticky Header ===================*/
    function stickyHeader () {
        var scroll = $(window).scrollTop();
        if (scroll > 200) {
            $(".mainmenu-area.stick, .header-lower.stick, .header-area.stick").addClass("sticky animated fadeInDown");
            var nav_height = $(".mainmenu-area.stick, .header-lower.stick, .header-area.stick").innerHeight();
            $(".menu-height").css({
                "height": nav_height
            });
        } else if (scroll < 200) {
            $(".mainmenu-area.stick, .header-lower.stick, .header-area.stick").removeClass("sticky animated fadeInDown");
            $(".menu-height").css({
                "height": 0
            });
        }
    }

//====Main menu===
    function mainmenu() {
        //Submenu Dropdown Toggle
        if($('.main-menu li.dropdown ul').length){
            $('.main-menu li.dropdown').append('<div class="dropdown-btn"></div>');
            
            //Dropdown Button
            $('.main-menu li.dropdown .dropdown-btn').click(function() {
                $(this).prev('ul').slideToggle(500);
            });
        }

    }

//===RevolutionSliderActiver===
    function revolutionSliderActiver () {
        if ($('.rev_slider_wrapper #slider1').length) {
            $("#slider1").revolution({
                sliderType:"standard",
                sliderLayout:"auto",
                delay:5000,
                
                navigationType:"bullet",
                navigationArrows:"0",
                navigationStyle:"preview3",
                
                dottedOverlay:'yes',
                
                hideTimerBar:"off",
                onHoverStop:"off",
                navigation: {
                    arrows:{enable:true}
                }, 
                responsiveLevels:[1920,1280,975,600,300],
                gridwidth: [1170, 720, 500, 500, 300],
                gridheight: [650, 600, 550, 450, 400]
            });
        };
    }


//===scoll to Top===
    function scrollToTop() {
        if ($('.scroll-to-target').length) {
            $(".scroll-to-target").click(function() {
                var target = $(this).attr('data-target');
                // animate
                $('html, body').animate({
                    scrollTop: $(target).offset().top
                }, 1000);

            });
        }
    }

//===Testmonial Slider Style 1===
    function testmonialcarousel () {
        if ($('.testmonial-carousel').length) {
            $('.testmonial-carousel').owlCarousel({
                loop:true,
                margin:30,
                nav:true,
                dots: true,
                autoplayHoverPause:true,
                autoplay: 6000,
                smartSpeed: 700,
                responsive:{
                    0:{
                        items:1
                    },
                    600:{
                        items:1
                    },
                    800:{
                        items:2
                    },
                    1024:{
                        items:2
                    },
                    1100:{
                        items:3
                    },
                    1200:{
                        items:3
                    }
                }
            })
        }
    }


//===Sponser Slider Style 2===
    function sponsercarousel () {
        if ($('.sponser-carousel').length) {
            $('.sponser-carousel').owlCarousel({
                loop:true,
                margin:30,
                nav:false,
                dots: false,
                autoplayHoverPause:true,
                autoplay: 6000,
                smartSpeed: 700,
                responsive:{
                    0:{
                        items:1
                    },
                    600:{
                        items:2
                    },
                    800:{
                        items:3
                    },
                    1024:{
                        items:4
                    },
                    1100:{
                        items:4
                    },
                    1200:{
                        items:4
                    }
                }
            })
        }
    }


/*=================== Accordion ===================*/
    function accordion () {
        $(".toggle").each(function(){
            $(this).find('.content').hide();
            $(this).find('h5:first').addClass('active').next().slideDown(500).parent().addClass("activate");
            $('h5', this).click(function() {
                if ($(this).next().is(':hidden')) {
                    $(this).parent().parent().find("h5").removeClass('active').next().slideUp(500).removeClass('animated fadeInUp').parent().removeClass("activate");
                    $(this).toggleClass('active').next().slideDown(500).addClass('animated fadeInUp').parent().toggleClass("activate");
                }
            });
        });
    }

//=== Fact counter ===
    function CounterNumberChanger () {
        var timer = $('.timer');
        if(timer.length) {
            timer.appear(function () {
                timer.countTo();
            })
        }
    }

//=== Select menu === 
    function selectDropdown () {
        if($(".selectmenu").length) {
            $( ".selectmenu" ).selectmenu();
        };
    }


//=== Thm scroll anim===
    function thmScrollAnim() {
        if ($('.wow').length) {
            var wow = new WOW({
                mobile: false
            });
            wow.init();
        };
    }


//=== Contact Form Validation ===
    function ContactFormValidation() {
      if(('.form-sec').length) {
        var form = $('#ajax-contact');
        var formMessages = $('.form-messages');
        $(form).submit(function(e) {
          e.preventDefault();
          var formData = $(form).serialize();
          $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData
          }).done(function(response) {
            $(formMessages).removeClass('error');
            $(formMessages).addClass('success');
            $(formMessages).text(response);
            $(this).find("input").val("");
            $(form).trigger("reset");
          }).fail(function(data) {
            $(formMessages).removeClass('success');
            $(formMessages).addClass('error');
            if (data.responseText !== '') {
              $(formMessages).text(data.responseText);
            } else {
              $(formMessages).text('Oops! An error occured and your message could not be sent.');
            }
          });
        });
    }

}

// Dom Ready Function
    jQuery(document).ready(function () {
        (function ($) {
            // add your functions
            revolutionSliderActiver ();
            mainmenu ();
            testmonialcarousel ();
            sponsercarousel ();
            scrollToTop ();
            CounterNumberChanger ();
            accordion ();
            ContactFormValidation ();
            selectDropdown ();
            thmScrollAnim ();
     
        })(jQuery);
    });

// Scroll Function
    jQuery(window).scroll(function(){
        (function ($) {
        stickyHeader()
        
        })(jQuery);
    });

// Instance Of Fuction while Window Load event
    jQuery(window).load(function() {
        (function($) {
            
        })(jQuery);
    });