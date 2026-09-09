# FRA362 Custom Research & Feasibility AI Multi-Agent System

A dual multi-agent system designed for **Dialectical Literature Research** and **TELOS-SDG Feasibility Consulting**, operating directly within the AI chat interface.

All agent SOPs, personas, and behavioral directives are defined cleanly in **Markdown** (`agents/*.md`), while the SDG indicator diagnostic questions are modularized in `sdg-rulebook/goals/`.

---

## Dual Multi-Agent Architecture

```mermaid
flowchart TD
    User([User / Project Lead]) <-->|Inquiry, /feasibility, or /ref| Lead{Active Group}
    
    subgraph Group 1: Dialectical Research
        Lead -->|Research Mode| M["(1-1-manager)"]
        M --> R["(1-2-researcher)"]
        R --> O["(1-3-objectionist)"]
        R & O -.-> NT["(1-4-note-taker)"]
        M --> S["(1-5-summarizer)"]
    end
    
    subgraph Group 2: TELOS-SDG Feasibility
        Lead -->|Feasibility Mode| J["(2-1-jury)"]
        J --> T["(2-2-tech-feasibility)"]
        J --> E["(2-3-economic-feasibility)"]
        J --> L["(2-4-legal-feasibility)"]
        J --> OP["(2-5-operational-feasibility)"]
        J --> SCH["(2-6-schedule-feasibility)"]
        J --> SDG["(2-7-sdgs-expert)"]
    end

    NT --> D1[("📁 note-taker-log/")]
    R --> D2[("📁 research-outcome/")]
    S & J --> D3[("📁 summarize-outcome/")]
    J --> D4[("📁 feasibility-goals/<br>TELOS_SDG_Matrix.xlsx")]
    T --> D5[("📁 teammate-persona/<br>team_skills.md")]
```

---

## The 12 Roles & Tag Protocol

### Group 1: Dialectical Research Team
- `(1-1-manager)`: Primary user communicator; clarifies ambiguous queries; concludes debate.
- `(1-2-researcher)`: Deep engineering source hunting with clickable live links (100% Free DuckDuckGo live web search + ArXiv open literature); produces system architectures, physical sensor specs, hydrodynamic control models ($Q = C_d \cdot b \cdot h_g \sqrt{2g \Delta h}$), and quantitative performance tables.
- `(1-3-objectionist)`: Adversarial engineering critic; quotes and highlights exact claims from sources (`> "Source claims: ..."`), contrasts them with environmental failure modes (rain fade, bio-fouling, $H_2S$ corrosion, mechanical jamming), and presents an FMEA risk matrix.
- `(1-4-note-taker)`: Continuous verbatim debate recorder in `note-taker-log/`.
- `(1-5-summarizer)`: Final engineering synthesis into HTML & Markdown in `summarize-outcome/` featuring a mandatory Quantitative Engineering Comparative Data Table.

### Group 2: TELOS-SDG Feasibility Team ("Consultors Setup Questions, Jury Takes Them All")
- `(2-1-jury)`: **Master Arbitrator & Collector**: Takes all questions proposed by the consultors, cuts off nonsense, interviews the user directly on unverified assumptions, freezes goals before scoring (anti-backpropagation rule), and compiles `TELOS_SDG_Matrix.xlsx` in `feasibility-goals/`.
- `(2-2-tech-feasibility)`: Sets up technical questions: audits actual human team capability (logged in `teammate-persona/`) and Pioneer Red Flag novelty risk.
- `(2-3-economic-feasibility)`: Sets up economic questions: evaluates whether it is worth it (constraints vs. attractiveness) with concrete benchmark examples.
- `(2-4-legal-feasibility)`: Sets up regulatory questions: statutory law, social norms, public ethics, and pending legislation.
- `(2-5-operational-feasibility)`: **Human & Team Centric**: Questions user the most regarding pre-launch workflow friction and post-launch ripple effects / 2 AM burnout.
- `(2-6-schedule-feasibility)`: Sets up timeline questions: critical-path realism, delivery guarantee conditions, and de-scoping contingency.
- `(2-7-sdgs-expert)`: **Indicator-Driven Feasibility**: Converts official **UN SDG Indicators** into exact diagnostic questions based on the [17 Modular SDG Files](sdg-rulebook/goals/README.md) across the 3 layers of the **SDG Wedding Cake** (Biosphere, Society, Economy).

---

## 📘 SDG Rulebook & Indicator Question Engine

Located in `sdg-rulebook/`:
* [**`sdg-rulebook/goals/`**](sdg-rulebook/goals/): **17 Modular Goal Files** (`goal-01.md` through `goal-17.md`) + [Routing Index](sdg-rulebook/goals/README.md). Designed for **optimal token consumption** (~1,500 tokens per evaluation instead of ~40,000 tokens) so agents only load the specific Goals relevant to the project idea. Contains all official UN Targets, Indicators (from SDG Move Thailand), and derived Feasibility Diagnostic Questions mapped to the Stockholm Resilience Centre Wedding Cake.

---

## 🇹🇭 Bilingual Fluency (Thai & English / รองรับภาษาไทย 100%)

The system natively understands and generates natural, professional Thai (ภาษาไทย):
- **Automatic Language Detection**: Prompting in Thai automatically activates Thai language directives across all 12 agents, whether using Perplexity, Gemini, OpenAI, or the offline dialectical engine.
- **Thai ArXiv Literature Discovery**: Queries in Thai (e.g. `น้ำท่วมกรุงเทพ`, `เกษตรอัจฉริยะ`) are intelligently mapped to English scientific query spaces to retrieve live, working academic papers from ArXiv.
- **Bilingual Deliverables**: Executive summaries, debate transcripts, persona logs, and feasibility reports are generated in professional Thai with English technical keywords in parentheses.
- **Safe Subfolder Naming**: Date and session subfolders safely preserve Thai unicode characters (`\u0e00-\u0e7f`).

---

## 🚀 In-Chat Workflow & Usage

No local terminal installation or Python scripts required. The agents operate directly within this chat interface:

### 1. Literature Research & Dialectical Debate
Simply ask any technical research topic in Thai or English:
- *Example*: `ระบบ IoT ตรวจวัดระดับน้ำและเปิดปิดประตูระบายน้ำอัตโนมัติ กรุงเทพ`
- *Process*:
  1. `(1-1-manager)` validates and clarifies scope if ambiguous.
  2. `(1-2-researcher)` performs live web searches, pulls engineering specs, formulas ($Q = C_d \cdot b \cdot h_g \sqrt{2g \Delta h}$), and empirical performance matrices.
  3. `(1-3-objectionist)` quotes highlighted claims from sources, identifies physical failure modes (rain fade, H₂S degradation, mechanical jams), and generates an **FMEA Matrix**.
  4. `(1-5-summarizer)` synthesizes the findings into a **Quantitative Engineering Comparative Data Table** and a 3-phase Go/No-Go roadmap.

### 2. TELOS-SDG Feasibility Consulting
Ask to assess any project idea using TELOS and SDG indicators:
- *Example*: `ประเมินความเป็นไปได้: โครงการประตูกั้นน้ำอัตโนมัติพลังงานแสงอาทิตย์ลุ่มน้ำเจ้าพระยา`
- *Process*:
  1. `(2-1-jury)` enforces Anti-Backpropagation rules, freezing requirements before scoring.
  2. The 6 Feasibility Specialists (`Tech`, `Economic`, `Legal`, `Operational`, `Schedule`, and `SDGs Expert`) examine constraints across all dimensions.
  3. `(2-7-sdgs-expert)` queries modular targets and indicators from [`sdg-rulebook/goals/`](sdg-rulebook/goals/README.md) mapped to the Stockholm Wedding Cake model.


