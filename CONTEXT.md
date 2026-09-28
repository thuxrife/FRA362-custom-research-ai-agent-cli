# CONTEXT.md — Multi-Agent Feasibility & Research System Context

> **Project:** FRA362 Engineering Project Management (FIBO, KMUTT)  
> **System:** Dual Multi-Agent Research & Systems-Thinking Feasibility System (TELOS+S + FIBO Robotics Axis)  
> **Last Updated:** September 26, 2026  
> **Purpose:** Persistent context ledger. If this chat session is closed, disconnected, or restarted, read this file first to resume immediately without losing project state.

---

## 1. Project Overview & Current State

### Dual Multi-Agent Architecture
1. **Group 1: Dialectical Research Team**:
   - Roles: `(1-1-manager)`, `(1-2-researcher)`, `(1-3-objectionist)`, `(1-4-note-taker)`, `(1-5-summarizer)`
   - Function: Literature survey, DuckDuckGo live search, ArXiv papers, FMEA risk matrix, dialectical debate.
2. **Group 2: TELOS+S Feasibility Consulting Team**:
   - Roles: `(2-1-jury)` (Chief Judge & Orchestrator), `(2-2-tech-feasibility)`, `(2-3-economic-feasibility)`, `(2-4-legal-feasibility)`, `(2-5-operational-feasibility)`, `(2-6-schedule-feasibility)`, `(2-7-sdgs-expert)`
   - Function: Rigorous systems-thinking feasibility audit based on LN5 curriculum (Anti-Tech Trap, cross-aspect interdependence, discrete whole integer scores `{1, 2, 3, 4, 5}`, knockout fatal flaw rule `MIN=1 -> VETOED`).
3. **Orthogonal Robotics Axis (FIBO Compatibility)**:
   - Scale: **0.0 to 12.0 points** (evaluated independently, **never** added to the 100-point TELOS+S score).
   - Core Triad: **Sense (Perception 4.0) $\to$ Think (Processing 4.0) $\to$ Act (Actuation 4.0)** closed-loop (3 pillars $\times$ 4 rubric levels = clean 12.0 points).

---

## 2. Active Intake Proposals (`solution-details/`)

Following the confirmed municipal drainage constraint (**"มีน้ำอยู่ในท่อไม่เกิน 20%"** — Water inside pipe $\le 20\%$, meaning $\ge 80\%$ open airspace), **Solution 3 (Underwater Sonar Profiling) is EXCLUDED** because sonar physically requires flooded submersion and fails in low-water conditions.

Currently, **3 candidate solutions** are evaluated (ordered by feasibility score descending):

1. **Solution 2 (`solution-details/solution-2.md`)**:
   - *Title*: `Pipe Inspection Instrument using Acoustic Reflectometry`
   - *Concept*: Airborne Acoustic Reflectometry across consecutive manholes (SL-RAT EPA USA Standard); digital signal processing (DSP) measures acoustic attenuation in the 80%+ pipe airspace and outputs automated **0–10 Cleanliness Score** for condition-based jetting dispatch.
   - *TELOS+S Feasibility*: **83.53 / 100 — HIGHLY VIABLE (ผ่านเกณฑ์ระดับดีเยี่ยม)**
     - Zero Fatal Flaws! Recalibrated for Bangkok Municipal Standing Water Reality ($\le 20\%$ dry-weather standing water and $\ge 80\%$ clear headspace).
     - `T-03=3` (TRL 5-6 with standing water compensation baseline), `E-01=4` (1-2 year payback covering 80-90% gravity lateral network), `O-02=3` (Street-level tripod/wand deployment without sewer entry).
     - Highest Economic ROI, lowest operational friction (zero robot in sewage, 100% fail-safe retrieval), perfect team skill alignment (Due's audio amp & JK's DSP).
   - *Robotics Potential*: **8.5 / 12.0** (Perception: 3.5/4.0, Processing: 3.5/4.0, Actuation: 1.5/4.0 — Advanced NDT acoustic reflectometry payload with spectral DSP).

2. **Solution 1 (`solution-details/solution-1.md`)**:
   - *Title*: `Pipe Inspection Robot using CCTV for profiling pipe`
   - *Concept*: 4K PTZ Camera + High-Power LED array mounted on a Wheeled Crawler Platform with YOLOv8 AI object detection for cracks, leaks, and blockages.
   - *TELOS+S Feasibility*: **59.30 / 100 — CONDITIONALLY VIABLE (ผ่านเกณฑ์แบบมีเงื่อนไข)**
     - Zero Fatal Flaws! Under $\le 20\%$ water level, camera sits in the upper air cavity avoiding total submersion. However, crawler wheels must maintain traction through sludge/wastewater.
     - Lowest scores are 2 on `T-01` (IP68 waterproofing chassis fabrication), `E-03` (Scrap buffer for high-spec camera/tether), `L-01` (Traffic/manhole closure permits), `O-04` (Multi-stage setup complexity), `S-01` (5-week development maturity).
   - *Robotics Potential*: **10.5 / 12.0** (Perception: 3.5/4.0, Processing: 3.5/4.0, Actuation: 3.5/4.0 — Genuine closed-loop mobile robotic crawler with edge AI vision).

3. **Solution 4 (`solution-details/solution-4.md`)**:
   - *Title*: `Pipe Inspection Instrument using LiDAR SLAM attaching with Robot`
   - *Concept*: 3D LiDAR laser time-of-flight scanning + IMU mounted on mobile crawler doing LiDAR SLAM to construct dense 3D point cloud pipe profiles.
   - *TELOS+S Feasibility*: **55.04 / 100 — VETOED / NON-VIABLE PENDING DE-SCOPING (ตกเกณฑ์ข้อบังคับวิกฤต)**
     - Fatal Flaw (`score == 1`): `E-03=1` (Scrap Margin / Budget Ceiling: 3D LiDAR sensor ~30,000 THB + Jetson exhausts 100% of student budget with zero spare allowance if flooded in sewage).
     - Critical Physical Flaw: `T-03=2` (Laser light 905nm suffers specular absorption/reflection on dark wastewater puddle surface at bottom 20%).
   - *Robotics Potential*: **11.5 / 12.0** (Perception: 4.0/4.0, Processing: 4.0/4.0, Actuation: 3.5/4.0 — Gold-standard capstone robotics depth).

*(Note: Solution 3 - Underwater Sonar is formally archived as non-viable due to fundamental operational mismatch with the $\le 20\%$ water constraint).*

---

### Latest Generated Deliverables:
- **JSON Matrix**: `feasibility-outcome/jury_eval_data.json` (3 solutions sorted by score)
- **Master Excel**: `feasibility-outcome/9-29-2026-0233_0.xlsx` (Executive Comparison tab + 3 solution tabs)
- **Executive Visualizations (`summary-image/`)**:
  - `summary-image/feasibility_robotics_cross_matrix.png` & `.svg` (2D Cross-Matrix for 3 solutions: Y-axis 0–12, X-axis 0-100)
  - `summary-image/telos_s_robotics_column_bar.png` & `.svg` (3 Big Columns Comparison: Solution 2, Solution 1, Solution 4 with 7-pillar bar chart & overall score)
- **Subagent Conversation Roster**:
  - `fe13f96f-6ed8-4e39-9331-dcd8dcfebe1a` (`fibo_robotics_auditor`)
  - `36f568c7-bf8e-40e3-b01b-63f688946acf` (`telos_specialist_auditor` - Technical 2.2)
  - `2147c166-449e-404e-8fe5-7cb83a07de03` (`telos_specialist_auditor` - Economic 2.3 & Legal 2.4)
  - `109428fa-ebb9-487b-adc8-6b3de490784e` (`telos_specialist_auditor` - Operational 2.5 & Schedule 2.6)
  - `344b9544-223c-4807-b83f-b012ba39b717` (`telos_specialist_auditor` - SDGs Sustainability 2.7)

---

## 3. Team Roster (`team-skills/`) & Schedule (`schedule-details/`)

### Team Members:
- **Due**: Mechatronics & Embedded Systems (SolidWorks CAD, ESP32 C/C++, custom PCB design, circuit assembly, MAX98357 audio amp, RFID, MQTT, Java Spring MySQL).
- **Fifa**: Mechanical Design & Prototyping (3D CAD, power transmission: shafts, pulleys, belts, gears, couplings, robotic assembly/maintenance, ESP32, load cell/laser calibration).
- **Jay**: Mechanical calculations (1 DOF pick-and-place, FEA, component calculation, CAD).
- **JK**: Robotics Software & Control Systems (Advanced math, differential equations, linear algebra, hydraulics $dh/dt$, Python, C/C++, ROS2, Micro-ROS, OpenCV, STM32/ESP32; *Cannot access Machine Shop, no custom PCB routing, low soldering*).
- **Kin**: AI Pipeline & Telemetry (Time-series data, ML, API ingestion backend, telemetry architecture, drainage domain knowledge).

### Schedule Constraints (`schedule-details/schedule.md`):
- **Week 9 (29/Sept)**: Proposal Presentation (TRL 2 target)
- **Week 10 (6/Oct)**: Feedback
- **Weeks 10+1 & 10+2**: **University Midterm Exams (Zero Development Hours / Blackout)**
- **Weeks 11–12**: Consultation / Project Time
- **Week 13 (10/Nov)**: Progress Update (TRL 3 Bench PoC target)
- **Weeks 14–15**: Consultation / Project Time
- **Weeks 15+1 & 15+2**: **University Final Exams (Zero Development Hours / Blackout)**
- **Week 16 (15/Dec)**: Final Presentation (TRL 4 Breadboard Demonstration & Full Report)

---

## 4. The 17 Standardized Questions & Normalized Weights (`question_raw.txt`)

All solutions are benchmarked against the exact same 17 problem-space questions with **5-level discrete integer rubrics `{1, 2, 3, 4, 5}`** and a **Two-Tier Normalized Weighting Architecture** totaling 100.0%:

| Pillar | ID | Question Title | Weight |
| :--- | :--- | :--- | :---: |
| **Technical (20.0%)** | `T-01` | Implementation (Build vs. Buy Burden) | 4.0% |
| | `T-02` | Access (Tech Stack & Ecosystem Permissions) | 4.0% |
| | `T-03` | Base Performance (Technology Readiness Level - TRL) | 4.0% |
| | `T-04` | Team Compatibility (Manpower & Skill Redundancy / SPOF) | 4.0% |
| | `T-05` | Learning Curve ("How much do we have to learn?") | 4.0% |
| **Economic (20.0%)** | `E-01` | ROI (Payback Period / Value Horizon) | 6.67% |
| | `E-02` | Dependency of Component (Vendor Lock-in & Reliability) | 6.67% |
| | `E-03` | Scrap Margin (Safety Allowance for Blown ICs & Iterations) | 6.66% |
| **Legal (15.0%)** | `L-01` | Felony and Civil Law (Regulatory, Traffic & Public Safety Compliance) | 7.5% |
| | `L-02` | IP and Licensing | 7.5% |
| **Operational (20.0%)** | `O-01` | User — Failure Impact ("If it fails, how severe is the effect?") | 5.0% |
| | `O-02` | User — Behavior & Problem-Solution Fit | 5.0% |
| | `O-03` | Developer — Contribution Dependency (Administrative & Lab Gatekeeping) | 5.0% |
| | `O-04` | Developer — Complexity (Step Count & Pipeline Friction) | 5.0% |
| **Schedule (15.0%)** | `S-01` | Production Time (Engineering Design Maturity by 5 Business Weeks) | 15.0% |
| **SDGs (10.0%)** | `SDG-01` | Stockholm Wedding Cake Coverage (Planet, People, Prosperity integration) | 5.0% |
| | `SDG-02` | Environmental Footprint, E-Waste & Circular Economy ("Do No Harm" & circularity) | 5.0% |
| **Total Weight** | | **6 Pillars / 17 Diagnostic Questions** | **100.0%** |

---

## 5. Subagent-Style Execution Protocol (Explicit User Mandate)

**Rule:** Do NOT let The Jury operate in solo mode thinking on behalf of all specialists. The user explicitly requested an actual **Subagent-driven execution style**:

1. **Subagent Invocations**:
   - `(2-2-tech-feasibility)`: Audits `T-01` to `T-05` and evaluates Man & Machine capabilities.
   - `(2-3-economic-feasibility)`: Audits `E-01` to `E-03` on CapEx, OpEx, and Zero-Action trade-offs.
   - `(2-4-legal-feasibility)`: Audits `L-01` to `L-02` on PDPA, road safety, and licensing.
   - `(2-5-operational-feasibility)`: Audits `O-01` to `O-04` on operator friction and developer setup.
   - `(2-6-schedule-feasibility)`: Audits `S-01` against university exam blackouts and 5-week TRL milestones.
   - `(2-7-sdgs-expert)`: Audits `SDG-01` to `SDG-03` against UN targets and Stockholm Wedding Cake.
   - `fibo_robotics_auditor`: Audits the **Perception $\to$ Processing $\to$ Actuation** triad on the 0.0–10.0 scale.
2. **Subagent Tool Usage**:
   - Use `invoke_subagent` to spawn specialists.
   - Subagents review `solution-details/`, `team-skills/`, `schedule-details/`, and `question_raw.txt`.
   - Subagents return their structured JSON assessment chunk containing scores `{1-5}`, rationale, evidence citations, and de-scoping advice.
3. **The Jury Synthesis & Compilation**:
   - `(2-1-jury)` receives subagent evaluations, verifies bias-free language, checks for Knockout violations (`score == 1`), and writes the unified array into `feasibility-outcome/jury_eval_data.json`.
   - Run `python feasibility-analysis.py` to compile the final timestamped Excel file `feasibility-outcome/{month}-{date}-{year}-{time}_{seq}.xlsx`.

---

## 6. Script Execution Pipeline & Adjustable Parameters

This system is completely decoupled: the Python code contains zero hardcoded questions, and all evaluation rules flow from `jury_eval_data.json`.

```
[update_jury_eval.py] ──> [jury_eval_data.json] ──┬──> [feasibility-analysis.py] ──> [Master Excel .xlsx]
                                                 ├──> [generate_summary_images.py] ──> [SVGs & PNGs]
                                                 └──> [verify_excel.py] ──> [Verification Audit]
```

### Script-to-Output Reference Table:

| Script | Input File | Output File | Purpose | What Can Be Adjusted |
| :--- | :--- | :--- | :--- | :--- |
| **`update_jury_eval.py`** | Solution MDs, Question rubrics | `feasibility-outcome/jury_eval_data.json` | Master Evaluation Engine & Data Source of Truth | • Solution inclusion/exclusion (add/remove solutions)<br>• Solution ordering/ranking<br>• Discrete scores `{1, 2, 3, 4, 5}` & question weights<br>• Diagnostic evidence citations & de-scoping advice<br>• Robotics triad scores (Perception, Processing, Actuation each 0.0–4.0, total /12) |
| **`feasibility-analysis.py`** | `feasibility-outcome/jury_eval_data.json` | `feasibility-outcome/{month}-{date}-{year}-{time}_{seq}.xlsx` | Transposed Horizontal TELOS+S Master Excel Matrix & Executive Comparison Sheet | • Excel output directory / custom filename (`--name`, `--outdir`)<br>• Excel styling, fonts (Segoe UI), color palettes (Navy/White)<br>• Excel formula definitions (`SUM`, `IF(MIN=1, VETOED, ...)` thresholds)<br>• Column widths and header labeling |
| **`generate_summary_images.py`** | `feasibility-outcome/jury_eval_data.json` | `summary-image/feasibility_robotics_cross_matrix.svg/.png`<br>`summary-image/telos_s_robotics_column_bar.svg/.png` | Executive Visualizations: 2D Cross-Matrix (TELOS+S vs. Robotics) & Ranked Column Bar Chart | • Color palette (`PALETTES` array: White-Purple theme)<br>• Cross-Matrix card callout positions (`card_configs`: coordinates, leader lines)<br>• Threshold lines (Feasibility $\ge 60$, Robotics $\ge 8.0$)<br>• Column card dimensions (`card_w`, `card_gap`, `start_x`)<br>• PNG export resolution / device scale factor (default: 2.0x scale) |
| **`verify_excel.py`** | Latest `.xlsx` in `feasibility-outcome/` | Console Audit Log | Validates Excel structural integrity, formula references, and tab counts | • Sheet validation rules<br>• Row/column verification ranges |

### Standard Execution Pipeline:
```powershell
# Step 1: Update/validate evaluation data engine
python update_jury_eval.py

# Step 2: Compile Master Excel workbook
python feasibility-analysis.py

# Step 3: Generate visual assets (SVGs and high-res PNGs)
python generate_summary_images.py

# Step 4: Verify generated Excel structure
python verify_excel.py
```

---
*End of Context Ledger. Keep this file updated after every major architecture or score change.*
