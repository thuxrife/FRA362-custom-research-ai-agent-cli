import os
import json

os.makedirs("summary-image", exist_ok=True)

# ==============================================================================
# DATA ENGINE: DYNAMIC LOADER FROM jury_eval_data.json
# ==============================================================================

def load_evaluation_data():
    """
    Loads latest scores dynamically from feasibility-outcome/jury_eval_data.json.
    Computes exact weighted TELOS+S scores, pillar star ratings, and robotics scale.
    """
    json_path = os.path.join("feasibility-outcome", "jury_eval_data.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            parsed = []
            for idx, s in enumerate(data):
                tot = round(sum((q["score"] / 5.0) * q["weight"] * 100 for q in s["assessment_data"]), 2)
                rob = s.get("robotic_data", {}).get("score", s.get("robotic_compatibility", {}).get("score", 0))
                pillars = {}
                for p in ["T", "E", "L", "O", "S", "SDG"]:
                    scs = [q["score"] for q in s["assessment_data"] if q["id"].split("-")[0] == p]
                    pillars[p] = round((sum(scs) / len(scs)) * 2) / 2 if scs else 3.0
                pillars["Robotic"] = round((rob / 12.0 * 5.0) * 2) / 2
                
                # Title formatting
                title = s.get("sheet_title", f"Solution_{idx+1}")
                clean_title = title.replace("Solution_", "Sol ").replace("_", " ")
                
                parsed.append({
                    "id": f"SOLUTION {idx+1}",
                    "short_id": f"SOL {idx+1}",
                    "title": s.get("sheet_title", f"Solution {idx+1}"),
                    "display_title": clean_title,
                    "concept": s.get("concept", ""),
                    "strength": s.get("strength", ""),
                    "bottleneck": s.get("bottleneck", ""),
                    "tot": tot,
                    "rob": rob,
                    "pillars": pillars,
                    "assessment_data": s.get("assessment_data", [])
                })
            return parsed
        except Exception as e:
            print(f"Warning: Could not parse jury_eval_data.json ({e}), using default scores.")

    return []


# ==============================================================================
# WHITE-PURPLE COLOR PALETTE FOR N SOLUTIONS
# ==============================================================================
PALETTES = [
    {
        "theme_color": "#8B5CF6",   # Vibrant Violet (Sol 1)
        "text_color": "#5B21B6",
        "bg_badge": "#F5F3FF",
        "border_badge": "#DDD6FE",
        "border_card": "#E2E8F0",
        "card_stroke_w": "1.2"
    },
    {
        "theme_color": "#581C87",   # Deep Royal Purple (Sol 2)
        "text_color": "#581C87",
        "bg_badge": "#F5F3FF",
        "border_badge": "#C4B5FD",
        "border_card": "#581C87",
        "card_stroke_w": "2.0"
    },
    {
        "theme_color": "#C084FC",   # Soft Orchid Purple (Sol 3)
        "text_color": "#7E22CE",
        "bg_badge": "#FAF5FF",
        "border_badge": "#E9D5FF",
        "border_card": "#E2E8F0",
        "card_stroke_w": "1.2"
    },
    {
        "theme_color": "#6366F1",   # Indigo Violet (Sol 4)
        "text_color": "#4338CA",
        "bg_badge": "#EEF2FF",
        "border_badge": "#C7D2FE",
        "border_card": "#E2E8F0",
        "card_stroke_w": "1.2"
    },
    {
        "theme_color": "#A855F7",   # Purple (Sol 5 fallback)
        "text_color": "#6B21A8",
        "bg_badge": "#FAF5FF",
        "border_badge": "#E9D5FF",
        "border_card": "#E2E8F0",
        "card_stroke_w": "1.2"
    }
]


# ==============================================================================
# 1. WHITE-PURPLE CROSS MATRIX (Y-Axis 0–12 complete, 1-N Legend, Dynamic Layout)
# ==============================================================================

def generate_clean_cross_matrix():
    data = load_evaluation_data()
    if not data:
        print("Error: No data found to render cross matrix.")
        return

    n_sol = len(data)
    width = 1280
    height = 800
    
    # Plot box coordinates with balanced margins
    x_min, x_max = 90, 1200
    y_min, y_max = 110, 700
    
    def get_x(telos):
        return x_min + (telos / 100.0) * (x_max - x_min)
        
    def get_y(robotics):
        return y_max - (robotics / 12.0) * (y_max - y_min)
        
    x_thresh_60 = get_x(60)
    y_thresh_8_0 = get_y(8.0)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
    <!-- Canvas Background -->
    <rect width="{width}" height="{height}" fill="#FFFFFF" />

    <!-- Header -->
    <g transform="translate(60, 36)">
        <text x="0" y="20" fill="#1E1B4B" font-size="20" font-weight="700" letter-spacing="-0.3">Feasibility Analysis vs. Robotic Potential Matrix</text>
        <text x="0" y="42" fill="#6B7280" font-size="13">TELOS+S Feasibility Score (0 - 100) vs. Robotic Potential Scale (0 - 12)</text>
    </g>

    <!-- Top Legend Arranged Dynamically -->
    <g transform="translate({x_max - (n_sol * 160)}, 42)">
'''
    for idx, sol in enumerate(data):
        pal = PALETTES[idx % len(PALETTES)]
        lx = idx * 160
        svg += f'''
        <circle cx="{lx + 8}" cy="8" r="5" fill="{pal['theme_color']}" />
        <text x="{lx + 18}" y="12" fill="#1E1B4B" font-size="11.5" font-weight="{'700' if idx==1 else '600'}">Sol {idx+1} ({sol['tot']:.2f})</text>
        '''

    svg += f'''
    </g>

    <!-- Plot Area Background -->
    <rect x="{x_min}" y="{y_min}" width="{x_max - x_min}" height="{y_max - y_min}" fill="#FFFFFF" stroke="#E2E8F0" stroke-width="1.2" />

    <!-- Subtle Grid Lines & Axis Ticks -->
'''

    # X-axis ticks (0 to 100 in steps of 10)
    for x_val in range(0, 101, 10):
        xp = get_x(x_val)
        is_key = (x_val in [0, 60, 100])
        svg += f'''
        <line x1="{xp}" y1="{y_min}" x2="{xp}" y2="{y_max}" stroke="#F5F3FF" stroke-width="1" />
        <line x1="{xp}" y1="{y_max}" x2="{xp}" y2="{y_max + 5}" stroke="#C4B5FD" stroke-width="1" />
        <text x="{xp}" y="{y_max + 20}" fill="{'#1E1B4B' if is_key else '#6B7280'}" font-size="11" font-weight="{'700' if is_key else '400'}" text-anchor="middle">{x_val}</text>
        '''

    # Y-axis ticks: COMPLETE 0 TO 12
    for y_val in range(0, 13):
        yp = get_y(y_val)
        is_key = (y_val in [0, 4, 8, 12])
        svg += f'''
        <line x1="{x_min}" y1="{yp}" x2="{x_max}" y2="{yp}" stroke="#F5F3FF" stroke-width="1" />
        <line x1="{x_min - 5}" y1="{yp}" x2="{x_min}" y2="{yp}" stroke="#C4B5FD" stroke-width="1" />
        <text x="{x_min - 10}" y="{yp + 4}" fill="{'#1E1B4B' if is_key else '#6B7280'}" font-size="11" font-weight="{'700' if is_key else '400'}" text-anchor="end">{y_val}</text>
        '''

    # Reference Thresholds
    svg += f'''
    <!-- Reference Threshold Lines -->
    <line x1="{x_thresh_60}" y1="{y_min}" x2="{x_thresh_60}" y2="{y_max}" stroke="#7C3AED" stroke-width="1.5" stroke-dasharray="6,4" />
    <text x="{x_thresh_60 + 8}" y="{y_min + 20}" fill="#581C87" font-size="11" font-weight="700">Feasibility Threshold (&gt;= 60)</text>

    <line x1="{x_min}" y1="{y_thresh_8_0}" x2="{x_max}" y2="{y_thresh_8_0}" stroke="#8B5CF6" stroke-width="1.3" stroke-dasharray="4,4" />
    <text x="{x_min + 10}" y="{y_thresh_8_0 - 8}" fill="#581C87" font-size="10" font-weight="600">High Robotics Content: Perception, Processing &amp; Actuation (&gt;= 8.0)</text>

    <!-- Axis Labels -->
    <text x="{(x_min + x_max)/2}" y="{y_max + 46}" fill="#1E1B4B" font-size="12" font-weight="600" text-anchor="middle">
        TELOS+S Feasibility Score (0 - 100) -&gt;
    </text>
    <text x="0" y="0" fill="#1E1B4B" font-size="12" font-weight="600" text-anchor="middle" transform="translate({x_min - 45}, {(y_min + y_max)/2}) rotate(-90)">
        Robotic Potential Scale (0 - 12) -&gt;
    </text>

    <!-- DATA POINTS & CALLOUT CARDS (COLLISION-FREE WITH LEADER LINES) -->
'''

    # Exact collision-free card placements with clear leader lines
    # Sol 1 (x=748.2, y=183.8)  -> Card placed to the Right at (820, 155)
    # Sol 2 (x=1052.0, y=282.1) -> Card placed Below-Left at (870, 380)
    # Sol 3 (x=461.1, y=183.8)  -> Card placed to the Left at (120, 155)
    # Sol 4 (x=700.9, y=134.6)  -> Card placed Below-Left at (440, 340)
    card_configs = [
        {
            # Sol 1 (CCTV Wheeled Crawler)
            "cx": 820, "cy": 155, "w": 250, "h": 56,
            "lx1": 756, "ly1": 184, "lx2": 820, "ly2": 184
        },
        {
            # Sol 2 (Acoustic SL-RAT)
            "cx": 870, "cy": 380, "w": 250, "h": 56,
            "lx1": 1017, "ly1": 296, "lx2": 995, "ly2": 380
        },
        {
            # Sol 3 (Underwater Sonar)
            "cx": 120, "cy": 155, "w": 250, "h": 56,
            "lx1": 453, "ly1": 184, "lx2": 370, "ly2": 184
        },
        {
            # Sol 4 (LiDAR SLAM)
            "cx": 440, "cy": 340, "w": 250, "h": 56,
            "lx1": 701, "ly1": 143, "lx2": 565, "ly2": 340
        }
    ]

    short_titles = [
        "CCTV Wheeled Crawler",
        "Acoustic Reflectometry",
        "Sonar 360 Profiling",
        "3D LiDAR SLAM"
    ]

    for idx, sol in enumerate(data):
        pal = PALETTES[idx % len(PALETTES)]
        sx, sy = get_x(sol["tot"]), get_y(sol["rob"])
        cfg = card_configs[idx] if idx < len(card_configs) else {"cx": sx + 40, "cy": sy - 30, "w": 250, "h": 56, "lx1": sx, "ly1": sy, "lx2": sx + 40, "ly2": sy - 30}
        stitle = short_titles[idx] if idx < len(short_titles) else sol["display_title"]

        svg += f'''
        <!-- SOLUTION {idx+1}: {sol['id']} (Point: {sx:.1f}, {sy:.1f}) -->
        <!-- Leader Line -->
        <line x1="{cfg['lx1']}" y1="{cfg['ly1']}" x2="{cfg['lx2']}" y2="{cfg['ly2']}" stroke="{pal['theme_color']}" stroke-width="1.3" stroke-dasharray="4,3" stroke-opacity="0.8" />
        
        <!-- Data Point Circle -->
        <g transform="translate({sx}, {sy})">
            <circle cx="0" cy="0" r="14" fill="{pal['theme_color']}" fill-opacity="0.2" />
            <circle cx="0" cy="0" r="7.5" fill="{pal['theme_color']}" stroke="#FFFFFF" stroke-width="2.5" />
        </g>
        
        <!-- Callout Card Box -->
        <g transform="translate({cfg['cx']}, {cfg['cy']})">
            <rect width="{cfg['w']}" height="{cfg['h']}" rx="6" fill="#FFFFFF" stroke="{pal['border_card']}" stroke-width="{pal['card_stroke_w']}" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.06))" />
            <rect x="8" y="8" width="58" height="18" rx="3" fill="{pal['bg_badge']}" stroke="{pal['border_badge']}" stroke-width="0.8"/>
            <text x="37" y="20" fill="{pal['text_color']}" font-size="9.5" font-weight="700" text-anchor="middle">SOL {idx+1}</text>
            <text x="74" y="21" fill="#1E1B4B" font-size="11.5" font-weight="700">{stitle}</text>
            <text x="8" y="43" fill="#6B7280" font-size="10.5">TELOS+S: <tspan fill="{pal['text_color']}" font-weight="700">{sol['tot']:.2f}</tspan> | Robotic: <tspan fill="{pal['text_color']}" font-weight="700">{sol['rob']:.1f} / 12</tspan></text>
        </g>
        '''

    svg += '</svg>'

    with open("summary-image/feasibility_robotics_cross_matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated: summary-image/feasibility_robotics_cross_matrix.svg")


# ==============================================================================
# 2. FOUR BIG COLUMNS COMPARISON (Each Column = 1 Solution)
# ==============================================================================

def generate_four_columns_comparison():
    data = load_evaluation_data()
    if not data:
        print("Error: No data found to render column comparison.")
        return

    n_sol = len(data)
    card_w = 360
    card_gap = 24
    start_x = 50
    width = start_x * 2 + n_sol * card_w + (n_sol - 1) * card_gap
    height = 700
    card_y = 90
    card_h = 560

    short_titles = [
        "CCTV Wheeled Crawler",
        "Acoustic Reflectometry",
        "Sonar 360 Profiling",
        "3D LiDAR SLAM"
    ]
    concepts = [
        "4K PTZ + YOLOv8 Defect Detection",
        "Acoustic Wave + EPA 0-10 Scale",
        "360° Underwater Sonar Scan",
        "3D Laser Point Cloud + SLAM"
    ]

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
    <!-- Canvas Background -->
    <rect width="{width}" height="{height}" fill="#FFFFFF" />

    <!-- Header -->
    <g transform="translate(50, 36)">
        <text x="0" y="20" fill="#1E1B4B" font-size="20" font-weight="700" letter-spacing="-0.3">Feasibility Analysis: TELOS+S &amp; Robotic Potential</text>
        <text x="0" y="42" fill="#6B7280" font-size="13">{n_sol}-Solution Direct Comparison | 7 Core Pillars (0 to 5 Star Scale)</text>
    </g>
'''

    for col_idx, sol in enumerate(data):
        pal = PALETTES[col_idx % len(PALETTES)]
        cx = start_x + col_idx * (card_w + card_gap)
        stitle = short_titles[col_idx] if col_idx < len(short_titles) else sol["display_title"]
        concept = concepts[col_idx] if col_idx < len(concepts) else sol["concept"][:40]

        bars = [
            {"code": "T", "title": "Technical", "val": sol["pillars"]["T"]},
            {"code": "E", "title": "Economic", "val": sol["pillars"]["E"]},
            {"code": "L", "title": "Legal", "val": sol["pillars"]["L"]},
            {"code": "O", "title": "Ops", "val": sol["pillars"]["O"]},
            {"code": "S", "title": "Sched", "val": sol["pillars"]["S"]},
            {"code": "+S", "title": "SDG", "val": sol["pillars"]["SDG"]},
            {"code": "Robotic", "title": "Robotic", "val": sol["pillars"]["Robotic"], "is_robotic": True}
        ]

        svg += f'''
        <!-- ============================================== -->
        <!-- COLUMN {col_idx + 1}: {sol["id"]} -->
        <!-- ============================================== -->
        <g transform="translate({cx}, {card_y})">
            <!-- Card Container -->
            <rect width="{card_w}" height="{card_h}" rx="8" fill="#FFFFFF" stroke="{pal['border_card']}" stroke-width="{pal['card_stroke_w']}" />

            <!-- Badge -->
            <g transform="translate(18, 18)">
                <rect x="0" y="0" width="85" height="20" rx="3" fill="{pal['bg_badge']}" stroke="{pal['border_badge']}" stroke-width="1" />
                <text x="42.5" y="14" fill="{pal['text_color']}" font-size="10" font-weight="700" text-anchor="middle">{sol['id']}</text>
            </g>

            <!-- Title & Concept -->
            <text x="18" y="62" fill="#1E1B4B" font-size="14.5" font-weight="700">{stitle}</text>
            <text x="18" y="78" fill="#6B7280" font-size="10.5">{concept}</text>

            <!-- Overall Score Banner -->
            <g transform="translate(18, 92)">
                <rect width="{card_w - 36}" height="48" rx="6" fill="#F8FAFC" stroke="{pal['border_badge']}" stroke-width="1" />
                <text x="14" y="19" fill="#6B7280" font-size="9" font-weight="700" letter-spacing="0.5">OVERALL SCORE</text>
                <text x="14" y="38" fill="{pal['text_color']}" font-size="18" font-weight="800">{sol['tot']:.2f} <tspan font-size="11" font-weight="500" fill="#6B7280">/ 100</tspan></text>
                <text x="{card_w - 52}" y="32" fill="{pal['text_color']}" font-size="11" font-weight="700" text-anchor="end">Robotic: {sol['rob']:.1f}/12</text>
            </g>

            <!-- Divider -->
            <line x1="18" y1="152" x2="{card_w - 18}" y2="152" stroke="#F1F5F9" stroke-width="1" />

            <!-- Subheading with Star Icon -->
            <g transform="translate(18, 172)">
                <text x="0" y="0" fill="#1E1B4B" font-size="11" font-weight="700">Pillar Star Rating (0 to 5</text>
                <!-- Vector Star matching title color -->
                <polygon points="0,-4.5 1.3,-1.2 4.5,-1.2 1.9,0.7 2.9,3.8 0,1.9 -2.9,3.8 -1.9,0.7 -4.5,-1.2 -1.3,-1.2" fill="#1E1B4B" transform="translate(136, -4) scale(0.9)" />
                <text x="147" y="0" fill="#1E1B4B" font-size="11" font-weight="700">Scale)</text>
            </g>
        '''

        # Bar Graph Inside Card
        gx_min = 36
        gx_max = card_w - 18
        plot_w = gx_max - gx_min
        gy_min = 195
        gy_max = 480
        plot_h = gy_max - gy_min

        # Y-Axis Gridlines & Vector Star Ticks (1 to 5 with clear spacing)
        for star in [1, 2, 3, 4, 5]:
            yp = gy_max - (star / 5.0) * plot_h
            svg += f'''
            <line x1="{gx_min}" y1="{yp}" x2="{gx_max}" y2="{yp}" stroke="#F5F3FF" stroke-width="1" />
            <text x="{gx_min - 16}" y="{yp + 3.5}" fill="#94A3B8" font-size="9" font-weight="600" text-anchor="end">{star}</text>
            <!-- Vector Star on Y-Axis Tick matching tick text color -->
            <polygon points="0,-4 1.1,-1.1 4,-1.1 1.7,0.6 2.6,3.4 0,1.7 -2.6,3.4 -1.7,0.6 -4,-1.1 -1.1,-1.1" fill="#94A3B8" transform="translate({gx_min - 6}, {yp}) scale(0.8)" />
            '''
        # Baseline
        svg += f'''<line x1="{gx_min}" y1="{gy_max}" x2="{gx_max}" y2="{gy_max}" stroke="#E2E8F0" stroke-width="1.2" />'''

        # 7 Column Bars
        n_bars = len(bars)
        col_slot = plot_w / n_bars
        b_width = 20

        for b_idx, bar_item in enumerate(bars):
            bx = gx_min + (b_idx + 0.5) * col_slot - (b_width / 2)
            b_val = bar_item["val"]
            bh = (b_val / 5.0) * plot_h
            by = gy_max - bh

            if bar_item.get("is_robotic"):
                svg += f'''
                <rect x="{gx_min + b_idx * col_slot}" y="{gy_min}" width="{col_slot}" height="{plot_h}" fill="#FAF5FF" rx="3" />
                '''

            bar_color = pal["theme_color"]
            svg += f'''
            <!-- Bar {bar_item['code']} -->
            <rect x="{bx}" y="{by}" width="{b_width}" height="{bh}" fill="{bar_color}" rx="3" />
            <text x="{bx + b_width/2}" y="{by - 5}" fill="{pal['text_color']}" font-size="9.5" font-weight="700" text-anchor="middle">{b_val}</text>
            <text x="{bx + b_width/2}" y="{gy_max + 16}" fill="#1E1B4B" font-size="10.5" font-weight="700" text-anchor="middle">{bar_item['code']}</text>
            <text x="{bx + b_width/2}" y="{gy_max + 28}" fill="#6B7280" font-size="8" font-weight="500" text-anchor="middle">{bar_item['title']}</text>
            '''

        # Card Footer Caption
        svg += f'''
            <g transform="translate(18, {card_h - 18})">
                <text x="0" y="8" fill="#94A3B8" font-size="9">TELOS+S Feasibility + Robotic Potential</text>
            </g>
        </g>
        '''

    svg += '</svg>'

    with open("summary-image/telos_s_robotics_column_bar.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated: summary-image/telos_s_robotics_column_bar.svg")


# ==============================================================================
# 3. HIGH-RESOLUTION PNG EXPORTER (300 DPI / CairoSVG & Selenium Fallback)
# ==============================================================================

def export_all_pngs():
    tasks = [
        ("summary-image/feasibility_robotics_cross_matrix.svg", "summary-image/feasibility_robotics_cross_matrix.png", 2.0),
        ("summary-image/telos_s_robotics_column_bar.svg", "summary-image/telos_s_robotics_column_bar.png", 2.0)
    ]

    # 1. Try CairoSVG
    try:
        import cairosvg
        print("\nExporting High-Resolution PNGs via CairoSVG (2x scale)...")
        for svg_file, png_file, scale in tasks:
            cairosvg.svg2png(url=svg_file, write_to=png_file, scale=scale)
            size_kb = os.path.getsize(png_file) / 1024
            print(f"Exported High-Res PNG: {png_file} ({size_kb:.1f} KB)")
        print("All High-Resolution PNGs exported successfully via CairoSVG!")
        return
    except Exception as e:
        print(f"CairoSVG export failed ({e}), attempting Selenium fallback...")

    # 2. Try Selenium Fallback
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By

        options = Options()
        options.add_argument('--headless=new')
        options.add_argument('--disable-gpu')
        options.add_argument('--force-device-scale-factor=2')

        driver = webdriver.Chrome(options=options)
        driver.set_window_size(2000, 1400)

        for svg_file, png_file, _ in tasks:
            abs_svg = os.path.abspath(svg_file).replace(os.sep, '/')
            abs_png = os.path.abspath(png_file)
            driver.get(f'file:///{abs_svg}')
            svg_elem = driver.find_element(By.TAG_NAME, 'svg')
            svg_elem.screenshot(abs_png)
            size_kb = os.path.getsize(abs_png) / 1024
            print(f"Exported High-Res PNG: {png_file} ({size_kb:.1f} KB)")

        driver.quit()
        print("All High-Resolution PNGs exported successfully via Selenium!")
    except Exception as e:
        print(f"Selenium export failed ({e}). SVGs remain ready for presentation use.")


if __name__ == "__main__":
    generate_clean_cross_matrix()
    generate_four_columns_comparison()
    export_all_pngs()
