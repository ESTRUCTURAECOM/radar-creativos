---
name: radar-creativos
description: Trae el estado REAL de los creativos de Meta (qué gana, por qué gana, qué matar, qué variante toca y con qué nombre) y el encargo de la semana con el brief de cada vídeo. Invócala SIEMPRE antes de crear creativos, escribir scripts o planificar la tanda de la semana — así se trabaja con los números de hoy y no de memoria. También cuando pregunten qué está funcionando, qué escalar o qué apagar.
---

# 📡 Radar de Creativos — el loop que se retroalimenta

Esta skill es el **puente entre los datos y la producción**. Sin ella se escriben
creativos a ciegas; con ella, cada tanda parte de lo que de verdad está
funcionando y el sistema aprende solo.

## 1. Lo primero, SIEMPRE: traer los datos

Antes de escribir una sola línea de creativo, ejecuta el script que está en
**esta misma carpeta de la skill**:

```bash
python ~/.claude/skills/radar-creativos/traer.py
```

En Windows:

```bash
python "%USERPROFILE%\.claude\skills\radar-creativos\traer.py"
```

Eso devuelve el **encargo de la semana**: los 25 vídeos que tocan, cada uno con
su brief completo. Variantes:

- `traer.py resumen` — solo el estado de la cuenta, más corto
- `traer.py last_30d` — mirando un periodo más largo (`last_7d`, `last_14d`, `last_30d`)

Lo que llega:

- **🟢 GANADORES** — y el **POR QUÉ** de cada uno: en qué fase del embudo gana
  (gancho / guion / promesa / landing / cierre) y en cuál se rompe
- **CONSERVAR** — lo que NO se puede tocar al hacer variantes
- **CORREGIR** — lo que hay que arreglar
- **El nombre exacto de cada vídeo**, con su número de variante
- **🟡 PROMESAS**, **🔴 MATAR**, **🧪 SIN PROBAR** y qué se ha aprendido ya

Si responde `SIN CONFIGURAR`, el propio mensaje dice qué hacer: en el radar,
pestaña «El Agente» → **⚙️ Configurar la skill**, y mover el archivo que se
descarga a la carpeta de la skill. No hay que escribir nada a mano.

## 2. Las reglas del loop (no negociables)

**Un ganador no se reinventa: se clona.** En una variante se cambia
**gancho, avatar y escenario**. El guion que ya gana NO se toca.

**Una cosa por vídeo.** Si cambias gancho, avatar y escenario a la vez y mejora,
no sabrás cuál de los tres fue. El brief ya dice qué cambia en cada copia.

**Explorar solo sobre lo que funciona.** Los tests nuevos salen de los cruces
que propone el radar (ángulo o formato que ya tira × algo sin probar). Nunca
ideas al azar.

**Cada creativo lleva su número de variante.** Es lo que permite saber si una
variante supera a su madre. Usa el nombre exacto que da el radar:

```
L3_M_HIN_TIMELINE_V2_PROGRESO VIDEO
 │  │   │      │      │   └ concepto + VIDEO/EST
 │  │   │      │      └ variante  ← OBLIGATORIO
 │  │   │      └ formato
 │  │   └ ángulo
 │  └ embudo T/M/B
 └ nivel de consciencia
```

**Respeta el diagnóstico.** Si un creativo gana en gancho pero se rompe en el
cierre, las variantes conservan ese gancho y atacan el cierre. No se cambia lo
que ya funciona.

## 3. Cómo se entrega

1. **Primero di qué vas a hacer** — un resumen corto: cuántas variantes de cada
   ganador, qué tests nuevos y por qué. La persona lo revisa **antes** de que
   escribas nada. Siempre manda su criterio: si pide algo que el radar marca
   como perdedor, se hace igual, avisando del dato una vez y sin insistir.
2. Con el visto bueno, escribe los creativos usando la skill de creativos que
   tengas instalada, que es la que lleva avatares, lenguaje real y prompts.
3. Entrega cada creativo **con su nombre de anuncio completo**, listo para
   pegar en Meta.

## 4. Por qué esto cierra el loop

Publicas con esos nombres → el radar los lee de Meta al día siguiente → compara
la variante con su madre → la que gana pasa a ser la nueva madre → la siguiente
tanda parte de ahí. Cada vuelta el sistema sabe un poco más, y llegar a 25-30
creativos a la semana deja de ser un problema de ideas.
