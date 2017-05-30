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

  // Inicializacion de la libreria dropzone.js para
  // drag and drog de archivos, este codigo es especifico para
  // la carga masiva de informacion en archivos de excel
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
