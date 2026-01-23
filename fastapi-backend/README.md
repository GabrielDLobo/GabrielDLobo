# FastAPI Backend Project

Um projeto backend completo utilizando Python e FastAPI com todas as melhores práticas.

## 🚀 Características

- **FastAPI** - Framework web moderno e de alta performance
- **SQLAlchemy** - ORM para interação com banco de dados
- **Pydantic** - Validação de dados e configurações
- **JWT Authentication** - Sistema de autenticação seguro
- **PostgreSQL** - Banco de dados relacional (com suporte para SQLite em desenvolvimento)
- **Docker** - Containerização da aplicação
- **CORS** - Configuração para Cross-Origin Resource Sharing
- **Alembic** - Migrações de banco de dados

## 📋 Pré-requisitos

- Python 3.11+
- Docker e Docker Compose (opcional, para execução em container)
- PostgreSQL (ou use SQLite para desenvolvimento local)

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone <repository-url>
cd fastapi-backend
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

## 🏃 Como Executar

### Modo Desenvolvimento (local)

```bash
# A partir do diretório fastapi-backend
uvicorn app.main:app --reload
```

A aplicação estará disponível em: `http://localhost:8000`

### Usando Docker Compose

```bash
docker-compose up --build
```

A aplicação estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/api/v1/openapi.json

## 🎯 Endpoints Principais

### Health Check
- `GET /` - Informações básicas da API
- `GET /health` - Status de saúde da aplicação

### Usuários (Users)
- `GET /api/v1/users` - Lista todos os usuários
- `GET /api/v1/users/{user_id}` - Obtém um usuário específico
- `POST /api/v1/users` - Cria um novo usuário
- `PUT /api/v1/users/{user_id}` - Atualiza um usuário
- `DELETE /api/v1/users/{user_id}` - Remove um usuário

### Items
- `GET /api/v1/items` - Lista todos os items
- `GET /api/v1/items/{item_id}` - Obtém um item específico
- `POST /api/v1/items` - Cria um novo item
- `PUT /api/v1/items/{item_id}` - Atualiza um item
- `DELETE /api/v1/items/{item_id}` - Remove um item

## 🏗️ Estrutura do Projeto

```
fastapi-backend/
├── app/
│   ├── api/                # Endpoints da API
│   │   ├── __init__.py
│   │   ├── items.py       # Endpoints de items
│   │   └── users.py       # Endpoints de usuários
│   ├── core/              # Configurações e segurança
│   │   ├── __init__.py
│   │   ├── config.py      # Configurações da aplicação
│   │   └── security.py    # Utilitários de segurança (JWT, hash)
│   ├── db/                # Configuração do banco de dados
│   │   ├── __init__.py
│   │   └── database.py    # Setup do SQLAlchemy
│   ├── models/            # Modelos do banco de dados
│   │   ├── __init__.py
│   │   └── models.py      # Definições dos modelos
│   ├── schemas/           # Schemas Pydantic
│   │   ├── __init__.py
│   │   └── schemas.py     # Schemas de validação
│   ├── __init__.py
│   └── main.py           # Aplicação principal
├── tests/                # Testes
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore           # Arquivos ignorados pelo Git
├── docker-compose.yml   # Configuração Docker Compose
├── Dockerfile           # Configuração Docker
├── requirements.txt     # Dependências Python
└── README.md           # Este arquivo
```

## 🧪 Testes

Para executar os testes:

```bash
pytest
```

Para executar com cobertura:

```bash
pytest --cov=app tests/
```

## 🔐 Segurança

- Senhas são hasheadas usando bcrypt
- Autenticação JWT implementada
- CORS configurado para origens permitidas
- Validação de dados com Pydantic

## 📦 Dependências Principais

- **fastapi** - Framework web
- **uvicorn** - Servidor ASGI
- **sqlalchemy** - ORM
- **pydantic** - Validação de dados
- **python-jose** - JWT tokens
- **passlib** - Hashing de senhas
- **alembic** - Migrações de banco de dados

## 🚀 Próximos Passos

1. Implementar autenticação completa com login
2. Adicionar rate limiting
3. Implementar paginação avançada
4. Adicionar logging estruturado
5. Implementar testes automatizados
6. Adicionar CI/CD pipeline
7. Configurar monitoramento e métricas

## 📝 Exemplos de Uso

### Criar um novo usuário

```bash
curl -X POST "http://localhost:8000/api/v1/users" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

### Criar um novo item

```bash
curl -X POST "http://localhost:8000/api/v1/items" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Meu Item",
    "description": "Descrição do item"
  }'
```

### Listar todos os items

```bash
curl -X GET "http://localhost:8000/api/v1/items"
```

## 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## 👤 Autor

**Gabriel D. Lobo**
- LinkedIn: [gabrieldelobo](https://www.linkedin.com/in/gabrieldelobo/)
- Email: gabrieldlobo@icloud.com

## 🙏 Agradecimentos

- FastAPI por criar um framework incrível
- Comunidade Python por todo suporte
