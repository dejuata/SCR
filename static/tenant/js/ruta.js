function initMap() {
   var ruta = new Array();
   var map = new google.maps.Map(document.getElementById('map'), {
     zoom: 6,
     center: {lat: 4.159746996685188, lng: -72.93036419999999}//Colombia
   });
   var directionsService = new google.maps.DirectionsService;
   var directionsDisplay = new google.maps.DirectionsRenderer({
     draggable: true,
     map: map,
     panel: document.getElementById('right-panel')
   });
   directionsDisplay.addListener('directions_changed', function() {
       document.getElementById('linkRuta').value = '';
       computeTotalDistance(directionsDisplay.getDirections());
       computeGeocode(directionsDisplay.getDirections(),ruta);
   });
   if(document.getElementById('origen').value !="" && document.getElementById('destino').value !="" && document.getElementById('linkRuta').value =="")
   {
     var origen = document.getElementById('origen').value;
     var destino = document.getElementById('destino').value;
     displayRoute(origen, destino, directionsService,
       directionsDisplay);
   }
   if(document.getElementById('origen').value !="" && document.getElementById('destino').value !="" && document.getElementById('linkRuta').value !="")
   {
     var routeTxt = document.getElementById('linkRuta').value;
     ruta = routeTxt.split(";");
     var origen = ruta[0];
     var destino = ruta[ruta.length-1]
     var waypts = [];
     for (var i = 1; i < ruta.length-1; i++) {
       waypts.push({
       stopover: true,
       location:{'placeId':ruta[i]}
       });
     }
     displayRouteWaypts(origen, destino, directionsService,
       directionsDisplay, waypts);
   }
 }
 //SE DEFINEN FUNCIONES
 function displayRoute(origin, destination, service, display) {
   service.route({
     origin: origin,
     destination: destination,
     //waypoints: [{location: origin},{location: origin}],
     travelMode: 'DRIVING',
     avoidTolls: true
   },function(response, status) {
     if (status === 'OK') {
       display.setDirections(response);
     } else {
       alert('Could not display directions due to: ' + status);
     }
     });
 }
 function displayRouteWaypts(origin, destination, service, display, waypts) {
   service.route({
     origin: {'placeId':origin},//PARA CONSULTAR
     destination: {'placeId':destination},//PARA CONSULTAR
     waypoints: waypts,//PLACE_ID
     travelMode: 'DRIVING',
     avoidTolls: true
   },function(response, status) {
     if (status === 'OK') {
       display.setDirections(response);
     } else {
       alert('Could not display directions due to: ' + status);
     }
     });
 }
 function computeTotalDistance(result) {
   var total = 0;
   var myroute = result.routes[0];
   for (var i = 0; i < myroute.legs.length; i++) {
     total += myroute.legs[i].distance.value;
   }
   total = total / 1000;
   document.getElementById('kilometros').value = total;
 }
 function computeGeocode(result,ruta) {
   var address;
   var geocoder = new google.maps.Geocoder;
   for (var i = 0; i < result.geocoded_waypoints.length; i++) {
     ruta[i]=result.geocoded_waypoints[i].place_id;
     if(i==result.geocoded_waypoints.length-1)
     {
       document.getElementById('linkRuta').value += result.geocoded_waypoints[i].place_id;
     }
     else
     {
       document.getElementById('linkRuta').value += result.geocoded_waypoints[i].place_id+';';
     }
   }
 }
