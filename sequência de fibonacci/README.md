# Sequência de Fibonacci: 
## Sequência ou Sucessão de Fibonacci 
* Para **n-ésima** posição:
    * 0 para n == 0;
    * 1 para n == 1;
    * f(n-1) + f(n-2) para n >= 2

Nesse exercício podemos ver como o tempo de processamento é afetado com o uso da **Recurssão** e como podemos amenizar esse problema, com a técnica da **Memoização**, quando usando a **Recurssão** .
O programa faz uso de três funções: 
* f_rec(n) ---> função **recursiva** apenas,
* f_mem(n) ---> função **recursiva com memoização**,
* f_it(n) ---> função **iterativa**.

Altere a variável **num** e veja a diferença de tempo de processamento entre elas. Use sempre inteiros positivos e comece com números baixos.  
Dica: A partir de 30, o processamento da função recursiva começa a demorar mais de segundos.
