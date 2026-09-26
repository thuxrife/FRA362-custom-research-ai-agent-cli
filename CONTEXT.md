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
   - Scale: **0.0 to 10.0 points** (evaluated independently, **never** added to the 100-point TELOS+S score).
   - Core Triad: **Sense (Perception) $\to$ Think (Processing) $\to$ Act (Actuation)** closed-loop.

---

## 2. Active Intake Proposals (`solution-details/`)

Currently, only **3 active solutions** are being evaluated (solutions 4 and 5 were deprecated):

1. **`solution-details/solution-1.md`**:
   - *Title*: `CCTV on the road (Visual water flow) + ultrasonic to measure the flow rate of the canal + alarm`
   - *Concept*: Computer vision (PTV/PIV, Optical Flow) on road CCTV combined with existing canal ultrasonic level meters.
   - *TELOS+S Feasibility*: **65.93 / 100 — VETOED / NON-VIABLE PENDING DE-SCOPING**
     - Fatal Flaws: `T-02=1` (BMA municipal firewall blocks RTSP streams), `T-03=1` (Uncalibrated LSPIV without seeding is TRL 2-3), `T-04=1` (Single Point of Failure: only JK has OpenCV, 0 have fluid velocimetry).
   - *Robotics Potential*: **4.8 / 10.0** (Perception: 2.5, Processing: 2.1, Actuation: 0.2 — Broken loop at Actuation, open-loop alert).
2. **`solution-details/solution-2.md`**:
   - *Title*: `Sewer Inspection by transmitter and receiver. Mapping Sewer profile`
   - *Concept*: Airborne Acoustic Reflectometry across manholes under normal low-water conditions; digital signal processing generates 2D cross-section and automated **Cleanliness Score (0–10)** for maintenance dispatch.
   - *TELOS+S Feasibility*: **69.10 / 100 — CONDITIONALLY VIABLE (ผ่านเกณฑ์แบบมีเงื่อนไข)**
     - Zero Fatal Flaws! Minimum score is 2 on `L-01` (Traffic/confined space permits required for public manholes).
     - Highest SDG Score (8.67 / 10.0) due to 100% fail-safe retrieval and zero e-waste left in sewers.
   - *Robotics Potential*: **5.8 / 10.0** (Perception: 2.8, Processing: 2.4, Actuation: 0.6 — Advanced NDT acoustic sensor payload, DSP filtering, automated 0-10 cleanliness score).
3. **`solution-details/solution-3.md`**:
   - *Title*: `ระบบปล่อยน้ำแบบ Adaptive เพื่อระบายความร้อนบนทางเดินเท้าและตรอกซอยอย่างมีประสิทธิภาพสูงสุด`
   - *Concept*: Contactless IR surface temperature sensor triggering high-pressure solenoid misting when $>45^\circ\text{C}$ between 11:00–14:00.
   - *TELOS+S Feasibility*: **67.17 / 100 — VETOED / NON-VIABLE PENDING DE-SCOPING**
     - Fatal Flaw: `E-01=1` (Payback $\ge 10$ yrs: continuous potable water and electricity consumption with zero direct financial return or labor savings in Bangkok's 80% RH climate).
     - Critical Operational Hazards: `O-01=2` (Pedestrian slipping hazards on wet pavement), `O-02=2` (Shopfront resistance against misting dampening wares).
   - *Robotics Potential*: **8.0 / 10.0** (Perception: 2.7, Processing: 3.0, Actuation: 2.3 — Complete closed-loop cyber-physical mechatronic system).

---

### Latest Generated Deliverables:
- **JSON Matrix**: `feasibility-outcome/jury_eval_data.json`
- **Master Excel**: `feasibility-outcome/9-26-2026-1648_0.xlsx`
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

## 4. The 18 Standardized Questions & Normalized Weights (`question_raw.txt`)

All solutions are benchmarked against the exact same 18 problem-space questions with **5-level discrete integer rubrics `{1, 2, 3, 4, 5}`** and a **Two-Tier Normalized Weighting Architecture** totaling 100.0%:

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
| **SDGs (10.0%)** | `SDG-01` | SDG-01: Public Impact vs. Academic Greenwashing (SDG 11.5 / 13.1) | 3.33% |
| | `SDG-02` | SDG-02: Environmental Footprint & E-Waste ("Do No Harm" — SDG 6.3 / 12.4) | 3.33% |
| | `SDG-03` | SDG-03: Algorithmic Equity & Decision Transparency (SDG 10.2 / 16.6) | 3.34% |
| **Total Weight** | | **6 Pillars / 18 Diagnostic Questions** | **100.0%** |

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
# 1. Update/check jury evaluation JSON (if running via helper script)
python update_jury_eval.py

# 2. Compile Excel workbook from jury_eval_data.json
python feasibility-analysis.py

# 3. Check git status
git status
```

---
*End of Context Ledger. Keep this file updated after every major architecture or score change.*
