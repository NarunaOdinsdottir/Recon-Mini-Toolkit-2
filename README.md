# Recon-Mini-Toolkit-2
# Nachtatem’s Vault — Python-Mittwochs-Missionen 🐉🏜️

**Willkommen zurück, Wanderer.**

Du kennst bereits Nachtatem — den alten Drachen, der in den Ruinen der digitalen Ödnis wacht. Dieses Repo ist seine neueste Sammlung: kleine, handliche Python-Tools für deine Mittwochs-Missionen. Alles sauber kommentiert, mit Sicherheitshinweisen und bereit für dein GitHub-Vault.

---

## ⚔️ Warum diese Tools?

Die Ödnis ist voller vergessener Maschinen, zerfetzter Logs und offener Türen. Nachtatem hat entschieden, du brauchst einen Satz zuverlässiger Werkzeuge, um:

* Logs zu durchforsten und IPs Fehler zu sammeln
* Tastatur-Events sicher zu untersuchen (nur sichtbar — Lernmodus)
* Screenshots automatisiert zu erstellen
* Subnetze per Ping zu prüfen
* Alles bequem über ein CLI-Toolkit zu starten

Kurz: kleine, praktische Python-Projekte für Security-Learning — verantwortungsbewusst und dokumentiert.

---

## 🗂️ Inhalt (Module)

### 1) Logfile-Parser — `parse_logs.py`

**Was es tut:** Liest Logdateien, extrahiert IPv4-Adressen und markiert Zeilen mit Fehler-Keywords (error, fail, exception, etc.).

**Output:** Zwei CSV-Dateien in `./out/` — `*_ips.csv` und `*_errors.csv`.

**Warum nützlich:** Schnell einen Überblick über beteiligte Hosts und Fehlerquellen bekommen.

---

### 2) Keyboard Listener — Lernvariante — `keyboard_listener_safe.py`

**Was es tut:** Lauscht auf Tastendrücke und zeigt sie live in der Konsole. Keine Speicherung, keine Übertragung.

**Wichtig:** Startet nur nach ausdrücklicher Zustimmung, sichtbar, endet mit `ESC`. Nicht für heimliche Überwachung verwenden.

---

### 3) Screenshot-Tool — `screenshot_tool.py`

**Was es tut:** Erstellt zeitgestempelte Screenshots (ganzer Bildschirm oder Bereich) und speichert sie in `./screenshots/`.

**Abhängigkeiten:** `pyautogui`, `pillow`. Auf Linux ggf. zusätzliche X11/Wayland-Pakete.

---

### 4) Ping-Sweeper — `ping_sweeper.py`

**Was es tut:** Pinget ein Subnetz (z. B. `192.168.1.0/24`) parallel und gibt erreichbare Hosts zurück.

**Hinweis:** ICMP kann in manchen Netzwerken geblockt sein — scanne nur mit Erlaubnis.

---

### 5) CLI-Toolkit — `hack_toolkit.py`

**Was es tut:** Bündelt die Module unter einer einfachen CLI (Subcommands: `parse`, `screenshot`, `ping`, `listenkeys`). Dein kleiner Pip-Boy für den Alltag.

**Beispiel:** `python hack_toolkit.py parse sample.log`

---

## 🚀 Schnellstart (so wie Nachtatem es mag)

1. Virtuelle Umgebung anlegen

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

2. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

**requirements.txt** (Minimalbeispiel)

```
pynput
pyautogui
pillow
```

3. Tools starten

```bash
# Log parsen
python hack_toolkit.py parse examples/sample.log

# Screenshot
python hack_toolkit.py screenshot

# Ping Sweep
python hack_toolkit.py ping 192.168.1.0/24

# Keyboard Listener (sichtbar, Lernzweck)
python hack_toolkit.py listenkeys
```

---

## 🔒 Sicherheits- & Legal-Hinweis (Nachtatem sagt: ernst nehmen)

Diese Tools sind für **Lernzwecke** und Ethical Hacking in **kontrollierten Umgebungen** gedacht. Missbrauch ist verboten.

* **Keylogger/Listener:** Nur auf eigenen Geräten, sichtbar, mit Zustimmung.
* **Netzwerk-Scanning:** Nur in Netzwerken, für die du Erlaubnis hast.
* **Keine Persistenz, keine Datenweitergabe:** Die Beispielskripte speichern oder übertragen keine sensiblen Daten.

Missbrauch kann rechtliche Folgen haben. Nachtatem beobachtet — und straft Leichtsinn.

---

## 🧪 Beispiele & Tests

Im Ordner `examples/` liegt `sample.log` für Tests mit `parse_logs.py`. Du kannst `parse_logs.py` gegen diese Datei laufen lassen, um die CSV-Ausgabe zu sehen.

Erweiterungen mit Unit-Tests (pytest) sind willkommen — bring deine PRs in den Drachenhort.

---

## 🛠️ Roadmap / Erweiterungen

* Realtime `log_watch` mit Alerts (Poll oder inotify)
* Optionaler `nmap`-Wrapper (nur wenn `nmap` installiert und erlaubt)
* Einfache Flask-UI: Vault-Console (Hosts, Alerts, Screenshots)
* Mehr Tests + CI (GitHub Actions)

---

## 🐉 Contributing

Fork, branch, PR. Kleine Commits, gute Messages (`feat:`, `fix:`, `docs:`). Bitte Sicherheitsanmerkungen zu neuen Modulen hinzufügen.

---

## 🧾 Lizenz

MIT — nutze die Werkzeuge verantwortungsbewusst.

---


Sag mir, welche Extras du willst — Nachtatem ist bereit.
