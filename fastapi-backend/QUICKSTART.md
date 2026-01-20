# Guia Rápido - FastAPI Backend

Este guia te ajudará a começar rapidamente com o projeto FastAPI.

## 🚀 Instalação Rápida

### 1. Instalar Dependências

```bash
cd fastapi-backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
# Edite o arquivo .env conforme necessário
```

### 3. Executar a Aplicação

```bash
uvicorn app.main:app --reload
```

A aplicação estará rodando em: http://localhost:8000

## 📚 Acessar Documentação

- **Swagger UI (Interativa)**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Executar Testes

```bash
pytest tests/ -v
```

## 🐳 Usando Docker

### Executar com Docker Compose (Recomendado)

```bash
docker-compose up --build
```

Isso irá:
- Criar um container PostgreSQL
- Criar um container da aplicação
- Conectar automaticamente ao banco de dados

### Parar os Containers

```bash
docker-compose down
```

## 📝 Exemplos de Uso da API

### Criar um Usuário

```bash
curl -X POST http://localhost:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@example.com",
    "username": "nomedousuario",
    "password": "senha123"
  }'
```

### Listar Todos os Usuários

```bash
curl http://localhost:8000/api/v1/users/
```

### Criar um Item

```bash
curl -X POST http://localhost:8000/api/v1/items/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Meu Primeiro Item",
    "description": "Esta é uma descrição"
  }'
```

### Listar Todos os Items

```bash
curl http://localhost:8000/api/v1/items/
```

### Atualizar um Item

```bash
curl -X PUT http://localhost:8000/api/v1/items/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Item Atualizado",
    "description": "Nova descrição"
  }'
```

### Deletar um Item

```bash
curl -X DELETE http://localhost:8000/api/v1/items/1
```

## 🔧 Estrutura de Pastas

```
fastapi-backend/
├── app/
│   ├── api/          # Endpoints da API
│   ├── core/         # Configurações e segurança
│   ├── db/           # Banco de dados
│   ├── models/       # Modelos do banco
│   ├── schemas/      # Schemas Pydantic
│   └── main.py       # Aplicação principal
├── tests/            # Testes
├── .env.example      # Exemplo de variáveis de ambiente
├── requirements.txt  # Dependências
└── docker-compose.yml # Configuração Docker
```

## 💡 Dicas

1. **Modo de Desenvolvimento**: Use `--reload` para recarregar automaticamente quando alterar código
2. **Documentação Interativa**: Use `/docs` para testar sua API diretamente no navegador
3. **Banco de Dados**: Por padrão usa SQLite (`test.db`). Para produção, use PostgreSQL
4. **Variáveis de Ambiente**: Sempre configure o arquivo `.env` antes de executar em produção

## 🆘 Problemas Comuns

### Porta 8000 já em uso

```bash
# Linux/Mac
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Erro de Permissão no Linux

```bash
chmod +x venv/bin/activate
```

### Dependências não instaladas

```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

## 📚 Próximos Passos

1. Personalize os modelos em `app/models/models.py`
2. Adicione novos endpoints em `app/api/`
3. Configure autenticação JWT completa
4. Adicione mais testes em `tests/`
5. Configure CI/CD para deploy automático

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie sua feature branch (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou problemas, entre em contato:
- Email: gabrieldlobo@icloud.com
- LinkedIn: [gabrieldelobo](https://www.linkedin.com/in/gabrieldelobo/)
