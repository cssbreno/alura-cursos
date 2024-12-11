/* 

alert("Bem vindo (a) ao jogo do número secreto!");
let range = 5;
let numeroSecreto = parseInt(Math.random() * range + 1);
console.log(numeroSecreto);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
  chute = prompt(`Escolha um número entre 1 e ${range}: `);
  if (chute == numeroSecreto) {
    break;
  } else {
    if (chute > numeroSecreto) {
      alert(`Você errou! O número secreto é menor que ${chute}.`);
    } else {
      alert(`Você errou! O número secreto é maior que ${chute}.`);
    }
    tentativas++;
  }
}
let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';

alert(`Parabéns, você descobriu o número secreto (${numeroSecreto}) com ${tentativas} ${palavraTentativa}`);

*/

// --------------------------------- Desafios 1 -------------------------------

//Desafio 1.1
// Mostre um alerta com a mensagem "Boas vindas ao nosso site!".
alert("Boas vindas ao nosso site!");

// Desafio 1.2
// Declare uma variável chamada nome e atribua a ela o valor "Lua".
var nome = "Lua";

// Desafio 1.3
// Crie uma variável chamada idade e atribua a ela o valor 25.
var idade = 25;

// Desafio 1.4
// Defina uma variável numeroDeVendas e atribua a ela o valor 50.
let numeroDeVendas = 50;

// Desafio 1.5
// Defina uma variável saldoDisponivel e atribua a ela o valor 1000.
let saldoDisponivel = 1000;

// Desafio 1.6
// Exiba um alerta com o texto "Erro! Preencha todos os campos"
alert("Erro! Preencha todos os campos");

// Desafio 1.7
// Declare uma variável chamada mensagemDeErro e atribua a ela o valor "Erro! Preencha todos os campos" Agora exiba um alerta com o valor da variável mensagemDeErro.
var mensagemDeErro = "Erro! Preencha todos os campos";
alert(mensagemDeErro);

// Desafio 1.8
// Use um prompt para perguntar o nome do usuário e armazená-lo na variável nome.
let nome = prompt("Digite o seu nome");

// Desafio 1.9
// Peça ao usuário para digitar sua idade usando um prompt e armazene-a na variável idade.
let idade = prompt("Digite sua idade");

// Desafio Final
// Agora, caso a idade seja maior ou igual que 18, exiba um alerta com a mensagem "Pode tirar a habilitação!".
let idade = prompt("Digite sua idade");
let podeTirarCNH =
  idade > 18 ? "Pode tirar a habilitação." : alert(podeTirarCNH);

// ----------------------------------- Desafios 2 --------------

// Desafio 2.1
// Pergunte ao usuário qual é o dia da semana. Se a resposta for "Sábado" ou "Domingo", mostre "Bom fim de semana!". Caso contrário, mostre "Boa semana!".
let diaDaSemana = prompt("Que dia da semana é hoje?");
let validaSemana =
  diaDaSemana == "Sábado" || "Domingo" ? "Bom fim de semana!" : "Boa semana";
alert(validaSemana);

// Desafio 2.2
// Verifique se um número digitado pelo usuário é positivo ou negativo. Mostre um alerta informando.
let numeroDigitado = prompt("Digite um número:");
validaNumero = numeroDeVendas > 0 ? "Número positivo" : "Número negativo";
alert(validaSemana);

// Desafio 2.3
// Crie um sistema de pontuação para um jogo. Se a pontuação for maior ou igual a 100, mostre "Parabéns, você venceu!". Caso contrário, mostre "Tente novamente para ganhar.".
let pontuacao = 2;
resultadoPontuacao =
  pontuacao >= 100 ? "Parabéns, você venceu!" : "Tente novamente para ganhar.";
alert(resultadoPontuacao);

// Desafio 2.4
// Crie uma mensagem que informa o usuário sobre o saldo da conta, usando uma template string para incluir o valor do saldo.
let saldoDaConta = prompt("Informe o valor do seu saldo na conta:");
alert(`O saldo atual da sua conta é ${saldoDaConta}.`);

// Desafio 2.5
// Peça ao usuário para inserir seu nome usando prompt. Em seguida, mostre um alerta de boas-vindas usando esse nome.
let nome = prompt("Informe seu nome");
alert(`Bem vindo (a), ${nome}!`);
