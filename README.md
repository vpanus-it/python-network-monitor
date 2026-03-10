# python-network-monitor
# 🌐 Python Network Monitor

**🚧 WORK IN PROGRESS (Aktivní vývoj) 🚧**

Tento repozitář obsahuje jednoduchý nástroj pro monitorování dostupnosti zařízení v síti pomocí ICMP protokolu (Ping). Projekt vyvíjím ve svém volném čase za účelem propojení mých znalostí z oblasti počítačových sítí (příprava na Cisco certifikaci) a objektově orientovaného programování v Pythonu.

## 🚀 Jak to funguje
Skript aktuálně prochází statický seznam IP adres a pomocí systémových nástrojů na pozadí zjišťuje jejich dostupnost. Výstupem je přehledný log v konzoli, který barevně/textově odliší online a offline zařízení.

## 🛠️ Použité technologie a principy
* **Python 3** (Standardní knihovny `subprocess` a `platform`)
* **Objektově orientované programování (OOP):** Logika je zapouzdřena ve třídě `NetworkMonitor`, což usnadňuje budoucí rozšiřování kódu.
* **Cross-platform kompatibilita:** Skript automaticky detekuje operační systém (Windows vs. Linux) a dynamicky upravuje parametry pro příkaz `ping` (`-n` vs `-c`).
* **Error Handling:** Ošetření chyb pomocí bloků `try-except` pro případ selhání systémového volání.

## 📌 Plánované funkce a opravy (To-Do list)
Projekt je v aktivním vývoji. Aktuálně pracuji na implementaci následujících bodů:

- [ ] **Oprava falešně pozitivních pingů (Bugfix):** Aktuálně systémový ping ve Windows vrací úspěšný kód `0` i při vypršení časového limitu (např. u neplatné IP "1"). Plánuji přepsat validaci tak, aby parsovala textový výstup a hledala hodnotu `TTL=`.
- [ ] **Externí vstupy:** Nahrazení statického seznamu IP adres načítáním ze souborů `.txt` nebo `.csv`.
- [ ] **Export výsledků:** Zápis výsledků monitoringu (Online/Offline) včetně časového razítka do logovacího souboru.

---
*Autor: Vojta Panuš*
