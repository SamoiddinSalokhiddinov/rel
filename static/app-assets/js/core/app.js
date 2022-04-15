/*=========================================================================================
  File Name: app.js
  Description: Template related app JS.
  ----------------------------------------------------------------------------------------
  Item Name: Frest HTML Admin Template
  Version: 1.0
  Author: Pixinvent
  Author URL: hhttp://www.themeforest.net/user/pixinvent
==========================================================================================*/

(function (window, document, $) {
  "use strict"
  var $html = $("html")
  var $body = $("body")

  function scrollTopFn() {
    var $scrollTop = $(window).scrollTop();
    if ($scrollTop > 20) {
      $("body").addClass("page-scrolled navbar-scrolled");
    }
    else {
      $("body").removeClass("page-scrolled navbar-scrolled");
    }
  }
  $(window).on('scroll', function () {
    scrollTopFn();
  });

  $(window).on("load", function () {
    var rtl
    var compactMenu = false // Set it to true, if you want default menu to be compact

    if ($body.hasClass("menu-collapsed")) {
      compactMenu = true
    }

    if ($("html").data("textdirection") == "rtl") {
      rtl = true
    }

    setTimeout(function () {
      $html.removeClass("loading").addClass("loaded")
    }, 1200)

    $.app.menu.init(compactMenu)

    // Livioncs are initialized for vertical menu
    $.each($(".menu-livicon"), function (i) {
      var $this = $(this),
        icon = $this.data("icon"),
        iconStyle = $("#main-menu-navigation").data("icon-style")

      $this.addLiviconEvo({
        name: icon,
        style: iconStyle,
        duration: 0.85,
        strokeWidth: "1.3px",
        eventOn: "none",
        strokeColor: menuIconColorsObj.iconStrokeColor,
        solidColor: menuIconColorsObj.iconSolidColor,
        fillColor: menuIconColorsObj.iconFillColor,
        strokeColorAlt: menuIconColorsObj.iconStrokeColorAlt,
        afterAdd: function () {
          if (i === $(".main-menu-content .menu-livicon").length - 1) {
            // When hover over any menu item, start animation and stop all other animation
            $(".main-menu-content .nav-item a").on("mouseenter", function () {
              if ($(".main-menu-content .menu-livicon").length) {
                $(".main-menu-content .menu-livicon").stopLiviconEvo()
                $(this)
                  .find(".menu-livicon")
                  .playLiviconEvo()
              }
            })
          }
        }
      })
    })

    function updateLivicon(el) {
      el.updateLiviconEvo({
        strokeColor: menuActiveIconColorsObj.iconStrokeColor,
        solidColor: menuActiveIconColorsObj.iconSolidColor,
        fillColor: menuActiveIconColorsObj.iconFillColor,
        strokeColorAlt: menuActiveIconColorsObj.iconStrokeColorAlt
      })
    }


  })



  // Header Notification Dropdown Remains Opened on click of switch Label

})(window, document, jQuery)

