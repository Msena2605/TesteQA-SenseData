# Teste QA - Sense Data

## Acessar "e-commerce" da saucedemo

Este tutorial tem como objetivo explicar o uso de Selenium com Python para automação de testes com escrita de testes em Gherkin no e-commerce da saucedemo.

## Pré-requisitos

Instalar Python 3.5+

Instalar VSCode e as extensões Cucumber e Python

Instale as dependências necessárias para o projeto de automação (pip install)

Instalar Selenium WebDriver


## Instalação

Execute no terminal os seguintes comandos:

pip install selenium
 
## Executando os testes

1. Crie um arquivo chamado compra.feature dentro da pasta features/bdd. Nele escreveremos nosso teste em Gherkin, uma amostra abaixo.
 
        #language: pt

        Funcionalidade: Fluxo de compra


        Cenario: Login com sucesso

            Dado que o usuário acessa o site da saucedemo

            E preencher o campo "username" com "standard_user"

            E preencher o campo "password" com "secret_sauce"

            Quando clicar no botão de login

            Então deve visualizar a página de produtos

    
2. Na raiz do projeto, crie um arquivo chamado acesso_ecommerce.py, no qual colocaremos as configurações de nosso teste. Executaremos o teste no Chrome, mas o browser pode ser alterado no comando webdriver.Chrome() por outro como o Firefox, Safari ou IE.
Colocaremos nele todos os comandos executados na página do Saucedeme e também os seletores.  
 
 
		from selenium.webdriver.common.by import By

		from selenium import webdriver
		
		import time

		driver = webdriver.Chrome()
		# Inicia o browser chrome, mas pode ser feito com outros como Firefox, Safari e IE
		
		driver.maximize_window()
		# Maximiza a janela do browser ao ser iniciado
		
		driver.get('https://www.saucedemo.com/')
		# acesso à url

		# Seletores dos elementos utilizados na página
		campoUsername = driver.find_element(By.ID, 'user-name').send_keys("standard_user")

		campoPassword = driver.find_element(By.ID, 'password').send_keys("secret_sauce")

		btnLogin = driver.find_element(By.ID, 'login-button').click()

		time.sleep(2)

		btnOrdenarPreco = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div[2]/span/select/option[3]').click()
		
		btnAddCart = driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
		
		btnAddCart2 = driver.find_element(By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)').click()
		
		time.sleep(2)
		
		btnCarrinho = driver.find_element(By.ID, 'shopping_cart_container').click()
		
		btnCheckout = driver.find_element(By.ID, 'checkout').click()

		campoFirstName = driver.find_element(By.ID, 'first-name').send_keys("Wallison")
		
		campoLastName = driver.find_element(By.ID, 'last-name').send_keys("Alves Dantas")
		
		campoPostalCode = driver.find_element(By.ID, 'postal-code').send_keys("58400515")
		
		time.sleep(2)

		btnContinue = driver.find_element(By.ID, 'continue').click()
		
		btnFinish = driver.find_element(By.ID, 'finish').click()
		

3. Finalizada a implementação, basta executar o código na raiz do projeto para rodar os testes no VSCode. O teste será executado e os resultados serão apresentados no próprio terminal.


## Expressões de gratidão
 
 Agraecer à todos da Sense Data pela oportunidade de participar desse teste, e quem venha mais.
