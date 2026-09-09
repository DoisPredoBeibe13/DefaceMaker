#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
import subprocess
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
║  {BOLD}{CYAN}🔰 DEFACEMAKER v2.0 - Gerador de Deface Pages{RESET}{RED}     ║
║  {BOLD}{WHITE}By: Tropa do Xoinho - Para Fins Educacionais{RESET}{RED}     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{RESET}
"""

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    clear_screen()
    print(BANNER)
    print(f"\n{BOLD}{YELLOW}[+] Gerando Deface Page...{RESET}\n")

def get_user_input():
    """Coleta as informações do usuário"""
    print(f"{BOLD}{CYAN}📝 INFORMAÇÕES DO DEFACE{RESET}\n")
    
    # Nome da tropa/grupo
    nome_tropa = input(f"{BOLD}{WHITE}🏴 Nome da Tropa/Grupo: {RESET}")
    if not nome_tropa:
        nome_tropa = "Tropa do Xoinho"
    
    # Nome do hacker
    nome_hacker = input(f"{BOLD}{WHITE}👤 Nome do Hacker: {RESET}")
    if not nome_hacker:
        nome_hacker = "Xoinho"
    
    # Título da página
    titulo = input(f"{BOLD}{WHITE}📌 Título do Deface: {RESET}")
    if not titulo:
        titulo = "SISTEMA BLOQUEADO"
    
    # URL da música (opcional)
    print(f"\n{BOLD}{YELLOW}🎵 MÚSICA DE FUNDO (OPCIONAL){RESET}")
    print(f"{CYAN}💡 Dica: Hospede o áudio no:{RESET}")
    print(f"   • {WHITE}https://pomf2.lain.la{RESET} (grátis, sem registro)")
    print(f"   • {WHITE}https://catbox.moe{RESET} (grátis, sem registro)")
    print(f"   • {WHITE}https://upfiles.com{RESET} (grátis, sem registro)")
    print(f"   • {WHITE}https://soundcloud.com{RESET} (precisa de conta)\n")
    
    musica_url = input(f"{BOLD}{WHITE}🔗 URL da música (ENTER para pular): {RESET}")
    
    # Escolher estilo
    print(f"\n{BOLD}{CYAN}🎨 ESTILOS DISPONÍVEIS{RESET}\n")
    print(f"  {BOLD}{WHITE}1.{RESET} 🎯 {CYAN}Tropa do Xoinho{RESET} - Estilo hacker clássico")
    print(f"  {BOLD}{WHITE}2.{RESET} 💀 {PURPLE}Dark Hacker{RESET} - Visual sombrio e agressivo")
    print(f"  {BOLD}{WHITE}3.{RESET} 🚀 {BLUE}Cyber Elite{RESET} - Estilo futurista neon")
    print(f"  {BOLD}{WHITE}4.{RESET} 👻 {WHITE}Ghost Squad{RESET} - Minimalista e misterioso")
    print(f"  {BOLD}{WHITE}5.{RESET} 🔴 {RED}Red Alert{RESET} - Alerta vermelho intenso\n")
    
    while True:
        try:
            estilo = int(input(f"{BOLD}{WHITE}Escolha um estilo (1-5): {RESET}"))
            if 1 <= estilo <= 5:
                break
            else:
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

def load_template(estilo):
    """Carrega o template HTML baseado no estilo"""
    templates = {
        1: 'templates/tropa_do_xoinho.html',
        2: 'templates/dark_hacker.html',
        3: 'templates/cyber_elite.html',
        4: 'templates/ghost_squad.html',
        5: 'templates/red_alert.html'
    }
    
    template_path = templates.get(estilo)
    if not template_path or not os.path.exists(template_path):
        print(f"{RED}❌ Template não encontrado: {template_path}{RESET}")
        sys.exit(1)
    
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()

def generate_deface(data):
    """Gera a página de deface com os dados do usuário"""
    template = load_template(data['estilo'])
    
    # Substitui os placeholders
    html = template.replace('{{NOME_TROPA}}', data['nome_tropa'])
    html = html.replace('{{NOME_HACKER}}', data['nome_hacker'])
    html = html.replace('{{TITULO}}', data['titulo'])
    html = html.replace('{{DATA}}', data['data'])
    
    # Música
    if data['musica_url']:
        musica_html = f'''
        <!-- Música de fundo -->
        <audio id="bg-music" autoplay loop>
            <source src="{data['musica_url']}" type="audio/mpeg">
            <source src="{data['musica_url']}" type="audio/ogg">
            <source src="{data['musica_url']}" type="audio/wav">
            Seu navegador não suporta áudio.
        </audio>
        <script>
            // Controle de volume (50%)
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
    print(f"\n{BOLD}{GREEN}✅ DEFACE GERADO COM SUCESSO!{RESET}\n")
    print(f"{BOLD}{WHITE}📁 Arquivo:{RESET} {filepath}")
    print(f"{BOLD}{WHITE}🏴 Tropa:{RESET} {data['nome_tropa']}")
    print(f"{BOLD}{WHITE}👤 Hacker:{RESET} {data['nome_hacker']}")
    print(f"{BOLD}{WHITE}🎵 Música:{RESET} {data['musica_url'] if data['musica_url'] else 'Nenhuma'}")
    
    print(f"\n{BOLD}{CYAN}📖 COMO HOSPEDAR A MÚSICA DE GRAÇA:{RESET}")
    print(f"""
{WHITE}1. Acesse https://pomf2.lain.la
2. Clique em "Upload" e selecione seu arquivo de áudio (MP3)
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
    
    # Coleta dados
    data = get_user_input()
    
    print(f"\n{BOLD}{YELLOW}⏳ Gerando página...{RESET}")
    time.sleep(1)
    
    # Gera HTML
    html = generate_deface(data)
    
    # Salva arquivo
    filepath = save_deface(html, data)
    
    # Mostra resultado
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
