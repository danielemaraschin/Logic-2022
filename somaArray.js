const values = [5, 10, 25, 14, 3];
var sumValue = 0;

//soma tem que dar 57

function somaValores(){
    for( var i = 0; i< values.length; i++){
        var valorNoIndex = values[i]; 
        sumValue = valorNoIndex + sumValue;  
    }
}
somaValores()
console.log(sumValue)