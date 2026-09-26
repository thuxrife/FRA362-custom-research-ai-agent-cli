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
    Fallback values are used if file is missing.
    """
    json_path = os.path.join("feasibility-outcome", "jury_eval_data.json")
    if os.path.exists(json_path):
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            parsed = []
            for s in data:
                tot = round(sum((q["score"] / 5.0) * q["weight"] * 100 for q in s["assessment_data"]), 2)
                rob = s.get("robotic_data", {}).get("score", 0)
                pillars = {}
                for p in ["T", "E", "L", "O", "S", "SDG"]:
                    scs = [q["score"] for q in s["assessment_data"] if q["id"].split("-")[0] == p]
                    pillars[p] = round((sum(scs) / len(scs)) * 2) / 2 if scs else 3.0
                pillars["Robotic"] = round((rob / 2.0) * 2) / 2
                parsed.append({
                    "title": s.get("sheet_title", ""),
                    "concept": s.get("concept", ""),
                    "tot": tot,
                    "rob": rob,
                    "pillars": pillars
                })
            return parsed
        except Exception as e:
            print(f"Warning: Could not parse jury_eval_data.json ({e}), using default scores.")

    # Defaults
    return [
        {"title": "Solution_1_CCTV_Flow", "concept": "Optical Flow + Canal Ultrasonic Alert", "tot": 65.93, "rob": 4.8, "pillars": {"T": 1.5, "E": 4.5, "L": 4.0, "O": 3.5, "S": 3.0, "SDG": 3.5, "Robotic": 2.5}},
        {"title": "Solution_2_Acoustic_Sewer", "concept": "Acoustic Inversion + Cleanliness Scale", "tot": 69.10, "rob": 5.8, "pillars": {"T": 3.5, "E": 3.5, "L": 3.5, "O": 3.5, "S": 3.0, "SDG": 4.5, "Robotic": 3.0}},
        {"title": "Solution_3_Adaptive_Misting", "concept": "IR Surface Thermometer + Solenoids", "tot": 67.17, "rob": 8.0, "pillars": {"T": 4.0, "E": 2.5, "L": 3.5, "O": 3.0, "S": 4.0, "SDG": 3.0, "Robotic": 4.0}}
    ]


# ==============================================================================
# WHITE-PURPLE DESIGN PALETTE
# ==============================================================================
# Background: #FFFFFF (Pure White)
# Primary Title / Text: #1E1B4B (Deep Violet Slate)
# Subtitle: #6B7280
# Grid lines: #F5F3FF / #E2E8F0
# Thresholds: #7C3AED / #8B5CF6
# Solution 1: #8B5CF6 (Vibrant Violet) - Text: #5B21B6
# Solution 2: #581C87 (Deep Royal Purple) - Text: #581C87
# Solution 3: #C084FC (Soft Orchid Purple) - Text: #7E22CE
# ==============================================================================


# ==============================================================================
# 1. WHITE-PURPLE CROSS MATRIX (Y-Axis 0–10 complete, 1-2-3 Legend, No Zones)
# ==============================================================================

def generate_clean_cross_matrix():
    data = load_evaluation_data()
    s1, s2, s3 = data[0], data[1], data[2]

    width = 1200
    height = 760
    
    # Plot box coordinates with balanced margins
    x_min, x_max = 90, 1130
    y_min, y_max = 100, 660
    
    def get_x(telos):
        return x_min + (telos / 100.0) * (x_max - x_min)
        
    def get_y(robotics):
        return y_max - (robotics / 10.0) * (y_max - y_min)
        
    x_thresh_60 = get_x(60)
    y_thresh_7 = get_y(7.0)

    # Dynamic Solution Coordinates
    s1_x, s1_y = get_x(s1["tot"]), get_y(s1["rob"])
    s2_x, s2_y = get_x(s2["tot"]), get_y(s2["rob"])
    s3_x, s3_y = get_x(s3["tot"]), get_y(s3["rob"])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">
    <!-- Canvas Background -->
    <rect width="{width}" height="{height}" fill="#FFFFFF" />

    <!-- Header -->
    <g transform="translate(60, 36)">
        <text x="0" y="20" fill="#1E1B4B" font-size="20" font-weight="700" letter-spacing="-0.3">Feasibility Analysis vs. Robotic Potential Matrix</text>
        <text x="0" y="42" fill="#6B7280" font-size="13">TELOS+S Feasibility Score (0–100) vs. Robotic Potential Scale (0–10)</text>
    </g>

    <!-- Top Legend Arranged Strictly as 1, 2, 3 (White-Purple Theme) -->
    <g transform="translate({x_max - 540}, 42)">
        <!-- Solution 1 -->
        <circle cx="8" cy="8" r="5" fill="#8B5CF6" />
        <text x="18" y="12" fill="#1E1B4B" font-size="11.5" font-weight="600">Solution 1 ({s1['tot']:.2f})</text>

        <!-- Solution 2 -->
        <circle cx="175" cy="8" r="5" fill="#581C87" />
        <text x="185" y="12" fill="#1E1B4B" font-size="11.5" font-weight="700">Solution 2 ({s2['tot']:.2f})</text>

        <!-- Solution 3 -->
        <circle cx="345" cy="8" r="5" fill="#C084FC" />
        <text x="355" y="12" fill="#1E1B4B" font-size="11.5" font-weight="600">Solution 3 ({s3['tot']:.2f})</text>
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

    # Y-axis ticks: COMPLETE 0 TO 10 (INCLUDING 3 AND 9)
    for y_val in range(0, 11):
        yp = get_y(y_val)
        is_key = (y_val in [0, 5, 7, 10])
        svg += f'''
        <line x1="{x_min}" y1="{yp}" x2="{x_max}" y2="{yp}" stroke="#F5F3FF" stroke-width="1" />
        <line x1="{x_min - 5}" y1="{yp}" x2="{x_min}" y2="{yp}" stroke="#C4B5FD" stroke-width="1" />
        <text x="{x_min - 10}" y="{yp + 4}" fill="{'#1E1B4B' if is_key else '#6B7280'}" font-size="11" font-weight="{'700' if is_key else '400'}" text-anchor="end">{y_val}</text>
        '''

    # Threshold Guidelines
    svg += f'''
    <!-- Vertical Cutoff at X=60 (Minimum Viability) -->
    <line x1="{x_thresh_60}" y1="{y_min}" x2="{x_thresh_60}" y2="{y_max}" stroke="#7C3AED" stroke-width="1.3" stroke-dasharray="4,4" />
    <text x="{x_thresh_60}" y="{y_min - 8}" fill="#581C87" font-size="10" font-weight="700" text-anchor="middle">Min Viable (60.0)</text>

    <!-- Horizontal Cutoff at Y=7.0 -->
    <line x1="{x_min}" y1="{y_thresh_7}" x2="{x_max}" y2="{y_thresh_7}" stroke="#8B5CF6" stroke-width="1.3" stroke-dasharray="4,4" />
    <text x="{x_min + 10}" y="{y_thresh_7 - 8}" fill="#581C87" font-size="10" font-weight="600">Highly related to perception, processing and actuation (≥ 7.0)</text>

    <!-- Axis Labels -->
    <text x="{(x_min + x_max)/2}" y="{y_max + 46}" fill="#1E1B4B" font-size="12" font-weight="600" text-anchor="middle">
        TELOS+S Feasibility Score (0 – 100) →
    </text>
    <text x="0" y="0" fill="#1E1B4B" font-size="12" font-weight="600" text-anchor="middle" transform="translate({x_min - 45}, {(y_min + y_max)/2}) rotate(-90)">
        Robotic Potential Scale (0 – 10) →
    </text>

    <!-- ============================================================== -->
    <!-- DATA POINTS & CARDS (WHITE-PURPLE THEME)                        -->
    <!-- ============================================================== -->

    <!-- SOLUTION 3: Adaptive Misting -->
    <g transform="translate({s3_x}, {s3_y})">
        <circle cx="0" cy="0" r="7" fill="#C084FC" stroke="#FFFFFF" stroke-width="2" />
        <circle cx="0" cy="0" r="13" fill="none" stroke="#C084FC" stroke-width="1" stroke-opacity="0.4" />
        <line x1="0" y1="0" x2="-45" y2="-20" stroke="#DDD6FE" stroke-width="1" stroke-dasharray="2,2" />
    </g>
    <g transform="translate(470, 160)">
        <rect width="260" height="54" rx="4" fill="#FFFFFF" stroke="#E9D5FF" stroke-width="1" />
        <rect x="8" y="8" width="60" height="16" rx="2" fill="#FAF5FF" stroke="#E9D5FF" stroke-width="0.8"/>
        <text x="38" y="19" fill="#7E22CE" font-size="9" font-weight="700" text-anchor="middle">SOL 3</text>
        <text x="76" y="20" fill="#1E1B4B" font-size="11" font-weight="700">Adaptive Misting</text>
        <text x="8" y="42" fill="#6B7280" font-size="10">TELOS+S: <tspan fill="#7E22CE" font-weight="700">{s3['tot']:.2f}</tspan> | Robotic: <tspan fill="#581C87" font-weight="700">{s3['rob']:.1f} / 10</tspan></text>
    </g>

    <!-- SOLUTION 2: Sewer AAR -->
    <g transform="translate({s2_x}, {s2_y})">
        <circle cx="0" cy="0" r="8" fill="#581C87" stroke="#FFFFFF" stroke-width="2" />
        <circle cx="0" cy="0" r="16" fill="none" stroke="#6D28D9" stroke-width="1.5" stroke-opacity="0.4" />
        <line x1="0" y1="0" x2="40" y2="0" stroke="#581C87" stroke-width="1.2" />
    </g>
    <g transform="translate(850, 312)">
        <rect width="250" height="56" rx="4" fill="#FFFFFF" stroke="#581C87" stroke-width="1.5" />
        <rect x="8" y="8" width="60" height="16" rx="2" fill="#F5F3FF" stroke="#C4B5FD" stroke-width="0.8"/>
        <text x="38" y="19" fill="#581C87" font-size="9" font-weight="700" text-anchor="middle">SOL 2</text>
        <text x="76" y="20" fill="#1E1B4B" font-size="11" font-weight="700">Sewer Reflectometry</text>
        <text x="8" y="42" fill="#6B7280" font-size="10">TELOS+S: <tspan fill="#581C87" font-weight="700">{s2['tot']:.2f}</tspan> | Robotic: <tspan fill="#581C87" font-weight="700">{s2['rob']:.1f} / 10</tspan></text>
    </g>

    <!-- SOLUTION 1: CCTV Flow -->
    <g transform="translate({s1_x}, {s1_y})">
        <circle cx="0" cy="0" r="7" fill="#8B5CF6" stroke="#FFFFFF" stroke-width="2" />
        <circle cx="0" cy="0" r="13" fill="none" stroke="#8B5CF6" stroke-width="1" stroke-opacity="0.4" />
        <line x1="0" y1="0" x2="-45" y2="20" stroke="#DDD6FE" stroke-width="1" stroke-dasharray="2,2" />
    </g>
    <g transform="translate(470, 420)">
        <rect width="260" height="54" rx="4" fill="#FFFFFF" stroke="#DDD6FE" stroke-width="1" />
        <rect x="8" y="8" width="60" height="16" rx="2" fill="#F5F3FF" stroke="#C4B5FD" stroke-width="0.8"/>
        <text x="38" y="19" fill="#5B21B6" font-size="9" font-weight="700" text-anchor="middle">SOL 1</text>
        <text x="76" y="20" fill="#1E1B4B" font-size="11" font-weight="700">CCTV Flow + Canal</text>
        <text x="8" y="42" fill="#6B7280" font-size="10">TELOS+S: <tspan fill="#5B21B6" font-weight="700">{s1['tot']:.2f}</tspan> | Robotic: <tspan fill="#5B21B6" font-weight="700">{s1['rob']:.1f} / 10</tspan></text>
    </g>
</svg>'''

    with open("summary-image/feasibility_robotics_cross_matrix.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated: summary-image/feasibility_robotics_cross_matrix.svg")


# ==============================================================================
# 2. THREE BIG COLUMNS COMPARISON (Each Column = 1 Solution)
# ==============================================================================

def generate_three_columns_comparison():
    data = load_evaluation_data()
    s1_data, s2_data, s3_data = data[0], data[1], data[2]

    width = 1320
    height = 680
    
    # 3 Solutions Data structure
    solutions = [
        {
            "id": "SOLUTION 1",
            "title": "CCTV Flow + Canal Level",
            "concept": "Optical Flow + Canal Ultrasonic Alert",
            "score": f"{s1_data['tot']:.2f}",
            "theme_color": "#8B5CF6",
            "text_color": "#5B21B6",
            "bg_badge": "#F5F3FF",
            "border_badge": "#DDD6FE",
            "border_card": "#E2E8F0",
            "card_stroke_w": "1.2",
            "bars": [
                {"code": "T", "title": "Technical", "val": s1_data["pillars"]["T"]},
                {"code": "E", "title": "Economic", "val": s1_data["pillars"]["E"]},
                {"code": "L", "title": "Legal", "val": s1_data["pillars"]["L"]},
                {"code": "O", "title": "Ops", "val": s1_data["pillars"]["O"]},
                {"code": "S", "title": "Sched", "val": s1_data["pillars"]["S"]},
                {"code": "+S", "title": "SDG", "val": s1_data["pillars"]["SDG"]},
                {"code": "Robotic", "title": "Robotic", "val": s1_data["pillars"]["Robotic"], "is_robotic": True}
            ]
        },
        {
            "id": "SOLUTION 2",
            "title": "Sewer Acoustic Reflectometry",
            "concept": "Acoustic Inversion + Cleanliness Scale",
            "score": f"{s2_data['tot']:.2f}",
            "theme_color": "#581C87",
            "text_color": "#581C87",
            "bg_badge": "#F5F3FF",
            "border_badge": "#C4B5FD",
            "border_card": "#C4B5FD",
            "card_stroke_w": "1.4",
            "bars": [
                {"code": "T", "title": "Technical", "val": s2_data["pillars"]["T"]},
                {"code": "E", "title": "Economic", "val": s2_data["pillars"]["E"]},
                {"code": "L", "title": "Legal", "val": s2_data["pillars"]["L"]},
                {"code": "O", "title": "Ops", "val": s2_data["pillars"]["O"]},
                {"code": "S", "title": "Sched", "val": s2_data["pillars"]["S"]},
                {"code": "+S", "title": "SDG", "val": s2_data["pillars"]["SDG"]},
                {"code": "Robotic", "title": "Robotic", "val": s2_data["pillars"]["Robotic"], "is_robotic": True}
            ]
        },
        {
            "id": "SOLUTION 3",
            "title": "Adaptive Walkway Misting",
            "concept": "IR Surface Thermometer + Solenoids",
            "score": f"{s3_data['tot']:.2f}",
            "theme_color": "#C084FC",
            "text_color": "#7E22CE",
            "bg_badge": "#FAF5FF",
            "border_badge": "#E9D5FF",
            "border_card": "#E2E8F0",
            "card_stroke_w": "1.2",
            "bars": [
                {"code": "T", "title": "Technical", "val": s3_data["pillars"]["T"]},
                {"code": "E", "title": "Economic", "val": s3_data["pillars"]["E"]},
                {"code": "L", "title": "Legal", "val": s3_data["pillars"]["L"]},
                {"code": "O", "title": "Ops", "val": s3_data["pillars"]["O"]},
                {"code": "S", "title": "Sched", "val": s3_data["pillars"]["S"]},
                {"code": "+S", "title": "SDG", "val": s3_data["pillars"]["SDG"]},
                {"code": "Robotic", "title": "Robotic", "val": s3_data["pillars"]["Robotic"], "is_robotic": True}
            ]
        }
    ]

    card_w = 380
    card_h = 560
    card_gap = 30
    start_x = 60
    card_y = 90

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" style="background-color: #FFFFFF; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;">
    <!-- Canvas Background -->
    <rect width="{width}" height="{height}" fill="#FFFFFF" />

    <!-- Header -->
    <g transform="translate(60, 36)">
        <text x="0" y="20" fill="#1E1B4B" font-size="20" font-weight="700" letter-spacing="-0.3">Feasibility Analysis: TELOS +S &amp; Robotic Potential</text>
        <text x="0" y="42" fill="#6B7280" font-size="13">3-Solution Direct Comparison | 7 Core Pillars (0 to 5 ★ Scale)</text>
    </g>
'''

    # Render 3 Big Columns (Cards)
    for col_idx, sol in enumerate(solutions):
        cx = start_x + col_idx * (card_w + card_gap)
        
        svg += f'''
        <!-- ============================================== -->
        <!-- COLUMN {col_idx + 1}: {sol["id"]} -->
        <!-- ============================================== -->
        <g transform="translate({cx}, {card_y})">
            <!-- Card Container -->
            <rect width="{card_w}" height="{card_h}" rx="8" fill="#FFFFFF" stroke="{sol['border_card']}" stroke-width="{sol['card_stroke_w']}" />

            <!-- Badge -->
            <g transform="translate(20, 20)">
                <rect x="0" y="0" width="85" height="20" rx="3" fill="{sol['bg_badge']}" stroke="{sol['border_badge']}" stroke-width="1" />
                <text x="42.5" y="14" fill="{sol['text_color']}" font-size="10" font-weight="700" text-anchor="middle">{sol['id']}</text>
            </g>

            <!-- Title & Concept -->
            <text x="20" y="64" fill="#1E1B4B" font-size="15" font-weight="700">{sol['title']}</text>
            <text x="20" y="82" fill="#6B7280" font-size="11">{sol['concept']}</text>

            <!-- Overall Score Banner -->
            <g transform="translate(20, 96)">
                <rect width="{card_w - 40}" height="48" rx="6" fill="#F8FAFC" stroke="{sol['border_badge']}" stroke-width="1" />
                <text x="16" y="20" fill="#6B7280" font-size="9.5" font-weight="700" letter-spacing="0.5">OVERALL SCORE</text>
                <text x="16" y="38" fill="{sol['text_color']}" font-size="18" font-weight="800">{sol['score']} <tspan font-size="11" font-weight="500" fill="#6B7280">/ 100</tspan></text>
            </g>

            <!-- Divider -->
            <line x1="20" y1="160" x2="{card_w - 20}" y2="160" stroke="#F1F5F9" stroke-width="1" />

            <!-- Subheading -->
            <text x="20" y="180" fill="#1E1B4B" font-size="11.5" font-weight="700">Pillar Star Rating (0 to 5 ★)</text>
        '''

        # Bar Graph Inside Card
        gx_min = 40
        gx_max = card_w - 25
        plot_w = gx_max - gx_min  # 315px
        gy_min = 205
        gy_max = 475
        plot_h = gy_max - gy_min  # 270px

        # Subtle Y-Axis Gridlines & Star Ticks (1 to 5)
        for star in [1, 2, 3, 4, 5]:
            yp = gy_max - (star / 5.0) * plot_h
            svg += f'''
            <line x1="{gx_min}" y1="{yp}" x2="{gx_max}" y2="{yp}" stroke="#F5F3FF" stroke-width="1" />
            <text x="{gx_min - 6}" y="{yp + 3.5}" fill="#94A3B8" font-size="9.5" font-weight="600" text-anchor="end">{star}★</text>
            '''
        # Baseline
        svg += f'''<line x1="{gx_min}" y1="{gy_max}" x2="{gx_max}" y2="{gy_max}" stroke="#E2E8F0" stroke-width="1.2" />'''

        # 7 Column Bars
        n_bars = len(sol["bars"])
        col_slot = plot_w / n_bars
        b_width = 24

        for b_idx, bar_item in enumerate(sol["bars"]):
            bx = gx_min + (b_idx + 0.5) * col_slot - (b_width / 2)
            b_val = bar_item["val"]
            bh = (b_val / 5.0) * plot_h
            by = gy_max - bh

            # Highlight background for Robotic column
            if bar_item.get("is_robotic"):
                svg += f'''
                <rect x="{gx_min + b_idx * col_slot}" y="{gy_min}" width="{col_slot}" height="{plot_h}" fill="#FAF5FF" rx="3" />
                '''

            bar_color = sol["theme_color"]
            svg += f'''
            <!-- Bar {bar_item['code']} -->
            <rect x="{bx}" y="{by}" width="{b_width}" height="{bh}" fill="{bar_color}" rx="3" />
            <text x="{bx + b_width/2}" y="{by - 6}" fill="{sol['text_color']}" font-size="10.5" font-weight="700" text-anchor="middle">{b_val}</text>
            <text x="{bx + b_width/2}" y="{gy_max + 18}" fill="#1E1B4B" font-size="11.5" font-weight="700" text-anchor="middle">{bar_item['code']}</text>
            <text x="{bx + b_width/2}" y="{gy_max + 32}" fill="#6B7280" font-size="9" font-weight="500" text-anchor="middle">{bar_item['title']}</text>
            '''

        # Card Footer Caption
        svg += f'''
            <g transform="translate(20, {card_h - 22})">
                <text x="0" y="10" fill="#94A3B8" font-size="9.5">TELOS+S Feasibility + Robotic Potential</text>
            </g>
        </g>
        '''

    svg += '</svg>'

    # Save to single deliverable path
    with open("summary-image/telos_s_robotics_column_bar.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Generated: summary-image/telos_s_robotics_column_bar.svg")


# ==============================================================================
# 3. HIGH-RESOLUTION PNG EXPORTER (2X / 300 DPI)
# ==============================================================================

def export_all_pngs():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By

    print("\nStarting High-Resolution PNG export (2x Device Scale)...")
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--force-device-scale-factor=2')

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1800, 1200)

    tasks = [
        ("summary-image/feasibility_robotics_cross_matrix.svg", "summary-image/feasibility_robotics_cross_matrix.png"),
        ("summary-image/telos_s_robotics_column_bar.svg", "summary-image/telos_s_robotics_column_bar.png")
    ]

    for svg_file, png_file in tasks:
        abs_svg = os.path.abspath(svg_file).replace(os.sep, '/')
        abs_png = os.path.abspath(png_file)
        driver.get(f'file:///{abs_svg}')
        svg_elem = driver.find_element(By.TAG_NAME, 'svg')
        svg_elem.screenshot(abs_png)
        size_kb = os.path.getsize(abs_png) / 1024
        print(f"Exported High-Res PNG: {png_file} ({size_kb:.1f} KB)")

    driver.quit()
    print("All High-Resolution PNGs exported successfully!")


if __name__ == "__main__":
    generate_clean_cross_matrix()
    generate_three_columns_comparison()
    export_all_pngs()
