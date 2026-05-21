"""
jenny_upscaler.py
=================
Extrae el personaje principal de una sprite sheet del Jenny Mod
(o cualquier sprite sheet con fondo negro), elimina el fondo,
y escala el personaje a 4096x4096 px con pixel-perfect (Nearest Neighbor).

Uso:
    python jenny_upscaler.py                        # abre GUI
    python jenny_upscaler.py sprite.png             # CLI auto
    python jenny_upscaler.py sprite.png 4096        # CLI con resolución
    python jenny_upscaler.py sprite.png 4096 C:/out # CLI con carpeta salida

Requisitos:
    pip install Pillow
"""

import sys
import os
import numpy as np
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    os.system(f"{sys.executable} -m pip install Pillow")
    from PIL import Image

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox, ttk, font
    HAS_TK = True
except ImportError:
    HAS_TK = False


# ─────────────────────────────────────────────────────────────────────────────
# LÓGICA DE PROCESAMIENTO
# ─────────────────────────────────────────────────────────────────────────────

def remove_black_background(img: Image.Image, threshold: int = 8) -> Image.Image:
    """Convierte píxeles negros (fondo) en transparentes."""
    arr = np.array(img.convert("RGBA"))
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    black = (r < threshold) & (g < threshold) & (b < threshold)
    arr[black, 3] = 0
    return Image.fromarray(arr)


def find_character_bbox(arr: np.ndarray, threshold: int = 8):
    """
    Encuentra el bounding box del contenido real (sin fondo negro).
    Retorna (x1, y1, x2, y2) o None si no encuentra contenido.
    """
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    a = arr[:,:,3] if arr.shape[2] == 4 else np.ones_like(r) * 255

    non_black = ~((r < threshold) & (g < threshold) & (b < threshold)) & (a > 10)

    if not non_black.any():
        return None

    rows = np.where(non_black.any(axis=1))[0]
    cols = np.where(non_black.any(axis=0))[0]
    return (int(cols.min()), int(rows.min()), int(cols.max()+1), int(rows.max()+1))


def find_character_region(img: Image.Image):
    """
    Detecta automáticamente la región del personaje principal dentro
    de la sprite sheet, buscando la zona con mayor densidad de píxeles
    tipo 'piel' (tonos beige/rosados) fuera del fondo negro.

    Retorna (x1, y1, x2, y2) de la mejor región encontrada.
    """
    arr = np.array(img.convert("RGBA"))
    h, w = arr.shape[:2]

    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]

    # Máscara de fondo negro
    black = (r < 8) & (g < 8) & (b < 8)
    # Máscara de tonos piel (beige, rosa, marrón claro)
    skin = (r > 130) & (r < 250) & (g > 85) & (g < 205) & (b > 55) & (b < 175) & (~black)

    # Encontrar separadores negros por filas y columnas (>60% negro)
    row_black_pct = black.mean(axis=1)
    col_black_pct = black.mean(axis=0)

    def get_content_zones(pcts, threshold=0.60, min_size=20):
        """Retorna rangos (inicio, fin) donde pct < threshold (= hay contenido)."""
        zones = []
        in_zone = False
        start = 0
        for i, p in enumerate(pcts):
            if p < threshold and not in_zone:
                in_zone = True
                start = i
            elif p >= threshold and in_zone:
                in_zone = False
                if i - start >= min_size:
                    zones.append((start, i))
        if in_zone and len(pcts) - start >= min_size:
            zones.append((start, len(pcts)))
        return zones

    row_zones = get_content_zones(row_black_pct)
    col_zones = get_content_zones(col_black_pct)

    if not row_zones or not col_zones:
        # Fallback: usar toda la imagen
        bbox = find_character_bbox(arr)
        return bbox if bbox else (0, 0, w, h)

    # Encontrar la combinación zona_fila x zona_col con mayor densidad de piel
    best_score = -1
    best_region = None

    for ry in row_zones:
        for cx in col_zones:
            zone_skin = skin[ry[0]:ry[1], cx[0]:cx[1]]
            zone_h = ry[1] - ry[0]
            zone_w = cx[1] - cx[0]
            if zone_h < 30 or zone_w < 30:
                continue
            skin_density = zone_skin.mean()
            size_score = min(zone_h, zone_w) / max(h, w)  # preferir zonas grandes
            score = skin_density * (1 + size_score)

            if score > best_score:
                best_score = score
                best_region = (cx[0], ry[0], cx[1], ry[1])

    if best_region is None:
        # Fallback al bounding box general
        bbox = find_character_bbox(arr)
        return bbox if bbox else (0, 0, w, h)

    return best_region


def upscale_sprite(
    input_path: str,
    target: int = 4096,
    output_dir: str = None,
    auto_detect: bool = True,
    black_threshold: int = 8,
    log=print
) -> str:
    """
    Procesa la sprite sheet y genera el personaje escalado.

    Parámetros:
        input_path    : ruta de la imagen de entrada
        target        : resolución de salida (por defecto 4096)
        output_dir    : carpeta donde guardar (por defecto misma carpeta)
        auto_detect   : True = detectar personaje automáticamente
        black_threshold: umbral para considerar un píxel como negro/fondo
        log           : función para mostrar mensajes

    Retorna la ruta del archivo guardado.
    """
    log("─" * 50)
    log(f"  Cargando: {input_path}")
    img = Image.open(input_path).convert("RGBA")
    orig_w, orig_h = img.size
    log(f"  Tamaño original : {orig_w} × {orig_h} px")

    if auto_detect:
        log("  Detectando región del personaje…")
        region = find_character_region(img)
        if region:
            x1, y1, x2, y2 = region
            log(f"  Región detectada : ({x1},{y1}) → ({x2},{y2})  [{x2-x1}×{y2-y1} px]")
            sprite = img.crop((x1, y1, x2, y2))
        else:
            log("  No se detectó región — usando imagen completa")
            sprite = img
    else:
        sprite = img

    # Eliminar fondo negro
    log("  Eliminando fondo negro…")
    sprite_clean = remove_black_background(sprite, black_threshold)

    # Encontrar bounding box del contenido limpio
    arr_clean = np.array(sprite_clean)
    bbox = find_character_bbox(arr_clean, black_threshold)
    if bbox:
        sprite_clean = sprite_clean.crop(bbox)
        log(f"  Sprite limpio    : {sprite_clean.size[0]} × {sprite_clean.size[1]} px")

    # Calcular factor de escala (entero para pixel-perfect)
    sw, sh = sprite_clean.size
    factor = min(target // sw, target // sh)
    if factor < 1:
        factor = 1
    scaled_w = sw * factor
    scaled_h = sh * factor

    log(f"  Factor de escala : ×{factor}  →  {scaled_w} × {scaled_h} px")

    # Escalar con Nearest Neighbor (pixel-perfect, sin blur)
    scaled = sprite_clean.resize((scaled_w, scaled_h), Image.NEAREST)

    # Centrar en canvas target × target
    canvas = Image.new("RGBA", (target, target), (0, 0, 0, 0))
    offset_x = (target - scaled_w) // 2
    offset_y = (target - scaled_h) // 2
    canvas.paste(scaled, (offset_x, offset_y), scaled)

    log(f"  Centrado en canvas {target}×{target} (offset {offset_x},{offset_y})")

    # Guardar
    input_path = Path(input_path)
    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = input_path.parent

    out_dir.mkdir(parents=True, exist_ok=True)
    out_name = f"{input_path.stem}_{target}px_upscaled.png"
    out_path = out_dir / out_name

    canvas.save(str(out_path), "PNG")
    log(f"  ✓ Guardado: {out_path}")
    log("─" * 50)
    return str(out_path)


# ─────────────────────────────────────────────────────────────────────────────
# GUI
# ─────────────────────────────────────────────────────────────────────────────

class App:
    BG    = "#111111"
    BG2   = "#1c1c1c"
    BG3   = "#252525"
    BLUE  = "#5b8fff"
    GREEN = "#4ade80"
    FG    = "#e0e0e0"
    MUTED = "#666666"

    def __init__(self, root):
        self.root = root
        self.root.title("Jenny Mod — Sprite Upscaler")
        self.root.geometry("560x580")
        self.root.resizable(False, False)
        self.root.configure(bg=self.BG)

        self.input_path  = tk.StringVar()
        self.output_dir  = tk.StringVar()
        self.target_res  = tk.StringVar(value="4096")
        self.auto_detect = tk.BooleanVar(value=True)
        self.threshold   = tk.IntVar(value=8)

        self._build()

    def _label(self, parent, text, **kw):
        kw.setdefault("bg", self.BG2)
        kw.setdefault("fg", self.MUTED)
        kw.setdefault("font", ("Segoe UI", 9))
        kw.setdefault("anchor", "w")
        return tk.Label(parent, text=text, **kw)

    def _section(self, title):
        frame = tk.Frame(self.root, bg=self.BG2, bd=0)
        frame.pack(fill="x", padx=14, pady=(0, 8))
        self._label(frame, title, fg="#888888",
                    font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=10, pady=(8,2))
        return frame

    def _entry_row(self, parent, var, btn_text, btn_cmd):
        row = tk.Frame(parent, bg=self.BG2)
        row.pack(fill="x", padx=10, pady=(0, 10))
        tk.Entry(row, textvariable=var, bg=self.BG3, fg=self.FG,
                 insertbackground=self.FG, relief="flat", font=("Segoe UI", 10),
                 bd=0, highlightthickness=1,
                 highlightbackground=self.BG3,
                 highlightcolor=self.BLUE).pack(side="left", fill="x", expand=True, ipady=5, padx=(0,6))
        tk.Button(row, text=btn_text, bg=self.BG3, fg=self.FG,
                  font=("Segoe UI", 9), relief="flat", bd=0,
                  activebackground="#333", activeforeground=self.FG,
                  cursor="hand2", padx=10,
                  command=btn_cmd).pack(side="left")

    def _build(self):
        # Título
        tk.Label(self.root, text="🎮  Sprite Upscaler",
                 bg=self.BG, fg="white",
                 font=("Segoe UI", 17, "bold")).pack(pady=(22, 2))
        tk.Label(self.root, text="Jenny Mod · Pixel-perfect · Fondo negro → transparente",
                 bg=self.BG, fg=self.MUTED,
                 font=("Segoe UI", 10)).pack(pady=(0, 18))

        # Entrada
        s1 = self._section("IMAGEN DE ENTRADA")
        self._entry_row(s1, self.input_path, "Buscar…", self._pick_input)

        # Salida
        s2 = self._section("CARPETA DE SALIDA")
        self._entry_row(s2, self.output_dir, "Buscar…", self._pick_output)

        # Config
        s3 = self._section("CONFIGURACIÓN")
        cfg = tk.Frame(s3, bg=self.BG2)
        cfg.pack(fill="x", padx=10, pady=(0, 10))

        # Resolución
        col1 = tk.Frame(cfg, bg=self.BG2)
        col1.pack(side="left", fill="both", expand=True, padx=(0, 8))
        self._label(col1, "Resolución destino").pack(anchor="w")
        combo = ttk.Combobox(col1, textvariable=self.target_res,
                             values=["256","512","1024","2048","4096"],
                             state="readonly", font=("Segoe UI", 11))
        combo.pack(fill="x", pady=(2,0))

        # Threshold
        col2 = tk.Frame(cfg, bg=self.BG2)
        col2.pack(side="left", fill="both", expand=True, padx=(0, 8))
        self._label(col2, "Umbral fondo negro (0-30)").pack(anchor="w")
        tk.Spinbox(col2, from_=0, to=30, textvariable=self.threshold,
                   bg=self.BG3, fg=self.FG, relief="flat",
                   font=("Segoe UI", 11), width=5).pack(fill="x", pady=(2,0))

        # Auto detect checkbox
        ck_frame = tk.Frame(s3, bg=self.BG2)
        ck_frame.pack(fill="x", padx=10, pady=(0,10))
        tk.Checkbutton(ck_frame, text="Detectar personaje automáticamente",
                       variable=self.auto_detect,
                       bg=self.BG2, fg=self.FG, activebackground=self.BG2,
                       selectcolor=self.BG3, font=("Segoe UI", 10),
                       relief="flat", bd=0).pack(anchor="w")

        # Botón principal
        tk.Button(self.root, text="▲   Extraer · Limpiar · Escalar · Guardar",
                  bg=self.BLUE, fg="white",
                  font=("Segoe UI", 12, "bold"),
                  relief="flat", bd=0, cursor="hand2",
                  activebackground="#4a7aee", activeforeground="white",
                  pady=12, command=self._run
                  ).pack(fill="x", padx=14, pady=(6, 4))

        # Log / status
        log_frame = tk.Frame(self.root, bg=self.BG2)
        log_frame.pack(fill="both", expand=True, padx=14, pady=(0, 14))
        self.log_text = tk.Text(log_frame, bg=self.BG3, fg="#aaaaaa",
                                font=("Consolas", 9), relief="flat",
                                bd=0, state="disabled", wrap="word",
                                height=8)
        self.log_text.pack(fill="both", expand=True, padx=6, pady=6)

        self._log("Listo. Selecciona una imagen para empezar.")

    def _log(self, msg: str):
        self.log_text.configure(state="normal")
        self.log_text.insert("end", msg + "\n")
        self.log_text.see("end")
        self.log_text.configure(state="disabled")
        self.root.update()

    def _pick_input(self):
        p = filedialog.askopenfilename(
            title="Selecciona la sprite sheet",
            filetypes=[("PNG", "*.png"), ("Todos", "*.*")]
        )
        if p:
            self.input_path.set(p)
            self._log(f"Imagen: {p}")

    def _pick_output(self):
        p = filedialog.askdirectory(title="Carpeta de salida")
        if p:
            self.output_dir.set(p)
            self._log(f"Salida: {p}")

    def _run(self):
        inp = self.input_path.get().strip()
        if not inp or not Path(inp).exists():
            messagebox.showerror("Error", "Selecciona una imagen válida.")
            return
        try:
            target = int(self.target_res.get())
        except ValueError:
            messagebox.showerror("Error", "Resolución inválida.")
            return

        out_dir = self.output_dir.get().strip() or None

        self._log("\nProcesando…")
        try:
            out_path = upscale_sprite(
                inp, target, out_dir,
                auto_detect=self.auto_detect.get(),
                black_threshold=self.threshold.get(),
                log=self._log
            )
            messagebox.showinfo("✓ Listo", f"Guardado en:\n{out_path}")
        except Exception as e:
            self._log(f"ERROR: {e}")
            messagebox.showerror("Error", str(e))


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) >= 2:
        inp    = sys.argv[1]
        target = int(sys.argv[2]) if len(sys.argv) >= 3 else 4096
        outdir = sys.argv[3] if len(sys.argv) >= 4 else None
        upscale_sprite(inp, target, outdir)
        return

    if HAS_TK:
        root = tk.Tk()
        App(root)
        root.mainloop()
    else:
        print("Tkinter no disponible. Usa modo CLI:")
        print("  python jenny_upscaler.py sprite.png 4096 C:/carpeta/salida")


if __name__ == "__main__":
    main()