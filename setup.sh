#!/bin/bash
# setup.sh - Instalador do DefaceMaker

# Cores
RED='\033[91m'
GREEN='\033[92m'
YELLOW='\033[93m'
BLUE='\033[94m'
CYAN='\033[96m'
WHITE='\033[97m'
BOLD='\033[1m'
RESET='\033[0m'

echo -e "${BOLD}${CYAN}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║  ${BOLD}${WHITE}██████╗ ███████╗███████╗ █████╗  ██████╗███████╗${RESET}${CYAN}  ║"
echo "║  ${BOLD}${WHITE}██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝${RESET}${CYAN}  ║"
echo "║  ${BOLD}${WHITE}██║  ██║█████╗  █████╗  ███████║██║     █████╗  ${RESET}${CYAN}  ║"
echo "║  ${BOLD}${WHITE}██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║     ██╔══╝  ${RESET}${CYAN}  ║"
echo "║  ${BOLD}${WHITE}██████╔╝███████╗██║     ██║  ██║╚██████╗███████╗${RESET}${CYAN}  ║"
echo "║  ${BOLD}${WHITE}╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝${RESET}${CYAN}  ║"
echo "║                                                               ║"
echo "║  ${BOLD}${WHITE}🔰 INSTALADOR DO DEFACEMAKER v2.0${RESET}${CYAN}              ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo -e "${RESET}"

echo -e "\n${BOLD}${YELLOW}[+] Criando estrutura de diretórios...${RESET}"

# Cria diretórios
mkdir -p templates
mkdir -p output

echo -e "${GREEN}✅ Diretórios criados!${RESET}"

echo -e "\n${BOLD}${YELLOW}[+] Baixando templates...${RESET}"

# Template 1: Tropa do Xoinho
cat > templates/tropa_do_xoinho.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔒 {{TITULO}} - {{NOME_TROPA}}</title>
    <meta name="robots" content="noindex, nofollow">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; cursor: default; }
        body {
            background: #0a0a0a;
            color: #fff;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0,255,0,0.03) 2px, rgba(0,255,0,0.03) 4px);
            pointer-events: none;
            z-index: 0;
        }
        .container {
            max-width: 900px;
            width: 100%;
            background: #121212;
            border: 2px solid #ff0000;
            box-shadow: 0 0 60px rgba(255,0,0,0.3);
            padding: 40px;
            text-align: center;
            position: relative;
            z-index: 1;
            border-radius: 12px;
        }
        .banner {
            background: linear-gradient(90deg, #ff0000, #cc0000, #ff0000);
            padding: 10px;
            font-weight: 900;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 3px;
            color: #fff;
            animation: bannerPulse 1.5s infinite;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        @keyframes bannerPulse { 0%,100% { opacity: 1; } 50% { opacity: 0.7; } }
        .icon { font-size: 4rem; color: #ff0000; animation: pulse 1s infinite; margin-bottom: 10px; }
        @keyframes pulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.08); } }
        h1 { color: #ff0000; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 5px; text-shadow: 0 0 40px rgba(255,0,0,0.3); margin-bottom: 10px; }
        .subtitle { color: #ff4444; font-size: 1rem; letter-spacing: 2px; margin-bottom: 20px; }
        .hacker-name { color: #00ff00; font-size: 1.2rem; margin: 20px 0; }
        .info { color: #888; font-size: 0.8rem; margin-top: 30px; border-top: 1px solid #222; padding-top: 20px; }
        .info span { color: #ff0000; }
        .block-overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.85); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column; backdrop-filter: blur(5px);
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #ff0000; animation: pulse 1s infinite; }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
        <div class="sub-msg" style="color:#888;font-size:0.9rem;margin-top:10px;">Tentativa de acesso não autorizada detectada</div>
    </div>

    {{MUSICA}}

    <div class="container">
        <div class="banner">⚠️ SISTEMA COMPROMETIDO - ACESSO NEGADO ⚠️</div>
        <div class="icon">💀</div>
        <h1>{{NOME_TROPA}}</h1>
        <div class="subtitle">🔴 {{TITULO}}</div>
        <div class="hacker-name">👤 Hacker: {{NOME_HACKER}}</div>
        <p style="color:#aaa;font-size:1rem;margin:20px 0;border-left:3px solid #ff0000;padding-left:15px;text-align:left;">
            ❗ Este sistema foi completamente comprometido. Todos os dados críticos estão sob nosso controle.
        </p>
        <div class="info">
            <span>⚠️</span> {{DATA}} <span>⚠️</span>
        </div>
    </div>

    <script>
        let overlayTimeout;
        function showBlockOverlay(msg) {
            const overlay = document.getElementById('blockOverlay');
            overlay.querySelector('.msg').innerText = '⛔ ' + msg;
            overlay.classList.add('show');
            clearTimeout(overlayTimeout);
            overlayTimeout = setTimeout(() => overlay.classList.remove('show'), 2000);
        }
        document.addEventListener('contextmenu', e => { e.preventDefault(); showBlockOverlay('CLIQUE DIREITO BLOQUEADO'); });
        document.addEventListener('keydown', e => {
            if ([123,122,121,120].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('TECLA ' + e.key + ' BLOQUEADA'); return; }
            if (e.ctrlKey && e.shiftKey && [73,74,67].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('INSPEÇÃO BLOQUEADA'); return; }
            if (e.ctrlKey && [85,83,80].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('AÇÃO BLOQUEADA'); return; }
        });
        ['copy','paste','cut','selectstart','dragstart'].forEach(ev => {
            document.addEventListener(ev, e => { e.preventDefault(); if (!['selectstart','dragstart'].includes(ev)) showBlockOverlay('AÇÃO BLOQUEADA'); });
        });
    </script>
</body>
</html>
EOF

echo -e "${GREEN}✅ Template 1: Tropa do Xoinho${RESET}"

# Template 2: Dark Hacker
cat > templates/dark_hacker.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>💀 {{TITULO}} - {{NOME_TROPA}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; cursor: default; }
        body {
            background: #0d0d0d;
            color: #fff;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(ellipse at center, #1a0000, #0a0a0a);
        }
        .container {
            max-width: 900px;
            width: 100%;
            background: rgba(10,10,10,0.9);
            border: 2px solid #660000;
            box-shadow: 0 0 80px rgba(100,0,0,0.5), inset 0 0 80px rgba(100,0,0,0.1);
            padding: 50px 40px;
            text-align: center;
            border-radius: 4px;
            backdrop-filter: blur(5px);
        }
        .glitch {
            font-size: 3.5rem;
            color: #ff0000;
            text-shadow: 0 0 20px rgba(255,0,0,0.8), 0 0 40px rgba(255,0,0,0.4);
            animation: glitch 2s infinite;
            letter-spacing: 5px;
            font-weight: 900;
        }
        @keyframes glitch {
            0%, 100% { transform: skew(0deg); }
            20% { transform: skew(2deg); text-shadow: 2px 0 #00ff00, -2px 0 #ff0000; }
            40% { transform: skew(-2deg); text-shadow: -2px 0 #00ff00, 2px 0 #ff0000; }
            60% { transform: skew(0deg); }
        }
        .skull { font-size: 6rem; color: #660000; animation: pulse 1.5s infinite; }
        @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
        .hacker { color: #00ff00; font-size: 1.2rem; margin: 20px 0; letter-spacing: 2px; }
        .hacker::before { content: '> '; color: #ff0000; }
        .info { color: #444; font-size: 0.8rem; margin-top: 30px; border-top: 1px solid #1a1a1a; padding-top: 20px; }
        .info span { color: #660000; }
        .block-overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.9); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column; backdrop-filter: blur(5px);
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #ff0000; animation: pulse 1s infinite; }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
    </div>

    {{MUSICA}}

    <div class="container">
        <div class="skull">💀</div>
        <div class="glitch">{{NOME_TROPA}}</div>
        <div style="color:#660000;font-size:0.9rem;letter-spacing:3px;margin:10px 0;">⚡ {{TITULO}} ⚡</div>
        <div class="hacker">{{NOME_HACKER}}</div>
        <div style="border:1px solid #1a1a1a;padding:15px;margin:20px 0;color:#888;font-size:0.9rem;text-align:left;">
            [SISTEMA] Acesso negado.<br>
            [STATUS] Comprometido em nível root.<br>
            [DADOS] Extraídos e criptografados.
        </div>
        <div class="info"><span>💀</span> {{DATA}} <span>💀</span></div>
    </div>

    <script>
        let overlayTimeout;
        function showBlockOverlay(msg) {
            const overlay = document.getElementById('blockOverlay');
            overlay.querySelector('.msg').innerText = '⛔ ' + msg;
            overlay.classList.add('show');
            clearTimeout(overlayTimeout);
            overlayTimeout = setTimeout(() => overlay.classList.remove('show'), 2000);
        }
        document.addEventListener('contextmenu', e => { e.preventDefault(); showBlockOverlay('BLOQUEADO'); });
        document.addEventListener('keydown', e => {
            if ([123,122,121,120].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('BLOQUEADO'); return; }
            if (e.ctrlKey && e.shiftKey && [73,74,67].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('BLOQUEADO'); return; }
            if (e.ctrlKey && [85,83,80].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('BLOQUEADO'); return; }
        });
        ['copy','paste','cut','selectstart','dragstart'].forEach(ev => {
            document.addEventListener(ev, e => { e.preventDefault(); if (!['selectstart','dragstart'].includes(ev)) showBlockOverlay('BLOQUEADO'); });
        });
    </script>
</body>
</html>
EOF

echo -e "${GREEN}✅ Template 2: Dark Hacker${RESET}"

# Template 3: Cyber Elite
cat > templates/cyber_elite.html << 'EOF'
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 {{TITULO}} - {{NOME_TROPA}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; cursor: default; }
        body {
            background: #000;
            color: #fff;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #000022, #000011);
        }
        .container {
            max-width: 900px;
            width: 100%;
            background: rgba(0,20,40,0.8);
            border: 2px solid #00ffff;
            box-shadow: 0 0 60px rgba(0,255,255,0.2), inset 0 0 60px rgba(0,255,255,0.05);
            padding: 40px;
            text-align: center;
            border-radius: 16px;
            backdrop-filter: blur(10px);
        }
        .neon-title {
            font-size: 2.8rem;
            color: #00ffff;
            text-shadow: 0 0 30px rgba(0,255,255,0.5), 0 0 60px rgba(0,255,255,0.2);
            letter-spacing: 8px;
            font-weight: 900;
        }
        .neon-sub {
            color: #0088ff;
            font-size: 1rem;
            letter-spacing: 4px;
            margin: 10px 0;
        }
        .hacker-name {
            color: #00ff88;
            font-size: 1.2rem;
            margin: 20px 0;
            border: 1px solid rgba(0,255,255,0.2);
            padding: 10px 30px;
            display: inline-block;
            border-radius: 30px;
            background: rgba(0,255,255,0.05);
        }
        .data-grid {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 15px;
            margin: 30px 0;
        }
        .data-item {
            background: rgba(0,20,40,0.5);
            border: 1px solid rgba(0,255,255,0.1);
            padding: 15px;
            border-radius: 8px;
        }
        .data-item .num { color: #00ffff; font-size: 1.5rem; font-weight: 900; }
        .data-item .label { color: #0088ff; font-size: 0.7rem; text-transform: uppercase; }
        .info { color: #004466; font-size: 0.8rem; margin-top: 20px; border-top: 1px solid rgba(0,255,255,0.1); padding-top: 20px; }
        .info span { color: #00ffff; }
        .block-overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.9); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column; backdrop-filter: blur(5px);
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #00ffff; animation: pulse 1s infinite; }
        @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
    </div>

    {{MUSICA}}

    <div class="container">
        <div style="font-size:3rem;">🚀</div>
        <div class="neon-title">{{NOME_TROPA}}</div>
        <div class="neon-sub">⚡ {{TITULO}} ⚡</div>
        <div class="hacker-name">👤 {{NOME_HACKER}}</div>
        <p style="color:#88ccff;font-size:0.9rem;margin:20px 0;">Sistema comprometido. Dados extraídos com sucesso.</p>
        <div class="data-grid">
            <div class="data-item"><div class="num">100%</div><div class="label">Comprometido</div></div>
            <div class="data-item"><div class="num">∞</div><div class="label">Acesso</div></div>
            <div class="data-item"><div class="num">0</div><div class="label">Defesas</div></div>
        </div>
        <div class="info"><span>🚀</span> {{DATA}} <span>🚀</span></div>
    </div>

    <script>
        let overlayTimeout;
        function showBlockOverlay(msg) {
            const overlay = document.getElementById('blockOverlay');
            overlay.querySelector('.msg').innerText = '⛔ ' + msg;
            overlay.classList.add('show');
            clearTimeout(overlayTimeout);
            overlayTimeout = setTimeout(() => overlay.classList.remove('show'), 2000);
        }
        document.addEventListener('contextmenu', e => { e.preventDefault(); showBlockOverlay('BLOQUEADO'); });
        document.addEventListener('keydown', e => {
            if ([123,122,121,120].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('BLOQUEADO'); return; }
            if (e.ctrlKey && e.shiftKey && [73,74,67].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('
