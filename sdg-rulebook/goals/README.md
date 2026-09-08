# SDG Goals & Indicator Index (Token-Optimized Rulebook)

> **Purpose:** Optimize LLM token consumption by splitting the full SDG Move dataset into 17 modular, targeted Goal files.
> **Source Data:** [SDG Move: เป้าหมายย่อย และตัวชี้วัด](https://www.sdgmove.com/%e0%b9%80%e0%b8%9b%e0%b9%89%e0%b8%b2%e0%b8%ab%e0%b8%a1%e0%b8%b2%e0%b8%a2%e0%b8%a2%e0%b9%88%e0%b8%ad%e0%b8%a2-%e0%b9%81%e0%b8%a5%e0%b8%b0%e0%b8%95%e0%b8%b1%e0%b8%a7%e0%b8%8a%e0%b8%b5%e0%b9%89/)  
> **Model:** Stockholm Resilience Centre Wedding Cake (Biosphere, Society, Economy, Partnerships)

---

## 🧭 Token Optimization Lookup Table

Instead of loading the entire 150KB / 571-line SDG Move document into context, load **only the relevant Goal files** matching your project's domain:

| Goal # | Goal Name (English & Thai) | Wedding Cake Tier | File to Load | Core Diagnostic Scope |
| :---: | :--- | :---: | :--- | :--- |
| **01** | **No Poverty** (ยุติความยากจน) | Society | [`goal-01-no-poverty.md`](goal-01-no-poverty.md) | Basic services access, disaster economic resilience for vulnerable groups. |
| **02** | **Zero Hunger** (ยุติความหิวโหย) | Society | [`goal-02-zero-hunger.md`](goal-02-zero-hunger.md) | Food security, sustainable agriculture, soil and crop flood protection. |
| **03** | **Good Health & Well-being** (สุขภาพและความเป็นอยู่ที่ดี) | Society | [`goal-03-good-health-and-well-being.md`](goal-03-good-health-and-well-being.md) | Waterborne diseases, chemical pollution, hazardous exposure prevention. |
| **04** | **Quality Education** (การศึกษาที่มีคุณภาพ) | Society | [`goal-04-quality-education.md`](goal-04-quality-education.md) | Technical ICT skills, sustainability education, resilient schools. |
| **05** | **Gender Equality** (ความเท่าเทียมทางเพศ) | Society | [`goal-05-gender-equality.md`](goal-05-gender-equality.md) | Inclusive leadership, equitable access to digital alert technology. |
| **06** | **Clean Water & Sanitation** (น้ำสะอาดและสุขอนามัย) | **Biosphere** | [`goal-06-clean-water-and-sanitation.md`](goal-06-clean-water-and-sanitation.md) | Water quality, wastewater treatment, integrated water resources (IWRM). |
| **07** | **Affordable & Clean Energy** (พลังงานสะอาด) | Society | [`goal-07-affordable-and-clean-energy.md`](goal-07-affordable-and-clean-energy.md) | Renewable energy micro-power, energy efficiency, low compute power. |
| **08** | **Decent Work & Economic Growth** (งานที่มีคุณค่า) | Economy | [`goal-08-decent-work-and-economic-growth.md`](goal-08-decent-work-and-economic-growth.md) | Labor safety in hazardous environments, economic productivity. |
| **09** | **Industry, Innovation & Infrastructure** (โครงสร้างพื้นฐาน) | Economy | [`goal-09-industry-innovation-and-infrastructure.md`](goal-09-industry-innovation-and-infrastructure.md) | Resilient infrastructure (>99.5% uptime), retrofit existing systems. |
| **10** | **Reduced Inequalities** (ลดความเหลื่อมล้ำ) | Economy | [`goal-10-reduced-inequalities.md`](goal-10-reduced-inequalities.md) | Equitable benefit distribution to informal settlements, fair water allocation. |
| **11** | **Sustainable Cities & Communities** (เมืองและชุมชนยั่งยืน) | Society | [`goal-11-sustainable-cities-and-communities.md`](goal-11-sustainable-cities-and-communities.md) | **Disaster loss reduction (11.5)**, Sendai Framework (11.b), drainage waste. |
| **12** | **Responsible Consumption & Production** (การบริโภคยั่งยืน) | Economy | [`goal-12-responsible-consumption-and-production.md`](goal-12-responsible-consumption-and-production.md) | Modular repair, e-waste minimization, RoHS compliance, circular design. |
| **13** | **Climate Action** (การรับมือสภาพภูมิอากาศ) | **Biosphere** | [`goal-13-climate-action.md`](goal-13-climate-action.md) | Extreme weather adaptation, multi-hazard early warning broadcasts. |
| **14** | **Life Below Water** (ทรัพยากรทางทะเล) | **Biosphere** | [`goal-14-life-below-water.md`](goal-14-life-below-water.md) | Marine debris interception, coastal runoff nutrient prevention. |
| **15** | **Life on Land** (ระบบนิเวศบนบก) | **Biosphere** | [`goal-15-life-on-land.md`](goal-15-life-on-land.md) | Nature-based solutions (NbS), soil conservation, wetlands preservation. |
| **16** | **Peace, Justice & Strong Institutions** (สถาบันที่เข้มแข็ง) | Society | [`goal-16-peace-justice-and-strong-institutions.md`](goal-16-peace-justice-and-strong-institutions.md) | Anti-corruption, open data telemetry, transparent public administration. |
| **17** | **Partnerships for the Goals** (หุ้นส่วนความร่วมมือ) | Partnership | [`goal-17-partnerships-for-the-goals.md`](goal-17-partnerships-for-the-goals.md) | Multi-stakeholder collaboration (Gov, Academia, Civic), open telemetry. |

---

## ⚡ Agent Usage Protocol for `(2-7-sdgs-expert)`

1. **Step 1: Domain Tagging**: Identify the 2–3 most relevant Goals for the user's project (e.g. for Flood/Drainage $\rightarrow$ Goals 6, 11, and 13).
2. **Step 2: Targeted File Read**: Read **only** those specific Goal files (e.g. `goal-06-clean-water-and-sanitation.md` and `goal-11-sustainable-cities-and-communities.md`).
3. **Step 3: Indicator-to-Question Extraction**: Extract the specific UN Indicators from those files and submit the formulated diagnostic questions to `(2-1-jury)`.
