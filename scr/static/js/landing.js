$(document).ready(function() {
    //Funcion para obtener el scroll
    function getScrolled() {
        try {
          return window.pageYOffset || body.scrollTop || html.scrollTop;
        } catch(exp) {
          return 0;
        }
    }

    //Funcion que me muestra el menu de navegacion cuando hago scroll en la pagina
    $(document).on("scroll", function(event){

        var header = $('.header')
        //Almaceno el desplazamiento actual de la pagina
        var desplazamientoActual = getScrolled();
        console.log(desplazamientoActual)
        //Accedo a la barra de navegación
        var div = $(".header");

        //mostrar navegacion
        if(desplazamientoActual >= 100)
        {
            div.addClass('header-scroll');
            // return;
        }
        else if(desplazamientoActual < 100 && (div.hasClass('header-scroll')))
        {
            div.removeClass('header-scroll');
            // return;
        }
        if(desplazamientoActual > 100 && desplazamientoActual < 300)
        {
            $('.animated-left').addClass('fadeInLeft')
            $('.animated-right').addClass('fadeInRight')
        }
        if(desplazamientoActual > 800)
        {
            $('.services-one').addClass('fadeInLeft')
            $('.services-two').addClass('fadeInUp')
            $('.services-three').addClass('fadeInRight')
        }


        event.preventDefault();
    });

    $(".navbar-option").click( function(event){
        event.preventDefault();

        var posicion = $(this);//almaceno el objeto actual
        console.log(posicion)

       //desplazamiento de la pagina a la seccion seleccionada
        $("html, body").animate({
            scrollTop: $(posicion.attr('href')).offset().top - 50
        }, 1500, 'easeInOutExpo'); //'easeInOutExpo' tipo de animacion


    });

});
