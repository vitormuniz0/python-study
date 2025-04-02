# Sistema Bancário Simples em Python

Este é um pequeno projeto desenvolvido durante meus primeiros estudos em Python. Ele simula um sistema bancário simples com as funcionalidades de **depósito**, **saque** e **extrato**.

## 🚀 Funcionalidades

O sistema oferece as seguintes opções para o usuário:

1. **Depositar**: Permite adicionar um valor positivo ao saldo.
2. **Sacar**: Realiza um saque caso haja saldo suficiente e o valor não ultrapasse o limite estabelecido.
3. **Extrato**: Exibe todas as transações realizadas e o saldo atual.
4. **Sair**: Finaliza o programa.

---

## 🔧 Como Executar o Programa

Para rodar o programa, basta copiar o código e executá-lo em um interpretador Python 3.

### **Requisitos:**
- Python 3 instalado no sistema

### **Passo a passo:**
1. Abra um terminal ou prompt de comando
2. Navegue até o diretório onde o arquivo `bank.py` está salvo
3. Execute o comando:
   ```sh
   python bank.py

## 📝 Exemplo de Uso

```sh
[1] Depositar 
[2] Sacar 
[3] Extrato
[4] Sair

=> 1
Informe o valor do depósito: 100
Depósito de R$ 100.00 realizado com sucesso!

=> 2
Informe o valor do Saque: 50
Saque de R$ 50.00 realizado com sucesso!

=> 3
-------EXTRATO--------
Depósito: +R$ 100.00
Saque: -R$ 50.00
----------------------
Saldo atual: R$ 50.00

```

## 📌 Regras de Negócio
- Depósitos devem ser valores positivos.
- O saque deve respeitar o saldo disponível.
- Existe um limite de saque de **R$ 500,00** por transação.
- O usuário pode realizar **no máximo 3 saques** por execução do programa.

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, pude aprender conceitos básicos de Python, como:

- Manipulação de variáveis e tipos de dados
- Uso de estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`while`)
- Formatação de strings com `f-strings`

Este é um dos meus primeiros projetos em Python e ainda há muito a aprender! 🚀