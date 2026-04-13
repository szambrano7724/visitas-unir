import asyncio
from playwright.async_api import async_playwright
import random

URL = "https://sites.google.com/view/samuymau"

async def simular():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1280, "height": 720}
        )
        page = await context.new_page()

        print("➡️ Visitando página...")
        await page.goto(URL)

        # Espera inicial (muy importante)
        await page.wait_for_timeout(random.randint(8000, 12000))

        # Scroll humano
        for _ in range(random.randint(3, 6)):
            await page.mouse.wheel(0, random.randint(500, 1200))
            await page.wait_for_timeout(random.randint(2000, 4000))

        # Tiempo final
        await page.wait_for_timeout(random.randint(5000, 10000))

        print("✔️ Visita completada")
        await browser.close()


async def main():
    while True:
        await simular()

        # Espera entre visitas (15 min aprox)
        espera = random.randint(800, 1000)
        print(f"⏳ Esperando {espera} segundos...")
        await asyncio.sleep(espera)

asyncio.run(main())
