"""Generate the cyberpunk SVG assets for the GitHub profile README."""
import math
import random
import sys
from pathlib import Path

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

FONT = "'Share Tech Mono','JetBrains Mono','Cascadia Mono',Consolas,'SF Mono',Menlo,'DejaVu Sans Mono',monospace"
RED = "#ff3860"
BG = "#05010f"
CYAN = "#00f0ff"
MAGENTA = "#ff2bd6"
YELLOW = "#f9f002"
PURPLE = "#7a00ff"

COMMON_DEFS = f"""
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glowBig" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="7" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#ffffff" opacity="0.035"/>
  </pattern>
"""


def banner():
    rnd = random.Random(2077)
    W, H = 1200, 400
    horizon = 300

    def skyline(color, base_h, var, wmin, wmax, windows, seed_off):
        r = random.Random(77 + seed_off)
        parts, x = [], -10
        while x < W + 10:
            w = r.randint(wmin, wmax)
            h = base_h + r.randint(0, var)
            y = horizon - h
            parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}"/>')
            if r.random() < 0.25:
                parts.append(
                    f'<rect x="{x + w // 2 - 1}" y="{y - 18}" width="2" height="18" fill="{color}"/>'
                    f'<circle cx="{x + w // 2}" cy="{y - 19}" r="2" fill="{MAGENTA}">'
                    f'<animate attributeName="opacity" values="1;0.1;1" dur="{r.uniform(1.2, 2.6):.1f}s" repeatCount="indefinite"/></circle>'
                )
            if windows:
                for wy in range(y + 8, horizon - 6, 11):
                    for wx in range(x + 4, x + w - 5, 8):
                        if r.random() < 0.22:
                            c = r.choice([CYAN, MAGENTA, YELLOW, CYAN])
                            op = r.uniform(0.35, 0.9)
                            anim = ""
                            if r.random() < 0.08:
                                anim = (f'<animate attributeName="opacity" values="{op:.2f};0;{op:.2f}" '
                                        f'dur="{r.uniform(2, 6):.1f}s" begin="{r.uniform(0, 4):.1f}s" repeatCount="indefinite"/>')
                            parts.append(f'<rect x="{wx}" y="{wy}" width="3" height="4" fill="{c}" opacity="{op:.2f}">{anim}</rect>')
            x += w + r.randint(0, 6)
        return "\n".join(parts)

    rain_lines = []
    for _ in range(26):
        x = rnd.randint(0, 160)
        y = rnd.randint(0, 160)
        ln = rnd.randint(8, 18)
        rain_lines.append(f'<line x1="{x}" y1="{y}" x2="{x - 3}" y2="{y + ln}"/>')
    rain = "\n".join(rain_lines)

    # perspective floor grid
    vx = W / 2
    grid = []
    for i in range(-14, 15):
        grid.append(f'<line x1="{vx}" y1="{horizon}" x2="{vx + i * 110}" y2="{H}"/>')
    grid_h = []
    for k in range(1, 9):
        y = horizon + (H - horizon) * (k / 8) ** 1.8
        grid_h.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}"/>')

    title = "HITALO UZAN"
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Hitalo Uzan, Data Scientist e AI Engineer, banner cyberpunk">
<defs>{COMMON_DEFS}
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#030008"/>
    <stop offset="0.55" stop-color="#14002b"/>
    <stop offset="1" stop-color="#3b0752"/>
  </linearGradient>
  <linearGradient id="floor" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#2a0040"/>
    <stop offset="1" stop-color="{BG}"/>
  </linearGradient>
  <radialGradient id="moon" cx="0.5" cy="0.5" r="0.5">
    <stop offset="0" stop-color="{MAGENTA}" stop-opacity="0.55"/>
    <stop offset="1" stop-color="{MAGENTA}" stop-opacity="0"/>
  </radialGradient>
  <pattern id="rain" width="160" height="160" patternUnits="userSpaceOnUse">
    <g stroke="{CYAN}" stroke-opacity="0.22" stroke-width="1">{rain}</g>
    <animateTransform attributeName="patternTransform" type="translate" from="0 0" to="-30 160" dur="0.9s" repeatCount="indefinite"/>
  </pattern>
  <clipPath id="floorClip"><rect x="0" y="{horizon}" width="{W}" height="{H - horizon}"/></clipPath>
</defs>
<style>
  .t {{ font-family: {FONT}; font-weight: 700; }}
  .m {{ font-family: {FONT}; }}
  .g1 {{ animation: g1 3.2s infinite steps(1); }}
  .g2 {{ animation: g2 3.2s infinite steps(1); }}
  .flick {{ animation: flick 4s infinite; }}
  .blink {{ animation: blink 1s infinite steps(1); }}
  .scanbar {{ animation: scan 6s linear infinite; }}
  @keyframes g1 {{ 0%{{transform:translate(0,0)}} 88%{{transform:translate(-4px,1px)}} 90%{{transform:translate(6px,-2px)}} 92%{{transform:translate(-3px,0)}} 94%{{transform:translate(0,0)}} }}
  @keyframes g2 {{ 0%{{transform:translate(0,0)}} 88%{{transform:translate(4px,-1px)}} 90%{{transform:translate(-6px,2px)}} 92%{{transform:translate(3px,0)}} 94%{{transform:translate(0,0)}} }}
  @keyframes flick {{ 0%,19%,21%,62%,64%,100%{{opacity:1}} 20%,63%{{opacity:0.25}} }}
  @keyframes blink {{ 0%{{opacity:1}} 50%{{opacity:0}} }}
  @keyframes scan {{ 0%{{transform:translateY(-40px)}} 100%{{transform:translateY({H + 40}px)}} }}
</style>

<rect width="{W}" height="{H}" fill="url(#sky)"/>
<circle cx="960" cy="150" r="170" fill="url(#moon)"/>
<circle cx="960" cy="150" r="62" fill="none" stroke="{MAGENTA}" stroke-width="2" opacity="0.7" filter="url(#glow)"/>
<g opacity="0.55">{skyline("#1d0638", 120, 130, 30, 70, True, 1)}</g>
<g>{skyline("#0b0218", 50, 110, 40, 95, True, 2)}</g>

<!-- vertical neon sign -->
<g class="flick" filter="url(#glow)">
  <rect x="86" y="96" width="44" height="150" rx="3" fill="#0b0218" stroke="{MAGENTA}" stroke-width="2"/>
  <text x="108" y="130" text-anchor="middle" class="t" font-size="26" fill="{MAGENTA}">D</text>
  <text x="108" y="160" text-anchor="middle" class="t" font-size="26" fill="{MAGENTA}">A</text>
  <text x="108" y="190" text-anchor="middle" class="t" font-size="26" fill="{MAGENTA}">T</text>
  <text x="108" y="220" text-anchor="middle" class="t" font-size="26" fill="{MAGENTA}">A</text>
  <text x="108" y="238" text-anchor="middle" class="m" font-size="10" fill="{CYAN}">0xBQ</text>
</g>
<g filter="url(#glow)">
  <rect x="1060" y="208" width="104" height="34" fill="#0b0218" stroke="{CYAN}" stroke-width="2"/>
  <text x="1112" y="231" text-anchor="middle" class="t" font-size="16" fill="{CYAN}">24/7 ETL</text>
</g>

<rect x="0" y="{horizon}" width="{W}" height="{H - horizon}" fill="url(#floor)"/>
<g clip-path="url(#floorClip)" stroke="{MAGENTA}" stroke-opacity="0.45" stroke-width="1">
  {''.join(grid)}
  {''.join(grid_h)}
</g>
<line x1="0" y1="{horizon}" x2="{W}" y2="{horizon}" stroke="{CYAN}" stroke-width="2" filter="url(#glow)"/>

<rect width="{W}" height="{H}" fill="url(#rain)"/>

<!-- title plate -->
<g transform="translate({W / 2},176)">
  <text text-anchor="middle" class="t g1" font-size="78" fill="{CYAN}" opacity="0.85" letter-spacing="6">{title}</text>
  <text text-anchor="middle" class="t g2" font-size="78" fill="{MAGENTA}" opacity="0.85" letter-spacing="6">{title}</text>
  <text text-anchor="middle" class="t" font-size="78" fill="#f5f0ff" letter-spacing="6" filter="url(#glow)">{title}</text>
  <rect x="-300" y="22" width="600" height="34" fill="{YELLOW}" transform="skewX(-12)"/>
  <text y="46" text-anchor="middle" class="t" font-size="19" fill="#0b0218" letter-spacing="3">DATA SCIENTIST // AI ENGINEER</text>
</g>

<!-- HUD -->
<g class="m" font-size="13" fill="{CYAN}">
  <text x="24" y="30">SYS://NEURAL_LINK  v20.77</text>
  <text x="{W - 24}" y="30" text-anchor="end">SECTOR: BR // GRID: GCP-SA-EAST</text>
  <text x="24" y="{H - 18}">&gt; jack-in --user hitalo-uzan<tspan class="blink" fill="{YELLOW}"> █</tspan></text>
  <text x="{W - 24}" y="{H - 18}" text-anchor="end"><tspan fill="{MAGENTA}">●</tspan> LINK ONLINE · LATENCY 3ms</text>
</g>
<g stroke="{CYAN}" stroke-width="2" fill="none" opacity="0.8">
  <path d="M12 52 V12 H52"/><path d="M{W - 52} 12 H{W - 12} V52"/>
  <path d="M12 {H - 52} V{H - 12} H52"/><path d="M{W - 52} {H - 12} H{W - 12} V{H - 52}"/>
</g>

<rect width="{W}" height="{H}" fill="url(#scan)"/>
<rect class="scanbar" x="0" y="0" width="{W}" height="30" fill="{CYAN}" opacity="0.05"/>
</svg>
"""
    (OUT / "banner.svg").write_text(svg, encoding="utf-8")


def identity():
    W, H = 1200, 440
    axes = [
        ("LLM / AGENTES", 95),
        ("DATA ENG", 92),
        ("CLOUD / GCP", 88),
        ("AUTOMAÇÃO", 90),
        ("BACKEND / API", 82),
        ("ML / ESTATÍSTICA", 86),
    ]
    cx, cy, R = 905, 240, 128

    def pt(i, frac):
        a = math.radians(-90 + 60 * i)
        return cx + R * frac * math.cos(a), cy + R * frac * math.sin(a)

    rings = []
    for f in (0.25, 0.5, 0.75, 1.0):
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, f) for i in range(6)))
        rings.append(f'<polygon points="{pts}" fill="none" stroke="{PURPLE}" stroke-opacity="{0.35 + 0.15 * f:.2f}" stroke-width="1"/>')
    spokes = "".join(
        f'<line x1="{cx}" y1="{cy}" x2="{pt(i, 1)[0]:.1f}" y2="{pt(i, 1)[1]:.1f}" stroke="{PURPLE}" stroke-opacity="0.45"/>'
        for i in range(6)
    )
    data_pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in (pt(i, v / 100) for i, (_, v) in enumerate(axes)))
    dots = "".join(
        f'<circle cx="{pt(i, v / 100)[0]:.1f}" cy="{pt(i, v / 100)[1]:.1f}" r="4" fill="{YELLOW}"/>'
        for i, (_, v) in enumerate(axes)
    )
    labels = []
    for i, (name, v) in enumerate(axes):
        x, y = pt(i, 1.22)
        anchor = "middle" if abs(x - cx) < 5 else ("start" if x > cx else "end")
        labels.append(
            f'<text x="{x:.1f}" y="{y + 4:.1f}" text-anchor="{anchor}" class="m" font-size="13" fill="{CYAN}">{name} '
            f'<tspan fill="{YELLOW}">{v}</tspan></text>'
        )

    fields = [
        ("HANDLE", "hitalo-uzan"),
        ("CLASSE", "Netrunner · Data Sci / AI Eng"),
        ("ORIGEM", "BR · Ciência da Computação"),
        ("AFILIAÇÃO", "████████ [REDACTED]"),
        ("ESPECIALIDADE", "pipelines · agentes LLM · modelos"),
        ("ARMA FAVORITA", "Python + BigQuery + Claude"),
    ]
    rows = []
    for k, (label, val) in enumerate(fields):
        y = 128 + k * 40
        color = MAGENTA if label == "AFILIAÇÃO" else "#e9e4ff"
        rows.append(
            f'<text x="220" y="{y}" class="m" font-size="12" fill="{CYAN}" opacity="0.8">{label}</text>'
            f'<text x="220" y="{y + 15}" class="m" font-size="15" fill="{color}">{val}</text>'
        )

    r = random.Random(42)
    bars, bx = [], 60
    while bx < 400:
        w = r.choice([1, 2, 2, 3, 4])
        bars.append(f'<rect x="{bx}" y="372" width="{w}" height="26" fill="{CYAN}" opacity="0.75"/>')
        bx += w + r.choice([1, 2, 3])

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Cartão de identidade netrunner e radar de habilidades: LLM e agentes 95, Data Eng 92, Automação 90, Cloud GCP 88, ML e estatística 86, Backend e API 82">
<defs>{COMMON_DEFS}
  <linearGradient id="holo" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="{CYAN}" stop-opacity="0.16"/>
    <stop offset="0.5" stop-color="{PURPLE}" stop-opacity="0.10"/>
    <stop offset="1" stop-color="{MAGENTA}" stop-opacity="0.18"/>
  </linearGradient>
  <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/>
    <stop offset="0.5" stop-color="#fff" stop-opacity="0.13"/>
    <stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <clipPath id="card"><polygon points="40,40 560,40 600,80 600,420 80,420 40,380"/></clipPath>
</defs>
<style>
  .t {{ font-family: {FONT}; font-weight: 700; }}
  .m {{ font-family: {FONT}; }}
  .blink {{ animation: blink 1.2s infinite steps(1); }}
  .sweep {{ animation: sweep 5s ease-in-out infinite; }}
  .spin {{ transform-origin: {cx}px {cy}px; animation: spin 8s linear infinite; }}
  .pulse {{ transform-origin: {cx}px {cy}px; animation: pulse 3s ease-in-out infinite; }}
  .scanline {{ animation: sl 3.5s linear infinite; }}
  @keyframes blink {{ 0%{{opacity:1}} 50%{{opacity:0.15}} }}
  @keyframes sweep {{ 0%{{transform:translateX(-700px)}} 60%,100%{{transform:translateX(700px)}} }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  @keyframes pulse {{ 0%,100%{{transform:scale(1)}} 50%{{transform:scale(1.04)}} }}
  @keyframes sl {{ 0%{{transform:translateY(0)}} 100%{{transform:translateY(118px)}} }}
</style>
<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>

<!-- ID card -->
<g>
  <polygon points="40,40 560,40 600,80 600,420 80,420 40,380" fill="#0d0420"/>
  <polygon points="40,40 560,40 600,80 600,420 80,420 40,380" fill="url(#holo)"/>
  <g clip-path="url(#card)"><rect class="sweep" x="0" y="40" width="260" height="380" fill="url(#shine)" transform="skewX(-20)"/></g>
  <polygon points="40,40 560,40 600,80 600,420 80,420 40,380" fill="none" stroke="{CYAN}" stroke-width="2" filter="url(#glow)"/>
  <rect x="40" y="40" width="300" height="34" fill="{YELLOW}"/>
  <text x="54" y="63" class="t" font-size="16" fill="#0b0218" letter-spacing="2">ID://NETRUNNER-0x2077</text>
  <text x="548" y="63" text-anchor="end" class="m" font-size="12" fill="{MAGENTA}"><tspan class="blink">● ONLINE</tspan></text>

  <!-- avatar -->
  <g transform="translate(130,236)">
    <polygon points="0,-82 71,-41 71,41 0,82 -71,41 -71,-41" fill="#140630" stroke="{MAGENTA}" stroke-width="2" filter="url(#glow)"/>
    <polygon points="0,-64 55,-32 55,32 0,64 -55,32 -55,-32" fill="none" stroke="{CYAN}" stroke-opacity="0.5" stroke-dasharray="4 4"/>
    <text y="16" text-anchor="middle" class="t" font-size="46" fill="#f5f0ff" filter="url(#glow)">HU</text>
    <g clip-path="url(#card)"><rect class="scanline" x="-71" y="-60" width="142" height="2" fill="{CYAN}" opacity="0.8"/></g>
    <text y="112" text-anchor="middle" class="m" font-size="11" fill="{CYAN}">BIOMETRIA OK</text>
  </g>
  {''.join(rows)}
  {''.join(bars)}
  <text x="580" y="392" text-anchor="end" class="m" font-size="11" fill="{CYAN}" opacity="0.7">CHECKSUM 0xC0FFEE</text>
  <text x="580" y="408" text-anchor="end" class="m" font-size="11" fill="{MAGENTA}" opacity="0.8">NÍVEL DE ACESSO: ROOT*</text>
</g>

<!-- radar -->
<text x="{cx}" y="36" text-anchor="middle" class="t" font-size="16" fill="{MAGENTA}" letter-spacing="3">// SCAN DE IMPLANTES NEURAIS</text>
<g class="spin" opacity="0.5">
  <circle cx="{cx}" cy="{cy}" r="{R + 30}" fill="none" stroke="{CYAN}" stroke-width="1" stroke-dasharray="2 10"/>
</g>
{''.join(rings)}
{spokes}
<g class="pulse">
  <polygon points="{data_pts}" fill="{MAGENTA}" fill-opacity="0.28" stroke="{MAGENTA}" stroke-width="2.5" filter="url(#glow)"/>
  {dots}
</g>
{''.join(labels)}
<text x="{cx}" y="{H - 14}" text-anchor="middle" class="m" font-size="11" fill="{PURPLE}">*root só em ambiente local. produção é read-only até aprovação humana.</text>
<rect width="{W}" height="{H}" rx="14" fill="url(#scan)"/>
</svg>
"""
    (OUT / "identity.svg").write_text(svg, encoding="utf-8")


def netmap():
    W, H = 1200, 500
    sources = [("ERP", "SAP HANA"), ("E-COMMERCE", "VTEX"), ("CRM", "Marketing Cloud"),
               ("ADS", "Meta Ads"), ("PLANILHAS", "Google Sheets")]
    outputs = [("DASHBOARDS", "FastAPI + chat IA"), ("AGENTES IA", "copy · juízes · eval"),
               ("ATIVAÇÃO CRM", "tiers + públicos"), ("APPS INTERNOS", "Firestore"),
               ("MODELOS", "elasticidade · MMM")]
    ys = [90 + i * 80 for i in range(5)]
    ingest = (330, 250)
    core = (600, 250)
    brain = (600, 100)
    serve = (870, 250)

    parts, paths, packets = [], [], []
    colors = [CYAN, MAGENTA, YELLOW, CYAN, MAGENTA]

    for i, ((name, sub), y) in enumerate(zip(sources, ys)):
        parts.append(
            f'<g><rect x="30" y="{y - 26}" width="180" height="52" fill="#0d0420" stroke="{CYAN}" stroke-opacity="0.8"/>'
            f'<rect x="30" y="{y - 26}" width="4" height="52" fill="{colors[i]}"/>'
            f'<text x="46" y="{y - 4}" class="t" font-size="14" fill="#f5f0ff">{name}</text>'
            f'<text x="46" y="{y + 14}" class="m" font-size="12" fill="{CYAN}" opacity="0.8">{sub}</text></g>'
        )
        pid = f"s{i}"
        paths.append(f'<path id="{pid}" d="M210 {y} C 270 {y}, 260 {ingest[1]}, {ingest[0] - 60} {ingest[1]}"/>')
        packets.append((pid, colors[i], 2.2 + i * 0.3, i * 0.4))

    for i, ((name, sub), y) in enumerate(zip(outputs, ys)):
        parts.append(
            f'<g><rect x="990" y="{y - 26}" width="180" height="52" fill="#0d0420" stroke="{MAGENTA}" stroke-opacity="0.8"/>'
            f'<rect x="1166" y="{y - 26}" width="4" height="52" fill="{colors[-1 - i]}"/>'
            f'<text x="1006" y="{y - 4}" class="t" font-size="14" fill="#f5f0ff">{name}</text>'
            f'<text x="1006" y="{y + 14}" class="m" font-size="12" fill="{MAGENTA}" opacity="0.85">{sub}</text></g>'
        )
        pid = f"o{i}"
        paths.append(f'<path id="{pid}" d="M{serve[0] + 60} {serve[1]} C 930 {serve[1]}, 930 {y}, 990 {y}"/>')
        packets.append((pid, colors[-1 - i], 2.0 + i * 0.25, 1 + i * 0.35))

    paths.append(f'<path id="ic" d="M{ingest[0] + 60} {ingest[1]} L {core[0] - 70} {core[1]}"/>')
    paths.append(f'<path id="cs" d="M{core[0] + 70} {core[1]} L {serve[0] - 60} {serve[1]}"/>')
    paths.append(f'<path id="cb" d="M{core[0]} {core[1] - 70} L {brain[0]} {brain[1] + 34}"/>')
    paths.append(f'<path id="bs" d="M{brain[0] + 110} {brain[1]} C 800 {brain[1]}, {serve[0]} 150, {serve[0]} {serve[1] - 40}"/>')
    for pid, c, d, b in [("ic", CYAN, 1.4, 0), ("ic", MAGENTA, 1.4, 0.7), ("cs", YELLOW, 1.3, 0.2),
                         ("cs", CYAN, 1.3, 0.85), ("cb", MAGENTA, 1.1, 0), ("bs", YELLOW, 1.8, 0.5)]:
        packets.append((pid, c, d, b))

    path_draw = "".join(
        p.replace("<path ", f'<path fill="none" stroke="{PURPLE}" stroke-width="1.5" stroke-opacity="0.7" ')
        .replace(' id="', ' data-id="')
        for p in paths
    )
    pk = "".join(
        f'<circle r="4" fill="{c}" filter="url(#glow)"><animateMotion dur="{d:.2f}s" begin="{b:.2f}s" repeatCount="indefinite"><mpath href="#{pid}"/></animateMotion></circle>'
        for pid, c, d, b in packets
    )

    hexagon = " ".join(
        f"{core[0] + 70 * math.cos(math.radians(60 * k)):.1f},{core[1] + 70 * math.sin(math.radians(60 * k)):.1f}"
        for k in range(6)
    )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Mapa da rede de dados: ERP, e-commerce, CRM, ads e planilhas entram por jobs no Cloud Run, viram tabelas no BigQuery, passam pelo Claude e saem como dashboards, agentes de IA, ativação de CRM, apps internos e modelos">
<defs>{COMMON_DEFS}
  {''.join(paths)}
</defs>
<style>
  .t {{ font-family: {FONT}; font-weight: 700; }}
  .m {{ font-family: {FONT}; }}
  .spin {{ transform-origin: {core[0]}px {core[1]}px; animation: spin 14s linear infinite; }}
  .spinr {{ transform-origin: {core[0]}px {core[1]}px; animation: spin 9s linear infinite reverse; }}
  .beat {{ animation: beat 1.6s ease-in-out infinite; }}
  @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
  @keyframes beat {{ 0%,100%{{opacity:0.55}} 50%{{opacity:1}} }}
</style>
<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
<text x="30" y="34" class="t" font-size="15" fill="{YELLOW}" letter-spacing="3">// MAPA DA REDE · ONDE MEUS DADOS CIRCULAM</text>
<text x="{W - 30}" y="34" text-anchor="end" class="m" font-size="12" fill="{CYAN}" opacity="0.7">tráfego simulado · pacotes reais são confidenciais</text>
{path_draw}
{''.join(parts)}

<!-- ingest -->
<g>
  <rect x="{ingest[0] - 60}" y="{ingest[1] - 90}" width="120" height="180" fill="#0d0420" stroke="{CYAN}" stroke-width="2" filter="url(#glow)"/>
  <text x="{ingest[0]}" y="{ingest[1] - 60}" text-anchor="middle" class="t" font-size="13" fill="{CYAN}">INGESTÃO</text>
  {''.join(f'<rect x="{ingest[0] - 44}" y="{ingest[1] - 44 + k * 22}" width="88" height="14" fill="{CYAN}" opacity="0.18"><animate attributeName="opacity" values="0.12;0.6;0.12" dur="1.8s" begin="{k * 0.3:.1f}s" repeatCount="indefinite"/></rect>' for k in range(5))}
  <text x="{ingest[0]}" y="{ingest[1] + 78}" text-anchor="middle" class="m" font-size="11" fill="#e9e4ff">Cloud Run jobs</text>
</g>

<!-- core -->
<g>
  <circle class="spin" cx="{core[0]}" cy="{core[1]}" r="92" fill="none" stroke="{MAGENTA}" stroke-width="1.5" stroke-dasharray="12 8" opacity="0.7"/>
  <circle class="spinr" cx="{core[0]}" cy="{core[1]}" r="82" fill="none" stroke="{CYAN}" stroke-width="1" stroke-dasharray="3 6" opacity="0.6"/>
  <polygon points="{hexagon}" fill="#140630" stroke="{MAGENTA}" stroke-width="2.5" filter="url(#glowBig)"/>
  <text x="{core[0]}" y="{core[1] - 8}" text-anchor="middle" class="t" font-size="15" fill="#f5f0ff">DATA CORE</text>
  <text x="{core[0]}" y="{core[1] + 12}" text-anchor="middle" class="m" font-size="12" fill="{MAGENTA}">BigQuery</text>
  <text x="{core[0]}" y="{core[1] + 28}" text-anchor="middle" class="m" font-size="10" fill="{CYAN}">RAW → MAIN → DM_*</text>
</g>

<!-- brain -->
<g class="beat">
  <rect x="{brain[0] - 110}" y="{brain[1] - 34}" width="220" height="68" rx="34" fill="#1a0a10" stroke="{YELLOW}" stroke-width="2" filter="url(#glow)"/>
  <text x="{brain[0]}" y="{brain[1] - 6}" text-anchor="middle" class="t" font-size="14" fill="{YELLOW}">NEURAL ENGINE</text>
  <text x="{brain[0]}" y="{brain[1] + 14}" text-anchor="middle" class="m" font-size="12" fill="#f5f0ff">Claude · tools · MCP</text>
</g>

<!-- serve -->
<g>
  <rect x="{serve[0] - 60}" y="{serve[1] - 40}" width="120" height="80" fill="#0d0420" stroke="{MAGENTA}" stroke-width="2" filter="url(#glow)"/>
  <text x="{serve[0]}" y="{serve[1] - 6}" text-anchor="middle" class="t" font-size="13" fill="{MAGENTA}">SERVING</text>
  <text x="{serve[0]}" y="{serve[1] + 14}" text-anchor="middle" class="m" font-size="11" fill="#e9e4ff">APIs · services</text>
</g>

{pk}

<g class="m" font-size="11" fill="{PURPLE}">
  <text x="30" y="{H - 18}">CI: lint · testes · cobertura ≥ 80% no diff · secret scan</text>
  <text x="{W - 30}" y="{H - 18}" text-anchor="end">merge só com aprovação humana · deploy automático</text>
</g>
<rect width="{W}" height="{H}" rx="14" fill="url(#scan)"/>
</svg>
"""
    (OUT / "netmap.svg").write_text(svg, encoding="utf-8")


def footer():
    W, H = 1200, 120
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Fim da transmissão">
<defs>{COMMON_DEFS}</defs>
<style>
  .t {{ font-family: {FONT}; font-weight: 700; }}
  .m {{ font-family: {FONT}; }}
  .type {{ animation: type 5s steps(40) infinite; }}
  .blink {{ animation: blink 1s infinite steps(1); }}
  @keyframes type {{ 0%{{clip-path: inset(0 100% 0 0)}} 50%,100%{{clip-path: inset(0 0 0 0)}} }}
  @keyframes blink {{ 0%{{opacity:1}} 50%{{opacity:0}} }}
</style>
<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
<line x1="30" y1="22" x2="{W - 30}" y2="22" stroke="{MAGENTA}" stroke-width="2" stroke-dasharray="30 6 4 6" filter="url(#glow)"/>
<text x="{W / 2}" y="66" text-anchor="middle" class="t type" font-size="22" fill="{CYAN}" letter-spacing="4" filter="url(#glow)">// FIM DA TRANSMISSÃO · JACKING OUT...</text>
<text x="{W / 2}" y="96" text-anchor="middle" class="m" font-size="13" fill="{YELLOW}">wake up, samurai. we have data to ship.<tspan class="blink" fill="{MAGENTA}"> █</tspan></text>
</svg>
"""
    (OUT / "footer.svg").write_text(svg, encoding="utf-8")


STYLE_BASE = f"""
  .t {{ font-family: {FONT}; font-weight: 700; }}
  .m {{ font-family: {FONT}; }}
  .blink {{ animation: blink 1s infinite steps(1); }}
  @keyframes blink {{ 0%{{opacity:1}} 50%{{opacity:0}} }}
  @keyframes show {{ to {{ opacity: 1; }} }}
  .ln {{ opacity: 0; animation: show 0.01s steps(1) forwards; }}
"""


def terminal():
    W, H = 1200, 360
    lines = [
        # (indent, [(text, color, bold)])
        (0, [("┌──(", CYAN, False), ("netrunner@grid", MAGENTA, True), (")-[", CYAN, False), ("~/neural-link", "#f5f0ff", False), ("]", CYAN, False)]),
        (0, [("└─$ ", CYAN, False), ("whoami", YELLOW, True)]),
        (2, [("Cientista de Dados ", "#f5f0ff", True), ("&amp;", MAGENTA, True), (" AI Engineer.", "#f5f0ff", True)]),
        (2, [("Construo a encanação que leva dados do ", "#cfc8ea", False), ("ERP", CYAN, False), (", do ", "#cfc8ea", False), ("e-commerce", CYAN, False), (" e do ", "#cfc8ea", False), ("CRM", CYAN, False), (" até o warehouse —", "#cfc8ea", False)]),
        (2, [("e depois faço esses dados falarem: ", "#cfc8ea", False), ("dashboards", MAGENTA, False), (", ", "#cfc8ea", False), ("modelos", MAGENTA, False), (" e ", "#cfc8ea", False), ("agentes de IA", MAGENTA, False), (" em produção.", "#cfc8ea", False)]),
        (0, []),
        (0, [("└─$ ", CYAN, False), ("cat /etc/diretrizes", YELLOW, True)]),
        (2, [("[01] ", MAGENTA, True), ("dado sem teste é boato", "#f5f0ff", False)]),
        (2, [("[02] ", MAGENTA, True), ("produção é sagrada: merge só com aprovação humana", "#f5f0ff", False)]),
        (2, [("[03] ", MAGENTA, True), ("nunca confie num default — leia a doc, depois o código", "#f5f0ff", False)]),
        (2, [("[04] ", MAGENTA, True), ("se dá pra automatizar, já devia estar num job", "#f5f0ff", False)]),
        (0, [("└─$ ", CYAN, False)]),
    ]
    out = []
    y0, step = 92, 21
    for i, (ind, segs) in enumerate(lines):
        y = y0 + i * step
        spans = "".join(f'<tspan fill="{c}"{" font-weight=\"700\"" if b else ""}>{t}</tspan>' for t, c, b in segs)
        if i == len(lines) - 1:
            spans += f'<tspan fill="{YELLOW}" class="blink">█</tspan>'
        out.append(f'<text x="{60 + ind * 9}" y="{y}" class="m" font-size="15" xml:space="preserve"><animate attributeName="opacity" values="0;0;1" keyTimes="0;0.98;1" dur="{0.3 + i * 0.22:.2f}s" fill="freeze"/>{spans}</text>')
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Terminal: whoami. Cientista de Dados e AI Engineer. Construo a encanação que leva dados do ERP, do e-commerce e do CRM até o warehouse, e depois faço esses dados falarem: dashboards, modelos e agentes de IA em produção. Diretrizes: dado sem teste é boato; produção é sagrada, merge só com aprovação humana; nunca confie num default; se dá pra automatizar, já devia estar num job.">
<defs>{COMMON_DEFS}
  <linearGradient id="bar" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{MAGENTA}"/><stop offset="1" stop-color="{PURPLE}"/>
  </linearGradient>
</defs>
<style>{STYLE_BASE}</style>
<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
<rect x="24" y="20" width="{W - 48}" height="{H - 40}" rx="10" fill="#0b0218" stroke="{MAGENTA}" stroke-width="1.5" filter="url(#glow)"/>
<path d="M34 20 H{W - 34} a10 10 0 0 1 10 10 V52 H24 V30 a10 10 0 0 1 10 -10 Z" fill="url(#bar)" opacity="0.9"/>
<circle cx="48" cy="36" r="6" fill="{RED}"/><circle cx="68" cy="36" r="6" fill="{YELLOW}"/><circle cx="88" cy="36" r="6" fill="{CYAN}"/>
<text x="{W / 2}" y="41" text-anchor="middle" class="t" font-size="13" fill="#05010f" letter-spacing="2">netrunner@grid: ~/neural-link — zsh — 120×24</text>
<text x="{W - 44}" y="41" text-anchor="end" class="m" font-size="12" fill="#05010f">● SECURE</text>
{''.join(out)}
<rect x="24" y="20" width="{W - 48}" height="{H - 40}" rx="10" fill="url(#scan)"/>
</svg>
"""
    (OUT / "terminal.svg").write_text(svg, encoding="utf-8")


def contracts():
    W, H = 1200, 560
    cards = [
        ("0x01", "IA GENERATIVA", "GHOSTWRITER DE MARCA", ["agente que escreve copy de varejo", "com guarda-corpos de marca, juiz", "LLM, feedback e eval automatizado"], "ONLINE", 92, MAGENTA),
        ("0x02", "ATIVAÇÃO", "CRM DE ALTA VOLTAGEM", ["warehouse → plataforma de marketing,", "clientes segmentados em tiers e", "públicos de ads renovados a cada 3h"], "ONLINE", 80, CYAN),
        ("0x03", "OPERAÇÕES", "COFRE DE BRINDES", ["gestão de estoque e pedidos migrada", "pra NoSQL, com travas atômicas e", "reconciliação automática"], "ONLINE", 100, YELLOW),
        ("0x04", "MODELAGEM", "ORÁCULO DE PREÇOS", ["eficiência de venda, elasticidade", "de preço e Marketing Mix Modeling", "em cima do data mart de vendas"], "CALIBRANDO", 55, CYAN),
        ("0x05", "FINANCEIRO", "FLUXO DE APROVAÇÕES", ["solicitações de pagamento com", "aprovação em etapas — adeus,", "automação no-code"], "ONLINE", 100, YELLOW),
        ("0x06", "DEV TOOLING", "CYBERDECK DO TIME", ["marketplace de plugins pro Claude", "Code + second brain que guarda", "memória entre sessões"], "ONLINE", 85, MAGENTA),
    ]
    cw, ch, gx, gy, x0, y0 = 368, 220, 22, 22, 30, 74
    out = []
    for i, (code, dist, title, desc, status, prog, c) in enumerate(cards):
        col, row = i % 3, i // 3
        x, y = x0 + col * (cw + gx), y0 + row * (ch + gy)
        cut = 22
        poly = f"{x},{y} {x + cw - cut},{y} {x + cw},{y + cut} {x + cw},{y + ch} {x + cut},{y + ch} {x},{y + ch - cut}"
        st_color = "#3dff9a" if status == "ONLINE" else YELLOW
        desc_svg = "".join(f'<text x="{x + 20}" y="{y + 118 + k * 20}" class="m" font-size="13.5" fill="#cfc8ea">{d}</text>' for k, d in enumerate(desc))
        bar_w = cw - 40
        out.append(f"""
<g>
  <polygon points="{poly}" fill="#0d0420"/>
  <polygon points="{poly}" fill="{c}" opacity="0.05"/>
  <polygon points="{poly}" fill="none" stroke="{c}" stroke-width="1.6" class="edge" style="animation-delay:{i * 0.5:.1f}s" filter="url(#glow)"/>
  <rect x="{x}" y="{y}" width="64" height="24" fill="{c}"/>
  <text x="{x + 32}" y="{y + 17}" text-anchor="middle" class="t" font-size="13" fill="#05010f">{code}</text>
  <text x="{x + 78}" y="{y + 17}" class="m" font-size="12" fill="{c}" letter-spacing="2">{dist}</text>
  <circle cx="{x + cw - 96}" cy="{y + 42}" r="4" fill="{st_color}" class="blink" style="animation-duration:{1.2 + i * 0.15:.2f}s"/>
  <text x="{x + cw - 86}" y="{y + 46}" class="m" font-size="11" fill="{st_color}">{status}</text>
  <text x="{x + 20}" y="{y + 82}" class="t" font-size="19" fill="#f5f0ff" letter-spacing="1">{title}</text>
  <line x1="{x + 20}" y1="{y + 94}" x2="{x + 120}" y2="{y + 94}" stroke="{c}" stroke-width="2"/>
  {desc_svg}
  <rect x="{x + 20}" y="{y + ch - 26}" width="{bar_w}" height="6" fill="#ffffff" opacity="0.08"/>
  <rect x="{x + 20}" y="{y + ch - 26}" width="{bar_w * prog / 100:.0f}" height="6" fill="{c}"><animate attributeName="width" from="0" to="{bar_w * prog / 100:.0f}" dur="{1.2 + i * 0.15:.2f}s" fill="freeze"/></rect>
  <text x="{x + cw - 20}" y="{y + ch - 32}" text-anchor="end" class="m" font-size="10" fill="{c}" opacity="0.8">SYNC {prog}%</text>
</g>""")
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Contratos ativos: 0x01 Ghostwriter de marca, agente de copy com juiz LLM e eval; 0x02 CRM de alta voltagem, segmentação em tiers e públicos de ads; 0x03 Cofre de brindes, estoque e pedidos em NoSQL com travas atômicas; 0x04 Oráculo de preços, eficiência de venda, elasticidade e MMM; 0x05 Fluxo de aprovações de pagamento; 0x06 Cyberdeck do time, plugins pro Claude Code e second brain.">
<defs>{COMMON_DEFS}</defs>
<style>{STYLE_BASE}
  .edge {{ animation: edge 3s ease-in-out infinite; }}
  @keyframes edge {{ 0%,100%{{stroke-opacity:0.45}} 50%{{stroke-opacity:1}} }}
  .fill {{ transform-box: fill-box; transform-origin: left; transform: scaleX(0); animation: grow 1.4s ease-out forwards; }}
  @keyframes grow {{ to {{ transform: scaleX(1); }} }}
</style>
<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>
<text x="30" y="44" class="t" font-size="15" fill="{YELLOW}" letter-spacing="3">// QUADRO DE CONTRATOS · 6 ATIVOS</text>
<text x="{W - 30}" y="44" text-anchor="end" class="m" font-size="12" fill="{CYAN}" opacity="0.7">clientes e codinomes reais: [CRIPTOGRAFADO]</text>
{''.join(out)}
<rect width="{W}" height="{H}" rx="14" fill="url(#scan)"/>
</svg>
"""
    (OUT / "contracts.svg").write_text(svg, encoding="utf-8")


def restricted():
    W, H = 1200, 300
    term = [
        ("$ sudo rm -rf /bugs", YELLOW),
        ("[sudo] senha para netrunner: ********", "#cfc8ea"),
        ("✖ ACESSO NEGADO — bugs não se apagam.", RED),
        ("  se testam, se corrigem e viram nota no second brain.", "#cfc8ea"),
        ("$ SELECT COUNT(*) FROM bugs WHERE status = 'aberto';", YELLOW),
        ("  0   -- (até o próximo deploy)", "#3dff9a"),
    ]
    lines = "".join(
        f'<text x="380" y="{92 + i * 26}" class="m" font-size="15" fill="{c}" xml:space="preserve"><animate attributeName="opacity" values="0;0;1" keyTimes="0;0.98;1" dur="{0.5 + i * 0.45:.2f}s" fill="freeze"/>{t}</text>'
        for i, (t, c) in enumerate(term)
    )
    stripes = "".join(f'<polygon points="{x},0 {x + 18},0 {x - 2},22 {x - 20},22" fill="{YELLOW}"/>' for x in range(0, W + 40, 40))
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Área restrita: sudo rm -rf /bugs. Acesso negado, bugs não se apagam: se testam, se corrigem e viram nota no second brain. Bugs abertos: 0, até o próximo deploy.">
<defs>{COMMON_DEFS}
  <clipPath id="r"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<style>{STYLE_BASE}
  .g1 {{ animation: g1 2.6s infinite steps(1); }}
  .g2 {{ animation: g2 2.6s infinite steps(1); }}
  @keyframes g1 {{ 0%{{transform:translate(0,0)}} 85%{{transform:translate(-4px,1px)}} 88%{{transform:translate(5px,-1px)}} 91%{{transform:translate(0,0)}} }}
  @keyframes g2 {{ 0%{{transform:translate(0,0)}} 85%{{transform:translate(4px,-1px)}} 88%{{transform:translate(-5px,1px)}} 91%{{transform:translate(0,0)}} }}
  .shake {{ animation: shake 4s infinite; transform-origin: 170px 150px; }}
  @keyframes shake {{ 0%,80%,100%{{transform:rotate(0)}} 83%{{transform:rotate(-8deg)}} 86%{{transform:rotate(8deg)}} 89%{{transform:rotate(-4deg)}} 92%{{transform:rotate(0)}} }}
</style>
<g clip-path="url(#r)">
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect width="{W}" height="{H}" fill="{RED}" opacity="0.04"/>
<g opacity="0.85">{stripes}</g>
<g transform="translate(0,{H - 22})" opacity="0.85">{stripes}</g>

<!-- lock -->
<g class="shake" filter="url(#glow)">
  <path d="M135 140 V112 a35 35 0 0 1 70 0 V140" fill="none" stroke="{RED}" stroke-width="10" stroke-linecap="round"/>
  <rect x="115" y="138" width="110" height="88" rx="10" fill="#1a0610" stroke="{RED}" stroke-width="3"/>
  <circle cx="170" cy="174" r="11" fill="{RED}"/>
  <rect x="166" y="180" width="8" height="24" rx="3" fill="{RED}"/>
</g>
<text x="170" y="256" text-anchor="middle" class="m" font-size="11" fill="{RED}" letter-spacing="3">NÍVEL 5 · ROOT</text>

<g transform="translate(380,60)">
  <text class="t g1" font-size="22" fill="{CYAN}" opacity="0.8" letter-spacing="4">⚠ ÁREA RESTRITA</text>
  <text class="t g2" font-size="22" fill="{MAGENTA}" opacity="0.8" letter-spacing="4">⚠ ÁREA RESTRITA</text>
  <text class="t" font-size="22" fill="{RED}" letter-spacing="4">⚠ ÁREA RESTRITA</text>
</g>
{lines}
<line x1="330" y1="48" x2="330" y2="{H - 40}" stroke="{RED}" stroke-opacity="0.4" stroke-dasharray="4 6"/>
<rect width="{W}" height="{H}" fill="url(#scan)"/>
</g>
</svg>
"""
    (OUT / "restricted.svg").write_text(svg, encoding="utf-8")


banner()
terminal()
contracts()
restricted()
identity()
netmap()
footer()
print("ok")
