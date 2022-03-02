/*
esta atrasado e pode entrar na aula se for a terceira vez será suspenso, se for menos que isso ai pode entrar sim 


elif else
*/


var numero_de_atrasos = 0;

if (numero_de_atrasos >= 3) {
    console.log('Você está suspenso')
} else if (numero_de_atrasos === 1) {
    console.log('pode entrar, mas se tomar mais 2 atrasos será suspenso.')
} else if (numero_de_atrasos === 2) {
    console.log('pode entrar, mas se tomar mais 1 atraso, será suspenso.')
} else {
    console.log('pode entrar')
}
