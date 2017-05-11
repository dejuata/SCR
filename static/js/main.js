$(document).ready(function() {

  $.uploadPreview({
    input_field: "#id_logo",
    preview_box: "#image-preview",
    label_field: "#image-label",
    label_default: "Elegir imagen",
    label_selected: "Cambiar imagen",
    no_label: false
  });
});
