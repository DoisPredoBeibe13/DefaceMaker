#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from datetime import datetime

# Cores para terminal
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
║  {BOLD}{CYAN}🔰 DEFACEMAKER v3.0 - Gerador de Deface Pages{RESET}{RED}     ║
║  {BOLD}{WHITE}By: Tropa do Xoinho - Para Fins Educacionais{RESET}{RED}     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{RESET}
"""

# ============================================
# TEMPLATES HTML EMBUTIDOS
# ============================================

TEMPLATES = {
    1: {
        'nome': 'Tropa do Xoinho',
        'icon': '🎯',
        'desc': 'Estilo hacker clássico',
        'html': '''<!DOCTYPE html>
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
        .block-overlay .sub-msg { color: #888; font-size: 0.9rem; margin-top: 10px; }
    </style>
</head>
<body>
    <div class="block-overlay" id="blockOverlay">
        <div class="big-icon">⛔</div>
        <div class="msg">ACESSO BLOQUEADO</div>
        <div class="sub-msg">Tentativa de acesso não autorizada detectada</div>
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
</html>'''
    },
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
        }
        .container {
            max-width: 800px;
            width: 100%;
            background: #0a0a0a;
            border: 1px solid #222;
            padding: 50px 40px;
            text-align: center;
            box-shadow: 0 0 100px rgba(255,255,255,0.02);
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
        }
        .container {
            max-width: 900px;
            width: 100%;
            background: #0a0000;
            border: 3px solid #ff0000;
            box-shadow: 0 0 80px rgba(255,0,0,0.5), inset 0 0 80px rgba(255,0,0,0.05);
            padding: 40px;
            text-align: center;
            animation: borderPulse 2s infinite;
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


def get_user_input():
    """Coleta as informações do usuário"""
    print(f"{BOLD}{CYAN}📝 INFORMAÇÕES DO DEFACE{RESET}\n")
    
    nome_tropa = input(f"{BOLD}{WHITE}🏴 Nome da Tropa/Grupo: {RESET}")
    if not nome_tropa:
        nome_tropa = "Tropa do Xoinho"
    
    nome_hacker = input(f"{BOLD}{WHITE}👤 Nome do Hacker: {RESET}")
    if not nome_hacker:
        nome_hacker = "Xoinho"
    
    titulo = input(f"{BOLD}{WHITE}📌 Título do Deface: {RESET}")
    if not titulo:
        titulo = "SISTEMA BLOQUEADO"
    
    print(f"\n{BOLD}{YELLOW}🎵 MÚSICA DE FUNDO (OPCIONAL){RESET}")
    print(f"{CYAN}💡 Dica: Hospede o áudio em sites grátis:{RESET}")
    print(f"   • {WHITE}https://pomf2.lain.la{RESET}")
    print(f"   • {WHITE}https://catbox.moe{RESET}")
    print(f"   • {WHITE}https://upfiles.com{RESET}\n")
    
    musica_url = input(f"{BOLD}{WHITE}🔗 URL da música (ENTER para pular): {RESET}")
    
    print(f"\n{BOLD}{CYAN}🎨 ESTILOS DISPONÍVEIS{RESET}\n")
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
        'estilo': estilo,
        'data': datetime.now().strftime('%d/%m/%Y %H:%M')
    }


def generate_deface(data):
    """Gera a página de deface com os dados do usuário"""
    template_html = TEMPLATES[data['estilo']]['html']
    
    html = template_html.replace('{{NOME_TROPA}}', data['nome_tropa'])
    html = html.replace('{{NOME_HACKER}}', data['nome_hacker'])
    html = html.replace('{{TITULO}}', data['titulo'])
    html = html.replace('{{DATA}}', data['data'])
    
    if data['musica_url']:
        musica_html = f'''
        <audio id="bg-music" autoplay loop>
            <source src="{data['musica_url']}" type="audio/mpeg">
            <source src="{data['musica_url']}" type="audio/ogg">
            <source src="{data['musica_url']}" type="audio/wav">
            Seu navegador não suporta áudio.
        </audio>
        <script>
            const audio = document.getElementById('bg-music');
            if (audio) {{
                audio.volume = 0.5;
                audio.play().catch(e => console.log('Áudio bloqueado pelo navegador'));
            }}
        </script>
        '''
        html = html.replace('{{MUSICA}}', musica_html)
    else:
        html = html.replace('{{MUSICA}}', '')
    
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
    estilo_nome = TEMPLATES[data['estilo']]['nome']
    
    print(f"\n{BOLD}{GREEN}✅ DEFACE GERADO COM SUCESSO!{RESET}\n")
    print(f"{BOLD}{WHITE}📁 Arquivo:{RESET} {filepath}")
    print(f"{BOLD}{WHITE}🎨 Estilo:{RESET} {estilo_nome}")
    print(f"{BOLD}{WHITE}🏴 Tropa:{RESET} {data['nome_tropa']}")
    print(f"{BOLD}{WHITE}👤 Hacker:{RESET} {data['nome_hacker']}")
    print(f"{BOLD}{WHITE}🎵 Música:{RESET} {data['musica_url'] if data['musica_url'] else 'Nenhuma'}")
    
    print(f"\n{BOLD}{CYAN}📖 COMO HOSPEDAR A MÚSICA DE GRAÇA:{RESET}")
    print(f"""
{WHITE}1. Acesse https://pomf2.lain.la
2. Clique em "Upload" e selecione seu arquivo MP3
3. Copie o link gerado (ex: https://pomf2.lain.la/f/abc123.mp3)
4. Cole o link no campo de música do DefaceMaker
5. Pronto! A música vai tocar automaticamente na página{RESET}
""")
    
    print(f"\n{BOLD}{YELLOW}💡 Para testar localmente:{RESET}")
    print(f"   {WHITE}python3 -m http.server 8080{RESET}")
    print(f"   {WHITE}Acesse: http://localhost:8080/output/{os.path.basename(filepath)}{RESET}")
    
    print(f"\n{BOLD}{GREEN}🔥 Deface pronto para uso!{RESET}\n")


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
