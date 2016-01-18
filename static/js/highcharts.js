$(document).ready(function() {
  $.ajax({
    url: "/rango/reclama_datos",
    type: 'get',
    success: function(datos) {
      Visualiza_datos(datos);
    },
    failure: function(datos) {
      alert('esto no vá');
    }
  });
  function Visualiza_datos(datos) {
   var chart = {
      type: 'bar'
   };
   var xAxis = {
      categories: datos[0]
   };
   var yAxis = {
      title: {
         text: 'Bares visitados'
      }
   };


   var series =  [
      {
         name: 'Visitas',
         data: datos[1]
      }
   ];

   var title = {
       text: 'Número de visitas por bar'
   }

   var json = {};

   json.title = title;
   json.chart = chart;
   json.xAxis = xAxis;
   json.yAxis = yAxis;
   json.series = series;

   $('#container').highcharts(json);

 }
});
