# TestLogin

Documentação do Teste Automatizado
Projeto: Teste Automatizado de Login – CASH PAGO
Tipo: Teste Automatizado
Ferramenta Sugerida: Selenium - Python
 Objetivo
O objetivo deste teste é validar a funcionalidade da tela de login da aplicação CASH PAGO. Será verificado se o usuário consegue realizar o login com credenciais válidas e se mensagens de erro apropriadas são exibidas para credenciais inválidas.
 Pré-requisitos
- Python 3.x instalado https://www.python.org/downloads/
- Selenium WebDriver instalado (`pip install selenium`)
- Navegador Chrome instalado
- ChromeDriver correspondente ao navegador Chrome instalado e no PATH do sistema (Extraia o arquivo chromedriver.exe do chromedriver-win64.zip)

 Cenários de Teste
1. Login com credenciais válidas
   - Dado: Usuário está na página de login
   - Quando: Insere credenciais válidas (usuário e senha) e clica em "Login"
   - Então: Deve ser redirecionado para a página inicial da aplicação
2. Login com credenciais inválidas
   - Dado: Usuário está na página de login
   - Quando: Insere credenciais inválidas (usuário ou senha incorretos) e clica em "Login"
   - Então: Deve ser exibida uma mensagem de erro informando "Usuário ou senha inválidos"
3. Tentativa de login com campos vazios
   - Dado: Usuário está na página de login
   - Quando: Deixa os campos de usuário ou senha vazios e clica em "Login"
   - Então: Deve ser exibida uma mensagem de erro informando "Campos obrigatórios não podem estar vazios"

Configuração e Implementação do Teste Automatizado
 Arquivo de Configuração do Selenium
Arquivo: `test_selenium.py`

Instruções para Execução
1. Certifique-se de que o Python 3.x e o Selenium WebDriver estão instalados.
2. Baixe o ChromeDriver compatível com sua versão do navegador Chrome e adicione-o ao PATH do sistema.
3. Salve o código acima em um arquivo chamado ` test_selenium.py `.
4. Execute o script com o comando: python test_selenium.py
   
Criar um Ambiente Virtual (opcional):
   Para evitar conflitos, você pode criar um ambiente virtual e instalar o Selenium nele: python -m venv myenv
 Ative o ambiente virtual:
    Windows: myenv\Scripts\activate
   Mac/Linux: source myenv/bin/activate
    
Instale o Selenium no ambiente virtual: pip install selenium
Executar o Script no Ambiente Virtual:  python test_selenium.py
![image](https://github.com/QANOW/TestLogin/assets/155574624/d140f85f-55fc-49a5-b408-ab0efb74e5bd)


Grato!!!
