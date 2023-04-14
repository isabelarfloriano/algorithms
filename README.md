# Projeto Algorithms! :desktop_computer::mag:

A Trybe propôs seis desafios que envolvem a resolução e otimização de algoritmos, utilizando conceitos como recursividade e iteratividade, complexidade de tempo e espaço, aplicação de algoritmos de busca e ordenação não nativos do Python, além da realização de testes. Esses desafios podem ser solucionados utilizando a linguagem Python.

<details>
  <summary><strong>Objetivos de prática</strong></summary><br />
    <ul>
      <li>Lógica</li>
      <li>Capacidade de interpretação de problemas</li>
      <li>Capacidade de interpretação de um código legado</li>
      <li>Capacidade de otimizar a resolução de problemas</li>
      <li>Otimizar algoritmos sob pressão</li>
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
├── challenges
│   ├──🔹 challenge_anagrams.py
│   ├──🔸 challenge_encrypt_message.py
│   ├──🔹 challenge_find_the_duplicate.py
│   ├──🔹 challenge_palindromes_iterative.py
│   ├──🔹 challenge_palindromes_recursive.py
│   └──🔹 challenge_study_schedule.py
├── tests
│   ├── encrypt
│   │   ├──🔸 __init__.py
│   │   └──🔹 test_encrypt.py
│   ├──🔸 __init__.py
│   ├──🔸 complexities.py
│   └──🔸 geradores.py
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
  <p>challenges/challenge_study_schedule.py</p>
    <ul>
      <li>O objetivo é determinar quantos estudantes estão online com base nos horários fornecidos em um array de tuplas, em comparação com a hora atual informada.</li>
    </ul>	
  <p>challenges/challenge_palindromes_recursive.py</p>
    <ul>
      <li>Realizar a avaliação recursiva de uma palavra para determinar se ela é um palíndromo.</li>
    </ul>
  <p>challenges/challenge_anagrams.py</p>
    <ul>
      <li>O objetivo é verificar se as palavras fornecidas são anagramas.</li>
    </ul>
  <p>challenge_find_the_duplicate.py</p>
    <ul>
      <li>O desafio consistia em encontrar o número duplicado em um array de números.</li>
    </ul>
  <p>challenge_palindromes_iterative.py</p>
    <ul>
      <li>Realizar a avaliação de uma palavra para determinar se ela é um palíndromo, porém dessa vez utilizando a solução iterativa.</li>
    </ul>
</details>
