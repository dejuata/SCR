// Animacion para turbolinks
$(document).on('turbolinks:request-start', function(){
  $('#content').addClass('fadeOut');
})
$(document).on('turbolinks:render', function(){
  $('#content').addClass('fadeOut');
  $('#content').removeClass();
  $('#content').addClass('fadeIn');
})

// Cuando el DOM esta cargado
$(document).ready(function() {

  // Visualizar imagen al momento de cargarla
  // por medio de la libreria uploadPreview
  $.uploadPreview({
    input_field: "#id_logo",
    preview_box: "#image-preview",
    label_field: "#image-label",
    label_default: "Elegir imagen",
    label_selected: "Cambiar imagen",
    no_label: false
  });

  $(".alert").fadeIn("slow").delay(2000).fadeOut("slow");
  $('.datepicker').pikaday({ firstDay: 1 });
  $('#id_file').addClass('inputfile');

  function tabActive(id){
    $('.active').removeClass('active');
    $(id).addClass('active')
  }

  // Configuracion de la libreria dropzone.js
  // para subir archivos drap and drop
  Dropzone.options.upload = {
    // Prevents Dropzone from uploading dropped files immediately
    autoProcessQueue : false,
    uploadMultiple: false,
    maxFilesize: 5,
    maxFiles:	1,
    addRemoveLinks: true,
    acceptedFiles: '.xls,.xlsx',
    dictDefaultMessage: 'Arrastra los archivos aqui para subirlos',

    init : function() {
        var submitButton = $("#upload-submit")
        myDropzone = this;

        submitButton.click(function() {
            myDropzone.processQueue();

        });
        // You might want to show the submit button only when
        // files are dropped here:
        this.on("addedfile", function() {
            $('#upload-submit').removeClass('hide')
        });

    },

    success: function(request){
      this.on("complete", function(file) {
        myDropzone.removeFile(file);
      });
      // Cerrar el modal
      $('#modalUpload').modal('hide')
      console.log(request)
    }
  };

});
