<div align="center">
  <h1>Cloud-Native Homelab & DevOps Workspace</h1>
  <p>Prywatne centrum danych i zintegrowane srodowisko do nauki architektury chmurowej, automatyzacji i nowoczesnego programowania.</p>

  <img src="https://img.shields.io/badge/Proxmox-E57000?style=flat-square&logo=proxmox&logoColor=white" alt="Proxmox" />
  <img src="https://img.shields.io/badge/Tailscale-FFFFFF?style=flat-square&logo=tailscale&logoColor=black" alt="Tailscale" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white" alt="C++" />
  <img src="https://img.shields.io/badge/PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes" />
  <img src="https://img.shields.io/badge/CI%2FCD-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="CI/CD" />
</div>

***

## Cel Projektu
Repozytorium stanowi dokumentacje oraz kod zrodlowy prywatnego srodowiska serwerowego. Projekt to fizyczny poligon doswiadczalny wdrazajacy koncepcje Infrastructure as Code (IaC), Zero Trust Network, ciaglej integracji i konteneryzacji.

## Architektura i Tech Stack

### 1. Wirtualizacja i Infrastruktura (Bare-Metal)
- Proxmox VE: Glowny hiperwizor do zarzadzania zasobami.
- LXC & ZFS: Lekkie kontenery dla uslug bazowych z systemem plikow odpornym na korupcje danych.
- Tiered Storage: Separacja warstw wejscia/wyjscia (NVMe na system, SSD SATA na kopie, HDD na archiwum).

### 2. Siec i Zabezpieczenia (NetSec)
- Tailscale: Dostep oparty na szyfrowanym Mesh VPN.
- Pi-hole z MagicDNS: Izolacja ruchu, lokalne rozwiazywanie nazw.
- SSH Key-Based Auth: Calkowite wylaczenie uwierzytelniania haslem na rzecz kluczy Ed25519.

### 3. Srodowisko Deweloperskie (Dev Workspace)
- VS Code Remote-SSH: Plynna praca na izolowanym srodowisku linuksowym.
- Python: Kod pisany z zachowaniem Type Hints oraz standardow PEP 8.
- C++ (Standard C++20): Implementacja narzedzi CLI przy uzyciu Smart Pointers.

## Roadmap i Cele Edukacyjne

### Faza 1: Fundamenty i Kodowanie (Zakonczona)
- [x] Wdrozenie Proxmox VE, kontenerow LXC i sieci Tailscale.
- [x] Podpiecie automatycznych powiadomien pod Discord.
- [x] Utworzenie ustandaryzowanego srodowiska deweloperskiego.

### Faza 2: Bazy Danych i Continuous Integration (CI/CD)
- [ ] Bazy Danych (SQL): Wdrozenie relacyjnej bazy danych do logow systemowych.
- [ ] Docker: Wdrozenie uslug zewnetrznych (Jellyfin, Immich).
- [ ] CI/CD Pipelines: Implementacja procesow GitHub Actions.

### Faza 3: Architektura Chmurowa (Cloud-Native & Orchestration)
- [ ] Kubernetes (K8s): Migracja uslug do pelnoprawnego klastra.
- [ ] Infrastructure as Code (IaC): Automatyzacja powolywania srodowisk (Terraform/Ansible).