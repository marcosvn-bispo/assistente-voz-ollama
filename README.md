# 🎙️ Assistente de Voz com Ollama

## 📌 Descrição

Este projeto implementa um assistente de voz em Python capaz de:

* 🎤 Capturar comandos por voz
* 🧠 Processar linguagem natural com o Ollama
* 🔊 Responder utilizando síntese de fala

O objetivo é demonstrar a integração entre reconhecimento de voz, inteligência artificial local e resposta em áudio.

---

## 🚀 Funcionalidades

* Reconhecimento de voz em português (pt-BR)
* Integração com modelo LLM via Ollama
* Respostas em áudio (Text-to-Speech)
* Execução contínua com loop de interação

---

## 🧱 Estrutura do Projeto

```
assistente-voz-ollama/
│
├── src/
│   ├── main.py
│   ├── speech.py
│   ├── tts.py
│   └── assistant.py
│
├── notebooks/
│   └── Assistente_de_voz_com_ollama.ipynb
│
├── run.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/marcosvn-bispo/assistente-voz-ollama.git
cd assistente-voz-ollama
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Execução

Execute o assistente com:

```bash
python run.py
```

---

## ⚠️ Pré-requisitos

Antes de rodar o projeto, certifique-se de que:

* O Ollama está instalado e rodando localmente
* Um modelo (ex: `llama3`) está disponível no Ollama
* Seu microfone está configurado corretamente

---

## 🧠 Tecnologias Utilizadas

* Python
* SpeechRecognition
* gTTS (Google Text-to-Speech)
* Requests
* Ollama (LLM local)

---

## 💡 Possíveis melhorias futuras

* Interface gráfica (GUI)
* Deploy como aplicação web
* Integração com APIs externas
* Melhor tratamento de erros e comandos
* Ativação por palavra-chave (wake word)

---

## 👨‍💻 Autor

Marcos Vinicius Bispo

---

## 📄 Licença

Este projeto é apenas para fins educacionais.
