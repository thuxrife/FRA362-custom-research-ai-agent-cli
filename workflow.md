# Multi-Agent Research & Feasibility Workflow Specification

## 1. System Overview
This project implements a **Dual Multi-Agent Architecture**:
- **Group 1: Dialectical Research Team (Thesis → Antithesis → Synthesis)**
  - Roles: 1.1 Manager, 1.2 Researcher, 1.3 Objectionist, 1.4 Note-Taker, 1.5 Summarizer
- **Group 2: TELOS+S Feasibility Consulting Team (Systems-Thinking Robotics Audit)**
  - Roles: 2.1 The Jury, 2.2 Technology, 2.3 Economic, 2.4 Legal & Outreach, 2.5 Operational, 2.6 Schedule, 2.7 SDGs Expert

All agent personas and SOPs are maintained in modular Markdown files located in `agents/`.

---

## 2. Directory & Folder Organization

### A. The 3 Structured Intake Folders (User Input)
Feasibility analysis is driven strictly by three evidence-backed intake folders located at the root of the project:

```text
📁 solution-details/
├── solution-1.md                       <-- Solution proposal or subsystem concept 1
└── solution-2.md (or *.md)             <-- Alternative solutions or teammate contributions
                                            (The Jury accepts heterogeneous formats and writing styles)

📁 team-skills/
├── {name-1}.md                         <-- Individual teammate profile (e.g. somchai.md)
└── {name-2}.md                         <-- Individual teammate profile (e.g. jk.md)
                                            (Contains hard skills: Mech/Elec/Prog, outreach, and verified past project evidence)

📁 schedule-details/
└── schedule.md                         <-- Standalone single project schedule file with target deadline, 
                                            academic exam blackouts, milestones, and procurement lead times
```

### B. Session Deliverable Subfolders (USA Date Format)
Every session creates matching subfolders formatted as:
`M-D-YYYY_HHMM-{Topic_Slug}` (e.g. `9-22-2026_2310-TELOS_Drainage_QRT_Filtering`).

```text
feasibility-outcome/
├── jury_eval_data.json                  <-- Dynamic TELOS+S JSON generated autonomously by The Jury alone
└── {month}-{date}-{year}-{time}_{seq}.xlsx <-- Transposed horizontal Excel workbook (Strict integers 1-5)

teammate-persona/
└── <session>/
    └── team_skills.md                  <-- 4-Level Contextual Skill & Outreach Audit with evidence links

research-outcome/
└── <session>/
    └── sources.html                    <-- Interactive HTML with clickable hyperlinks

note-taker-log/
└── <session>/
    └── debate_log.md                   <-- Complete verbatim debate transcript

summarize-outcome/
└── <session>/
    ├── summary.html                    <-- Styled HTML executive report
    └── summary.md                      <-- Clean Markdown report
```

### C. Root Execution Tool
- **`feasibility-analysis.py`**: Automated Python script at the root directory that ingests the 3 intake folders, executes the TELOS+S stress-test, and compiles the transposed horizontal Excel matrix directly into `feasibility-outcome/{month}-{date}-{year}-{time}.xlsx`.

---

## 3. The Core Concept of Feasibility Study (TELOS+S)

Based on the engineering project management curriculum (LN5 Feasibility Study):

### 1. Practicality & Potential for Success
Feasibility is **an assessment of practicality and potential for success**, evaluating whether an idea is possible to execute easily, conveniently, and sustainably in the real world.

### 2. Beware "The Tech Trap" (Slide 17)
Engineering students frequently fall into **The Tech Trap**: spending 90% of their effort proving technical possibility while ignoring operational, economic, and human realities. Engineering projects rarely fail because code wouldn't compile or a motor wouldn't spin—they fail because operators refuse to use it, regulations block it, or budget and schedules collapse.

### 3. Cross-Aspect Interdependence (Slide 18)
No feasibility aspect exists in a silo. **All aspects affect the others**:
- Complex **Technology** choices inflate the **Schedule** and blow up the **Economic** BOM and scrap budget.
- **Operational** workflow resistance from operators kills the practical value of sophisticated algorithms.
- **Schedule** collisions with university exams constrain available engineering time, demanding radical hardware de-scoping.

### 4. Critical Context-Specific Stress-Test Questions (Anti-Bias & Anti-Generic)
- **Standardized Problem-Space Question Anchoring (Fair Multi-Solution Baseline)**:
  - When comparing alternative solutions (`solution-1.md` vs. `solution-2.md`), the **Diagnostic Question Codes and Core Prompts (Row 6) MUST remain standardized across all solutions** (anchored to the common problem space, operating environment, and system requirements).
  - Only the **Evidence Citations (Row 12)**, **Rubric Benchmarks (Row 8)**, and **Assigned Scores (Row 9)** adapt to each specific solution architecture. This eliminates question asymmetry and guarantees true Apple-to-Apple comparability.
- **Zero Solution Bias**: The Jury strictly rejects leading questions tailored to flatter the proposed technology.
- **Zero Generic Textbook Headers**: Questions must not be vague slide headers (e.g., *"Is the project technically possible?"* is forbidden).
- **Flexible 2 to 4 Core Questions per Pillar**: Each pillar contains 2 to 4 questions (12 to 24 questions total) rather than an arbitrary rigid 18-question template, ensuring every question probes a real failure mode without filler.

### 5. Two-Tier Normalized Weighting Architecture (Weighting Integrity)
To prevent the Technical aspect from mathematically overshadowing Operational or Economic realities (preventing "The Tech Trap" under the hood), all evaluations roll up through fixed Pillar Weights:
$$\text{Total Score} = \sum (\text{Pillar Weight} \times \text{Pillar Average Score}) \times 20$$
- **Technical ($T$)**: 20%
- **Economic ($E$)**: 20%
- **Legal & Outreach ($L$)**: 15%
- **Operational ($O$)**: 20% (The Anti-Tech-Trap Core)
- **Schedule ($S$)**: 15%
- **SDGs ($SDG$)**: 10%
- **Total Pillar Sum**: Exactly 100.0%
- Sub-questions within a pillar share that pillar's weight equally: $w_{q} = W_{\text{pillar}} / N_{\text{questions\_in\_pillar}}$.

### 6. The Knockout / Fatal-Flaw Gating Rule (Anti-Average-Score Trap)
Feasibility is fundamentally a series of **non-negotiable gates**, not merely an arithmetic average:
- If **ANY question** in ANY pillar receives an evidence-backed score of **`1`** (Fatal Failure / Non-Viable / Direct Law Violation / Hazard to Life), the solution is immediately flagged as:
  **`VETOED / NON-VIABLE PENDING DE-SCOPING (ตกเกณฑ์ข้อบังคับวิกฤต / ยุติโครงการชั่วคราว)`**
- High scores in other pillars CANNOT mathematically mask a fatal flaw. The solution remains Dead on Arrival (DOA) until the flaw is mitigated via formal de-scoping.

### 7. Strict Discrete Integer Scoring ({1, 2, 3, 4, 5} ONLY — Zero Decimals / No 0.5)
- All assigned diagnostic scores MUST be discrete whole integers strictly chosen from **`{1, 2, 3, 4, 5}`**.
- **No 0.5 or fractional decimals under any circumstances**: An aspect either satisfies the rubric criteria for an integer level or it does not. Evaluators must make decisive judgments based on evidence.

### 8. The 4-Level Contextual Learning & Outreach Scale
Evaluates human capability based on the **Contextual Gap** between past project evidence and required complexity:
* **Level 1 (Critical Deficit / High Barrier)**: Zero foundation; insurmountable learning curve; or team is unwilling/blocked from government or external facility outreach.
* **Level 2 (Foundational / Steep Learning Curve)**: Basic theoretical knowledge; no production hardware experience; willingness exists but lacks warm institutional contacts.
* **Level 3 (Adjacent Competence / Manageable Curve)**: Strong mastery in adjacent tech stacks (e.g. ESP32 to STM32; CAD to CNC); active access to faculty/university channels.
* **Level 4 (Proven Production Mastery / Direct Access)**: Direct track record delivering identical/higher complexity systems in past projects; active MoUs or approved permits.

---

## 4. Upgraded Feasibility Roles

| ID | Agent Name | Strict Tag Prefix | Destination Folder | Core Consulting Mission & Focus |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **The Jury** | `(2-1-jury)` | `feasibility-outcome/` | **Chief Judge, Solo Architect & Anti-Tech-Trap Gatekeeper**: Operates in dual modes: can audit all 6 TELOS+S pillars alone in 1 single step, or orchestrate specialists 2.2–2.7. Ingests the 3 intake folders, eliminates biased questions, enforces integer scoring `{1-5}`, two-tier weighting, knockout gating, and compiles `{month}-{date}-{year}-{time}_{seq}.xlsx`. |
| **2.2** | **Tech Feasibility** | `(2-2-tech-feasibility)` | `teammate-persona/` | **Man & Machine Auditor**: Audits real tool access, fabrication skills (Mech/Elec/Prog), and the time/cost overhead that technology choices extract from the project. Flags Pioneer Novelty Risks. |
| **2.3** | **Economic Feasibility** | `(2-3-economic-feasibility)` | N/A | **Cost-Benefit & Financial Reality Analyst**: Evaluates funding reality, budget ceilings, scrap/iteration allowances, and true worth compared to the Zero-Action baseline (doing nothing / manual labor). |
| **2.4** | **Legal & Outreach Feasibility** | `(2-4-legal-feasibility)` | N/A | **Institutional & Policy Gatekeeper**: Audits statutory law (PDPA, NBTC), municipal liabilities, IP infringements, and the team's verified capability to conduct in-person government agency liaisons. |
| **2.5** | **Operational Feasibility** | `(2-5-operational-feasibility)` | N/A | **The "Will It Actually Be Used?" Stress-Tester**: Audits dispatcher adoption, procedural resistance (e.g. Traffy Fondue photo evidence rules), workflow disruption, training burdens, and developer burnout. |
| **2.6** | **Schedule Feasibility** | `(2-6-schedule-feasibility)` | N/A | **Conflict & Deadline Realist**: Audits milestone delivery realism against formal TRL levels (TRL2, TRL3, TRL4), stress-testing against university exam blackouts and procurement lead times. |
| **2.7** | **SDGs Expert** | `(2-7-sdgs-expert)` | N/A | **Systemic Sustainability Consultant**: Evaluates multi-layer Stockholm Wedding Cake impact (Biosphere, Society, Economy), UN SDG indicators, and Do-No-Harm safeguards (preventing e-waste and vulnerability shifts). |

---

## 5. Transposed Horizontal Excel Matrix Specification (`{month}-{date}-{year}-{time}_{seq}.xlsx`)

Generated automatically via `openpyxl` directly inside `feasibility-outcome/{month}-{date}-{year}-{time}_{seq}.xlsx`.

### Layout Structure:
The matrix is transposed horizontally so that **headers and scores align parallel across columns**, allowing immediate horizontal comparison:
- **Column A**: Attribute Row Headers
  - **Row 4**: `Question Code` (e.g. T-01, E-01, O-01)
  - **Row 5**: `Pillar / Dimension` (Technical, Economic, Legal/Outreach, Operational, Schedule, SDGs)
  - **Row 6**: `Diagnostic Question (Standardized Problem-Space Prompt)`
  - **Row 7**: `Question Rationale (Why Asked & Failure Mode Guarded Against)`
  - **Row 8**: `Scoring Rubric Definition (Explicitly defines all 5 levels: 1, 2, 3, 4, 5 — ระบุเงื่อนไขครบทุกระดับ)`
  - **Row 9**: `ASSIGNED SCORE (1, 2, 3, 4, 5 STRICT INTEGER)` <--- Prominent horizontal inspection row
  - **Row 10**: `Normalized Weight (% derived from Two-Tier Pillar Allocation)`
  - **Row 11**: `Weighted Score (=Score * Weight)`
  - **Row 12**: `Description & Evidence Citation (The 'Why' / Exact citations from intake files)`
  - **Row 13**: `De-scoping & Risk Mitigation Action`
- **Columns B, C, D, ...**: Diagnostic questions arranged sequentially (2 to 4 questions per pillar).
- **Summary Column (Far Right Column)**:
  - **Row 9**: Total Aggregated Score (`=SUM(B11:...11)*20`)
  - **Row 10**: Total Weight Sum (`=SUM(B10:...10) = 100.0%`)
  - **Row 12**: Automated Verdict with **Knockout Gating Logic**:
    `=IF(MIN(B9:...9)=1, "VETOED / ตกเกณฑ์ข้อบังคับวิกฤต (คะแนนระดับ 1)", IF(Col9>=80, "ผ่านเกณฑ์ระดับสูง (HIGHLY VIABLE)", IF(Col9>=60, "ผ่านแบบมีเงื่อนไข (CONDITIONALLY VIABLE)", "ความเสี่ยงสูง (HIGH RISK)"))`

---

## 6. Bilingual Architecture & Token Optimization

1. **Bilingual Engine (Thai & English / สองภาษา)**:
   - All 12 agents operate seamlessly in Thai and English.
   - When processing Thai project files or prompts, all diagnostics, evidence citations, rationale descriptions, and verdicts are delivered in natural, professional engineering Thai with standard English technical terms in parentheses.
   - Session folder names safely preserve Thai Unicode characters (`\u0e00-\u0e7f`).

2. **Token Optimization via 17 Modular Files (`sdg-rulebook/goals/`)**:
   - `sdg-rulebook/goals/` contains 17 separate files (`goal-01.md` to `goal-17.md`).
   - Consultor `(2-7-sdgs-expert)` references `sdg-rulebook/goals/README.md` and loads only the 1–3 relevant Goals for the topic, keeping token usage efficient (~1,500–2,500 tokens).
