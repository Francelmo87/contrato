# Gestão de Contratos Públicos

O objetivo deste projeto visa ter uma gestão de todos os contratos público de um órgão em um sistema web.

## Motivação

De acordo com a nova lei de licitações e contratos (Lei 14.133/22), deve haver uma clara distinção entre o 
gestor de contrato e o fiscal do contrato com objetivo de evitar fraude e seguindo o princípio da segregação de funções.
Este sistema faz uma clara distinção entre aquele que faz as solicitações(Gestor) e aquele que receber os itens e confima
sua entrega (Fiscal). outra vantagem é que o orgão pode desgignar uma pessoa responsável para fazer a gestão de todos os 
contratos, como um supervisor de contratos, evitando faltas de bens e serviços, afin de solicitar licitações de forma planejada
evitando situações emergenciais.

## Tecnologias

- Linguagem: python 3.13
- Framework: django 5.2
-  Desenvolvimento: FullStack

 ## Características

  Requisitos funcionais
    * Cadastro de contratos, licitação, fornecedores, solicitação de itens do contrato e confirmação de chegada dos itens
    * Filtros de contratos
    * Cálculo automático da quantidade disponível no contrato para cada item do contrato
    * Sistema de login para usuários do sistema – Administrador, Gestor, Fiscal
    * Controle de permissões de usuários e/ou grupo, com diferentes níveis de acesso
     ** Administrador – Cadastros geral (tudo)
     ** Gestor – Solicita os itens do contrato que ele é responsável
     ** Fiscal – Confirma se os itens chegaram dos quais ele seja responsável
     ** suporte a futuras integrações/ automações

  Requisitos não funcionais
    * Segurança
    * Desempenho	
    * Escalabilidade
    * Usabilidade
    * Mantenabilidade
    * Responsividade
 
 
 
