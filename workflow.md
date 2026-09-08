# Multi-Agent Research & Feasibility Workflow Specification

## 1. System Overview
This project implements a **Dual Multi-Agent Architecture**:
- **Group 1: Dialectical Research Team (Thesis → Antithesis → Synthesis)**
  - Roles: 1.1 Manager, 1.2 Researcher, 1.3 Objectionist, 1.4 Note-Taker, 1.5 Summarizer
- **Group 2: TELOS-SDG Feasibility Consulting Team (Goal-First Evaluation)**
  - Roles: 2.1 The Jury, 2.2 Technology, 2.3 Economic, 2.4 Legal, 2.5 Operational, 2.6 Schedule, 2.7 SDGs Expert

All agent personas and SOPs are maintained in modular Markdown files located in `agents/`.

---

## 2. Subfolder Organization (USA Date Format)

Every session creates matching subfolders formatted as:
`M-D-YYYY_HHMM-{Topic_Slug}` (e.g. `9-8-2026_2322-TELOS_IoT_Distributed_Drainage`).

```text
feasibility-goals/
└── 9-8-2026_2322-TELOS_IoT_Distributed_Drainage/
    ├── goals.md                        <-- Predetermined goals (anti-backpropagation)
    └── TELOS_SDG_Matrix.xlsx           <-- Interactive Excel scoring workbook

teammate-persona/
└── 9-8-2026_2322-TELOS_IoT_Distributed_Drainage/
    └── team_skills.md                  <-- Team capabilities & human constraints

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

---

## 3. Group 2 Workflow Principle ("Consultors Setup Questions, Jury Takes Them All")

1. **Domain Consultors (2.2 through 2.7)**:
   - Each domain consultor is responsible for **formulating and setting up the diagnostic sub-questions** for their pillar based on the specific idea, examining human team skills, economic constraints, operational frictions, legal risks, timelines, and SDG targets.
2. **The Jury (2.1)**:
   - **Takes them all**: Aggregates all proposed questions from every consultor into the unified master matrix.
   - Audits each question for rigor, filtering out nonsense, vague claims, or duplicate metrics.
   - Puts questions to the user directly when internal facts or constraints need verification (Zero-Assumption Rule).
   - Tallies the final weighted score and issues the official feasibility verdict.

| ID | Agent Name | Strict Tag Prefix | Destination Folder | Core Consulting Mission |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **The Jury** | `(2-1-jury)` | `feasibility-goals/` | **Central Aggregator & Lead Judge**: Takes all questions from consultors, cuts off nonsense, interviews user, freezes goals (anti-backpropagation), and delivers `TELOS_SDG_Matrix.xlsx`. |
| **2.2** | **Tech Feasibility** | `(2-2-tech-feasibility)` | `teammate-persona/` | Sets up tech diagnostic questions: 1) Can actual team execute it? 2) Pioneer Red Flag check. |
| **2.3** | **Economic Feasibility** | `(2-3-economic-feasibility)` | N/A | Sets up economic questions: Is it worth it? Constraints vs. attractiveness, benchmark examples. |
| **2.4** | **Legal Feasibility** | `(2-4-legal-feasibility)` | N/A | Sets up legal questions: Statutory compliance, social norms/public trust, and pending legislation. |
| **2.5** | **Operational Feasibility** | `(2-5-operational-feasibility)` | N/A | **Human & Team Centric**: Sets up operational questions (questions user most): Pre-launch friction & post-launch ripple effects on ongoing work / 2 AM burnout. |
| **2.6** | **Schedule Feasibility** | `(2-6-schedule-feasibility)` | N/A | Sets up schedule questions: Timeline realism, critical path, and non-negotiable delivery guarantees. |
| **2.7** | **SDGs Expert** | `(2-7-sdgs-expert)` | N/A | Sets up SDG questions: Granular UN SDG Targets across the 3 layers of the Stockholm Wedding Cake. |

---

## 4. Excel Feasibility Matrix Template (`TELOS_SDG_Matrix.xlsx`)

Generated automatically via `openpyxl` with 4 dedicated sheets:
1. **`TELOS_SDG_Matrix`**: 19 diagnostic sub-questions formulated by the consultors, weighted formulas, 1–5 scoring, and automated viability verdict (>=80 Highly Viable, >=60 Conditionally Viable, <60 High Risk).
2. **`Scoring_Rubric_Guide`**: Objective 1–5 scale standards for tech, economic, and operational criteria.
3. **`Goals_and_Direction`**: Frozen goals and non-negotiable constraints (anti-backpropagation).
4. **`SDG_Wedding_Cake`**: Stockholm Resilience Centre multi-tier mapping (Biosphere, Society, Economy) with UN Targets and Indicators.

---

## 5. Bilingual Architecture & Token Optimization

1. **Bilingual Engine (Thai & English / สองภาษา)**:
   - All 12 agents understand and generate natural Thai and English.
   - When given Thai prompts, the system automatically routes Thai directives to Perplexity/Gemini/OpenAI or the local dialectical simulation engine.
   - Thai queries are mapped to English scientific taxonomy for querying ArXiv, returning live clickable links (HTTP 200).
   - Session folder names preserve Thai Unicode characters (`\u0e00-\u0e7f`).

2. **Token Optimization via 17 Modular Files (`sdg-rulebook/goals/`)**:
   - Rather than sending the full ~150 KB SDG Move handbook in prompt context (~40,000 tokens), `sdg-rulebook/goals/` contains 17 separate files (`goal-01.md` to `goal-17.md`).
   - Consultor `(2-7-sdgs-expert)` looks up `sdg-rulebook/goals/README.md` and reads only the 1–3 relevant Goals for the topic, reducing token consumption per evaluation to ~1,500–2,500 tokens.

