#!
"""Hello World Multi Linguas.
Denpendendo da lingua configurada no ambiente o programa exibe a mensagem cor
respondente.

Como usar:
Tenha a variável LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
#metadados 
__version__ = "0.0.1"
__autor__ = "Magalhaes"
__license__ = "Unlicense"

import os

#dunder = __

#Este Programa imprime Hello World
current_language = os.getenv("LANG")[:5]
#snake_case

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
     msg = "Ciao, Mondo!"
elif current_language == "es_SP":
     msg = "Hola, Mundo!"
elif current_language == "fr_FR":
     msg = "Bonjour Monde"

print(msg)
