$(document).ready(function () {
    $("#currencyCarousel").carousel({
      interval: 5000,
    });
  });
  
// Para que funcione la calculadora (igual esto tienen que cambiarlo ustedes para que ande en python)
var vUsdC=19.0043;
var vEurC=21.5561;
var vCanC=20; //var vCanC=N/E;
var vGbpC=24.0181;
var vJpyC=0.1768;

var tiposDeCambio=[1, vUsdC,vEurC,vGbpC, vJpyC, vCanC ];
var simbolos=["MXN", "USD","EUR","GBP", "JPY", "CAD" ];

$(document).ready(function(){

      $("#btn-calcular-divisa").click(function(){
        var monedaOrigen=$("#origen").val();
        var monedaDestino=$("#destino").val();
        var cantidadConverion=$("#campo-cantidad").val();
        var precioPesos=cantidadConverion*tiposDeCambio[monedaOrigen];
        var precioResultado=Math.round(precioPesos/tiposDeCambio[monedaDestino] * 100) / 100;
        $("#contenedor-resultado").html(cantidadConverion+" "+simbolos[monedaOrigen]+ " = " + precioResultado+" "+simbolos[monedaDestino]);
      });
    });