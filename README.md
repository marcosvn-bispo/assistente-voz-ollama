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


# ⚙️ Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/marcosvn-bispo/assistente-voz-ollama.git
cd assistente-voz-ollama
```

---

## 2. Crie e ative um ambiente virtual (recomendado)

### Windows (PowerShell)

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4. Instale o Ollama

Este projeto utiliza o **Ollama** para executar o modelo de linguagem localmente.

Baixe em:

https://ollama.com/download

Após instalar, verifique se está funcionando:

```bash
ollama --version
```

---

## 5. Baixe o modelo utilizado

O projeto utiliza o modelo **llama3**.

```bash
ollama pull llama3
```

---

# ▶️ Execução

## 1. Inicie o servidor do Ollama

```bash
ollama serve
```

O servidor será iniciado em:

```
http://localhost:11434
```

---

## 2. Execute o assistente

Em outro terminal, dentro da pasta do projeto:

```bash
python run.py
```

Se tudo estiver funcionando corretamente, aparecerá algo como:

```
Assistente iniciado. Pode falar.
🎤 Ouvindo...
```

---

# 🧠 Como funciona

Fluxo do assistente:

```
Microfone
   ↓
speech.py (Speech Recognition)
   ↓
assistant.py (envia comando para o Ollama)
   ↓
Modelo LLM (llama3)
   ↓
tts.py (Text-to-Speech)
   ↓
Resposta em áudio
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
* SoundDevice
* Ollama
* Llama 3
* Text-to-Speech (TTS)

---

## 💡 Possíveis melhorias futuras

* Interface gráfica (GUI)
* Deploy como aplicação web
* Integração com APIs externas
* Ativação por palavra-chave (wake word)

---

## 👨‍💻 Autor

Marcos Vinicius Bispo

---

## 📄 Licença

Este projeto é apenas para fins educacionais.
