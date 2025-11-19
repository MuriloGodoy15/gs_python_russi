# Sistema Russi de Empregos

Este projeto implementa um sistema simples de recomendação de carreiras com base em competências.  
A aplicação roda em modo texto (CLI) e permite cadastrar perfis, registrar suas competências e analisar automaticamente a compatibilidade com quatro carreiras predefinidas.

## Visão Geral

O sistema utiliza três classes principais:

- **comp**  
  Representa uma competência individual, contendo nome, tipo e nível (0–10).

- **perfil**  
  Agrupa várias competências e calcula média de proficiência.

- **carreira**  
  Define exigências e pesos para cada competência, gerando um percentual de compatibilidade com um perfil.

Além disso, a classe **Sistema** gerencia o fluxo geral da aplicação (menu, cadastro e análise).

## Funcionalidades

- Cadastro de perfis com quatro competências:
  - lógica  
  - criatividade  
  - colaboração  
  - adaptabilidade  

- Validação de níveis entre 0 e 10  
- Armazenamento interno dos perfis  
- Análise percentual de compatibilidade para:
  - Dev Software  
  - UX/UI Designer  
  - Analista de Dados  
  - Gerente de Projetos  

- Interface textual simples (CLI)  
- Menu interativo

## Estrutura do Código
class comp
class perfil
class carreira
class Sistema
main → instancia Sistema e chama menu()

## Como Funciona a Análise

Cada carreira possui:

- Uma tabela de **exigências** mínimas por competência  
- Um conjunto de **pesos** que influenciam o cálculo final  

A compatibilidade final é normalizada em porcentagem, permitindo ordenar as carreiras da mais compatível para a menos compatível.

## Como Executar

1. Instale Python 3.
2. Salve o arquivo do projeto em um diretório.
3. Execute no terminal:

```bash
python nome_do_arquivo.py

