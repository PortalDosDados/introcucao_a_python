# Capítulo 10 ■ Classes e Objetos

A Programação Orientada a Objetos (POO) é um paradigma de desenvolvimento que organiza o software em torno de **dados** e dos **comportamentos** associados a esses dados, modelando entidades do mundo real ou do domínio da aplicação.

---

## 10.1 Classes e Objetos

- **Classe**: Molde ou projeto conceitual que define atributos (características) e métodos (comportamentos).
- **Objeto**: Instância concreta de uma classe, com estado próprio armazenado na memória.

```python
class Televisao:
    def __init__(self, canal_inicial=2):
        self.ligada = False
        self.canal = canal_inicial


tv_sala = Televisao()
print(tv_sala.canal)  # 2
```

---

## 10.2 O Construtor `__init__` e o Parâmetro `self`

- `__init__`: Método especial executado automaticamente no momento em que um novo objeto é instanciado. Usado para inicializar atributos de instância.
- `self`: Referência explícita ao próprio objeto que está executando o método.

---

## 10.3 Métodos de Instância

Funções definidas dentro do corpo da classe que operam sobre os dados (`self`) da instância:

```python
class Televisao:
    def __init__(self, canal_min=2, canal_max=14):
        self.canal = canal_min
        self.min = canal_min
        self.max = canal_max

    def muda_canal_para_cima(self):
        if self.canal < self.max:
            self.canal += 1
        else:
            self.canal = self.min
```

---

## 10.4 Composição e Agregação

Relação onde uma classe contém instâncias de outras classes como atributos (relação "tem um"):

```python
class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.clientes = clientes  # Lista de objetos Cliente
        self.numero = numero
        self.saldo = saldo
```

---

## 10.5 Herança e Polimorfismo

- **Herança**: Permite que uma classe filha (*subclasse*) herde atributos e métodos de uma classe mãe (*superclasse*), promovendo o reúso de código.
- **Polimorfismo**: Capacidade de métodos com o mesmo nome terem comportamentos diferentes em classes distintas da hierarquia.

```python
class Conta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def pode_sacar(self, valor):
        return self.saldo >= valor


class ContaEspecial(Conta):
    def __init__(self, saldo=0, limite=500):
        super().__init__(saldo)
        self.limite = limite

    def pode_sacar(self, valor):
        return (self.saldo + self.limite) >= valor
```
