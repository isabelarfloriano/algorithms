# Projeto Algorithms! :desktop_computer::mag:

A Trybe propôs seis desafios que envolvem a resolução e otimização de algoritmos, utilizando conceitos como recursividade e iteratividade, complexidade de tempo e espaço, aplicação de algoritmos de busca e ordenação não nativos do Python, além da realização de testes. Esses desafios podem ser solucionados utilizando a linguagem Python.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
      <li>Trabalhar com `Hashmap` e `Dict`</li>
      <li>Trabalhar com `Set`</li>
    </ul>
</details>
<details>
  <summary><strong>Rodando Localmente a Aplicação</strong></summary><br />
  
  <p>Para executar a aplicação e os testes, siga os passos abaixo:</p>
  <ol>
    <li>Clone o projeto.</li>
    <li>Abra o terminal e navegue até a raiz do projeto.</li>
    <li>Crie o ambiente virtual com o comando <code>python3 -m venv .venv</code>.</li>
    <li>Ative o ambiente virtual com o comando <code>source .venv/bin/activate</code>.</li>
    <li>Instale as dependências com o comando <code>python3 -m pip install -r dev-requirements.txt</code>.</li>
    <li>Para gerar os relatórios via linha de comando, instale a dependência da linha de comando com o comando <code>pip install .</code>.</li>
    <li>Para executar todos os testes, execute o comando <code>python3 -m pytest</code> na raiz do projeto.</li>
  </ol>
</details>
<details>
  <summary><strong>Estrutura do Projeto</strong></summary><br />

  ```
.
├── data
│   ├──🔹 mkt_campaign.txt
│   ├──🔸 orders_1.csv
│   └──🔸 orders_2.csv
├── src
│   ├──🔹 analyze_log.py
│   ├──🔹 inventory_control.py
│   ├──🔸 main.py
│   └──🔹 track_orders.py
├── tests
│   └── 🔸__init__.py
├── 🔸dev-requirements.txt
├── 🔸pyproject.toml
├── 🔹README.md
├── 🔸requirements.txt
├── 🔸setup.cfg
└── 🔸setup.py
  
    Legenda:
  🔸Arquivos de propriedade intelectual da Trybe
  🔹Arquivos desenvolvidos por mim
  ```
</details>
<details>
  <summary><strong>Detalhes dos Desafios</strong></summary><br />
  <p>src/analyze_log.py</p>
    <ul>
      <li>A função lê os arquivos que contêm as informações dos pedidos realizados e gera o relatório solicitado.</li>
    </ul>	
  <p>src/track_orders.py</p>
    <ul>
      <li>Classe que simula um sistema de registro contínuo das informações de pedidos</li>
    </ul>
  <p>src/inventory_control.py</p>
    <ul>
      <li>Classe de gerenciamento do estoque de um estabelecimento</li>
    </ul>
</details>
