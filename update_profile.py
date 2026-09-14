#!/usr/bin/env python3
"""
Automated GitHub Profile README Generator & Sync Engine
Author: Jay Yogendrakumar Patel (@jaypatel29042008-glitch)

Usage:
  python update_profile.py          # Regenerates README.md from profile_data.json
  python update_profile.py --push   # Regenerates README.md, commits, and pushes to GitHub
"""

import json
import os
import sys
import subprocess
from datetime import datetime

sys.stdout.reconfigure(encoding='utf-8')

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(DIR_PATH, "profile_data.json")
README_FILE = os.path.join(DIR_PATH, "README.md")

def load_data():
    if not os.path.exists(DATA_FILE):
        print(f"[!] Error: {DATA_FILE} not found.")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_markdown(data):
    p = data.get("personal", {})
    honors = data.get("major_honors", [])
    sims = data.get("internships_and_simulations", [])
    projects = data.get("flagship_projects", [])
    certs = data.get("certifications", [])
    
    today_str = datetime.now().strftime("%B %d, %Y")
    
    typing_lines = (
        "ISRO+Bharatiya+Antariksh+Hackathon+Grand+Finale+Finalist;"
        "Google+Cloud+Gen+AI+Academy+Selected+APAC+Builder;"
        "Building+Autonomous+Agentic+Systems+%26+LLM+Routing+Gateways;"
        "B.Tech+Computer+Engineering+%40+LDRP-ITR%2C+GTU;"
        "Generative+AI+%28Diffusion+%26+GANs%29+%E2%80%A2+MCP+%E2%80%A2+Azure"
    )

    md = []
    
    # 1. CLEAN TOP HEADER WITH REAL NAME
    md.append('<div align="center">')
    md.append(f'  <h1>{p.get("name", "Jay Yogendrakumar Patel")}</h1>')
    md.append(f'  <h3>{p.get("tagline", "")}</h3>')
    md.append(f'  <p><b>{p.get("education", "")}</b></p>')
    md.append('')
    
    # BADGES - Inline without extra breaks or dead links to prevent broken image / stacking bugs
    md.append('  <p align="center">')
    md.append('    <img src="https://img.shields.io/badge/ISRO_Hackathon-Grand_Finale_Finalist-F59E0B?style=for-the-badge&logo=spacex&logoColor=white" alt="ISRO Finalist" />&nbsp;')
    md.append('    <img src="https://img.shields.io/badge/Google_Cloud-Selected_APAC_Builder-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white" alt="Google Cloud Builder" />&nbsp;')
    md.append('    <img src="https://img.shields.io/badge/IBM_SkillsBuild-Agentic_AI_Certified-0062FF?style=for-the-badge&logo=ibm&logoColor=white" alt="IBM Certified" />&nbsp;')
    md.append('    <img src="https://img.shields.io/badge/GitHub_Pro-Student_Pack-0969DA?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Pro" />')
    md.append('  </p>')
    md.append('')
    
    # ANIMATED TYPING (Direct image, no git.io anchor wrapper)
    md.append(f'  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=19&duration=2800&pause=1000&color=38BDF8&center=true&vCenter=true&width=700&lines={typing_lines}" alt="Typing Headline" />')
    md.append('</div>')
    md.append('')
    
    # BIO BLOCK (From Jay_Patel_GitHub_Profile_Content.pdf)
    md.append('> **About Me**: ' + p.get("bio_block", ""))
    md.append('>')
    md.append('> **Focus Areas**: ' + p.get("focus_areas", ""))
    md.append('')
    md.append('---')
    md.append('')

    # SYSTEM TELEMETRY (TERMINAL NEOFETCH)
    md.append('### ⚡ System Telemetry & Verified Profile')
    md.append('')
    md.append('```zsh')
    md.append('jaypatel@frontier-workstation:~$ neofetch --profile')
    md.append('----------------------------------------------------')
    md.append(f'Candidate    : {p.get("name", "Jay Yogendrakumar Patel")}')
    md.append(f'Education    : {p.get("education", "")}')
    md.append(f'Location     : {p.get("location", "")}')
    md.append('Specialization: Autonomous Agent Loops, LLM Gateway Routing & Remote Sensing Diffusion')
    md.append('Honors       : ISRO Bharatiya Antariksh Hackathon Finalist • Google Cloud APAC Builder')
    md.append('Leadership   : GeeksforGeeks Campus Mantri (LDRP-ITR) • SIH 2026 Team Lead')
    md.append('Internships  : IBM SkillsBuild × AICTE (Active) • CodeAlpha AI Intern (Completed)')
    md.append('Simulations  : Deloitte Technology • JPMorgan Chase Software Eng • PwC US Consulting')
    md.append('Status       : 🟢 Engineering robust agentic workflows & next-generation AI architectures')
    md.append('```')
    md.append('')
    md.append('---')
    md.append('')

    # MAJOR HONORS & HACKATHONS
    md.append('### 🏆 Major Honors, Hackathons & Community Leadership')
    md.append('')
    md.append('<table width="100%">')
    for i in range(0, len(honors), 2):
        md.append('  <tr>')
        for j in range(2):
            if i + j < len(honors):
                h = honors[i + j]
                md.append('    <td width="50%" valign="top">')
                md.append(f'      <b>{h["title"]}</b> &nbsp; <img src="https://img.shields.io/badge/{h["badge"].replace(" ", "_")}-{h.get("badge_color", "38BDF8")}?style=flat-square" /><br/>')
                md.append(f'      <sub>{h["desc"]}</sub>')
                md.append('    </td>')
            else:
                md.append('    <td width="50%" valign="top"></td>')
        md.append('  </tr>')
    md.append('</table>')
    md.append('')
    md.append('---')
    md.append('')

    # INDUSTRY EXPERIENCES & SIMULATIONS
    md.append('### 💼 Verified Industry Programs & Applied Simulations')
    md.append('')
    md.append('| Organization / Program | Role / Focus | Verification / Track | Core Engineering Impact |')
    md.append('|---|---|---|---|')
    for s in sims:
        md.append(f'| **{s["program"]}** | `{s["role"]}` | {s["period"]} | {s["desc"]} |')
    md.append('')
    md.append('---')
    md.append('')

    # ARCHITECTURE BLUEPRINT
    md.append('### 🧩 Autonomous Agent & Multi-Model Routing Architecture')
    md.append('')
    md.append('My local development environment integrates autonomous agentic loops, token preservation pipelines, and resilient multi-provider gateways:')
    md.append('')
    md.append('```')
    md.append('                    ┌─────────────────────────────────────────┐')
    md.append('                    │      Client / Prompt Engineering        │')
    md.append('                    │   (Claude Code / VS Code / Terminal)    │')
    md.append('                    └────────────────────┬────────────────────┘')
    md.append('                                         │')
    md.append('                    ┌────────────────────▼────────────────────┐')
    md.append('                    │       OmniRoute Local Gateway           │')
    md.append('                    │      (Dynamic Multi-Model Router)       │')
    md.append('                    └────────────┬───────────────────┬────────┘')
    md.append('                                 │                   │')
    md.append('                     ┌───────────▼─────────┐ ┌───────▼──────────────┐')
    md.append('                     │ Primary Frontier    │ │ Resilient Fallback   │')
    md.append('                     │ Copilot / Claude    │ │ Gemini 1M-2M / Free  │')
    md.append('                     └───────────┬─────────┘ └───────┬──────────────┘')
    md.append('                                 │                   │')
    md.append('                                 └─────────┬─────────┘')
    md.append('                                           │')
    md.append('                    ┌──────────────────────▼──────────────────┐')
    md.append('                    │  Token Compression & Context Pruning    │')
    md.append('                    │   (Headroom AST Optimizer • Caveman)    │')
    md.append('                    └─────────────────────────────────────────┘')
    md.append('```')
    md.append('')
    md.append('---')
    md.append('')

    # FLAGSHIP REPOSITORIES (Curated exact projects from PDF)
    md.append('### 🚀 Flagship Repositories & Engineering Artifacts')
    md.append('')
    md.append('<table width="100%">')
    for i in range(0, len(projects), 2):
        md.append('  <tr>')
        for j in range(2):
            if i + j < len(projects):
                proj = projects[i + j]
                tags_str = " ".join([f'<img src="https://img.shields.io/badge/{t.replace(" ", "_")}-24292F?style=flat-square" />' for t in proj.get("stack", [])])
                md.append('    <td width="50%" valign="top">')
                md.append(f'      <h3><a href="{proj["url"]}">{proj["name"]}</a></h3>')
                md.append(f'      <p>{proj["desc"]}</p>')
                md.append(f'      <p>{tags_str}</p>')
                md.append('    </td>')
            else:
                md.append('    <td width="50%" valign="top"></td>')
        md.append('  </tr>')
    md.append('</table>')
    md.append('')
    md.append('---')
    md.append('')

    # CERTIFICATIONS & CREDENTIALS
    md.append('### 📜 Verified Certifications & Credentials')
    md.append('')
    md.append('| Credential Title | Issuing Authority | Date | Verification Status |')
    md.append('|---|---|---|---|')
    for c in certs:
        md.append(f'| **{c["name"]}** | {c["issuer"]} | {c["date"]} | Verified Credential |')
    md.append('')
    md.append('---')
    md.append('')

    # TECHNICAL ARSENAL
    md.append('### 🛠️ Technical Arsenal & Ecosystem')
    md.append('')
    md.append('<div align="center">')
    md.append('')
    md.append('#### Core Programming Languages')
    md.append('<a href="https://skillicons.dev">')
    md.append('  <img src="https://skillicons.dev/icons?i=python,cpp,java,js,html,css,bash" alt="Languages" />')
    md.append('</a>')
    md.append('')
    md.append('<br/>')
    md.append('')
    md.append('#### Frameworks, Web & Cloud Infrastructure')
    md.append('<a href="https://skillicons.dev">')
    md.append('  <img src="https://skillicons.dev/icons?i=flask,nodejs,express,bootstrap,azure,linux,docker" alt="Frameworks & Cloud" />')
    md.append('</a>')
    md.append('')
    md.append('<br/>')
    md.append('')
    md.append('#### Developer Toolchain & Engineering Suite')
    md.append('<a href="https://skillicons.dev">')
    md.append('  <img src="https://skillicons.dev/icons?i=vscode,git,github,githubactions,postman" alt="Dev Tools" />')
    md.append('</a>')
    md.append('')
    md.append('<br/><br/>')
    md.append('')
    md.append('| Technical Discipline | Tooling & Implementations |')
    md.append('|---|---|')
    md.append('| **Autonomous AI & Reasoning** | Multi-agent swarms, LLM router combos (OmniRoute), context compression (Headroom), prompt tuning |')
    md.append('| **Backend & Cloud Services** | Python (FastAPI, Flask), Next.js, Microsoft Azure ($100 Student Tier), Linux (WSL2) |')
    md.append('| **Data Science & ML Pipelines**| PyTorch, GeoTIFF remote sensing, Diffusion models, Scikit-Learn, Pandas, RAG architectures |')
    md.append('| **Productivity & Dev Rig**    | JetBrains Toolbox, Termius SSH, GitKraken, VS Code, Bootstrap Studio, Postman |')
    md.append('')
    md.append('</div>')
    md.append('')
    md.append('---')
    md.append('')

    # REAL-TIME GITHUB ANALYTICS
    md.append('### 📊 Real-Time GitHub Analytics')
    md.append('')
    md.append('<div align="center">')
    md.append('  <table border="0">')
    md.append('    <tr>')
    md.append('      <td align="center">')
    md.append(f'        <a href="{p.get("github")}">')
    md.append(f'          <img src="https://github-readme-stats-fast.vercel.app/api?username={p.get("username")}&show_icons=true&theme=tokyonight&hide_border=true&card_width=450" alt="GitHub Stats" />')
    md.append('        </a>')
    md.append('      </td>')
    md.append('      <td align="center">')
    md.append(f'        <a href="{p.get("github")}">')
    md.append(f'          <img src="https://github-readme-stats-fast.vercel.app/api/top-langs/?username={p.get("username")}&layout=compact&theme=tokyonight&hide_border=true&card_width=350" alt="Top Languages" />')
    md.append('        </a>')
    md.append('      </td>')
    md.append('    </tr>')
    md.append('  </table>')
    md.append('')
    md.append('  <br/>')
    md.append('')
    md.append(f'  <a href="{p.get("github")}">')
    md.append(f'    <img src="https://github-readme-streak-stats.herokuapp.com/?user={p.get("username")}&theme=tokyonight&hide_border=true&card_width=480" alt="GitHub Streak" />')
    md.append('  </a>')
    md.append('</div>')
    md.append('')
    md.append('---')
    md.append('')

    # CONNECT & FOOTER
    md.append('### 🌐 Connect & Verified Identity')
    md.append('')
    md.append('<div align="center">')
    md.append(f'  <a href="{p.get("github")}">')
    md.append(f'    <img src="https://img.shields.io/badge/GitHub-{p.get("username")}-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />')
    md.append('  </a>')
    md.append('  &nbsp;')
    md.append(f'  <a href="{p.get("linkedin")}">')
    md.append('    <img src="https://img.shields.io/badge/LinkedIn-Jay_Patel-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />')
    md.append('  </a>')
    md.append('  &nbsp;')
    md.append(f'  <a href="mailto:{p.get("email")}">')
    md.append(f'    <img src="https://img.shields.io/badge/Email-{p.get("email")}-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />')
    md.append('  </a>')
    md.append('</div>')
    md.append('')
    md.append('<br/>')
    md.append('')
    md.append('<div align="center">')
    md.append(f'  <sub>⚡ <i>"The best way to predict the future is to build autonomous loops that construct it."</i> &nbsp;•&nbsp; Last Synced: {today_str}</sub>')
    md.append('</div>')
    md.append('')
    
    return "\n".join(md)

def update(push=False):
    data = load_data()
    md_content = generate_markdown(data)
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"[+] README.md compiled successfully at: {README_FILE}")
    
    if push:
        print("[*] Committing and pushing changes to GitHub...")
        try:
            subprocess.run(["git", "add", "README.md", "profile_data.json", "update_profile.py"], cwd=DIR_PATH, check=True)
            today_tag = datetime.now().strftime("%Y-%m-%d")
            commit_msg = f"fix(profile): display full name, bio block, and fix badge alignment [{today_tag}]"
            subprocess.run(["git", "commit", "-m", commit_msg], cwd=DIR_PATH, check=True)
            subprocess.run(["git", "push", "origin", "main"], cwd=DIR_PATH, check=True)
            print("[+] Profile successfully deployed live to GitHub!")
            print(f"[*] Live URL: {data.get('personal', {}).get('github', 'https://github.com')}")
        except subprocess.CalledProcessError as e:
            print(f"[!] Git push failed: {e}")

if __name__ == "__main__":
    push_flag = "--push" in sys.argv
    update(push=push_flag)
