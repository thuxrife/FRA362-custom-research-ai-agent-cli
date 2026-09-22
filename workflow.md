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
- **Zero Solution Bias**: The Jury strictly rejects leading questions tailored to flatter the proposed technology (e.g., asking *"Can Python calculate in 500ms?"* is forbidden).
- **Zero Generic Textbook Headers**: Questions must not be vague slide headers (e.g., *"Is the project technically possible?"* is forbidden).
- **The True Sweet Spot**: Questions must be **sharp, context-specific engineering stress-tests** that probe:
  1. *Real Constraints*: Citing specific conditions from the intake files (e.g. municipal photo evidence mandates, solo developer, 4 exam weeks).
  2. *Failure Modes*: Testing whether the project survives real-world human, mechanical, or regulatory bottlenecks.
  3. *Cross-Aspect Consequences*: Explicitly auditing how decisions in one pillar constrain the others.

### 5. Strict Discrete Integer Scoring ({1, 2, 3, 4, 5} ONLY — Zero Decimals / No 0.5)
- All assigned diagnostic scores MUST be discrete whole integers strictly chosen from **`{1, 2, 3, 4, 5}`**.
- **No 0.5 or fractional decimals under any circumstances**: An aspect either satisfies the rubric criteria for an integer level or it does not. Evaluators must make decisive judgments based on evidence.
- The only numbers containing decimals in the entire system are calculated weighted products (`Score * Weight`) and the final total aggregated score.

### 6. The 4-Level Contextual Learning & Outreach Scale
Evaluates human capability based on the **Contextual Gap** between past project evidence and required complexity:
* **Level 1 (Critical Deficit / High Barrier)**: Zero foundation; insurmountable learning curve; or team is unwilling/blocked from government or external facility outreach.
* **Level 2 (Foundational / Steep Learning Curve)**: Basic theoretical knowledge; no production hardware experience; willingness exists but lacks warm institutional contacts.
* **Level 3 (Adjacent Competence / Manageable Curve)**: Strong mastery in adjacent tech stacks (e.g. ESP32 to STM32; CAD to CNC); active access to faculty/university channels.
* **Level 4 (Proven Production Mastery / Direct Access)**: Direct track record delivering identical/higher complexity systems in past projects; active MoUs or approved permits.

---

## 4. Upgraded Feasibility Roles

| ID | Agent Name | Strict Tag Prefix | Destination Folder | Core Consulting Mission & Focus |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **The Jury** | `(2-1-jury)` | `feasibility-outcome/` | **Chief Judge, Solo Architect & Anti-Tech-Trap Gatekeeper**: Operates in dual modes: can audit all 6 TELOS+S pillars alone in 1 single step, or orchestrate specialists 2.2–2.7. Ingests the 3 intake folders, eliminates biased questions, enforces integer scoring `{1-5}`, and compiles `{month}-{date}-{year}-{time}_{seq}.xlsx`. |
| **2.2** | **Tech Feasibility** | `(2-2-tech-feasibility)` | `teammate-persona/` | **Man & Machine Auditor**: Audits real tool access, fabrication skills (Mech/Elec/Prog), and the time/cost overhead that technology choices extract from the project. Flags Pioneer Novelty Risks. |
| **2.3** | **Economic Feasibility** | `(2-3-economic-feasibility)` | N/A | **Cost-Benefit & Financial Reality Analyst**: Evaluates funding reality, budget ceilings, scrap/iteration allowances, and true worth compared to the Zero-Action baseline (doing nothing / manual labor). |
| **2.4** | **Legal & Outreach Feasibility** | `(2-4-legal-feasibility)` | N/A | **Institutional & Policy Gatekeeper**: Audits statutory law (PDPA, NBTC), municipal liabilities, IP infringements, and the team's verified capability to conduct in-person government agency liaisons. |
| **2.5** | **Operational Feasibility** | `(2-5-operational-feasibility)` | N/A | **The "Will It Actually Be Used?" Stress-Tester**: Audits dispatcher adoption, procedural resistance (e.g. Traffy Fondue photo evidence rules), workflow disruption, training burdens, and developer burnout. |
| **2.6** | **Schedule Feasibility** | `(2-6-schedule-feasibility)` | N/A | **Conflict & Deadline Realist**: Audits milestone delivery realism against formal TRL levels (TRL2, TRL3, TRL4), stress-testing against university exam blackouts and procurement lead times. |
| **2.7** | **SDGs Expert** | `(2-7-sdgs-expert)` | N/A | **Systemic Sustainability Consultant**: Evaluates multi-layer Stockholm Wedding Cake impact (Biosphere, Society, Economy), UN SDG indicators, and Do-No-Harm safeguards (preventing e-waste and vulnerability shifts). |

---

## 5. Transposed Horizontal Excel Matrix Specification (`{month}-{date}-{year}-{time}.xlsx`)

Generated automatically via `openpyxl` directly inside `feasibility-outcome/{month}-{date}-{year}-{time}.xlsx`.

### Layout Structure:
The matrix is transposed horizontally so that **headers and scores align parallel across columns**, allowing immediate horizontal comparison:
- **Column A**: Attribute Row Headers
  - **Row 4**: `Question Code` (e.g. T-01, E-01, O-01)
  - **Row 5**: `Pillar / Dimension` (Technical, Economic, Legal/Outreach, Operational, Schedule, SDGs)
  - **Row 6**: `Diagnostic Question` (Critical, Context-Specific Stress-Test Question)
  - **Row 7**: `Question Rationale (Why Asked & Failure Mode Guarded Against)`
  - **Row 8**: `Scoring Rubric Definition (Objective 1 vs. 5 Standards)`
  - **Row 9**: `ASSIGNED SCORE (1, 2, 3, 4, 5 STRICT INTEGER)` <--- Prominent horizontal inspection row
  - **Row 10**: `Weight (%)`
  - **Row 11**: `Weighted Score (=Score * Weight)`
  - **Row 12**: `Description & Evidence Citation (The 'Why' / Exact citations from intake files)`
  - **Row 13**: `De-scoping & Risk Mitigation Action`
- **Columns B through S**: Individual diagnostic questions arranged sequentially.
- **Far Right Column**: Total Summary Column computing total weighted score, weight sum, and automated viability verdict (>=80 Highly Viable, >=60 Conditionally Viable, <60 High Risk).

---

## 6. Bilingual Architecture & Token Optimization

1. **Bilingual Engine (Thai & English / สองภาษา)**:
   - All 12 agents operate seamlessly in Thai and English.
   - When processing Thai project files or prompts, all diagnostics, evidence citations, rationale descriptions, and verdicts are delivered in natural, professional engineering Thai with standard English technical terms in parentheses.
   - Session folder names safely preserve Thai Unicode characters (`\u0e00-\u0e7f`).

2. **Token Optimization via 17 Modular Files (`sdg-rulebook/goals/`)**:
   - `sdg-rulebook/goals/` contains 17 separate files (`goal-01.md` to `goal-17.md`).
   - Consultor `(2-7-sdgs-expert)` references `sdg-rulebook/goals/README.md` and loads only the 1–3 relevant Goals for the topic, keeping token usage efficient (~1,500–2,500 tokens).
