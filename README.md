# 🤖 HollowScript

Um bot de Discord desenvolvido em **Python** com a biblioteca [discord.py](https://discordpy.readthedocs.io/).  
Feito para **aprendizado**, testes e diversão com comandos *slash*.

---

## ✨ Funcionalidades iniciais

- `/ping` → responde com 🏓 Pong!
- Estrutura pronta para adicionar novos comandos
- Uso de **variáveis de ambiente** para manter o token seguro
- Organizado em pastas para facilitar a manutenção

---

## 📂 Estrutura do projeto

```
nexapy/
 ┣ src/
 ┃ ┗ bot.py          # código principal do bot
 ┣ .env.example      # modelo de variáveis de ambiente
 ┣ .gitignore        # arquivos/pastas ignorados no GitHub
 ┣ requirements.txt  # dependências do projeto
 ┗ README.md         # este arquivo
```

---

## ⚙️ Pré-requisitos

- [Python 3.12+](https://www.python.org/downloads/)
- Conta no [Discord Developer Portal](https://discord.com/developers/applications) com um bot criado e token gerado
- Git instalado (opcional, para versionamento e upload no GitHub)

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório e entre na pasta
```bash
git clone https://github.com/seu-usuario/nexapy.git
cd nexapy
```

### 2. Crie o ambiente virtual e ative
No Windows (CMD):
```bash
python -m venv venv
venv\Scripts\activate.bat
```

No PowerShell:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

⚠️ Importante: o bot **não lê** o `.env.example`, ele só serve como modelo.  
Você deve criar um arquivo **`.env`** na raiz do projeto com seu token real:

- `.env.example` (vai pro GitHub, modelo):
  ```env
  DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
  ```

- `.env` (fica só na sua máquina, **não sobe pro GitHub**):
  ```env
  DISCORD_TOKEN=SEU_TOKEN_AQUI
  ```

### 5. Execute o bot
```bash
python src/bot.py
```

Se tudo estiver certo, aparecerá:
```
✅ Slash commands sincronizados.
🤖 HollowScript está online como Nexa#1234
```

E o comando `/ping` estará disponível no seu servidor 🎉.

---

## 📌 Próximos passos / Ideias futuras

- [ ] Sistema de inventário (para RPG)
- [ ] Escolha de classes (guerreiro, mago, arqueiro, etc.)
- [ ] Mini-jogos interativos no chat
- [ ] Comandos de economia (moedas virtuais, loja, etc.)
- [ ] Sistema de XP e level up

---

## 🛠️ Tecnologias usadas

- [Python](https://www.python.org/)  
- [discord.py](https://discordpy.readthedocs.io/)  
- [python-dotenv](https://pypi.org/project/python-dotenv/)  

---

## ⚠️ Aviso importante

- **Nunca compartilhe seu token real do Discord.**  
- O arquivo `.env` está no `.gitignore` para evitar vazamentos.  
- Use sempre o `.env.example` como referência para outros desenvolvedores.

---

## 📜 Licença

Este projeto está sob a licença MIT.  
Sinta-se livre para usar, modificar e compartilhar 🚀.

---

👨‍💻 Criado com fins educativos por **[Seu Nome](https://github.com/seu-usuario)**.
