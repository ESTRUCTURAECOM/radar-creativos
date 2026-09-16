# -*- coding: utf-8 -*-
"""
Trae del Radar lo que hay que producir, con los números de HOY.

Lo ejecuta la skill ANTES de escribir ningún creativo, para que la IA no
trabaje de memoria. Es lo que hace que el loop se retroalimente solo.

Uso:
    python traer.py                 -> el ENCARGO de la semana (25 vídeos con
                                       su brief completo, uno a uno)
    python traer.py resumen         -> solo el estado de la cuenta, más corto
    python traer.py brief last_30d  -> el encargo mirando los últimos 30 días

Configuración: cuenta.json, al lado de este archivo. Lo más cómodo es NO
escribirlo a mano: en tu radar, pestaña «El Agente», pulsa «⚙️ Configurar la
skill» y te lo descarga ya relleno. Si lo haces a mano:

    {"url": "https://tu-radar.onrender.com",
     "token": "EAA...",          <- token de Meta con ads_read
     "cuenta": "1234567890",     <- ID de la cuenta publicitaria, sin act_
     "rango": "last_7d"}
"""
import json
import os
import sys
import urllib.request

# La consola de Windows no habla UTF-8 por defecto y el informe viene lleno de
# acentos y emojis: sin esto, el script se cae al imprimir en vez de dar datos.
try:
    if (sys.stdout.encoding or "").lower().replace("-", "") != "utf8":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

AQUI = os.path.dirname(os.path.abspath(__file__))
CONF = os.path.join(AQUI, "cuenta.json")

RANGOS = ("last_7d", "last_14d", "last_30d")
# Qué pedir: el encargo completo (lo normal) o solo el estado de la cuenta.
DESTINOS = {"brief": "/api/brief", "resumen": "/api/briefing"}


def _sin_configurar():
    print("SIN CONFIGURAR: no existe cuenta.json.\n"
          f"Tiene que estar aquí: {CONF}\n\n"
          "La forma fácil: abre tu radar, pestaña «El Agente», pulsa\n"
          "«⚙️ Configurar la skill» y mueve el archivo que se descarga a esa\n"
          "carpeta. No hay que escribir nada.\n\n"
          "A mano, si lo prefieres:\n"
          '{"url": "https://tu-radar.onrender.com", "token": "EAA...", '
          '"cuenta": "1234567890", "rango": "last_7d"}\n'
          "El token se saca en business.facebook.com → Usuarios del sistema →\n"
          "Generar token, con el permiso ads_read.")
    return 1


def main():
    if not os.path.exists(CONF):
        return _sin_configurar()
    try:
        with open(CONF, encoding="utf-8") as f:
            c = json.load(f)
    except json.JSONDecodeError as e:
        print(f"cuenta.json está mal escrito ({e}).\nBórralo y vuelve a "
              "descargarlo desde el radar con «⚙️ Configurar la skill».")
        return 1

    faltan = [k for k in ("url", "token", "cuenta") if not c.get(k)]
    if faltan:
        print(f"A cuenta.json le faltan datos: {', '.join(faltan)}.\n"
              "Vuelve a descargarlo desde el radar con «⚙️ Configurar la skill».")
        return 1

    # Los argumentos pueden venir en cualquier orden: 'brief'/'resumen' y el rango.
    modo, rango = "brief", c.get("rango") or "last_7d"
    for a in sys.argv[1:]:
        a = a.strip().lower()
        if a in DESTINOS:
            modo = a
        elif a in RANGOS:
            rango = a
        elif a in ("7", "14", "30"):
            rango = f"last_{a}d"

    url = c["url"].rstrip("/") + DESTINOS[modo]
    cuerpo = json.dumps({"token": c["token"], "cuenta": c["cuenta"],
                         "codigo": c.get("codigo", ""),   # si tiene agente 24/7,
                         "rango": rango}).encode("utf-8")  # trae también lo de la noche
    req = urllib.request.Request(url, data=cuerpo,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            print(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"EL RADAR HA RESPONDIDO CON UN ERROR {e.code}.\n"
              + e.read().decode("utf-8", "ignore")[:400])
        return 1
    except Exception as e:
        print(f"NO SE HA PODIDO LEER EL RADAR: {e}\n\n"
              "Repasa dos cosas:\n"
              f"  1. Que esta URL sea la tuya y se abra en el navegador: {c['url']}\n"
              "  2. Que el servicio esté encendido en Render (si está dormido,\n"
              "     la primera llamada puede tardar; vuelve a intentarlo).")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
