# Gestão de Contratos Públicos

Projeto Django para gestão completa de contratos públicos com histórico, permissões, filtros e relatórios.

👉 Link da aplicação rodando: **(adicione quando estiver deployado)**

## 💡 Objetivo do sistema

De acordo com a nova lei de licitações e contratos (Lei 14.133/22), deve haver uma clara distinção entre o 
gestor de contrato e o fiscal do contrato com objetivo de evitar fraude e seguindo o princípio da segregação de funções.
Este sistema faz uma clara distinção entre aquele que faz as solicitações(Gestor) e aquele que receber os itens e confima
sua entrega (Fiscal). Outra vantagem é que o orgão pode desgignar uma pessoa responsável para fazer a gestão de todos os 
contratos, como um supervisor de contratos, evitando faltas de bens e serviços, afin de solicitar licitações de forma planejada
evitando situações emergenciais.

## Tecnologias usadas

- python 3.13
- Django 5.2
- PostgreSQL
- FullStack

## Como rodar o projeto localmente? 

~~~~
- Clone esse repositório
    git clone https://github.com/Francelmo87/contrato.git
- Entre na pasta
    cd app
- Crie um virtualenv com Python 3 (use UV preferenciamente)
    uv venv ou
    python3 -m venv .venv
- Ative o virtualenv.
    source .venv/bin/activate 
- Instale as dependências.
    uv add -r ./requirements.txt ou
    pip install -r requirements.txt
- Rode as migrações.
    python manage.py migrate
- Crie um superusuário
    python manage.py createsuperuser
- Rode o projeto
    python manage.py runserver
~~~~

 ## Características

Requisitos funcionais

* Cadastro de contratos, licitação, fornecedores, solicitação de itens do contrato e confirmação de chegada dos itens
* Filtros de contratos
* Cálculo automático da quantidade disponível no contrato para cada item do contrato
* Sistema de login para usuários do sistema – Administrador, Gestor, Fiscal
* Controle de permissões de usuários e/ou grupo, com diferentes níveis de acesso
 * Administrador – Cadastros geral (tudo)
 * Gestor – Solicita os itens do contrato que ele é responsável
 * Fiscal – Confirma se os itens chegaram dos quais ele seja responsável
 * suporte a futuras integrações/ automações

Requisitos não funcionais

* Segurança
* Desempenho	
* Escalabilidade
* Usabilidade
* Mantenabilidade
* Responsividade


## Modelagem do banco de dados
![image](https://github.com/user-attachments/assets/b232351f-609f-4da0-934e-c27659bb5729)

## Projeto (os Dados são fictícios)

### login
![image](https://github.com/user-attachments/assets/24b13708-0a20-4ec1-b34f-4c43489bbae8) digite o seu usuário criado com superuser

### Tela iniicial
![image](https://github.com/user-attachments/assets/e6d5e701-e10d-4486-b65b-d2f8c150605b)

### Àrea do admin
![image](https://github.com/user-attachments/assets/d8741aa4-1035-4806-ad33-d81541077dde) Tela da área administrativa

![image](https://github.com/user-attachments/assets/983a5d0b-a736-42fb-a146-125b22dbbf26) Adiciona a licitção

![image](https://github.com/user-attachments/assets/f433c379-6976-4709-838f-57733a5641b8) Adiciona o fornecedor

### Sistema de Contratos
![image](https://github.com/user-attachments/assets/75ddd687-6083-44e8-931a-69f72d870d2d) Lista de Contratos(Dados ficticios)
![image](https://github.com/user-attachments/assets/069da563-190d-47bc-b089-ce3240e5340e) Cadastrar novo contrato

### Consumo de contrato por meio de solicitações
![image](https://github.com/user-attachments/assets/56524c9f-28a6-4dad-8c18-60ba6cf39a62) Lista de Solicitação

![image](https://github.com/user-attachments/assets/651dcd0b-7f28-451d-b093-0884c2ae1c6f) Detalhes da solicitação

![image](https://github.com/user-attachments/assets/cba6300b-d57b-4431-84f3-1c3e1084fbb4) Fazer a solicitação dos itens do contrato

### Confirmação da entrega
![image](https://github.com/user-attachments/assets/7b4ab4f3-1ebb-48e5-bb72-d97e5b2d9ab9) Lista de pedido solicitados
![image](https://github.com/user-attachments/assets/283ab213-4752-45ca-b96f-d9b3a78f49d9) Confimação de entrega










