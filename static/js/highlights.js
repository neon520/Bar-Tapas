$(document).ready(function(){  # de  jquery, se ejecuta cuando se carga la página
  alert("hola")
  $.ajax({
		url: "/reclama_datos",
		type: 'get',
		success: function(datos) {
			Visualiza_datos(datos);
		},
		failure: function(datos) {
			alert('esto no vá');
		}
	});

	function Visualiza_datos(datos) {

    $('#container').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Número de visitas por bar'
        },
        xAxis: {
            categories: datos[0]
        },
        yAxis: {
            title: {
                text: 'Bares visitados'
            }
        },
        series:[{
          name:'Visitas',
          data: datos[1]
        }],
    });

	};

});
