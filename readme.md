## DESAFIO 1 V.1

Fomos contratados por um grande banco para desenvolver o seu novo sitema. Esse banco deseja modernizar suas opeações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: DEPÓSITO, SAQUE e EXTRATO.

**Operação de Depósito**
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depositos devem ser armazenados em uma variável e exibidos na operação de extrato.

**Operação de Saque**
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não é possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

**Operação de Extrato**
Essa operação deve listar is depósitos e saques realizados na conta. No fim da listagen deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, Exemplo: 1500.45 = R$ 1500.45

## DESAFIO 2 V.2

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastras conta bancária.

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: sacar, depositar e visualizar histórico. Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: criar usuário (cliente do banco) e cria conta corrente (vincular com usuário).

Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por você da forma que achar melhor.

-**Saque**
A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_saques. Sugestão de retorno: Saldo e extrato.

-**Depósito**
A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

-**Extrato**
A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

-**Novas Funções**

Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

-**Criar usuário (cliente)**

O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, nro - bairro - cidade/sigla estado. Deve ser armazenado somento os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

-**Criar conta corrente**

O programa deve armazenar contas em uma lista, Uma conta é composta por: Agência número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". Usuário pode ter mais de uma conta mas uma conta pertence a somente um usuário

-**Dica**
Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista