
# 🛒 Mercado Livre Scraper

[![Python](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Um scraper robusto e eficiente em Python para extrair informações de produtos do Mercado Livre com suporte a paginação automática e filtros avançados.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para facilitar a coleta automatizada de dados de produtos do Mercado Livre, oferecendo uma solução completa para:

- **Pesquisa de mercado**: Análise de produtos e tendências de preços
- **Monitoramento competitivo**: Acompanhamento de concorrência e posicionamento
- **Análise de dados**: Coleta estruturada para análises estatísticas
- **Automação de processos**: Integração em pipelines de dados e relatórios

## ✨ Funcionalidades

- 🔍 **Busca avançada**: Pesquise por qualquer termo no Mercado Livre
- 📄 **Paginação automática**: Navegação inteligente através de múltiplas páginas
- 🚫 **Filtros negativos**: Sistema robusto de exclusão por palavras-chave
- 📊 **Extração estruturada**: Coleta título, preço e metadados dos produtos
- 🛡️ **Proteção anti-bot**: Headers realísticos e rate limiting integrado
- ⚡ **Performance otimizada**: URLs diretas e sessão persistente para maior velocidade
- 🔄 **Tratamento de erros**: Detecção automática de fim de resultados e recuperação de falhas

## 🛠️ Tecnologias Utilizadas

- **Python 3.13+**
- **BeautifulSoup4**: Para parsing do HTML
- **Requests**: Para requisições HTTP
- **Type Hints**: Para melhor documentação do código

## 📦 Instalação

1. **Clone o repositório**:
```bash
git clone https://github.com/joao-marco-jf/lista-mercadolivre-scraper.git
cd lista-mercadolivre-scraper
```

2. **Instale as dependências**:
```bash
pip install -r requirements.txt
```

## 🚀 Como Usar

### Uso Simples (Recomendado)

```python
from scraper import ListaMercadoLivreScraper

# Buscar produtos com execução completa automatizada
scraper = ListaMercadoLivreScraper(
    search="notebook lenovo ideapad i3",
    negative_keywords=["recondicionado", "usado"],
    max_pages=5
)

# Executar scraping completo
items = scraper.run()

# Processar resultados
for item in items:
    print(f"Produto: {item['title']}")
    print(f"Preço: R$ {item['price']}")
    print("-" * 50)
```

### Parâmetros do Construtor

| Parâmetro | Tipo | Obrigatório | Descrição | Padrão |
|-----------|------|-------------|-----------|---------|
| `search` | `str` | ✅ | Termo de busca no Mercado Livre | - |
| `negative_keywords` | `list[str]` | ❌ | Palavras-chave para filtrar produtos indesejados | `[]` |
| `max_pages` | `int` | ❌ | Número máximo de páginas para processar | `1` |

### Estrutura dos Dados Retornados

```python
[
    {
        "title": "notebook lenovo ideapad 3i intel core i3-1215u",
        "price": "2299"
    },
    {
        "title": "notebook lenovo ideapad gaming 3 amd ryzen 5",
        "price": "3499"
    }
]
```

### Exemplos Avançados

#### Busca com Múltiplas Páginas
```python
# Coletar até 10 páginas de resultados
scraper = ListaMercadoLivreScraper(
    search="smartphone samsung galaxy",
    max_pages=10
)
items = scraper.run()
print(f"Total de produtos encontrados: {len(items)}")
```

#### Filtros Negativos Avançados
```python
# Excluir múltiplos termos indesejados
scraper = ListaMercadoLivreScraper(
    search="iphone 15",
    negative_keywords=[
        "usado", "recondicionado", "replica", 
        "capa", "pelicula", "carregador"
    ]
)
```

#### Uso Manual dos Métodos (Avançado)
```python
# Para casos que necessitam controle granular
scraper = ListaMercadoLivreScraper("notebook gamer")

try:
    html = scraper.fetch()  # Buscar HTML da página atual
    scraper.parse(html)     # Processar produtos encontrados
    items = scraper.get_items()  # Obter lista de produtos
except Exception as e:
    print(f"Erro durante scraping: {e}")
```

## � Estrutura do Projeto

```
lista-mercadolivre-scraper/
├── 📄 scraper.py           # Classe ListaMercadoLivreScraper com toda a lógica
├── 📄 main.py              # Script de exemplo e demonstração
├── 📄 requirements.txt     # Dependências Python necessárias
├── 📄 README.md            # Documentação completa (este arquivo)
└── 📄 LICENSE              # Licença MIT do projeto
```

### Componentes Principais

- **`ListaMercadoLivreScraper`**: Classe principal com métodos para busca, parsing e paginação
- **`run()`**: Método de execução completa automatizada
- **`fetch()`**: Realiza requisições HTTP com headers otimizados  
- **`parse()`**: Processa HTML e extrai dados estruturados
- **`get_items()`**: Retorna lista filtrada de produtos encontrados

## 🔧 Arquitetura e Funcionamento

### Fluxo de Execução

1. **Inicialização**: Configura parâmetros de busca, filtros e sessão HTTP persistente
2. **Paginação Automática**: Navega sequencialmente pelas páginas de resultados
3. **Requisições Otimizadas**: Utiliza URLs diretas com parâmetros de performance
4. **Parsing Estruturado**: Extrai dados usando seletores CSS específicos
5. **Filtragem Inteligente**: Aplica filtros negativos em tempo real
6. **Tratamento de Erros**: Detecta automaticamente fim de resultados (HTTP 404)

### Detalhes Técnicos

- **URL Base**: `https://lista.mercadolivre.com.br/{busca}_NoIndex_True`
- **Paginação**: `{busca}_Desde_{offset}_NoIndex_True`
- **Seletores**:
  - Container: `.poly-card`
  - Título: `h3.poly-component__title-wrapper`
  - Preço: `.poly-price__current .andes-money-amount__fraction`
- **Rate Limiting**: Delay de 1 segundo entre requisições
- **Headers**: User-Agent realístico para Windows/Chrome
- **Sessão**: Mantém cookies e conexões TCP reutilizáveis

## ⚠️ Limitações e Boas Práticas

### Limitações Técnicas

- **Dependência de DOM**: Sujeito a mudanças na estrutura HTML do site
- **Rate Limiting**: Limite de ~1 requisição por segundo para evitar bloqueios
- **Dados Limitados**: Extrai apenas título e preço básico (sem descrições ou imagens)
- **Sem JavaScript**: Não processa conteúdo carregado dinamicamente via JS

### Recomendações de Uso

✅ **Boas Práticas**:
- Use delays apropriados entre execuções do scraper
- Implemente cache local para evitar requisições desnecessárias
- Monitore logs de erro para detectar mudanças no site
- Processe dados em lotes para melhor performance

❌ **Evite**:
- Executar múltiplas instâncias simultâneas
- Fazer requisições muito frequentes (< 1 segundo)
- Ignorar erros HTTP sem tratamento adequado
- Usar em produção sem monitoramento de saúde

### Considerações Legais e Éticas

- **Uso Responsável**: Respeite os termos de uso do Mercado Livre
- **Fins Educacionais**: Projeto destinado a aprendizado e pesquisa
- **Volume Moderado**: Evite sobrecarregar os servidores do site
- **Dados Públicos**: Processa apenas informações publicamente visíveis

## 🚀 Roadmap e Melhorias Futuras

- [ ] **Extração ampliada**: Descrições, imagens e avaliações dos produtos
- [ ] **Filtros avançados**: Por preço, localização e condição do produto  
- [ ] **Export de dados**: Suporte para CSV, JSON e bases de dados
- [ ] **Monitoramento**: Alertas para mudanças de preço
- [ ] **Proxy rotation**: Suporte a proxies para maior escalabilidade
- [ ] **API REST**: Interface web para uso não-técnico

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Este projeto segue as melhores práticas de desenvolvimento colaborativo.

### Como Contribuir

1. **Fork** o repositório
2. **Clone** seu fork: `git clone https://github.com/SEU-USERNAME/lista-mercadolivre-scraper.git`
3. **Crie uma branch**: `git checkout -b feature/nova-funcionalidade`
4. **Faça suas alterações** seguindo os padrões do projeto
5. **Teste** suas mudanças localmente
6. **Commit**: `git commit -am 'feat: adiciona nova funcionalidade'`
7. **Push**: `git push origin feature/nova-funcionalidade`
8. **Abra um Pull Request** com descrição detalhada

### Diretrizes de Desenvolvimento

- Mantenha **compatibilidade** com Python 3.13+
- Siga **PEP 8** para estilo de código
- Adicione **type hints** em novos métodos
- Inclua **docstrings** detalhadas
- **Teste** funcionalidades antes de submeter

## 📊 Status do Projeto

![GitHub last commit](https://img.shields.io/github/last-commit/joao-marco-jf/lista-mercadolivre-scraper)
![GitHub issues](https://img.shields.io/github/issues/joao-marco-jf/lista-mercadolivre-scraper)
![GitHub stars](https://img.shields.io/github/stars/joao-marco-jf/lista-mercadolivre-scraper)

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** - veja o arquivo [LICENSE](LICENSE) para detalhes completos.

### Resumo da Licença
- ✅ Uso comercial permitido
- ✅ Modificação permitida  
- ✅ Distribuição permitida
- ❗ Sem garantia ou responsabilidade

## 👨‍💻 Autor

**João M. Jensen Francisco**
- GitHub: [@joao-marco-jf](https://github.com/joao-marco-jf)
- LinkedIn: [Conecte-se comigo](https://linkedin.com/in/joao-marco-jf)

---

<div align="center">

### ⭐ Se este projeto foi útil para você, considere dar uma estrela!

**Feito com ❤️ em Python | Licenciado sob MIT**

</div>