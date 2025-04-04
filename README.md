﻿# Analisador de Transcrições PDF

Sistema de análise automatizada de transcrições em formato PDF que extrai resumos, tópicos principais e ganchos relevantes do texto.

### 📋 Pré-requisitos

Para rodar este projeto, você precisa dos seguintes softwares instalados:

- **Python 3.6+** (Linguagem de programação)
- **Git** (Para fazer clone do repositório)
- **Pip** (Gerenciador de pacotes Python)

### 🔧 Instalação

Primeiramente faça um clone deste repositório para sua máquina:

```bash
git clone "https://github.com/seu-usuario/analisetranscricao"
```

Recomendamos a criação de um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instalação das dependências necessárias:

```bash
pip install PyPDF2
```

Para rodar a aplicação:

```bash
python main.py
```

## 🔩 Explicando o Funcionamento

O script analisa arquivos PDF contendo transcrições de texto e realiza as seguintes operações:

1. **Leitura do PDF**: Extrai o texto completo de um arquivo PDF chamado "transcription.pdf"
2. **Análise do Texto**: 
   - Divide o texto em sentenças
   - Remove palavras de parada (stop words)
   - Identifica palavras frequentes
3. **Geração de Resultados**:
   - **Resumo**: Extrai as três primeiras sentenças do texto
   - **Tópicos**: Identifica as cinco palavras mais frequentes no texto
   - **Ganchos**: Busca sentenças contendo palavras-chave como "dica" ou "nunca", ou as sentenças mais longas

Os resultados são exibidos no console e salvos em um arquivo JSON chamado "resultado.json".

## ⚙️ Executando o programa

O programa espera encontrar um arquivo chamado "transcription.pdf" no mesmo diretório. Para analisar um arquivo diferente, você precisará modificar a linha:

```python
with open("transcription.pdf", 'rb') as file:
```

Após a execução, verifique o arquivo "resultado.json" para ver o resultado da análise.

## 📦 Estrutura do código

O código é composto por:

- **Função `analyze_transcript(text)`**: Realiza toda a análise do texto e retorna um dicionário com os resultados
- **Bloco principal**: Lê o arquivo PDF, chama a função de análise e salva os resultados

O resultado é um dicionário JSON com a seguinte estrutura:
```json
{
  "resumo": "Início do texto...",
  "topicos": ["palavra1", "palavra2", "palavra3", "palavra4", "palavra5"],
  "ganchos": ["Sentença relevante 1.", "Sentença relevante 2.", "Sentença relevante 3."]
}
```

## 🛠️ Construído com

- [Python](https://www.python.org/) - Linguagem de programação
- [PyPDF2](https://pypdf2.readthedocs.io/) - Biblioteca para leitura de arquivos PDF
- [json](https://docs.python.org/3/library/json.html) - Módulo para manipulação de dados JSON
- [re](https://docs.python.org/3/library/re.html) - Módulo para uso de expressões regulares

## ✒️ Autores

Projeto desenvolvido por:
- **Seu Nome** - *Trabalho Inicial* - [seu-usuario](https://github.com/seu-usuario)

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](https://github.com/JoaoLuiz92/analisetranscricao/blob/main/LICENSE.md) para detalhes.

## 🎁 Expressões de gratidão

- Projeto desenvolvido para automatizar a análise de transcrições e extrair informações relevantes
- Ideal para criadores de conteúdo, pesquisadores ou qualquer pessoa que precise processar grandes volumes de texto
- Contribuições são bem-vindas através de pull requests ou sugestões de melhorias!
