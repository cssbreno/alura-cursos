- Python usando +
    - Caso você use + entre strings, ele concatena
    - Se você mistura string e numeros, o python não consegue interpretar
    - Se você usa o + em números, ele soma
    - Se você usa o * em números, multiplica, e o mesmo acontece em strings

Uso do f-string:

```python
nome = 'Breno Soares'
altura = 1.69
peso = 65
imc = peso / altura ** 2
# ** (ao quadrado)

linha_1 = f'{nome} tem {altura:.1f} de altura'
# formatação de strings

formato = ''.format(a, b, c)

print(formato)

a = breno
b = soares
c = 23

string = 'b={1} a={0} a={0} c={2:.2f}'
# impressão = soares breno breno 23.00
# usando indices para acessar os objetos
```

- Tudo que vier depois de um parametro nomeado precisa ser nomeado também

```python
formato = string.format(
a, nome2=b, nome3=c
)
# nome2/3 é um parâmetro nomeado e o que vem depois do = é um argumento
# parâmetro = nome da variável / argumento = valor da variável
```

- Função dentro de objeto = método

```python
input('Qual o seu nome? ')
```

Trazer a variável (nome) e o valor dela ⇒ basta colocar {variável=}

A função input retorna uma string

---

## Strings em Python são iteráveis (você pode acessá-los por índice)

```python
nome = Breno
# Para acessar uma string por índice:
print(nome[3]
# saída = n

	# outra alternativa seria usar o in e not in para checar se um elemento está dentro do outro
print('o' in nome)
print('o' not in nome)
```

---

## Fatiamento de string e função len

```python
fatiamento = variável[1:7] # omitir um deles indica que é pra pegar tudo
len # função que pega o tamanho / quantidade
# tem o passo no fatiamento, que seria o [c:f:p] - normalmente o p será 1,
# onde ele pula de 1 em 1
```

---

## Try / Except

Try → tenta executar algum código

Except → ocorreu algum erro ao tentar executar o código (captura o erro)

---

### Constantes, melhores práticas e complexidade de código

Constante = variável que não muda

Letra maiúscula para o que não vai mudar no código

Evitar usar muitos ifs

---

## Armazenamento na memória

Em Python, a depender de alguns fatores, ele vai atribuir o mesmo ID a duas variáveis, ou dois elementos, como por exemplo, no código abaixo:

```python
v1 = 'a'
v2 = 'a'

print(id(v1))
print(id(v2))
```

No caso acima, como ambas as variáveis são do mesmo tipo tem o mesmo valor

---

## Saber se o interpretador passou por alguma parte do código

None = não valor (ausência de valor) // ≠ de 0 e diferente de vazia

Flag ⇒ marcar um local

is e is not = é ou não (tipo, valor, identidade)

id = identidade

---

## Tipos built-in - embutidos (nativos)

https://docs.python.org/pt-br/3.13/library/stdtypes.html

---

## Laços de repetição

While / Break

```python
while condicao:
	print('Verdade')
	# mesma sintaxe do if
```

Repete enquanto a condição for verdadeira

Pode-se usar o break para interromper o laço

```python
numero = 0

while numero<10:
    numero+=1
    print(numero)

print('Chegamos no numero 10')
```

Resultado:

```python
1
2
3
4
5
6
7
8
9
10
Chegamos no numero 10
```

---

## While e continue

Diferente do break, que interrompe o laço, o continue para o laço naquele momento e começa o laço novamente, ignorando o que tiver depois dele no laço

A diferença entre `continue` e `break` dentro de um loop `while` em Python reside na forma como eles alteram o fluxo de execução do loop:

- **`break`**:Python
    - Quando o `break` é encontrado dentro de um loop `while`, ele **interrompe completamente** a execução do loop.
    - O programa sai do loop e continua a execução da primeira instrução que segue o bloco do `while`.
    - Nenhuma iteração restante do loop é executada.
    
    **Exemplo com `break`:**
    
    ```python
    i = 0
    while i < 5:
        print(f"Iteração {i}")
        if i == 2:
            print("Encontrei o 2, saindo do loop com break.")
            break  # O loop será interrompido aqui
        i += 1
    print("Fora do loop.")
    ```
    
    **Saída:**
    
    ```
    Iteração 0
    Iteração 1
    Iteração 2
    Encontrei o 2, saindo do loop com break.
    Fora do loop.
    ```
    
    Nesse exemplo, o loop para quando `i` é 2.
    
- **`continue`**:Python
    - Quando o `continue` é encontrado dentro de um loop `while`, ele **pula a iteração atual** do loop.
    - O restante do código dentro do bloco do `while` para a iteração atual é ignorado.
    - O controle de execução salta para o início da próxima iteração do loop, reavaliando a condição do `while`.
    
    **Exemplo com `continue`:**
    
    ```python
    i = 0
    while i < 5:
        i += 1  # É importante incrementar 'i' antes do 'continue' para evitar loop infinito
        if i == 3:
            print(f"Pulei a iteração quando i é {i} com continue.")
            continue  # O restante do código desta iteração será pulado
        print(f"Processando a iteração {i}")
    print("Fora do loop.")
    ```
    
    **Saída:**
    
    ```
    Processando a iteração 1
    Processando a iteração 2
    Pulei a iteração quando i é 3 com continue.
    Processando a iteração 4
    Processando a iteração 5
    Fora do loop.
    ```
    
    Nesse exemplo, quando `i` é 3, a linha `print(f"Processando a iteração {i}")` é pulada, e o loop continua para a próxima iteração.
    

**Em resumo:**

- **`break`**: Sai do loop *totalmente*.
- **`continue`**: Pula a *iteração atual* e continua para a próxima.


## While e else

- Sempre que um while tem um break dentro dele, o else fora do while não é 
executado
- O roda depois que o while termina sem break
- Pouco usado (não é um recurso comumente utilizado)
- Pouco usado no dia a dia, mas aparece em buscas ou validações

🔹 Quando usar?
- Quando quer fazer algo apenas se o laço completou normalmente, sem break.
- Útil em buscas, autenticações, verificações.
