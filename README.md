# Knowledge Miner Pipeline

Uma pipeline automatizada de extração, transcrição e processamento de dados não estruturados (áudio/vídeo) para a geração de acervo intelectual e resumos lógicos de alta densidade, utilizando Modelos de Linguagem de Grande Escala (LLMs).

## Objetivo do Projeto
Transformar conteúdos audiovisuais extensos em conhecimento estruturado e indexável. O sistema atua como um extrator de repertório, focando na mineração da arquitetura de raciocínio, teses centrais e dimensões simbólicas do autor original, entregando documentos em Markdown prontos para uso.

## Arquitetura e Fluxo de Dados (ETL)
O projeto foi desenhado sob o princípio de responsabilidade única (Single Responsibility Principle) e modularidade, dividindo a esteira em micro-etapas:

1. **Extract (Extração):** Download otimizado da melhor stream de áudio via `yt-dlp`.
2. **Transform (Transcrição & Limpeza):** Conversão de fala para texto offline utilizando o modelo Whisper da OpenAI, seguido de uma etapa de sanitização via Regex para padronização do corpus de texto.
3. **Load / Process (Processamento IA):** Injeção do texto limpo em templates de prompt pré-configurados e envio à API da OpenAI para reestruturação semântica e lógica.
4. **Output:** Geração de um artefato final `.md` com metadados estruturados para consumo imediato.

## AI Design & Engenharia de Prompts
A lógica de instrução da IA foi intencionalmente desacoplada do código-fonte Python. Os prompts residem no diretório `/prompts` em arquivos `.txt` dedicados. 

* **Isolamento de Contexto:** Permite o refinamento contínuo das personas e diretrizes de extração (como ontologia, léxico específico e filtros de qualidade) sem necessidade de alterar o core da aplicação.
* **Injeção Dinâmica:** O sistema utiliza placeholders para acoplar a transcrição ao template de forma programática no momento da execução.

## Estrutura do Projeto

    knowledge-miner/
    ├── prompts/
    │   ├── knowledge.txt
    │   └── summary.txt
    ├── services/
    │   ├── ai_processor.py
    │   ├── transcription.py
    │   └── youtube.py
    ├── utils/
    │   ├── cleaner.py
    │   └── file_manager.py
    ├── output/
    ├── main.py
    ├── config.py
    ├── .env
    ├── .gitignore
    └── requirements.txt

## Stack Tecnológica
* **Linguagem:** Python 3.x
* **Processamento de Áudio:** yt-dlp
* **Speech-to-Text (STT):** openai-whisper
* **IA Generativa / LLM:** openai (API)
* **Segurança e Configuração:** python-dotenv

## Como Executar Localmente

1. Clone o repositório.
2. Instale as dependências executando o comando na raiz do projeto:
    pip install -r requirements.txt

3. Configure suas credenciais criando um arquivo .env na raiz do projeto:
    OPENAI_API_KEY=sua_chave_aqui

4. Execute o orquestrador:
    python main.py
