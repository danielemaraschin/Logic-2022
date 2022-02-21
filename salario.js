var salarioMes = 5000;
var horasTrabalhadasSemana = 36


function horasTrabalhadas() {
    var horasMes = horasTrabalhadasSemana * 4;
    return horasMes;
    
}
 

function valorHora() {
   var horasMes= horasTrabalhadas()
   // var valorHora = 0
   
    var valorHora = salarioMes/horasMes
    return valorHora

}


console.log(valorHora())