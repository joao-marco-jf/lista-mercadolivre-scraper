
# 🛒 Mercado Livre Scraper

Um scraper em Python para extrair informações de produtos do Mercado Livre de forma simples e eficiente.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para facilitar a coleta de dados de produtos do Mercado Livre, permitindo buscar itens específicos e filtrar resultados indesejados através de palavras-chave negativas. É especialmente útil para análises de mercado, comparação de preços e monitoramento de produtos.

## ✨ Funcionalidades

- 🔍 **Busca personalizada**: Pesquise por qualquer produto no Mercado Livre
- 🚫 **Filtros negativos**: Exclua produtos com palavras-chave específicas
- 📊 **Extração de dados**: Coleta título e preço dos produtos
- 🤖 **Comportamento humano**: Utiliza delays e headers para evitar bloqueios
- 🎯 **Foco nos resultados**: URL otimizada para melhor performance nas buscas

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

### Exemplo Básico

```python
from scraper import ListaMercadoLivreScraper

# Criar uma instância do scraper
scraper = ListaMercadoLivreScraper(search="iphone 16 pro", negative_keywords=["max"])

# Buscar e extrair dados
html = scraper.fetch()
scraper.parse(html)
items = scraper.get_items()

# Exibir resultados
for item in items:
    print(f"Título: {item['title']}")
    print(f"Preço: R$ {item['price']}")
    print("-" * 50)
```

### Parâmetros da Classe ListaMercadoLivreScraper

- **search** (str): Termo de busca (obrigatório)
- **negative_keywords** (list[str], opcional): Lista de palavras para filtrar resultados indesejados
- **pages** (int, opcional): Número de páginas para scraping (padrão: 3, *em desenvolvimento*)

### Exemplo com Filtros

```python
# Buscar iPhone 16, mas excluir modelos Pro Max e Plus
scraper = ListaMercadoLivreScraper(
    search="iphone 16",
    negative_keywords=["pro max", "plus", "usado"]
)
```

## 📝 Estrutura do Projeto

```
lista-mercadolivre-scraper/
├── scraper.py          # Classe principal do scraper
├── main.py             # Exemplo de uso
├── requirements.txt    # Dependências do projeto
└── README.md           # Este arquivo
```

## 🔧 Como Funciona

1. **URL Otimizada**: O scraper utiliza uma URL simplificada (`https://lista.mercadolivre.com.br/{busca}_NoIndex_True`) que remove categorias desnecessárias para melhor performance

2. **Parsing Inteligente**: Busca elementos com classe `poly-card` e extrai:
   - Título do produto (elemento `h3` com classe `poly-component__title-wrapper`)
   - Preço (elemento `span` com classe `andes-money-amount__fraction`)

3. **Filtros Negativos**: Remove automaticamente produtos que contenham palavras-chave indesejadas no título

4. **Headers Humanos**: Utiliza User-Agent e delays para simular comportamento humano

## ⚠️ Considerações Importantes

- **Uso Responsável**: Este scraper deve ser usado respeitando os termos de uso do Mercado Livre
- **Rate Limiting**: Inclui delays para evitar sobrecarga nos servidores
- **Fins Educacionais**: Projeto desenvolvido para fins educacionais e de pesquisa

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👤 Autor

Desenvolvido por João M. Jensen Francisco

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!