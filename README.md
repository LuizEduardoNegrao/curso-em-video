# Curso de Python do Curso em video
Repositorio criado para por em pratica as ideias, exercicos e logicas estudadas no curso de Python que estou estudando e outras anotações

---

## Tipos Primitivos(basicos)
- int(inteiro/entire) : 1, 2, -9, 10
- float : 0.9, 7.0, 0.000092, 1.9
- bool(boolean) : true or false // verdadeiro ou falso
- str(string) : 'ola', '14', 'cinco5quatro4'

---

## Operadores Aritimeticos:

**Igual `==` é diferente de recebe `=`**

- Adição (`+`) : 5 + 2 == 7
- Subtração (`-`) : 5 - 2 == 3
- Multiplicação (`*`) : 5 x 2 == 10
- Potência (`**`) : 5 elevado 2 == 25
- Divisão (`/`) : 5 / 2 == 2.5
- Divisão Inteira (`//`) : 5 // 2 == 2
- Resto da Divisão (`%`) : 5 % 2 == 1
- Raiz Quadrada (n`**``(1/2)`)

### Ordem de precendência:

- 1: `()` Os parênteses sempre vão ser operados em primeiro
- 2: `**` Em seguida as Potências
- 3: `*` => `/` => `//` => `%` Multiplicação, Divisão, Divisão Inteira e Resto da Divisão respectivamente são as proximas a serem atuadas
- 4: `+` e `-` Adição e Subitrção são as ultimas a serem resolvidas

---

## Utilizando Módulos

Módulos são bibliotecas que contêm funções, classes e variáveis pré-definidas para expandir as capacidades do Python.

### Importação de Módulos
- Importação Completa
```
import math
import random
```
- Importação Específica (Recomendado)
```
from math import sqrt, pow, pi
from random import randint, choice, random
```
- Importação com Alias - as (é apenas uma "encurtação")
```
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```
### Vantagens da Importação Específica
1 - Menos consumo de memória: Carrega apenas o necessário

2 - Código mais limpo: Não precisa usar prefixos

3 - Performance melhorada: Menos overhead de importação

### Módulos Úteis por Categoria
- Matemática e Ciência
```
import math          # Funções matemáticas
import numpy as np   # Computação científica
import statistics    # Estatísticas básicas
```
- Aleatoriedade
```
import random        # Geração de números aleatórios
import secrets       # Para criptografia e segurança
```
Data e Hora
```
import datetime      # Manipulação de datas e horas
import time          # Funções relacionadas ao tempo
```
Sistema e OS
```
import os            # Interação com sistema operacional
import sys           # Configurações do sistema
```
### Boas Práticas
1. Organização de Imports
```
# Imports padrão
import math
import os

# Imports de terceiros
import numpy as np

# Imports locais
from minha_pasta import meus_modulos
```
2. Importação Condicional
```
try:
    import numpy as np
except ImportError:
    print("NumPy não instalado. Use: pip install numpy")
```
3. Verificação de Recursos
```
if hasattr(math, 'sqrt'):
    resultado = math.sqrt(25)
```
### Exemplos Práticos
- Exemplo 1: Matemática
```
from math import sqrt, pi, pow

raio = 5
area = pi * pow(raio, 2)
print(f"Área do círculo: {area:.2f}")
```
- Exemplo 2: Aleatoriedade
```
from random import randint, choice

dado = randint(1, 6)
frutas = ['maçã', 'banana', 'laranja']
sorteio = choice(frutas)
```
- Exemplo 3: Data e Hora
```
from datetime import datetime

agora = datetime.now()
print(f"Data: {agora.strftime('%d/%m/%Y')}")
print(f"Hora: {agora.strftime('%H:%M:%S')}")
```
### Observações Importantes e mais boas práticas
Evite importação completa desnecessária: from module import *

Usar aliases para módulos com nomes longos

Mantenha os imports organizados no topo do arquivo

Documente imports não óbvios

 Instalação de Módulos Externos
```
# Instalar via pip
pip install nome-do-modulo
```
```
# Instalar versão específica
pip install numpy==1.21.0
```
```
# Instalar de requirements.txt
pip install -r requirements.txt
 ```
# Anotações:
```
contatenação: juntar uma string a outra
```
