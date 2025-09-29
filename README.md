# Projeto Category - DDD com Eventos de Domínio

Este projeto implementa uma entidade de domínio `Category` seguindo os princípios de Domain-Driven Design (DDD), com funcionalidades de serialização e eventos de domínio.

## Estrutura do Projeto

```
backend p1/
├── __init__.py
├── category.py          # Entidade Category principal
├── events/
│   ├── __init__.py
│   └── category_events.py  # Eventos de domínio
├── main.py              # Demonstração das funcionalidades
└── README.md
```

## Funcionalidades Implementadas

### 1. Entidade Category

A classe `Category` é uma entidade de domínio que possui:

- **Atributos**: `id`, `name`, `description`, `is_active`
- **Validações**: Nome obrigatório, limites de caracteres
- **Comportamentos**: Criação, atualização, ativação/desativação

### 2. Serialização

- **`to_dict()`**: Converte a categoria em dicionário
- **`from_dict()`**: Reconstrói categoria a partir de dicionário
- Inclui campo `class_name` para identificação da entidade

### 3. Eventos de Domínio

Eventos implementados:
- `CategoryCreated`: Disparado na criação
- `CategoryUpdated`: Disparado na atualização de atributos
- `CategoryActivated`: Disparado na ativação
- `CategoryDeactivated`: Disparado na desativação

Cada evento contém:
- `category_id`: Identificador da categoria
- `timestamp`: Momento do evento
- Dados específicos do evento (ex: mudanças, valores anteriores)

### 4. Conceitos Aplicados

- **@dataclass**: Simplifica criação de classes de dados
- **Eventos de Domínio**: Rastreamento de mudanças significativas
- **DDD**: Entidade com comportamentos e validações de negócio
- **Serialização**: Conversão entre objetos e dicionários

## Como Executar

```bash
python main.py
```

## Exemplo de Uso

```python
from category import Category

# Criar categoria
category = Category(name="Eletrônicos", description="Produtos eletrônicos")

# Atualizar
category.update(name="Eletrônicos e Informática")

# Serializar
data = category.to_dict()

# Reconstruir
new_category = Category.from_dict(data)

# Verificar eventos
print(f"Eventos registrados: {len(category.events)}")
```

## Resumo dos Conceitos

### @staticmethod
- Método que não precisa de acesso ao estado da instância
- Não recebe `self` ou `cls` automaticamente
- Útil para funções utilitárias da classe

### Dataclasses
- Decorador que automatiza criação de classes de dados
- Gera `__init__`, `__repr__`, `__eq__` automaticamente
- Suporte a valores padrão e pós-inicialização

### Eventos de Domínio
- Representam mudanças significativas no domínio
- Facilitam auditoria e rastreamento
- Permitem desacoplamento entre componentes

### Decoradores
- Funções que modificam comportamento de outras funções/classes
- Permitem adicionar funcionalidades de forma limpa
- Exemplos: `@property`, `@staticmethod`, `@dataclass`

### DDD (Domain-Driven Design)
- Foco no domínio do negócio
- Entidades com identidade e comportamentos
- Eventos para rastrear mudanças importantes
- Separação clara entre domínio e infraestrutura