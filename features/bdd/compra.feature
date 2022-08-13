# language: pt

Funcionalidade: Fluxo de compra
Para ter acesso ao sistema
O usuario do saucedemo
Deseja logar no site
Escolher o/os produto/produtos
E finalizar o pedido de compra

  Cenario: Login com sucesso
    Dado que o usuário acessa o site da saucedemo
    E preencher o campo "username" com "standard_user"
    E preencher o campo "password" com "secret_sauce"
    Quando clicar no botão de login
    Então deve visualizar a página de produtos

  Cenario: Comprar produto
    Dado que o usuário se encontra na página de produto
    E clicar no botão para ordenação
    E clicar no produto que deseja
    Quando clicar no carrinho de compras
    Então deve visualizar a página de descrição do produto

  Cenario: Checkout do pedido
    Dado que o usuário se encontra na página de descrição do pedido
    E clicar no botão "checkout"
    Então deve visualizar a página de preenchimento de seus dados

  Cenario: Preencher dados pessoais
    Dado que o usuário se encontra na página de preenchimento de seus dados
    E preencher o campo "First Name"
    E preencher o campo "Last Name"
    E preencher o campo "Zip/Postal Code" 
    Quando clicar no botão "continue"
    Então deve visualizar a página de finalização do pedido

  Cenario: Pedido realizado com sucesso
    Dado que o usuário se encontra na página de finalização do pedido
    Quando clicar no botão "finish"
    Então deve visualizar a mensagem "obrigado pelo seu pedido"
