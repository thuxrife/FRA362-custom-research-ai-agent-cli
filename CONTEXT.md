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

Currently, **4 active solutions** are evaluated for the urban pipe inspection and condition-based maintenance domain:

1. **`solution-details/solution-1.md`**:
   - *Title*: `Pipe Inspection Robot using CCTV for profiling pipe`
   - *Concept*: 4K PTZ Camera + High-Power LED array mounted on a Wheeled Crawler Platform with YOLOv8 AI object detection for cracks, leaks, and blockages.
   - *TELOS+S Feasibility*: **59.30 / 100 — CONDITIONALLY VIABLE (ผ่านเกณฑ์แบบมีเงื่อนไข)**
     - Zero Fatal Flaws! Lowest scores are 2 on `T-01` (IP68 waterproofing chassis fabrication), `E-03` (Scrap buffer for high-spec camera/tether), `L-01` (Traffic/manhole closure permits), `O-04` (Multi-stage setup complexity), `S-01` (5-week development maturity).
   - *Robotics Potential*: **10.5 / 12.0** (Perception: 3.5/4.0, Processing: 3.5/4.0, Actuation: 3.5/4.0 — Genuine closed-loop mobile robotic crawler with edge AI vision).

2. **`solution-details/solution-2.md`**:
   - *Title*: `Pipe Inspection Instrument using Acoustic using Reflectometry`
   - *Concept*: Airborne Acoustic Reflectometry across consecutive manholes (SL-RAT EPA USA Standard); digital signal processing (DSP) measures acoustic attenuation and outputs automated **0–10 Cleanliness Score** for condition-based jetting dispatch.
   - *TELOS+S Feasibility*: **83.53 / 100 — HIGHLY VIABLE / TOP RECOMMENDED (ผ่านเกณฑ์ระดับดีเยี่ยม)**
     - Zero Fatal Flaws! Recalibrated for Bangkok Municipal Standing Water Reality (Roadside gravity laterals with 10–30% dry-weather standing water and 70–90% headspace).
     - `T-03=3` (TRL 5-6 with standing water compensation baseline), `E-01=4` (2-3 year payback covering 65-75% roadside network), `O-02=3` (Triage rule: use on gravity laterals with headspace, avoid 100% submerged inverted siphons).
     - Highest Economic ROI, lowest operational friction (zero robot in sewage, 100% fail-safe retrieval), perfect team skill alignment (Due's audio amp & JK's DSP).
   - *Robotics Potential*: **8.5 / 12.0** (Perception: 3.5/4.0, Processing: 3.5/4.0, Actuation: 1.5/4.0 — Advanced NDT acoustic reflectometry payload with spectral DSP).

3. **`solution-details/solution-3.md`**:
   - *Title*: `Pipe Inspection Instrument using Sonar Frequency Profiling attaching with Robot`
   - *Concept*: Submersible 360° rotating underwater Sonar transducer on float/crawler doing frequency profiling and 3D cross-sectional geometry mapping through dirty wastewater.
   - *TELOS+S Feasibility*: **33.43 / 100 — VETOED / NON-VIABLE PENDING DE-SCOPING (ตกเกณฑ์ข้อบังคับวิกฤต)**
     - Fatal Flaws (`score == 1`): `T-01=1` (Build from scratch underwater piezo matching), `T-04=1` (Zero team members have underwater hydrophone experience), `T-05=1` (Total reset learning curve), `E-02=1` (Proprietary vendor lock-in), `E-03=1` (Zero scrap buffer for >50k THB sonar head), `O-04=1` (Convoluted pipeline), `S-01=1` (0% design maturity impossible in 5 weeks).
   - *Robotics Potential*: **10.5 / 12.0** (Perception: 4.0/4.0, Processing: 3.5/4.0, Actuation: 3.0/4.0 — Exemplary deep sensing robotics, but non-viable for capstone constraints).

4. **`solution-details/solution-4.md`**:
   - *Title*: `Pipe Inspection Instrument using LiDAR SLAM attaching with Robot`
   - *Concept*: 3D LiDAR laser time-of-flight scanning + IMU mounted on mobile crawler doing LiDAR SLAM to construct dense 3D point cloud pipe profiles.
   - *TELOS+S Feasibility*: **55.04 / 100 — VETOED / NON-VIABLE PENDING DE-SCOPING (ตกเกณฑ์ข้อบังคับวิกฤต)**
     - Fatal Flaw (`score == 1`): `E-03=1` (Scrap Margin / Budget Ceiling: 3D LiDAR sensor ~30,000 THB + Jetson exhausts 100% of budget with zero spare allowance if flooded in sewage).
     - Critical Physical Flaw: `T-03=2` (Laser light 905nm suffers total absorption/refraction on wastewater, fails in flooded/foggy sewer pipes).
   - *Robotics Potential*: **11.5 / 12.0** (Perception: 4.0/4.0, Processing: 4.0/4.0, Actuation: 3.5/4.0 — Gold-standard capstone robotics depth).

---

### Latest Generated Deliverables:
- **JSON Matrix**: `feasibility-outcome/jury_eval_data.json`
- **Master Excel**: `feasibility-outcome/9-28-2026-2331_0.xlsx`
- **Executive Visualizations (`summary-image/`)**:
  - `summary-image/feasibility_robotics_cross_matrix.png` & `.svg` (2D Cross-Matrix for 4 solutions: Y-axis 0–12, X-axis 0-100)
  - `summary-image/telos_s_robotics_column_bar.png` & `.svg` (4 Big Columns Comparison: 1 column per solution with individual 7-pillar bar chart & overall score)
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

## 6. Execution Command Quick Reference

```powershell
# 1. Update/check jury evaluation JSON (Master Source of Truth)
python update_jury_eval.py

# 2. Compile Excel workbook from jury_eval_data.json
python feasibility-analysis.py

# 3. Generate Executive Visualizations (SVGs & 300 DPI PNGs in summary-image/)
python generate_summary_images.py

# 4. Check git status
git status
```

---
*End of Context Ledger. Keep this file updated after every major architecture or score change.*
