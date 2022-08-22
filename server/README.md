# Backend

Aplicação feita com Python 3.10 e Django Rest Framework.


## Documentação da API

#### Retorna todos os produtos.

```http
  GET /api/search
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `term` | `string` | **Obrigatório**. Nome do produto |


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

### SECRET
Tipo: String

Variável de ambiente NECESSARIA para rodar a aplicação.
Link útil: https://djecrety.ir/

Exemplo: 

```
SECRET=e-r22b#!pg#*8u!d%h2gei8pfw@6=^o_iw6bdc_rrgrnau)c7$
```

### DEBUG
Tipo: Boolean

Variavel que controle o DEBUG do Django.

Exemplo:
```
DEBUG=False
```
## Rodando localmente
Entre no diretório do projeto

```bash
  cd server
```

Instale as dependências

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  python manage.py runserver
```