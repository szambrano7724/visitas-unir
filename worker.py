from playwright.sync_api import sync_playwright
import os
import time
import random
from datetime import datetime

# Instalar navegador (seguro en Render)
os.system("playwright install chromium")

URL = "https://sites.google.com/view/samuymau"

def dentro_horario():
    ahora = datetime.now().time()
    return ahora >= datetime.strptime("07:45", "%H:%M").time() and ahora <= datetime.strptime("22:45", "%H:%M").time()

def simular_visita():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("➡️ Visitando página...")
        page.goto(URL)

        duracion = random.randint(180, 240)  # 3 a 4 min

        inicio = time.time()
        while time.time() - inicio < duracion:
            scroll = random.randint(200, 800)
            page.mouse.wheel(0, scroll)
            time.sleep(random.randint(5, 15))

        browser.close()
        print("✅ Visita terminada")

# 🔁 LOOP INFINITO (LO QUE FALTABA)
while True:
    if dentro_horario():
        simular_visita()
        espera = random.randint(600, 900)  # 10 a 15 min
        print(f"⏳ Esperando {espera/60:.1f} minutos...")
        time.sleep(espera)
    else:
        print("🌙 Fuera de horario...")
        time.sleep(300)
