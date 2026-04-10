import time
import random
from datetime import datetime
from playwright.sync_api import sync_playwright

URL = "https://sites.google.com/view/samuymau"

inicio_global = datetime(2026, 4, 10, 13, 39)
fin_global = datetime(2026, 4, 13, 15, 45)

hora_inicio = (7, 45)
hora_fin = (22, 45)

def dentro_horario():
    ahora = datetime.now()
    if ahora < inicio_global or ahora > fin_global:
        return False

    actual = ahora.hour*60 + ahora.minute
    inicio = hora_inicio[0]*60 + hora_inicio[1]
    fin = hora_fin[0]*60 + hora_fin[1]

    return inicio <= actual <= fin


def simular():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL)
        time.sleep(random.randint(5, 10))

        duracion = random.randint(180, 240)
        inicio = time.time()

        while time.time() - inicio < duracion:
            page.mouse.wheel(0, random.randint(200, 800))
            time.sleep(random.randint(3, 6))

        browser.close()


while True:
    if dentro_horario():
        print("👤 visita nube")
        simular()
        time.sleep(random.randint(800, 1000))
    else:
        print("⏸ fuera horario")
        time.sleep(300)