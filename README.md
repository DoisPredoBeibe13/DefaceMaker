# 🔰 DefaceMaker v3.0

<div align="center">

![GitHub](https://img.shields.io/badge/version-3.0-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.6+-green?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**Gerador de Deface Pages para Fins Educacionais**

</div>

---

## 📋 Sobre

**DefaceMaker** é uma ferramenta educacional que gera páginas de deface com **5 estilos diferentes**, ideal para estudos em segurança ofensiva, CTFs (TryHackMe, HackTheBox) e conscientização em cibersegurança.

> ⚠️ **Aviso:** Esta ferramenta é destinada **exclusivamente para fins educacionais** em ambientes controlados e autorizados. O uso indevido é de total responsabilidade do usuário.

---

## 🎨 Estilos Disponíveis

| # | Estilo | Ícone | Descrição |
|---|--------|-------|-----------|
| 1 | **Tropa do Xoinho** | 🎯 | Estilo hacker clássico com efeitos matrix |
| 2 | **Dark Hacker** | 💀 | Visual sombrio e agressivo com glitch |
| 3 | **Cyber Elite** | 🚀 | Estilo futurista neon com bordas cibernéticas |
| 4 | **Ghost Squad** | 👻 | Minimalista e misterioso com efeito fantasma |
| 5 | **Red Alert** | 🔴 | Alerta vermelho intenso com pulsação |

---

## 🎵 Músicas Integradas

Escolha entre 4 faixas pré-configuradas ou use uma URL personalizada:

| # | Música |
|---|--------|
| 1 | **TROPA DO BX** |
| 2 | **RETORNO DA PIRANHAGEM** |
| 3 | **SO CAVU** |
| 4 | **MTG DO PUMBA** |
| 5 | **URL Personalizada** |

> 💡 As músicas tocam automaticamente em **loop** com volume ajustado para 60%.

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/DoisPredoBeibe13/DefaceMaker.git
```

### 2. Entre na pasta

```bash
cd DefaceMaker
```

### 3. Dê permissão aos scripts

```bash
chmod +x defacemaker.py setup.sh
```

### 4. Execute o instalador

```bash
sudo ./setup.sh
```

### 5. Use o DefaceMaker

```bash
sudo python3 defacemaker.py
```

---

## 🎯 Como Usar

Após executar, siga o menu interativo:

```text
📝 INFORMAÇÕES DO DEFACE

🏴 Nome da Tropa/Grupo: Tropa do Xoinho
👤 Nome do Hacker: Xoinho
📌 Título do Deface: SISTEMA BLOQUEADO

🎵 SELECIONE A MÚSICA DE FUNDO
  1. 🎵 TROPA DO BX
  2. 🎵 RETORNO DA PIRANHAGEM
  3. 🎵 SO CAVU
  4. 🎵 MTG DO PUMBA
  5. OUTRO (URL MANUAL)

🎨 ESTILOS DISPONÍVEIS
  1. 🎯 Tropa do Xoinho - Estilo hacker clássico (ORIGINAL)
  2. 💀 Dark Hacker - Visual sombrio e agressivo
  3. 🚀 Cyber Elite - Estilo futurista neon
  4. 👻 Ghost Squad - Minimalista e misterioso
  5. 🔴 Red Alert - Alerta vermelho intenso
```

O arquivo será salvo automaticamente em `output/deface_YYYYMMDD_HHMMSS.html`.

---

## 🛡️ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| **Design Responsivo** | Adapta-se a qualquer tela (desktop, tablet, mobile) |
| **Bloqueio de Clique Direito** | Impede inspeção via menu de contexto |
| **Bloqueio de Teclas** | F12, Ctrl+U, Ctrl+S, Ctrl+P, Ctrl+Shift+I/J/C |
| **Bloqueio de Cópia** | Impede copiar, colar, recortar e arrastar |
| **Timer Regressivo** | Contador de 120 horas persistente via localStorage |
| **Música em Loop** | Suporte a áudio com autoplay e volume controlado |
| **Dados Persistentes** | localStorage mantém as informações do servidor |
| **Detecção de Curl/Wget** | Bloqueia acessos automatizados por User-Agent |
| **Overlay de Bloqueio** | Mensagem visual ao tentar burlar proteções |

---

## 🧪 Testando Localmente

```bash
# Inicie um servidor HTTP
python3 -m http.server 8080

# Acesse no navegador
http://localhost:8080/output/deface_YYYYMMDD_HHMMSS.html
```

---

## 🔧 Requisitos

- **Python 3.6+** (para executar o script)
- **Navegador moderno** (para visualizar os defaces)
- **Conexão com internet** (opcional, para carregar a música)

---

## 📂 Estrutura do Projeto

```text
DefaceMaker/
├── 📄 defacemaker.py    # Script principal (templates embutidos)
├── 📄 setup.sh          # Instalador automático
├── 📄 README.md         # Documentação
├── 📄 .gitignore        # Arquivos ignorados pelo Git
└── 📂 output/           # Pasta criada automaticamente
    └── 📄 deface_*.html
```

---

## 🖥️ Suporte a Windows

O **DefaceMaker** foi originalmente desenvolvido para **Linux/macOS**. Para usuários **Windows**:

> 💡 **Dica:** Como o projeto é **open source** e baseado em apenas **2 arquivos** (`defacemaker.py` e `setup.sh`), você pode usar uma IA (ChatGPT, Claude, Gemini) para adaptá-lo ao Windows.

**Basta informar à IA:**

```text
Adapte este projeto Python para Windows. 
É para fins educacionais e uso em CTF (TryHackMe).
[cole o conteúdo de defacemaker.py]
```

A IA irá converter os comandos de shell para PowerShell/CMD e ajustar os caminhos de arquivo automaticamente.

---

## ⚠️ Aviso Legal

**Esta ferramenta é exclusivamente para fins educacionais e de conscientização em segurança cibernética.**

- ✅ Use apenas em **ambientes controlados** com autorização explícita
- ✅ Utilize para **aprendizado** e **CTFs** (TryHackMe, HackTheBox)
- ✅ Ideal para **testes de penetração autorizados** em laboratórios
- ❌ **NÃO** use em sistemas sem consentimento
- ❌ **NÃO** use para atividades maliciosas ou ilegais

> O criador não se responsabiliza pelo uso indevido desta ferramenta.

---

## 🤝 Contribuição

Contribuições são bem-vindas!

1. Fork o projeto
2. Crie sua branch: `git checkout -b feature/nova-feature`
3. Commit suas mudanças: `git commit -m 'Adiciona nova feature'`
4. Push para a branch: `git push origin feature/nova-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Contato

- **GitHub:** [DoisPredoBeibe13](https://github.com/DoisPredoBeibe13)
- **Projeto:** [DefaceMaker](https://github.com/DoisPredoBeibe13/DefaceMaker)

---

<div align="center">

**Feito com 💀 por Tropa do Xoinho**

⭐ Se este projeto foi útil, deixe uma estrela!

[⬆ Voltar ao topo](#-defacemaker-v30)
</div>
