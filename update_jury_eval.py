import os
import json

# ==============================================================================
# JURY EVALUATION DATA ENGINE: 3 ACTIVE SOLUTIONS (SORTED BY FEASIBILITY SCORE)
# Solution 2 (Acoustic Reflectometry) - 83.53%
# Solution 1 (CCTV Wheeled Crawler) - 59.30%
# Solution 4 (LiDAR SLAM Crawler) - 55.04%
# Note: Solution 3 (Underwater Sonar) has been dropped due to failing pipe dry/20% water requirements.
# ==============================================================================

data = [
    # --------------------------------------------------------------------------
    # SOLUTION 2 - ACOUSTIC REFLECTOMETRY (WINNER)
    # --------------------------------------------------------------------------
    {
        "sheet_title": "Solution_2_Acoustic_Reflect",
        "concept": "Solution 2: Pipe Inspection Instrument using Acoustic Reflectometry (Airborne Acoustic Inversion + SL-RAT EPA USA Cleanliness Scale)",
        "strength": "ตรวจประเมินท่อจากผิวดินได้อย่างรวดเร็ว (3–5 นาทีต่อช่วงท่อ) โดยไม่ต้องปล่อยหุ่นยนต์ลงไปสัมผัสน้ำเสีย ใช้พลังงานต่ำ ต้นทุนอุปกรณ์ต่ำมาก ไม่มีความเสี่ยงเรื่องอุปกรณ์ติดค้างในท่อ และสอดรับกับข้อจำกัดน้ำในท่อไม่เกิน 20% ได้อย่างสมบูรณ์แบบ",
        "bottleneck": "ไม่สามารถทำงานได้ในสภาวะที่น้ำท่วมเต็มท่อระบายน้ำ (Airspace ปิดกั้น) และไม่ได้ภาพ 3D เรขาคณิตของผิวท่อ",
        "advice": "พัฒนาท่อส่งคลื่นเสียงแบบ Telescoping Pole ที่สามารถปรับระดับความลึกตามปากท่อได้ พร้อมบันทึกพิกัด GPS อัตโนมัติเพื่อเชื่อมต่อแผนที่ระบบท่อของ กทม.",
        "robotic_compatibility": {
            "score": 8.5,
            "domains": {
                "perception": "Score 3.5/4.0: Active airborne acoustic reflectometry transducer, swept-sine/chirp acoustic wave excitation, and precision condenser microphone array capturing acoustic impulse response.",
                "control_algorithms": "Score 3.5/4.0: Digital signal processing (DSP), acoustic energy attenuation deconvolution, spectral bandpass filtering, and automated 0-10 EPA SL-RAT cleanliness score generation.",
                "actuation_mechanics": "Score 1.5/4.0: High-output acoustic compression driver transducer with telescoping manhole deployment rig; non-mobile surface-operated payload."
            },
            "fibo_alignment_rationale": "Solution 2 exercises FIBO signal processing, acoustical physics, digital filtering, and sensor interface engineering without unnecessary mechanical locomotion risks in underground sewage."
        },
        "robotic_data": {
            "score": 8.5,
            "domains": {
                "perception": "Score 3.5/4.0: Active airborne acoustic reflectometry transducer, swept-sine/chirp acoustic wave excitation, and precision condenser microphone array capturing acoustic impulse response.",
                "control_algorithms": "Score 3.5/4.0: Digital signal processing (DSP), acoustic energy attenuation deconvolution, spectral bandpass filtering, and automated 0-10 EPA SL-RAT cleanliness score generation.",
                "actuation_mechanics": "Score 1.5/4.0: High-output acoustic compression driver transducer with telescoping manhole deployment rig; non-mobile surface-operated payload."
            },
            "fibo_alignment_rationale": "Solution 2 exercises FIBO signal processing, acoustical physics, digital filtering, and sensor interface engineering without unnecessary mechanical locomotion risks in underground sewage."
        },
        "assessment_data": [
            {
                "id": "T-01",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับการสร้างเองเทียบกับการซื้อสำเร็จรูป (Build vs. Buy Burden) ของสถาปัตยกรรมระบบตรวจประเมินท่อระบายน้ำ?",
                "rationale": "ประเมินภาระการวิจัยและพัฒนาชิ้นส่วนกลไก อิเล็กทรอนิกส์ และอัลกอริทึม ป้องกันการเสียเวลากับงานประดิษฐ์ขึ้นใหม่โดยไม่จำเป็น",
                "rubric": "1: ต้องวิจัยและสร้างขึ้นเองทั้งหมด 100% (ไม่มีพิมพ์เขียว อัลกอริทึม หรือไลบรารีอ้างอิง)\n2: มีชิ้นส่วนหลักในท้องตลาด แต่ต้องดัดแปลงโครงสร้างอย่างหนักและเขียนโค้ดเชื่อมต่อเองทั้งหมด\n3: บูรณาการชิ้นส่วน COTS เข้ากับแท่นยึดแบบกำหนดเอง และเขียนโค้ดเชื่อมต่อบางส่วน\n4: ประกอบจากโมดูลมาตรฐานสำเร็จรูป (DIN-rail, I2C/CAN shields) มีงานประกอบกลไกเล็กน้อย\n5: ซื้อมาติดตั้งใช้งานได้ทันที (Plug-and-Play) ไม่ต้องตัดกลึงหรือบัดกรีวงจรเพิ่มเติม",
                "score": 3,
                "weight": 0.04,
                "evidence": "solution-details/solution-2.md lines 33-36; combines standard COTS compression driver horn, precision condenser mic, MAX98357 I2S audio amp, and ESP32 with 3D printed manhole acoustic baffles.",
                "descope": "Use modular 3D-printed acoustic impedance horns and commercial I2S microphone/DAC breakout boards to eliminate custom analog PCB revisions."
            },
            {
                "id": "T-02",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "สิทธิ์ในการเข้าถึงเทคโนโลยี ซอฟต์แวร์ และระบบนิเวศข้อมูล (Access & Permissions) ของระบบตรวจประเมินท่อ?",
                "rationale": "ตรวจสอบข้อจำกัดด้านกรรมสิทธิ์ การล็อกสิทธิ์ใช้งาน และการอนุญาตเข้าถึง เพื่อป้องกันการพัฒนาระบบบนฐานข้อมูลที่ไม่สามารถเข้าถึงได้จริง",
                "rubric": "1: ล็อกสิทธิ์ภายใต้สัญญา NDA ระบบปิด ติดไฟร์วอลล์องค์กร หรือไม่มีสิทธิ์เข้าถึงฝั่งนักพัฒนา\n2: ซอฟต์แวร์หรือเฟิร์มแวร์กรรมสิทธิ์ปิด ทำงานแบบ Black-box โดยไม่มี Source Code หรือ Telemetry\n3: บัญชีเพื่อการศึกษา/ทดลองใช้ที่มีโควตาหรือ Rate Limit เข้มงวด ต้องรอการอนุมัติอย่างเป็นทางการ\n4: มี SDK หรือ Open API สาธารณะพร้อมเอกสารครบถ้วน แต่ไม่สามารถแก้ไขสถาปัตยกรรมระดับล่างได้\n5: สถาปัตยกรรมเปิดสมบูรณ์ (Open Source/Open HW) ทีมงานมีสิทธิ์ระดับ Root/Admin เต็มรูปแบบ",
                "score": 5,
                "weight": 0.04,
                "evidence": "solution-details/solution-2.md lines 27-36; open-source audio DSP algorithms, public EPA SL-RAT mathematical standards, standard Python/SciPy signal processing libraries, and full root developer control on ESP32/STM32.",
                "descope": "Implement standard Python/NumPy FFT processing pipeline without proprietary vendor licenses."
            },
            {
                "id": "T-03",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับความพร้อมทางเทคโนโลยี (Base Performance / TRL) ในสภาพแวดล้อมจริงของท่อระบายน้ำใต้ดิน?",
                "rationale": "วัดวุฒิภาวะของเทคโนโลยีว่าผ่านการพิสูจน์ในสภาพแวดล้อมใต้ดินที่มีความชื้น สารกัดกร่อน หรือน้ำขังจริงแล้วหรือไม่",
                "rubric": "1: ระดับแนวคิด/สมการคณิตศาสตร์ (TRL 2–3) ทดสอบเฉพาะในห้องทดลองที่ควบคุมสภาพแวดล้อมได้\n2: เบรดบอร์ดทำงานได้ในแล็บ (TRL 4) สายไฟเปราะบาง ยังไม่ผ่านการสอบเทียบในสภาพแวดล้อมจริง\n3: ตัวต้นแบบประกอบลงกล่อง (TRL 5–6) ผ่านการทดสอบในสภาพแวดล้อมจำลอง ต้องมีคนคอยดูแล\n4: ต้นแบบระดับพรีโปรดักชัน (TRL 7) ทำงานได้อย่างมีเสถียรภาพในสภาพแวดล้อมปฏิบัติงานจริง\n5: ผลิตภัณฑ์เชิงพาณิชย์สมบูรณ์ (TRL 8–9) ผ่านการรับรองมาตรฐาน มีค่า MTBF ยืนยันความทนทาน",
                "score": 3,
                "weight": 0.04,
                "evidence": "solution-details/solution-2.md lines 15, 31, 38-42; Airborne acoustic reflectometry is an EPA-verified commercial standard (TRL 7-8). Under the newly confirmed constraint of <=20% water depth, 80%+ pipe airspace is open, ensuring robust acoustic propagation; custom student prototype operates at TRL 5-6 requiring water-level compensation baseline calibration.",
                "descope": "Establish a baseline acoustic lookup table on dry and 10-20% flooded PVC pipe mockups before field deployment."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความเข้ากันได้ของทีม (Manpower & Skill Redundancy) ด้านวิศวกรรมเฉพาะทาง?",
                "rationale": "ประเมินความเสี่ยงกรณีขาดแคลนบุคลากรที่มีความเชี่ยวชาญเฉพาะด้าน (Bus Factor) ว่ามีคนทำงานทดแทนกันได้หรือไม่",
                "rubric": "1: ขาดแคลนทักษะเฉพาะด้านโดยสิ้นเชิง (ไม่มีใครในทีมมีความรู้ในเทคโนโลยีหลักนี้เลย)\n2: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (Bus Factor = 1) หากคนนี้ไม่อยู่ โครงการจะหยุดชะงักทันที\n3: มีผู้รับผิดชอบหลัก 1 คน และมีผู้ช่วยที่พอเข้าใจระบบ แต่ยังแก้ไขปัญหาเชิงลึกแทนไม่ได้\n4: มีทักษะทดแทนกันได้ (Primary & Secondary) อย่างน้อย 2 คนสามารถสลับงานกันได้อย่างราบรื่น\n5: สมาชิกทุกคนในทีมมีทักษะระดับสูง ทำงานแทนกันได้ทันที และมีเอกสารคู่มือการทำงานครบถ้วน",
                "score": 4,
                "weight": 0.04,
                "evidence": "team-skills/due.md, jk.md, kin.md; Due has verified hardware experience building MAX98357 audio amp & ESP32 circuits; JK handles DSP math & Fourier analysis; Kin handles data ingestion & scoring backend.",
                "descope": "Maintain shared PlatformIO project repo and DSP simulation Jupyter notebook so Due, JK, and Kin can cross-debug."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันของเส้นทางการเรียนรู้ (Learning Curve) ด้านวิศวกรรมระบบ?",
                "rationale": "ประเมินเวลาและความยากในการเรียนรู้เทคโนโลยีใหม่ ว่าทีมงานสามารถเข้าใจและนำมาใช้ได้ทันเวลาหรือไม่",
                "rubric": "1: เทคโนโลยีใหม่ทั้งหมด ต้องใช้เวลาเรียนรู้เกิน 8 สัปดาห์ และต้องการทักษะคณิตศาสตร์ชั้นสูง\n2: มีแนวคิดซับซ้อน ต้องศึกษาทฤษฎีใหม่ที่ไม่เคยเรียนมาก่อน ใช้เวลาทำความเข้าใจ 4–6 สัปดาห์\n3: ต่อยอดจากพื้นฐานเดิมที่เคยเรียน แต่ต้องเรียนรู้เครื่องมือหรือสถาปัตยกรรมใหม่ ใช้เวลา 2–3 สัปดาห์\n4: เป็นเทคโนโลยีที่คุ้นเคย มีตัวอย่างโค้ดและวงจรอ้างอิงชัดเจน ใช้เวลาปรับตัวเพียง 1 สัปดาห์\n5: ทำงานบนพื้นฐานทักษะประจำวันของทีม ทำได้ทันทีโดยไม่ต้องศึกษาทฤษฎีหรือเครื่องมือเพิ่มเติม",
                "score": 4,
                "weight": 0.04,
                "evidence": "team-skills/due.md, jk.md; team has built audio amplifiers and implemented DSP bandpass filtering in previous projects; ramp-up only requires configuring I2S audio sampling and attenuation lookup tables.",
                "descope": "Utilize existing SciPy signal processing functions rather than deriving custom C++ Fourier transforms from scratch."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (Payback Period / Value Horizon) ของระบบ?",
                "rationale": "ประเมินผลตอบแทนทางเศรษฐศาสตร์และการลดต้นทุนการขุดลอกท่อระบายน้ำของหน่วยงานรัฐ",
                "rubric": "1: ระยะเวลาคืนทุนเกิน 7 ปี หรือต้นทุนการดำเนินงานสูงกว่ามูลค่าความเสียหายที่ป้องกันได้\n2: ระยะเวลาคืนทุน 5–7 ปี ให้ผลตอบแทนทางอ้อมเป็นหลัก และมีความไม่แน่นอนทางการเงินสูง\n3: ระยะเวลาคืนทุน 3–5 ปี มีความคุ้มค่าระดับปานกลาง จำเป็นต้องได้รับการอุดหนุนงบประมาณจากรัฐ\n4: ระยะเวลาคืนทุน 1–3 ปี ประหยัดค่าใช้จ่ายการซ่อมบำรุงเชิงแก้ไขได้อย่างชัดเจน คุ้มค่าสูง\n5: คืนทุนได้ภายใน 1 ปีแรก ลดต้นทุนการบำรุงรักษาได้ทันที และสร้างมูลค่าเพิ่มทางตรงอย่างมหาศาล",
                "score": 4,
                "weight": 0.0667,
                "evidence": "solution-details/solution-2.md lines 6-7, 15, 38; 2-person crew inspects 2–3 km/day in under 3 minutes per segment. Under confirmed <=20% water depth, covers ~80-90% of gravity lateral drainage networks without dewatering pumps, achieving rapid payback in 1-2 years.",
                "descope": "Focus initial pilot deployment on high-clogging commercial gravity pipes to demonstrate immediate budget savings."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระดับการพึ่งพาชิ้นส่วนและผู้จัดจำหน่ายภายนอก (Component Dependency & Vendor Lock-in)?",
                "rationale": "ประเมินความเสี่ยงด้านห่วงโซ่อุปทานและการผูกขาดชิ้นส่วน ป้องกันระบบล่มสลายจากผู้ผลิตรายเดียว",
                "rubric": "1: ผูกขาดโดยผู้ผลิตรายเดียว (Sole Source) ชิ้นส่วนสั่งทำพิเศษ ขาดตลาดง่าย นำเข้ายาก\n2: มีผู้จัดจำหน่าย 2 ราย แต่ชิ้นส่วนมีราคาสูง ใช้เวลาจัดส่งนานเกิน 4 สัปดาห์ และไม่มีอะไหล่ทดแทน\n3: ชิ้นส่วนมาตรฐานแต่มีบางโมดูลต้องสั่งนำเข้า มีระยะเวลารอคอย 2–3 สัปดาห์\n4: ใช้ชิ้นส่วนมาตรฐานอุตสาหกรรม (COTS) มีผู้ขายในประเทศหลายราย จัดหาทดแทนได้ใน 3–5 วัน\n5: อะไหล่หาง่ายทั่วไปตามร้านค้าอุปกรณ์อิเล็กทรอนิกส์ในประเทศ ซื้อทดแทนได้ทันทีภายใน 24 ชม.",
                "score": 5,
                "weight": 0.0667,
                "evidence": "solution-details/solution-2.md lines 33-36; 100% generic electronic and acoustic components (compression driver speaker, condenser mic, ESP32); self-serviceable by any engineer with zero proprietary vendor lock-in.",
                "descope": "Select components readily stocked by local electronics distributors (Ban Mo / Shopee TH / INEX)."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "สัดส่วนงบประมาณสำรองความเสียหาย (Scrap Margin / Safety Allowance) ของชิ้นส่วน?",
                "rationale": "ตรวจสอบความปลอดภัยทางการเงินกรณีทำอุปกรณ์เสียหายระหว่างการทดลองในน้ำเสีย",
                "rubric": "1: ไม่มีงบสำรองเลย หากชิ้นส่วนพังโครงการจะหยุดชะงักทันที (ราคาชิ้นส่วนเท่ากับงบประมาณทั้งหมด)\n2: งบสำรองรองรับการเสียหายได้ไม่เกิน 1 ครั้ง ชิ้นส่วนสำคัญไม่มีอะไหล่สำรอง\n3: มีงบสำรอง 20–30% ซื้อชิ้นส่วนราคาปานกลางสำรองได้ แต่ไม่มีอะไหล่สำหรับโมดูลหลักราคาแพง\n4: มีงบสำรอง 50% มีชิ้นส่วนหลักและไอซีสำคัญสำรองอย่างน้อย 2–3 ชุด ทดลองได้อย่างมั่นใจ\n5: งบประมาณเหลือเฟือ ชิ้นส่วนราคาถูกมาก สามารถซื้อชุดสำรองแบบสมบูรณ์ได้เกิน 3 ชุดขึ้นไป",
                "score": 4,
                "weight": 0.0666,
                "evidence": "team-skills/due.md; total hardware BOM for audio driver, mic capsule, amplifier, and ESP32 is very low (< 3,000 THB total), allowing the team to purchase 3x full sets of backup components comfortably.",
                "descope": "Pre-purchase 3 complete sets of ESP32 boards, MAX98357 amplifiers, and microphone capsules upfront."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมาย (Legal 2.4)",
                "question": "ความสอดคล้องกับกฎหมายความปลอดภัยสาธารณะและการจราจร (Regulatory & Public Safety Compliance)?",
                "rationale": "ประเมินความเสี่ยงการละเมิดกฎหมายควบคุมอาคาร ระเบียบงานทาง และข้อบังคับการจราจรขณะปฏิบัติงาน",
                "rubric": "1: เสี่ยงต่อการกระทำผิดกฎหมายอาญา ละเมิด พ.ร.บ. ทางหลวงอย่างร้ายแรง และไม่มีทางขออนุญาตได้\n2: ต้องขออนุญาตปิดการจราจรช่องทางหลัก เสี่ยงต่ออุบัติเหตุร้ายแรง และมีขั้นตอนอนุมัติยาวนาน\n3: ต้องขออนุญาตทำงานในเขตทางสาธารณะ แต่เป็นงานขนาดเล็ก ใช้กรวยจราจรและป้ายเตือนชั่วคราว\n4: ปฏิบัติงานบนทางเท้าหรือขอบทางได้โดยไม่กีดขวางการจราจร สอดคล้องตามระเบียบงานสาธารณูปโภค\n5: ไม่กระทบต่อการจราจรและพื้นที่สาธารณะเลย ปฏิบัติการเสร็จสิ้นในเวลารวดเร็วโดยไม่ต้องขออนุญาตพิเศษ",
                "score": 3,
                "weight": 0.075,
                "evidence": "solution-details/solution-2.md lines 27-29; requires opening manhole covers for 3 minutes from sidewalk/road edge; rapid turnaround substantially lowers traffic impact compared to rovers, but requires standard municipal maintenance protocol.",
                "descope": "Coordinate testing on KMUTT campus drainage manholes to avoid public street traffic jurisdiction."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมาย (Legal 2.4)",
                "question": "ทรัพย์สินทางปัญญา ลิขสิทธิ์ซอฟต์แวร์ และสิทธิบัตร (IP & Software Licensing)?",
                "rationale": "ตรวจสอบความปลอดภัยด้านสิทธิบัตรเพื่อป้องกันการถูกฟ้องร้องละเมิดทรัพย์สินทางปัญญา",
                "rubric": "1: ละเมิดสิทธิบัตรที่ยังมีผลคุ้มครองอย่างชัดเจน หรือใช้ซอฟต์แวร์ผิดสัญญาอนุญาตทางการค้า\n2: มีความคลุมเครือด้านสิทธิบัตร มีความเสี่ยงที่จะถูกฟ้องร้องจากเจ้าของเทคโนโลยีเดิม\n3: ใช้ไลบรารีที่มีสัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น AGPL) ซึ่งบังคับให้ต้องเปิดเผยซอร์สโค้ดทั้งหมด\n4: ซอฟต์แวร์และฮาร์ดแวร์อยู่ภายใต้สัญญาอนุญาตแบบเสรี (Permissive License เช่น MIT, BSD, Apache 2.0)\n5: เทคโนโลยีเป็นสาธารณสมบัติ (Public Domain) สิทธิบัตรหมดอายุแล้ว หรือสร้างสรรค์ขึ้นใหม่ทั้งหมด",
                "score": 5,
                "weight": 0.075,
                "evidence": "solution-details/solution-2.md lines 31, 34-36; EPA SL-RAT acoustic inspection methodology and mathematical attenuation formulations are in the public domain and widely published in academic literature; open-source SciPy algorithms.",
                "descope": "Rely exclusively on open academic acoustic reflectometry papers and MIT/Apache-licensed DSP libraries."
            },
            {
                "id": "O-01",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบต่อระบบหากเกิดความล้มเหลวขณะปฏิบัติงาน (Operational Failure Impact)?",
                "rationale": "ประเมินความรุนแรงของผลกระทบกรณีระบบขัดข้อง ว่าทำให้อุดตันท่อหรือระบบระบายน้ำเสียหายหรือไม่",
                "rubric": "1: อุปกรณ์ติดค้างในท่อกลายเป็นสิ่งกีดขวางทางน้ำอย่างถาวร ต้องทุบถนนขุดลอกท่อเพื่อเก็บกู้\n2: การขัดข้องทำให้ระบบประเมินค่าผิดพลาดจนส่งผลให้เกิดน้ำท่วมขัง และการเก็บกู้ต้องใช้เครื่องมือหนัก\n3: อุปกรณ์หยุดทำงานแต่สามารถดึงสายสลิงเก็บกู้ได้ง่าย โดยไม่ส่งผลกระทบต่อการไหลของน้ำ\n4: ระบบขัดข้องเฉพาะบางเซนเซอร์ ยังสามารถประเมินผลเบื้องต้นได้ และเก็บกู้ได้ทันทีโดยสลักนิรภัย\n5: ทำงานจากผิวดินแบบ Fail-Safe 100% หากระบบหยุดทำงานก็ไม่มีชิ้นส่วนใดค้างอยู่ในท่อระบายน้ำ",
                "score": 5,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 27-29, 39; system operates strictly from the surface above the wastewater line; if battery dies or audio fails, the operator simply pulls up the pole; zero risk of blocking pipe.",
                "descope": "Attach safety wrist straps to acoustic wand poles to prevent accidental drops into the manhole."
            },
            {
                "id": "O-02",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมผู้ใช้และสภาพหน้างานจริง (User Behavior & Problem-Solution Fit)?",
                "rationale": "ประเมินความสะดวกของเจ้าหน้าที่หน้างาน ว่าระบบใช้งานง่ายและตอบสนองขั้นตอนการทำงานจริงหรือไม่",
                "rubric": "1: ขัดแย้งกับขั้นตอนการทำงานเดิมโดยสิ้นเชิง เจ้าหน้าที่ปฏิเสธการใช้งานเพราะยุ่งยากและอันตราย\n2: ต้องใช้เวลาฝึกอบรมเจ้าหน้าที่นานเกิน 4 สัปดาห์ และต้องปรับเปลี่ยนขั้นตอนการทำงานเกือบทั้งหมด\n3: เจ้าหน้าที่ยอมรับได้แต่ต้องมีขั้นตอนพิเศษเพิ่มเติม เช่น การต่อสายไฟและตั้งค่าหน้างานหลายขั้นตอน\n4: ใช้งานง่าย สอดคล้องกับขั้นตอนการตรวจท่อปกติ เจ้าหน้าที่เรียนรู้การทำงานได้ภายใน 1 วัน\n5: ใช้งานได้ทันทีโดยไม่ต้องเปลี่ยนพฤติกรรมเดิม (Zero-learning curve) ออกแบบตามสรีรศาสตร์หน้างาน",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 15, 27-31, 41-42; Lightweight handheld poles take < 3 minutes per manhole pair. Since water depth is constrained <=20%, field crews can operate with clear air space without crawler retrieval hassles, requiring only simple manhole opening protocol.",
                "descope": "Provide a simple color-coded LED traffic light display (Green/Yellow/Red) on the pole to indicate blockage score without requiring laptop viewing."
            },
            {
                "id": "O-03",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนเชิงบริหารของนักพัฒนา (Administrative & Lab Dependency)?",
                "rationale": "ประเมินความคล่องตัวในการพัฒนา ว่าต้องรอการอนุมัติหรือติดขัดการใช้ห้องแล็บเฉพาะทางหรือไม่",
                "rubric": "1: ต้องใช้ห้องปฏิบัติการพิเศษที่มีการควบคุมความปลอดภัยสูง ต้องทำเรื่องขออนุมัติล่วงหน้าหลายสัปดาห์\n2: พึ่งพาเครื่องจักรหนักในช็อปวิศวกรรม มีคิวรอใช้งานยาวนาน และเข้าใช้งานได้เฉพาะเวลาทำการ\n3: ต้องการพื้นที่ทดสอบจำลองขนาดใหญ่ในแล็บ แต่สามารถจัดสรรเวลาทำงานร่วมกับทีมอื่นได้\n4: ใช้อุปกรณ์ในแล็บทั่วไป มีความพร้อมใช้งานสูง และสามารถนำกลับไปทดสอบต่อที่หอพักได้\n5: พัฒนาและทดสอบได้ทุกที่อย่างอิสระ ไม่ต้องพึ่งพาห้องแล็บหรือการอนุมัติเชิงบริหารใดๆ ทั้งสิ้น",
                "score": 5,
                "weight": 0.05,
                "evidence": "team-skills/due.md, jk.md; audio circuitry and DSP code development can be tested entirely on dorm/lab bench using PVC pipe sections with zero machine shop gatekeeping.",
                "descope": "Build a tabletop PVC drainage test pipe in the dorm to conduct all acoustic wave tuning."
            },
            {
                "id": "O-04",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประมวลผลและการเตรียมระบบ (Step Count & Pipeline Friction)?",
                "rationale": "วัดจำนวนขั้นตอนและความยุ่งยากในการเตรียมระบบก่อนเริ่มใช้งานจริง",
                "rubric": "1: มีขั้นตอนซับซ้อนเกิน 10 ขั้นตอน ต้องปรับเทียบเซนเซอร์และต่อสายสัญญาณยุ่งยากหน้างาน\n2: มีขั้นตอน 7–10 ขั้นตอน ต้องใช้คอมพิวเตอร์ตั้งโต๊ะและอุปกรณ์เสริมหลายชิ้นในการเริ่มระบบ\n3: มีขั้นตอน 4–6 ขั้นตอน ต้องเชื่อมต่อสายสัญญาณและเปิดโปรแกรมตามลำดับที่กำหนด\n4: มีขั้นตอน 2–3 ขั้นตอน เพียงเปิดสวิตช์และกดปุ่มเริ่มทำงาน ระบบจะปรับเทียบตัวเองโดยอัตโนมัติ\n5: ทำงานแบบสัมผัสเดียว (One-Touch Operation) เสียบปลั๊ก/เปิดเครื่องแล้วเริ่มประมวลผลได้ทันที",
                "score": 4,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 27-36; straightforward transmitter-receiver setup with standard ESP32 Arduino/PlatformIO toolchain and automated signal analysis script.",
                "descope": "Automate chirp triggering via a single physical pushbutton on the transmitter horn unit."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงาน (Schedule 2.6)",
                "question": "ความพร้อมของระบบและการส่งมอบต้นแบบภายในกรอบเวลา 5 สัปดาห์ทำงาน (Design Maturity & Schedule Compliance)?",
                "rationale": "ประเมินความเป็นไปได้ในการสร้าง ทดสอบ และส่งมอบต้นแบบวิศวกรรมให้เสร็จทันกำหนด 5 สัปดาห์",
                "rubric": "1: ไม่สามารถทำเสร็จได้ทันใน 5 สัปดาห์แน่นอน ต้องใช้เวลาพัฒนาอย่างน้อย 10–12 สัปดาห์ขึ้นไป\n2: มีความเสี่ยงสูงมากที่จะล่าช้า งานวิจัยและพัฒนาชิ้นส่วนกลไกอาจกินเวลาเกินกว่า 6 สัปดาห์\n3: มีความเป็นไปได้แต่ตึงเครียดมาก ต้องทำงานล่วงเวลาและตัดทอนฟังก์ชันย่อยบางส่วนออก\n4: มีความเป็นไปได้สูง แผนงานสอดคล้องกับศักยภาพทีม มีเวลาทดสอบระบบรวมอย่างน้อย 1 สัปดาห์\n5: มั่นใจว่าเสร็จสมบูรณ์ก่อนกำหนด มีต้นแบบที่ทำงานได้ในสัปดาห์ที่ 3 และมีเวลาปรับแต่งอย่างเต็มที่",
                "score": 4,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; electronic schematics and acoustic software can be finalized in 2 weeks; breadboard PoC achievable before midterm with production testing in Weeks 11-13.",
                "descope": "Freeze hardware architecture at Week 9 and focus remaining sprint entirely on software calibration."
            },
            {
                "id": "SDG-01",
                "pillar": "ความยั่งยืน (SDGs 2.7)",
                "question": "ผลกระทบต่อสิ่งแวดล้อม สังคม และเศรษฐกิจตามกรอบ SDG Wedding Cake (Biosphere, Society, Economy)?",
                "rationale": "ประเมินคุณค่าที่แท้จริงต่อเป้าหมายการพัฒนาที่ยั่งยืน 3 ชั้น ป้องกันการสร้างภาพลักษณ์สีเขียว (Greenwashing)",
                "rubric": "1: สร้างภาพลักษณ์สีเขียวโดยไม่มีผลกระทบเชิงประจักษ์ (Greenwashing) หรือไม่ตอบโจทย์ SDG ชั้นใดเลย\n2: ตอบโจทย์เฉพาะชั้นเศรษฐกิจหรือสังคมอย่างผิวเผิน แต่ไม่มีผลกระทบต่อการอนุรักษ์ชีวมณฑล (Biosphere)\n3: มีผลกระทบเชิงบวกที่ชัดเจนใน 1 มิติ (เช่น ป้องกันน้ำท่วมในมิติสังคม หรือลดขยะในมิติชีวมณฑล)\n4: บูรณาการอย่างเข้มแข็งข้าม 2 มิติ (เช่น ชีวมณฑลด้านการจัดการน้ำ ร่วมกับสังคมเมืองที่ปลอดภัย)\n5: บูรณาการครบทั้ง 3 ชั้นของ SDG Wedding Cake: ชีวมณฑล (น้ำสะอาด) + สังคม (เมืองยั่งยืน) + เศรษฐกิจ (คุ้มค่า)",
                "score": 5,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 6-10, 15; completely unites Biosphere (SDG 6.3 preventing sewer blockages and dirty overflow), Society (SDG 11.5 urban flood mitigation), and Economy (SDG 8.2 & 12.2 optimizing municipal maintenance resources).",
                "descope": "Frame capstone report explicitly using the Stockholm Resilience Centre SDG Wedding Cake model."
            },
            {
                "id": "SDG-02",
                "pillar": "ความยั่งยืน (SDGs 2.7)",
                "question": "รอยเท้าสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และระบบเก็บกู้ที่ปลอดภัย (Environmental Footprint & E-Waste Safeguards)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 5,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 38-40; 100% fail-safe surface retrieval; zero electronic components or toxic batteries enter wastewater; ultra-low power consumption with rechargeable lithium cells.",
                "descope": "Package surface pole electronics in reusable IP65 ABS plastic instrument enclosures."
            }
        ]
    },

    # --------------------------------------------------------------------------
    # SOLUTION 1 - CCTV WHEELED CRAWLER (CONDITIONALLY VIABLE)
    # --------------------------------------------------------------------------
    {
        "sheet_title": "Solution_1_CCTV_Crawler",
        "concept": "Solution 1: Pipe Inspection Robot using CCTV for profiling pipe (4K PTZ Camera + YOLOv8 Wheeled Crawler)",
        "strength": "ให้ภาพวิดีโอความละเอียดสูง (HD/4K) ภายในท่อจริง พร้อมโมเดล AI (YOLOv8) ตรวจจับรอยแตกร้าว รอยรั่ว และสิ่งอุดตันได้โดยอัตโนมัติ โดยสอดรับกับข้อจำกัดน้ำในท่อไม่เกิน 20% ทำให้กล้องมองเห็นผิวท่อส่วนบนได้ชัดเจน",
        "bottleneck": "ต้องใช้หุ่นยนต์ลงไปสัมผัสน้ำเสียในท่อจริง แม้น้ำไม่เกิน 20% แต่ล้อและระบบซีลยังต้องทนทานต่อน้ำและคราบไขมัน (IP68), มีความเสี่ยงหุ่นยนต์ติดค้าง/สาย Tether พันกันในท่อ (O-01=3), และต้องใช้เวลาสร้างระบบกลไกกันน้ำสูงเกินกรอบเวลา 5 สัปดาห์ (S-01=2)",
        "advice": "ลดสโคปกลไกขับเคลื่อนที่ซับซ้อน หันมาใช้โครงสร้างล้อสำเร็จรูป (COTS Crawler Chassis) พร้อมติดตั้งชุดสาย Tether แบบ Slip-Ring คุณภาพสูง และทดสอบระบบกันน้ำในถังทดสอบก่อนลงพื้นที่จริง",
        "robotic_compatibility": {
            "score": 10.5,
            "domains": {
                "perception": "Score 3.5/4.0: 4K PTZ Optical Camera with High-Power LED array and wheel distance encoders; captures visual defect features under active illumination.",
                "control_algorithms": "Score 3.5/4.0: Edge AI YOLOv8 deep learning object detection for real-time crack/blockage classification and spatial defect map indexing.",
                "actuation_mechanics": "Score 3.5/4.0: Multi-wheel motorized crawler platform traversing hazardous underground pipe geometry with differential steering and tether management."
            },
            "fibo_alignment_rationale": "Solution 1 implements a genuine closed-loop mobile robotic system across all three FIBO pillars: active high-resolution optical perception, edge neural network defect inferencing, and mobile robotic pipe locomotion, utilizing mechatronics and control skills directly."
        },
        "robotic_data": {
            "score": 10.5,
            "domains": {
                "perception": "Score 3.5/4.0: 4K PTZ Optical Camera with High-Power LED array and wheel distance encoders; captures visual defect features under active illumination.",
                "control_algorithms": "Score 3.5/4.0: Edge AI YOLOv8 deep learning object detection for real-time crack/blockage classification and spatial defect map indexing.",
                "actuation_mechanics": "Score 3.5/4.0: Multi-wheel motorized crawler platform traversing hazardous underground pipe geometry with differential steering and tether management."
            },
            "fibo_alignment_rationale": "Solution 1 implements a genuine closed-loop mobile robotic system across all three FIBO pillars: active high-resolution optical perception, edge neural network defect inferencing, and mobile robotic pipe locomotion, utilizing mechatronics and control skills directly."
        },
        "assessment_data": [
            {
                "id": "T-01",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับการสร้างเองเทียบกับการซื้อสำเร็จรูป (Build vs. Buy Burden) ของสถาปัตยกรรมระบบตรวจประเมินท่อระบายน้ำ?",
                "rationale": "ประเมินภาระการวิจัยและพัฒนาชิ้นส่วนกลไก อิเล็กทรอนิกส์ และอัลกอริทึม ป้องกันการเสียเวลากับงานประดิษฐ์ขึ้นใหม่โดยไม่จำเป็น",
                "rubric": "1: ต้องวิจัยและสร้างขึ้นเองทั้งหมด 100% (ไม่มีพิมพ์เขียว อัลกอริทึม หรือไลบรารีอ้างอิง)\n2: มีชิ้นส่วนหลักในท้องตลาด แต่ต้องดัดแปลงโครงสร้างอย่างหนักและเขียนโค้ดเชื่อมต่อเองทั้งหมด\n3: บูรณาการชิ้นส่วน COTS เข้ากับแท่นยึดแบบกำหนดเอง และเขียนโค้ดเชื่อมต่อบางส่วน\n4: ประกอบจากโมดูลมาตรฐานสำเร็จรูป (DIN-rail, I2C/CAN shields) มีงานประกอบกลไกเล็กน้อย\n5: ซื้อมาติดตั้งใช้งานได้ทันที (Plug-and-Play) ไม่ต้องตัดกลึงหรือบัดกรีวงจรเพิ่มเติม",
                "score": 2,
                "weight": 0.04,
                "evidence": "solution-details/solution-1.md lines 32-38; requires custom waterproof IP68 motor pods, sealed differential drivetrain, custom chassis fabrication for wastewater resistance, and tether reel slip-ring integration.",
                "descope": "Purchase a pre-sealed commercial off-the-shelf (COTS) IP68 RC crawler chassis and mount camera modules externally to avoid custom rotary shaft seal fabrication."
            },
            {
                "id": "T-02",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "สิทธิ์ในการเข้าถึงเทคโนโลยี ซอฟต์แวร์ และระบบนิเวศข้อมูล (Access & Permissions) ของระบบตรวจประเมินท่อ?",
                "rationale": "ตรวจสอบข้อจำกัดด้านกรรมสิทธิ์ การล็อกสิทธิ์ใช้งาน และการอนุญาตเข้าถึง เพื่อป้องกันการพัฒนาระบบบนฐานข้อมูลที่ไม่สามารถเข้าถึงได้จริง",
                "rubric": "1: ล็อกสิทธิ์ภายใต้สัญญา NDA ระบบปิด ติดไฟร์วอลล์องค์กร หรือไม่มีสิทธิ์เข้าถึงฝั่งนักพัฒนา\n2: ซอฟต์แวร์หรือเฟิร์มแวร์กรรมสิทธิ์ปิด ทำงานแบบ Black-box โดยไม่มี Source Code หรือ Telemetry\n3: บัญชีเพื่อการศึกษา/ทดลองใช้ที่มีโควตาหรือ Rate Limit เข้มงวด ต้องรอการอนุมัติอย่างเป็นทางการ\n4: มี SDK หรือ Open API สาธารณะพร้อมเอกสารครบถ้วน แต่ไม่สามารถแก้ไขสถาปัตยกรรมระดับล่างได้\n5: สถาปัตยกรรมเปิดสมบูรณ์ (Open Source/Open HW) ทีมงานมีสิทธิ์ระดับ Root/Admin เต็มรูปแบบ",
                "score": 5,
                "weight": 0.04,
                "evidence": "solution-details/solution-1.md lines 33-36; utilizes open-source YOLOv8 architecture, standard RTSP video streaming, open Python/OpenCV stacks, and ESP32/STM32 motor control with full root/developer access.",
                "descope": "Maintain fully open-source pipeline using Ultralytics YOLOv8 and standard ROS2 camera drivers."
            },
            {
                "id": "T-03",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับความพร้อมทางเทคโนโลยี (Base Performance / TRL) ในสภาพแวดล้อมจริงของท่อระบายน้ำใต้ดิน?",
                "rationale": "วัดวุฒิภาวะของเทคโนโลยีว่าผ่านการพิสูจน์ในสภาพแวดล้อมใต้ดินที่มีความชื้น สารกัดกร่อน หรือน้ำขังจริงแล้วหรือไม่",
                "rubric": "1: ระดับแนวคิด/สมการคณิตศาสตร์ (TRL 2–3) ทดสอบเฉพาะในห้องทดลองที่ควบคุมสภาพแวดล้อมได้\n2: เบรดบอร์ดทำงานได้ในแล็บ (TRL 4) สายไฟเปราะบาง ยังไม่ผ่านการสอบเทียบในสภาพแวดล้อมจริง\n3: ตัวต้นแบบประกอบลงกล่อง (TRL 5–6) ผ่านการทดสอบในสภาพแวดล้อมจำลอง ต้องมีคนคอยดูแล\n4: ต้นแบบระดับพรีโปรดักชัน (TRL 7) ทำงานได้อย่างมีเสถียรภาพในสภาพแวดล้อมปฏิบัติงานจริง\n5: ผลิตภัณฑ์เชิงพาณิชย์สมบูรณ์ (TRL 8–9) ผ่านการรับรองมาตรฐาน มีค่า MTBF ยืนยันความทนทาน",
                "score": 3,
                "weight": 0.04,
                "evidence": "solution-details/solution-1.md lines 15, 40-49; CCTV pipe crawling is established commercially (TRL 8-9). With water depth confirmed <=20%, the PTZ camera sits in clear air space, avoiding murkiness, but student crawler wheels must negotiate sludge and grease, operating at TRL 5-6.",
                "descope": "Bench-test optical detection under simulated low-light wet pipe conditions using pre-recorded sewer footage before building crawler chassis."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความเข้ากันได้ของทีม (Manpower & Skill Redundancy) ด้านวิศวกรรมเฉพาะทาง?",
                "rationale": "ประเมินความเสี่ยงกรณีขาดแคลนบุคลากรที่มีความเชี่ยวชาญเฉพาะด้าน (Bus Factor) ว่ามีคนทำงานทดแทนกันได้หรือไม่",
                "rubric": "1: ขาดแคลนทักษะเฉพาะด้านโดยสิ้นเชิง (ไม่มีใครในทีมมีความรู้ในเทคโนโลยีหลักนี้เลย)\n2: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (Bus Factor = 1) หากคนนี้ไม่อยู่ โครงการจะหยุดชะงักทันที\n3: มีผู้รับผิดชอบหลัก 1 คน และมีผู้ช่วยที่พอเข้าใจระบบ แต่ยังแก้ไขปัญหาเชิงลึกแทนไม่ได้\n4: มีทักษะทดแทนกันได้ (Primary & Secondary) อย่างน้อย 2 คนสามารถสลับงานกันได้อย่างราบรื่น\n5: สมาชิกทุกคนในทีมมีทักษะระดับสูง ทำงานแทนกันได้ทันที และมีเอกสารคู่มือการทำงานครบถ้วน",
                "score": 3,
                "weight": 0.04,
                "evidence": "team-skills/due.md, fifa.md, jk.md, kin.md; Fifa and Due form a primary/secondary mechanical engineering pair; JK and Kin handle computer vision and AI model training.",
                "descope": "Document motor wiring pinouts and ROS2 camera topics clearly in repo README to avoid single-developer dependency."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันของเส้นทางการเรียนรู้ (Learning Curve) ด้านวิศวกรรมระบบ?",
                "rationale": "ประเมินเวลาและความยากในการเรียนรู้เทคโนโลยีใหม่ ว่าทีมงานสามารถเข้าใจและนำมาใช้ได้ทันเวลาหรือไม่",
                "rubric": "1: เทคโนโลยีใหม่ทั้งหมด ต้องใช้เวลาเรียนรู้เกิน 8 สัปดาห์ และต้องการทักษะคณิตศาสตร์ชั้นสูง\n2: มีแนวคิดซับซ้อน ต้องศึกษาทฤษฎีใหม่ที่ไม่เคยเรียนมาก่อน ใช้เวลาทำความเข้าใจ 4–6 สัปดาห์\n3: ต่อยอดจากพื้นฐานเดิมที่เคยเรียน แต่ต้องเรียนรู้เครื่องมือหรือสถาปัตยกรรมใหม่ ใช้เวลา 2–3 สัปดาห์\n4: เป็นเทคโนโลยีที่คุ้นเคย มีตัวอย่างโค้ดและวงจรอ้างอิงชัดเจน ใช้เวลาปรับตัวเพียง 1 สัปดาห์\n5: ทำงานบนพื้นฐานทักษะประจำวันของทีม ทำได้ทันทีโดยไม่ต้องศึกษาทฤษฎีหรือเครื่องมือเพิ่มเติม",
                "score": 3,
                "weight": 0.04,
                "evidence": "team-skills/fifa.md, jk.md; team has proven experience in ROS2, OpenCV, and 3D CAD, but waterproofing rotary shafts, tether slip rings, and lighting calibration in reflective wet pipes require a 2-3 week ramp-up.",
                "descope": "Use pre-trained YOLOv8 defect models and off-the-shelf IP68 waterproof cable glands."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (Payback Period / Value Horizon) ของระบบ?",
                "rationale": "ประเมินผลตอบแทนทางเศรษฐศาสตร์และการลดต้นทุนการขุดลอกท่อระบายน้ำของหน่วยงานรัฐ",
                "rubric": "1: ระยะเวลาคืนทุนเกิน 7 ปี หรือต้นทุนการดำเนินงานสูงกว่ามูลค่าความเสียหายที่ป้องกันได้\n2: ระยะเวลาคืนทุน 5–7 ปี ให้ผลตอบแทนทางอ้อมเป็นหลัก และมีความไม่แน่นอนทางการเงินสูง\n3: ระยะเวลาคืนทุน 3–5 ปี มีความคุ้มค่าระดับปานกลาง จำเป็นต้องได้รับการอุดหนุนงบประมาณจากรัฐ\n4: ระยะเวลาคืนทุน 1–3 ปี ประหยัดค่าใช้จ่ายการซ่อมบำรุงเชิงแก้ไขได้อย่างชัดเจน คุ้มค่าสูง\n5: คืนทุนได้ภายใน 1 ปีแรก ลดต้นทุนการบำรุงรักษาได้ทันที และสร้างมูลค่าเพิ่มทางตรงอย่างมหาศาล",
                "score": 3,
                "weight": 0.0667,
                "evidence": "solution-details/solution-1.md lines 6-7, 15, 43; condition-based visual inspection prevents unnecessary cleanings and provides actionable visual proof; moderate payback period of 3–4 years due to mechanical crawler deployment overhead.",
                "descope": "Package visual reporting into an automated PDF generation tool for municipal engineers to prove immediate inspection ROI."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระดับการพึ่งพาชิ้นส่วนและผู้จัดจำหน่ายภายนอก (Component Dependency & Vendor Lock-in)?",
                "rationale": "ประเมินความเสี่ยงด้านห่วงโซ่อุปทานและการผูกขาดชิ้นส่วน ป้องกันระบบล่มสลายจากผู้ผลิตรายเดียว",
                "rubric": "1: ผูกขาดโดยผู้ผลิตรายเดียว (Sole Source) ชิ้นส่วนสั่งทำพิเศษ ขาดตลาดง่าย นำเข้ายาก\n2: มีผู้จัดจำหน่าย 2 ราย แต่ชิ้นส่วนมีราคาสูง ใช้เวลาจัดส่งนานเกิน 4 สัปดาห์ และไม่มีอะไหล่ทดแทน\n3: ชิ้นส่วนมาตรฐานแต่มีบางโมดูลต้องสั่งนำเข้า มีระยะเวลารอคอย 2–3 สัปดาห์\n4: ใช้ชิ้นส่วนมาตรฐานอุตสาหกรรม (COTS) มีผู้ขายในประเทศหลายราย จัดหาทดแทนได้ใน 3–5 วัน\n5: อะไหล่หาง่ายทั่วไปตามร้านค้าอุปกรณ์อิเล็กทรอนิกส์ในประเทศ ซื้อทดแทนได้ทันทีภายใน 24 ชม.",
                "score": 4,
                "weight": 0.0667,
                "evidence": "solution-details/solution-1.md lines 32-38; uses standard COTS DC gearmotors, standard USB/RTSP cameras, and open microcontrollers available from multiple domestic vendors.",
                "descope": "Select widely distributed geared motors (e.g. planetary 12V DC) available from Thai hobby and robotics suppliers."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "สัดส่วนงบประมาณสำรองความเสียหาย (Scrap Margin / Safety Allowance) ของชิ้นส่วน?",
                "rationale": "ตรวจสอบความปลอดภัยทางการเงินกรณีทำอุปกรณ์เสียหายระหว่างการทดลองในน้ำเสีย",
                "rubric": "1: ไม่มีงบสำรองเลย หากชิ้นส่วนพังโครงการจะหยุดชะงักทันที (ราคาชิ้นส่วนเท่ากับงบประมาณทั้งหมด)\n2: งบสำรองรองรับการเสียหายได้ไม่เกิน 1 ครั้ง ชิ้นส่วนสำคัญไม่มีอะไหล่สำรอง\n3: มีงบสำรอง 20–30% ซื้อชิ้นส่วนราคาปานกลางสำรองได้ แต่ไม่มีอะไหล่สำหรับโมดูลหลักราคาแพง\n4: มีงบสำรอง 50% มีชิ้นส่วนหลักและไอซีสำคัญสำรองอย่างน้อย 2–3 ชุด ทดลองได้อย่างมั่นใจ\n5: งบประมาณเหลือเฟือ ชิ้นส่วนราคาถูกมาก สามารถซื้อชุดสำรองแบบสมบูรณ์ได้เกิน 3 ชุดขึ้นไป",
                "score": 2,
                "weight": 0.0666,
                "evidence": "team-skills/due.md, fifa.md; waterproof crawler chassis, 4K PTZ camera, and high-spec tether cable consume over 60-70% of available team budget, leaving minimal spare funds if the primary camera or drive unit is flooded.",
                "descope": "Substitute expensive industrial PTZ camera with a modular waterproof action camera (or sealed webcam with dual servos) to keep unit cost under 1,500 THB."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมาย (Legal 2.4)",
                "question": "ความสอดคล้องกับกฎหมายความปลอดภัยสาธารณะและการจราจร (Regulatory & Public Safety Compliance)?",
                "rationale": "ประเมินความเสี่ยงการละเมิดกฎหมายควบคุมอาคาร ระเบียบงานทาง และข้อบังคับการจราจรขณะปฏิบัติงาน",
                "rubric": "1: เสี่ยงต่อการกระทำผิดกฎหมายอาญา ละเมิด พ.ร.บ. ทางหลวงอย่างร้ายแรง และไม่มีทางขออนุญาตได้\n2: ต้องขออนุญาตปิดการจราจรช่องทางหลัก เสี่ยงต่ออุบัติเหตุร้ายแรง และมีขั้นตอนอนุมัติยาวนาน\n3: ต้องขออนุญาตทำงานในเขตทางสาธารณะ แต่เป็นงานขนาดเล็ก ใช้กรวยจราจรและป้ายเตือนชั่วคราว\n4: ปฏิบัติงานบนทางเท้าหรือขอบทางได้โดยไม่กีดขวางการจราจร สอดคล้องตามระเบียบงานสาธารณูปโภค\n5: ไม่กระทบต่อการจราจรและพื้นที่สาธารณะเลย ปฏิบัติการเสร็จสิ้นในเวลารวดเร็วโดยไม่ต้องขออนุญาตพิเศษ",
                "score": 2,
                "weight": 0.075,
                "evidence": "solution-details/solution-1.md lines 18, 27; deploying wheeled crawler requires opening street manholes, stationing cable reels and operators on roadway shoulder for 30–60 minutes per section, requiring formal municipal work permits.",
                "descope": "Restrict field trials to pedestrian sidewalk manholes or off-road residential drainage channels."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมาย (Legal 2.4)",
                "question": "ทรัพย์สินทางปัญญา ลิขสิทธิ์ซอฟต์แวร์ และสิทธิบัตร (IP & Software Licensing)?",
                "rationale": "ตรวจสอบความปลอดภัยด้านสิทธิบัตรเพื่อป้องกันการถูกฟ้องร้องละเมิดทรัพย์สินทางปัญญา",
                "rubric": "1: ละเมิดสิทธิบัตรที่ยังมีผลคุ้มครองอย่างชัดเจน หรือใช้ซอฟต์แวร์ผิดสัญญาอนุญาตทางการค้า\n2: มีความคลุมเครือด้านสิทธิบัตร มีความเสี่ยงที่จะถูกฟ้องร้องจากเจ้าของเทคโนโลยีเดิม\n3: ใช้ไลบรารีที่มีสัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น AGPL) ซึ่งบังคับให้ต้องเปิดเผยซอร์สโค้ดทั้งหมด\n4: ซอฟต์แวร์และฮาร์ดแวร์อยู่ภายใต้สัญญาอนุญาตแบบเสรี (Permissive License เช่น MIT, BSD, Apache 2.0)\n5: เทคโนโลยีเป็นสาธารณสมบัติ (Public Domain) สิทธิบัตรหมดอายุแล้ว หรือสร้างสรรค์ขึ้นใหม่ทั้งหมด",
                "score": 5,
                "weight": 0.075,
                "evidence": "solution-details/solution-1.md lines 35-36; YOLOv8 educational license, OpenCV (Apache 2.0), and open ROS2 packages provide full legal and intellectual property clearance.",
                "descope": "Use AGPL-compliant open-source release or standard permissive MIT wrappers."
            },
            {
                "id": "O-01",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบต่อระบบหากเกิดความล้มเหลวขณะปฏิบัติงาน (Operational Failure Impact)?",
                "rationale": "ประเมินความรุนแรงของผลกระทบกรณีระบบขัดข้อง ว่าทำให้อุดตันท่อหรือระบบระบายน้ำเสียหายหรือไม่",
                "rubric": "1: อุปกรณ์ติดค้างในท่อกลายเป็นสิ่งกีดขวางทางน้ำอย่างถาวร ต้องทุบถนนขุดลอกท่อเพื่อเก็บกู้\n2: การขัดข้องทำให้ระบบประเมินค่าผิดพลาดจนส่งผลให้เกิดน้ำท่วมขัง และการเก็บกู้ต้องใช้เครื่องมือหนัก\n3: อุปกรณ์หยุดทำงานแต่สามารถดึงสายสลิงเก็บกู้ได้ง่าย โดยไม่ส่งผลกระทบต่อการไหลของน้ำ\n4: ระบบขัดข้องเฉพาะบางเซนเซอร์ ยังสามารถประเมินผลเบื้องต้นได้ และเก็บกู้ได้ทันทีโดยสลักนิรภัย\n5: ทำงานจากผิวดินแบบ Fail-Safe 100% หากระบบหยุดทำงานก็ไม่มีชิ้นส่วนใดค้างอยู่ในท่อระบายน้ำ",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 15, 46-49; operating in <=20% water depth avoids total submergence, but if crawler flips over or gets entangled in debris/grease, manual recovery via tether reel is required (O-01=3).",
                "descope": "Incorporate a high-tensile steel recovery cable tether rated for 150 kg pull force."
            },
            {
                "id": "O-02",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมผู้ใช้และสภาพหน้างานจริง (User Behavior & Problem-Solution Fit)?",
                "rationale": "ประเมินความสะดวกของเจ้าหน้าที่หน้างาน ว่าระบบใช้งานง่ายและตอบสนองขั้นตอนการทำงานจริงหรือไม่",
                "rubric": "1: ขัดแย้งกับขั้นตอนการทำงานเดิมโดยสิ้นเชิง เจ้าหน้าที่ปฏิเสธการใช้งานเพราะยุ่งยากและอันตราย\n2: ต้องใช้เวลาฝึกอบรมเจ้าหน้าที่นานเกิน 4 สัปดาห์ และต้องปรับเปลี่ยนขั้นตอนการทำงานเกือบทั้งหมด\n3: เจ้าหน้าที่ยอมรับได้แต่ต้องมีขั้นตอนพิเศษเพิ่มเติม เช่น การต่อสายไฟและตั้งค่าหน้างานหลายขั้นตอน\n4: ใช้งานง่าย สอดคล้องกับขั้นตอนการตรวจท่อปกติ เจ้าหน้าที่เรียนรู้การทำงานได้ภายใน 1 วัน\n5: ใช้งานได้ทันทีโดยไม่ต้องเปลี่ยนพฤติกรรมเดิม (Zero-learning curve) ออกแบบตามสรีรศาสตร์หน้างาน",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 6-7, 27-30; operators must carry crawler and heavy cable spool, wash down the muddy vehicle after each run, and coordinate crawler speed via manual joystick control.",
                "descope": "Design an ergonomic quick-release battery pod and motorized tether winder."
            },
            {
                "id": "O-03",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนเชิงบริหารของนักพัฒนา (Administrative & Lab Dependency)?",
                "rationale": "ประเมินความคล่องตัวในการพัฒนา ว่าต้องรอการอนุมัติหรือติดขัดการใช้ห้องแล็บเฉพาะทางหรือไม่",
                "rubric": "1: ต้องใช้ห้องปฏิบัติการพิเศษที่มีการควบคุมความปลอดภัยสูง ต้องทำเรื่องขออนุมัติล่วงหน้าหลายสัปดาห์\n2: พึ่งพาเครื่องจักรหนักในช็อปวิศวกรรม มีคิวรอใช้งานยาวนาน และเข้าใช้งานได้เฉพาะเวลาทำการ\n3: ต้องการพื้นที่ทดสอบจำลองขนาดใหญ่ในแล็บ แต่สามารถจัดสรรเวลาทำงานร่วมกับทีมอื่นได้\n4: ใช้อุปกรณ์ในแล็บทั่วไป มีความพร้อมใช้งานสูง และสามารถนำกลับไปทดสอบต่อที่หอพักได้\n5: พัฒนาและทดสอบได้ทุกที่อย่างอิสระ ไม่ต้องพึ่งพาห้องแล็บหรือการอนุมัติเชิงบริหารใดๆ ทั้งสิ้น",
                "score": 3,
                "weight": 0.05,
                "evidence": "team-skills/due.md, fifa.md; mechanical chassis fabrication requires FIBO workshop 3D printers, laser cutters, and a water immersion pressure tank to verify IP68 sealing.",
                "descope": "Use commercial waterproof pelican-style cases to avoid custom CNC machining queues."
            },
            {
                "id": "O-04",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประมวลผลและการเตรียมระบบ (Step Count & Pipeline Friction)?",
                "rationale": "วัดจำนวนขั้นตอนและความยุ่งยากในการเตรียมระบบก่อนเริ่มใช้งานจริง",
                "rubric": "1: มีขั้นตอนซับซ้อนเกิน 10 ขั้นตอน ต้องปรับเทียบเซนเซอร์และต่อสายสัญญาณยุ่งยากหน้างาน\n2: มีขั้นตอน 7–10 ขั้นตอน ต้องใช้คอมพิวเตอร์ตั้งโต๊ะและอุปกรณ์เสริมหลายชิ้นในการเริ่มระบบ\n3: มีขั้นตอน 4–6 ขั้นตอน ต้องเชื่อมต่อสายสัญญาณและเปิดโปรแกรมตามลำดับที่กำหนด\n4: มีขั้นตอน 2–3 ขั้นตอน เพียงเปิดสวิตช์และกดปุ่มเริ่มทำงาน ระบบจะปรับเทียบตัวเองโดยอัตโนมัติ\n5: ทำงานแบบสัมผัสเดียว (One-Touch Operation) เสียบปลั๊ก/เปิดเครื่องแล้วเริ่มประมวลผลได้ทันที",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 27-38; multi-stage pipeline involves sealed mechanical deployment, tether spool uncoiling, video transmission handshake, and post-processing AI inference pipeline.",
                "descope": "Automate video recording and YOLOv8 inferencing with an onboard one-button trigger script."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงาน (Schedule 2.6)",
                "question": "ความพร้อมของระบบและการส่งมอบต้นแบบภายในกรอบเวลา 5 สัปดาห์ทำงาน (Design Maturity & Schedule Compliance)?",
                "rationale": "ประเมินความเป็นไปได้ในการสร้าง ทดสอบ และส่งมอบต้นแบบวิศวกรรมให้เสร็จทันกำหนด 5 สัปดาห์",
                "rubric": "1: ไม่สามารถทำเสร็จได้ทันใน 5 สัปดาห์แน่นอน ต้องใช้เวลาพัฒนาอย่างน้อย 10–12 สัปดาห์ขึ้นไป\n2: มีความเสี่ยงสูงมากที่จะล่าช้า งานวิจัยและพัฒนาชิ้นส่วนกลไกอาจกินเวลาเกินกว่า 6 สัปดาห์\n3: มีความเป็นไปได้แต่ตึงเครียดมาก ต้องทำงานล่วงเวลาและตัดทอนฟังก์ชันย่อยบางส่วนออก\n4: มีความเป็นไปได้สูง แผนงานสอดคล้องกับศักยภาพทีม มีเวลาทดสอบระบบรวมอย่างน้อย 1 สัปดาห์\n5: มั่นใจว่าเสร็จสมบูรณ์ก่อนกำหนด มีต้นแบบที่ทำงานได้ในสัปดาห์ที่ 3 และมีเวลาปรับแต่งอย่างเต็มที่",
                "score": 2,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; designing, machining, waterproofing, and debugging a functional motorized pipe crawler while maintaining midterm/final exam study schedules creates severe delivery risks within 5 business weeks.",
                "descope": "Adapt a pre-built tracked RC vehicle rather than fabricating custom gearboxes and aluminum wheel hubs."
            },
            {
                "id": "SDG-01",
                "pillar": "ความยั่งยืน (SDGs 2.7)",
                "question": "ผลกระทบต่อสิ่งแวดล้อม สังคม และเศรษฐกิจตามกรอบ SDG Wedding Cake (Biosphere, Society, Economy)?",
                "rationale": "ประเมินคุณค่าที่แท้จริงต่อเป้าหมายการพัฒนาที่ยั่งยืน 3 ชั้น ป้องกันการสร้างภาพลักษณ์สีเขียว (Greenwashing)",
                "rubric": "1: สร้างภาพลักษณ์สีเขียวโดยไม่มีผลกระทบเชิงประจักษ์ (Greenwashing) หรือไม่ตอบโจทย์ SDG ชั้นใดเลย\n2: ตอบโจทย์เฉพาะชั้นเศรษฐกิจหรือสังคมอย่างผิวเผิน แต่ไม่มีผลกระทบต่อการอนุรักษ์ชีวมณฑล (Biosphere)\n3: มีผลกระทบเชิงบวกที่ชัดเจนใน 1 มิติ (เช่น ป้องกันน้ำท่วมในมิติสังคม หรือลดขยะในมิติชีวมณฑล)\n4: บูรณาการอย่างเข้มแข็งข้าม 2 มิติ (เช่น ชีวมณฑลด้านการจัดการน้ำ ร่วมกับสังคมเมืองที่ปลอดภัย)\n5: บูรณาการครบทั้ง 3 ชั้นของ SDG Wedding Cake: ชีวมณฑล (น้ำสะอาด) + สังคม (เมืองยั่งยืน) + เศรษฐกิจ (คุ้มค่า)",
                "score": 4,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 6-10; strongly addresses Biosphere (SDG 6.3 preventing untreated sewer overflow) and Society (SDG 11.5 resilient urban drainage), but provides moderate economic efficiency due to mobilization costs.",
                "descope": "Quantify municipal carbon footprint reduction achieved by eliminating redundant vacuum truck trips."
            },
            {
                "id": "SDG-02",
                "pillar": "ความยั่งยืน (SDGs 2.7)",
                "question": "รอยเท้าสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และระบบเก็บกู้ที่ปลอดภัย (Environmental Footprint & E-Waste Safeguards)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 47; physical tether prevents total hardware loss, but sewage moisture, grease, and H2S gas cause rapid wear and electronic corrosion over repeated deployments.",
                "descope": "Conformal coat all internal electronics with silicone/polyurethane moisture barrier to extend hardware lifespan."
            }
        ]
    },

    # --------------------------------------------------------------------------
    # SOLUTION 4 - LIDAR SLAM CRAWLER (VETOED PENDING DE-SCOPING)
    # --------------------------------------------------------------------------
    {
        "sheet_title": "Solution_4_LiDAR_SLAM",
        "concept": "Solution 4: Pipe Inspection Instrument using LiDAR SLAM attaching with Robot (3D LiDAR + Laser SLAM Point Cloud Profiling)",
        "strength": "สร้างแผนที่ 3 มิติ (3D Point Cloud) ของท่อระบายน้ำได้อย่างแม่นยำระดับมิลลิเมตร สามารถตรวจวัดปริมาตรตะกอน (Buildup/Debris) และตรวจจับการเสียรูปเชิงเรขาคณิตของท่อได้อย่างชัดเจน",
        "bottleneck": "เซนเซอร์ 3D LiDAR และบอร์ดประมวลผล GPU/SBC มีราคาสูงมากเกินงบประมาณ (E-03=1: ไม่มีงบสำรองกรณีเซนเซอร์ตกน้ำหรือพังเสียหาย เกิด Fatal Flaw ทันที), เลเซอร์ไม่สามารถทะลุน้ำเสียหรือหมอกควันได้ (T-03=2), และต้องใช้เวลาประมวลผล Point Cloud สูง",
        "advice": "ลดสโคปจากการใช้ 3D LiDAR ราคาแพง มาใช้ 2D LiDAR ติดตั้งบนแกนหมุน หรือใช้ Depth Camera / Structured Light ในท่อแห้งเพื่อควบคุมต้นทุนไม่ให้เกินงบประมาณและปลดล็อก Fatal Flaw",
        "robotic_compatibility": {
            "score": 11.5,
            "domains": {
                "perception": "Score 4.0/4.0: 3D LiDAR spatial laser time-of-flight scanning with IMU fusion, acquiring dense point clouds with millimeter-level geometric accuracy.",
                "control_algorithms": "Score 4.0/4.0: 3D LiDAR SLAM state estimation (FAST-LIO / LIO-SAM), point cloud registration/ICP, non-linear optimization, and volumetric debris extraction.",
                "actuation_mechanics": "Score 3.5/4.0: Motorized pipe crawler mobile platform with encoder feedback, speed/heading regulation, and data tether management."
            },
            "fibo_alignment_rationale": "Solution 4 exercises the peak FIBO robotics curriculum: 3D spatial laser perception, advanced SLAM state estimation, and mobile mechatronic locomotion, representing a gold-standard capstone robotics architecture."
        },
        "robotic_data": {
            "score": 11.5,
            "domains": {
                "perception": "Score 4.0/4.0: 3D LiDAR spatial laser time-of-flight scanning with IMU fusion, acquiring dense point clouds with millimeter-level geometric accuracy.",
                "control_algorithms": "Score 4.0/4.0: 3D LiDAR SLAM state estimation (FAST-LIO / LIO-SAM), point cloud registration/ICP, non-linear optimization, and volumetric debris extraction.",
                "actuation_mechanics": "Score 3.5/4.0: Motorized pipe crawler mobile platform with encoder feedback, speed/heading regulation, and data tether management."
            },
            "fibo_alignment_rationale": "Solution 4 exercises the peak FIBO robotics curriculum: 3D spatial laser perception, advanced SLAM state estimation, and mobile mechatronic locomotion, representing a gold-standard capstone robotics architecture."
        },
        "assessment_data": [
            {
                "id": "T-01",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับการสร้างเองเทียบกับการซื้อสำเร็จรูป (Build vs. Buy Burden) ของสถาปัตยกรรมระบบตรวจประเมินท่อระบายน้ำ?",
                "rationale": "ประเมินภาระการวิจัยและพัฒนาชิ้นส่วนกลไก อิเล็กทรอนิกส์ และอัลกอริทึม ป้องกันการเสียเวลากับงานประดิษฐ์ขึ้นใหม่โดยไม่จำเป็น",
                "rubric": "1: ต้องวิจัยและสร้างขึ้นเองทั้งหมด 100% (ไม่มีพิมพ์เขียว อัลกอริทึม หรือไลบรารีอ้างอิง)\n2: มีชิ้นส่วนหลักในท้องตลาด แต่ต้องดัดแปลงโครงสร้างอย่างหนักและเขียนโค้ดเชื่อมต่อเองทั้งหมด\n3: บูรณาการชิ้นส่วน COTS เข้ากับแท่นยึดแบบกำหนดเอง และเขียนโค้ดเชื่อมต่อบางส่วน\n4: ประกอบจากโมดูลมาตรฐานสำเร็จรูป (DIN-rail, I2C/CAN shields) มีงานประกอบกลไกเล็กน้อย\n5: ซื้อมาติดตั้งใช้งานได้ทันที (Plug-and-Play) ไม่ต้องตัดกลึงหรือบัดกรีวงจรเพิ่มเติม",
                "score": 3,
                "weight": 0.04,
                "evidence": "solution-details/solution-4.md lines 27-36; mounts COTS 3D LiDAR module and embedded SBC (Jetson/Pi) on a custom crawler chassis, running standard ROS2 SLAM packages.",
                "descope": "Use open-source robot base (e.g. Turtlebot3 chassis) with standard ROS2 LiDAR mounting brackets."
            },
            {
                "id": "T-02",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "สิทธิ์ในการเข้าถึงเทคโนโลยี ซอฟต์แวร์ และระบบนิเวศข้อมูล (Access & Permissions) ของระบบตรวจประเมินท่อ?",
                "rationale": "ตรวจสอบข้อจำกัดด้านกรรมสิทธิ์ การล็อกสิทธิ์ใช้งาน และการอนุญาตเข้าถึง เพื่อป้องกันการพัฒนาระบบบนฐานข้อมูลที่ไม่สามารถเข้าถึงได้จริง",
                "rubric": "1: ล็อกสิทธิ์ภายใต้สัญญา NDA ระบบปิด ติดไฟร์วอลล์องค์กร หรือไม่มีสิทธิ์เข้าถึงฝั่งนักพัฒนา\n2: ซอฟต์แวร์หรือเฟิร์มแวร์กรรมสิทธิ์ปิด ทำงานแบบ Black-box โดยไม่มี Source Code หรือ Telemetry\n3: บัญชีเพื่อการศึกษา/ทดลองใช้ที่มีโควตาหรือ Rate Limit เข้มงวด ต้องรอการอนุมัติอย่างเป็นทางการ\n4: มี SDK หรือ Open API สาธารณะพร้อมเอกสารครบถ้วน แต่ไม่สามารถแก้ไขสถาปัตยกรรมระดับล่างได้\n5: สถาปัตยกรรมเปิดสมบูรณ์ (Open Source/Open HW) ทีมงานมีสิทธิ์ระดับ Root/Admin เต็มรูปแบบ",
                "score": 4,
                "weight": 0.04,
                "evidence": "solution-details/solution-4.md lines 33-36; open-source ROS2 LiDAR drivers, Point Cloud Library (PCL), and open SLAM repositories (FAST-LIO, Cartographer) provide rich open developer access.",
                "descope": "Rely strictly on standard ROS2 Humble packages on Ubuntu 22.04 LTS."
            },
            {
                "id": "T-03",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับความพร้อมทางเทคโนโลยี (Base Performance / TRL) ในสภาพแวดล้อมจริงของท่อระบายน้ำใต้ดิน?",
                "rationale": "วัดวุฒิภาวะของเทคโนโลยีว่าผ่านการพิสูจน์ในสภาพแวดล้อมใต้ดินที่มีความชื้น สารกัดกร่อน หรือน้ำขังจริงแล้วหรือไม่",
                "rubric": "1: ระดับแนวคิด/สมการคณิตศาสตร์ (TRL 2–3) ทดสอบเฉพาะในห้องทดลองที่ควบคุมสภาพแวดล้อมได้\n2: เบรดบอร์ดทำงานได้ในแล็บ (TRL 4) สายไฟเปราะบาง ยังไม่ผ่านการสอบเทียบในสภาพแวดล้อมจริง\n3: ตัวต้นแบบประกอบลงกล่อง (TRL 5–6) ผ่านการทดสอบในสภาพแวดล้อมจำลอง ต้องมีคนคอยดูแล\n4: ต้นแบบระดับพรีโปรดักชัน (TRL 7) ทำงานได้อย่างมีเสถียรภาพในสภาพแวดล้อมปฏิบัติงานจริง\n5: ผลิตภัณฑ์เชิงพาณิชย์สมบูรณ์ (TRL 8–9) ผ่านการรับรองมาตรฐาน มีค่า MTBF ยืนยันความทนทาน",
                "score": 2,
                "weight": 0.04,
                "evidence": "solution-details/solution-4.md lines 15, 43-45; With water depth <=20%, laser scans upper 80% pipe headspace clearly. However, 905nm infrared laser beams suffer total specular absorption/reflection on dark wastewater puddle surfaces, leaving a blind floor segment requiring mathematical interpolation (TRL 4).",
                "descope": "Test LiDAR in dry PVC drainage pipes first to establish geometric ground truth before introducing water."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความเข้ากันได้ของทีม (Manpower & Skill Redundancy) ด้านวิศวกรรมเฉพาะทาง?",
                "rationale": "ประเมินความเสี่ยงกรณีขาดแคลนบุคลากรที่มีความเชี่ยวชาญเฉพาะด้าน (Bus Factor) ว่ามีคนทำงานทดแทนกันได้หรือไม่",
                "rubric": "1: ขาดแคลนทักษะเฉพาะด้านโดยสิ้นเชิง (ไม่มีใครในทีมมีความรู้ในเทคโนโลยีหลักนี้เลย)\n2: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (Bus Factor = 1) หากคนนี้ไม่อยู่ โครงการจะหยุดชะงักทันที\n3: มีผู้รับผิดชอบหลัก 1 คน และมีผู้ช่วยที่พอเข้าใจระบบ แต่ยังแก้ไขปัญหาเชิงลึกแทนไม่ได้\n4: มีทักษะทดแทนกันได้ (Primary & Secondary) อย่างน้อย 2 คนสามารถสลับงานกันได้อย่างราบรื่น\n5: สมาชิกทุกคนในทีมมีทักษะระดับสูง ทำงานแทนกันได้ทันที และมีเอกสารคู่มือการทำงานครบถ้วน",
                "score": 3,
                "weight": 0.04,
                "evidence": "team-skills/jk.md, fifa.md, due.md; JK is highly competent in ROS2, Linux, C++, and linear algebra for SLAM; Fifa and Due provide mechanical crawler support.",
                "descope": "Pair JK with Kin on ROS2 point cloud subscriber scripts to build redundancy."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันของเส้นทางการเรียนรู้ (Learning Curve) ด้านวิศวกรรมระบบ?",
                "rationale": "ประเมินเวลาและความยากในการเรียนรู้เทคโนโลยีใหม่ ว่าทีมงานสามารถเข้าใจและนำมาใช้ได้ทันเวลาหรือไม่",
                "rubric": "1: เทคโนโลยีใหม่ทั้งหมด ต้องใช้เวลาเรียนรู้เกิน 8 สัปดาห์ และต้องการทักษะคณิตศาสตร์ชั้นสูง\n2: มีแนวคิดซับซ้อน ต้องศึกษาทฤษฎีใหม่ที่ไม่เคยเรียนมาก่อน ใช้เวลาทำความเข้าใจ 4–6 สัปดาห์\n3: ต่อยอดจากพื้นฐานเดิมที่เคยเรียน แต่ต้องเรียนรู้เครื่องมือหรือสถาปัตยกรรมใหม่ ใช้เวลา 2–3 สัปดาห์\n4: เป็นเทคโนโลยีที่คุ้นเคย มีตัวอย่างโค้ดและวงจรอ้างอิงชัดเจน ใช้เวลาปรับตัวเพียง 1 สัปดาห์\n5: ทำงานบนพื้นฐานทักษะประจำวันของทีม ทำได้ทันทีโดยไม่ต้องศึกษาทฤษฎีหรือเครื่องมือเพิ่มเติม",
                "score": 2,
                "weight": 0.04,
                "evidence": "team-skills/jk.md; while JK knows ROS2 and differential equations, tuning 3D LiDAR SLAM in feature-degenerate cylindrical pipe tunnels requires extensive point cloud filtering and IMU tightly-coupled odometry.",
                "descope": "Use a 2D LiDAR with wheel odometry in Cartographer rather than full 3D non-linear ICP optimization."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (Payback Period / Value Horizon) ของระบบ?",
                "rationale": "ประเมินผลตอบแทนทางเศรษฐศาสตร์และการลดต้นทุนการขุดลอกท่อระบายน้ำของหน่วยงานรัฐ",
                "rubric": "1: ระยะเวลาคืนทุนเกิน 7 ปี หรือต้นทุนการดำเนินงานสูงกว่ามูลค่าความเสียหายที่ป้องกันได้\n2: ระยะเวลาคืนทุน 5–7 ปี ให้ผลตอบแทนทางอ้อมเป็นหลัก และมีความไม่แน่นอนทางการเงินสูง\n3: ระยะเวลาคืนทุน 3–5 ปี มีความคุ้มค่าระดับปานกลาง จำเป็นต้องได้รับการอุดหนุนงบประมาณจากรัฐ\n4: ระยะเวลาคืนทุน 1–3 ปี ประหยัดค่าใช้จ่ายการซ่อมบำรุงเชิงแก้ไขได้อย่างชัดเจน คุ้มค่าสูง\n5: คืนทุนได้ภายใน 1 ปีแรก ลดต้นทุนการบำรุงรักษาได้ทันที และสร้างมูลค่าเพิ่มทางตรงอย่างมหาศาล",
                "score": 3,
                "weight": 0.0667,
                "evidence": "solution-details/solution-4.md lines 6-10, 38-40; produces millimeter-accurate 3D CAD models of pipe deformation and sediment volume, delivering moderate 3-5 year payback for specialized structural asset management.",
                "descope": "Highlight 3D deformation inspection value for structural rehabilitation contractors."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระดับการพึ่งพาชิ้นส่วนและผู้จัดจำหน่ายภายนอก (Component Dependency & Vendor Lock-in)?",
                "rationale": "ประเมินความเสี่ยงด้านห่วงโซ่อุปทานและการผูกขาดชิ้นส่วน ป้องกันระบบล่มสลายจากผู้ผลิตรายเดียว",
                "rubric": "1: ผูกขาดโดยผู้ผลิตรายเดียว (Sole Source) ชิ้นส่วนสั่งทำพิเศษ ขาดตลาดง่าย นำเข้ายาก\n2: มีผู้จัดจำหน่าย 2 ราย แต่ชิ้นส่วนมีราคาสูง ใช้เวลาจัดส่งนานเกิน 4 สัปดาห์ และไม่มีอะไหล่ทดแทน\n3: ชิ้นส่วนมาตรฐานแต่มีบางโมดูลต้องสั่งนำเข้า มีระยะเวลารอคอย 2–3 สัปดาห์\n4: ใช้ชิ้นส่วนมาตรฐานอุตสาหกรรม (COTS) มีผู้ขายในประเทศหลายราย จัดหาทดแทนได้ใน 3–5 วัน\n5: อะไหล่หาง่ายทั่วไปตามร้านค้าอุปกรณ์อิเล็กทรอนิกส์ในประเทศ ซื้อทดแทนได้ทันทีภายใน 24 ชม.",
                "score": 3,
                "weight": 0.0667,
                "evidence": "solution-details/solution-4.md lines 33-36; dependent on specialized solid-state 3D LiDAR hardware (Livox/Velodyne) and high-performance embedded GPU SBCs.",
                "descope": "Ensure chosen LiDAR brand has an active Thai distributor or readily available university lab loan units."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "สัดส่วนงบประมาณสำรองความเสียหาย (Scrap Margin / Safety Allowance) ของชิ้นส่วน?",
                "rationale": "ตรวจสอบความปลอดภัยทางการเงินกรณีทำอุปกรณ์เสียหายระหว่างการทดลองในน้ำเสีย",
                "rubric": "1: ไม่มีงบสำรองเลย หากชิ้นส่วนพังโครงการจะหยุดชะงักทันที (ราคาชิ้นส่วนเท่ากับงบประมาณทั้งหมด)\n2: งบสำรองรองรับการเสียหายได้ไม่เกิน 1 ครั้ง ชิ้นส่วนสำคัญไม่มีอะไหล่สำรอง\n3: มีงบสำรอง 20–30% ซื้อชิ้นส่วนราคาปานกลางสำรองได้ แต่ไม่มีอะไหล่สำหรับโมดูลหลักราคาแพง\n4: มีงบสำรอง 50% มีชิ้นส่วนหลักและไอซีสำคัญสำรองอย่างน้อย 2–3 ชุด ทดลองได้อย่างมั่นใจ\n5: งบประมาณเหลือเฟือ ชิ้นส่วนราคาถูกมาก สามารถซื้อชุดสำรองแบบสมบูรณ์ได้เกิน 3 ชุดขึ้นไป",
                "score": 1,
                "weight": 0.0666,
                "evidence": "team-skills/due.md, fifa.md; 3D LiDAR sensor (25,000–35,000 THB) + Jetson SBC exhausts 100% of student team funding; zero budget exists for replacement if the sensor is damaged or dropped into sewage, triggering a fatal scrap margin flaw.",
                "descope": "CRITICAL DE-SCOPING REQUIRED: Downscale from 3D LiDAR to a low-cost rotating 2D LiDAR (3,000–5,000 THB, e.g. RPLiDAR) or borrow lab sensor to avoid fatal budget exhaustion."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมาย (Legal 2.4)",
                "question": "ความสอดคล้องกับกฎหมายความปลอดภัยสาธารณะและการจราจร (Regulatory & Public Safety Compliance)?",
                "rationale": "ประเมินความเสี่ยงการละเมิดกฎหมายควบคุมอาคาร ระเบียบงานทาง และข้อบังคับการจราจรขณะปฏิบัติงาน",
                "rubric": "1: เสี่ยงต่อการกระทำผิดกฎหมายอาญา ละเมิด พ.ร.บ. ทางหลวงอย่างร้ายแรง และไม่มีทางขออนุญาตได้\n2: ต้องขออนุญาตปิดการจราจรช่องทางหลัก เสี่ยงต่ออุบัติเหตุร้ายแรง และมีขั้นตอนอนุมัติยาวนาน\n3: ต้องขออนุญาตทำงานในเขตทางสาธารณะ แต่เป็นงานขนาดเล็ก ใช้กรวยจราจรและป้ายเตือนชั่วคราว\n4: ปฏิบัติงานบนทางเท้าหรือขอบทางได้โดยไม่กีดขวางการจราจร สอดคล้องตามระเบียบงานสาธารณูปโภค\n5: ไม่กระทบต่อการจราจรและพื้นที่สาธารณะเลย ปฏิบัติการเสร็จสิ้นในเวลารวดเร็วโดยไม่ต้องขออนุญาตพิเศษ",
                "score": 2,
                "weight": 0.075,
                "evidence": "solution-details/solution-4.md lines 18, 27-28; requires opening public road manhole covers and deploying crawler tether stations, necessitating formal municipal permits and safety lane closures.",
                "descope": "Conduct all field tests inside university closed drainage networks."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมาย (Legal 2.4)",
                "question": "ทรัพย์สินทางปัญญา ลิขสิทธิ์ซอฟต์แวร์ และสิทธิบัตร (IP & Software Licensing)?",
                "rationale": "ตรวจสอบความปลอดภัยด้านสิทธิบัตรเพื่อป้องกันการถูกฟ้องร้องละเมิดทรัพย์สินทางปัญญา",
                "rubric": "1: ละเมิดสิทธิบัตรที่ยังมีผลคุ้มครองอย่างชัดเจน หรือใช้ซอฟต์แวร์ผิดสัญญาอนุญาตทางการค้า\n2: มีความคลุมเครือด้านสิทธิบัตร มีความเสี่ยงที่จะถูกฟ้องร้องจากเจ้าของเทคโนโลยีเดิม\n3: ใช้ไลบรารีที่มีสัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น AGPL) ซึ่งบังคับให้ต้องเปิดเผยซอร์สโค้ดทั้งหมด\n4: ซอฟต์แวร์และฮาร์ดแวร์อยู่ภายใต้สัญญาอนุญาตแบบเสรี (Permissive License เช่น MIT, BSD, Apache 2.0)\n5: เทคโนโลยีเป็นสาธารณสมบัติ (Public Domain) สิทธิบัตรหมดอายุแล้ว หรือสร้างสรรค์ขึ้นใหม่ทั้งหมด",
                "score": 5,
                "weight": 0.075,
                "evidence": "solution-details/solution-4.md lines 33-36; ROS2 (Apache 2.0), Point Cloud Library (BSD), and FAST-LIO2 (GPL/BSD) are completely open source for academic research and prototyping.",
                "descope": "Comply with standard open-source academic citation guidelines."
            },
            {
                "id": "O-01",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบต่อระบบหากเกิดความล้มเหลวขณะปฏิบัติงาน (Operational Failure Impact)?",
                "rationale": "ประเมินความรุนแรงของผลกระทบกรณีระบบขัดข้อง ว่าทำให้อุดตันท่อหรือระบบระบายน้ำเสียหายหรือไม่",
                "rubric": "1: อุปกรณ์ติดค้างในท่อกลายเป็นสิ่งกีดขวางทางน้ำอย่างถาวร ต้องทุบถนนขุดลอกท่อเพื่อเก็บกู้\n2: การขัดข้องทำให้ระบบประเมินค่าผิดพลาดจนส่งผลให้เกิดน้ำท่วมขัง และการเก็บกู้ต้องใช้เครื่องมือหนัก\n3: อุปกรณ์หยุดทำงานแต่สามารถดึงสายสลิงเก็บกู้ได้ง่าย โดยไม่ส่งผลกระทบต่อการไหลของน้ำ\n4: ระบบขัดข้องเฉพาะบางเซนเซอร์ ยังสามารถประเมินผลเบื้องต้นได้ และเก็บกู้ได้ทันทีโดยสลักนิรภัย\n5: ทำงานจากผิวดินแบบ Fail-Safe 100% หากระบบหยุดทำงานก็ไม่มีชิ้นส่วนใดค้างอยู่ในท่อระบายน้ำ",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 43-45; crawler stuck in sewage requires manual recovery; laser optical glass easily smudged by splashing wastewater slurry, requiring aborting scan run.",
                "descope": "Install an emergency mechanical pull-cord and sacrificial protective film over the LiDAR optical window."
            },
            {
                "id": "O-02",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมผู้ใช้และสภาพหน้างานจริง (User Behavior & Problem-Solution Fit)?",
                "rationale": "ประเมินความสะดวกของเจ้าหน้าที่หน้างาน ว่าระบบใช้งานง่ายและตอบสนองขั้นตอนการทำงานจริงหรือไม่",
                "rubric": "1: ขัดแย้งกับขั้นตอนการทำงานเดิมโดยสิ้นเชิง เจ้าหน้าที่ปฏิเสธการใช้งานเพราะยุ่งยากและอันตราย\n2: ต้องใช้เวลาฝึกอบรมเจ้าหน้าที่นานเกิน 4 สัปดาห์ และต้องปรับเปลี่ยนขั้นตอนการทำงานเกือบทั้งหมด\n3: เจ้าหน้าที่ยอมรับได้แต่ต้องมีขั้นตอนพิเศษเพิ่มเติม เช่น การต่อสายไฟและตั้งค่าหน้างานหลายขั้นตอน\n4: ใช้งานง่าย สอดคล้องกับขั้นตอนการตรวจท่อปกติ เจ้าหน้าที่เรียนรู้การทำงานได้ภายใน 1 วัน\n5: ใช้งานได้ทันทีโดยไม่ต้องเปลี่ยนพฤติกรรมเดิม (Zero-learning curve) ออกแบบตามสรีรศาสตร์หน้างาน",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 44-45; generates massive 3D point cloud files (.pcd/.ply) requiring GIS/CAD engineering expertise to interpret, creating operational workflow friction for field maintenance crews.",
                "descope": "Build an automated python script that converts dense point clouds into a single 2D blockage percentage profile."
            },
            {
                "id": "O-03",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนเชิงบริหารของนักพัฒนา (Administrative & Lab Dependency)?",
                "rationale": "ประเมินความคล่องตัวในการพัฒนา ว่าต้องรอการอนุมัติหรือติดขัดการใช้ห้องแล็บเฉพาะทางหรือไม่",
                "rubric": "1: ต้องใช้ห้องปฏิบัติการพิเศษที่มีการควบคุมความปลอดภัยสูง ต้องทำเรื่องขออนุมัติล่วงหน้าหลายสัปดาห์\n2: พึ่งพาเครื่องจักรหนักในช็อปวิศวกรรม มีคิวรอใช้งานยาวนาน และเข้าใช้งานได้เฉพาะเวลาทำการ\n3: ต้องการพื้นที่ทดสอบจำลองขนาดใหญ่ในแล็บ แต่สามารถจัดสรรเวลาทำงานร่วมกับทีมอื่นได้\n4: ใช้อุปกรณ์ในแล็บทั่วไป มีความพร้อมใช้งานสูง และสามารถนำกลับไปทดสอบต่อที่หอพักได้\n5: พัฒนาและทดสอบได้ทุกที่อย่างอิสระ ไม่ต้องพึ่งพาห้องแล็บหรือการอนุมัติเชิงบริหารใดๆ ทั้งสิ้น",
                "score": 3,
                "weight": 0.05,
                "evidence": "team-skills/due.md, jk.md; requires access to FIBO robotics lab GPU workstations for point cloud processing and mechanical workshop for crawler chassis mounting.",
                "descope": "Use cloud GPU or personal gaming laptops with CUDA support for point cloud compilation."
            },
            {
                "id": "O-04",
                "pillar": "ด้านปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประมวลผลและการเตรียมระบบ (Step Count & Pipeline Friction)?",
                "rationale": "วัดจำนวนขั้นตอนและความยุ่งยากในการเตรียมระบบก่อนเริ่มใช้งานจริง",
                "rubric": "1: มีขั้นตอนซับซ้อนเกิน 10 ขั้นตอน ต้องปรับเทียบเซนเซอร์และต่อสายสัญญาณยุ่งยากหน้างาน\n2: มีขั้นตอน 7–10 ขั้นตอน ต้องใช้คอมพิวเตอร์ตั้งโต๊ะและอุปกรณ์เสริมหลายชิ้นในการเริ่มระบบ\n3: มีขั้นตอน 4–6 ขั้นตอน ต้องเชื่อมต่อสายสัญญาณและเปิดโปรแกรมตามลำดับที่กำหนด\n4: มีขั้นตอน 2–3 ขั้นตอน เพียงเปิดสวิตช์และกดปุ่มเริ่มทำงาน ระบบจะปรับเทียบตัวเองโดยอัตโนมัติ\n5: ทำงานแบบสัมผัสเดียว (One-Touch Operation) เสียบปลั๊ก/เปิดเครื่องแล้วเริ่มประมวลผลได้ทันที",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 27-36, 44-45; multi-stage setup: ROS2 network configuration, high-bandwidth sensor tethering, IMU extrinsic calibration, and point cloud registration pipeline.",
                "descope": "Pre-configure systemd service on SBC to launch ROS2 LiDAR launchfile automatically on boot."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงาน (Schedule 2.6)",
                "question": "ความพร้อมของระบบและการส่งมอบต้นแบบภายในกรอบเวลา 5 สัปดาห์ทำงาน (Design Maturity & Schedule Compliance)?",
                "rationale": "ประเมินความเป็นไปได้ในการสร้าง ทดสอบ และส่งมอบต้นแบบวิศวกรรมให้เสร็จทันกำหนด 5 สัปดาห์",
                "rubric": "1: ไม่สามารถทำเสร็จได้ทันใน 5 สัปดาห์แน่นอน ต้องใช้เวลาพัฒนาอย่างน้อย 10–12 สัปดาห์ขึ้นไป\n2: มีความเสี่ยงสูงมากที่จะล่าช้า งานวิจัยและพัฒนาชิ้นส่วนกลไกอาจกินเวลาเกินกว่า 6 สัปดาห์\n3: มีความเป็นไปได้แต่ตึงเครียดมาก ต้องทำงานล่วงเวลาและตัดทอนฟังก์ชันย่อยบางส่วนออก\n4: มีความเป็นไปได้สูง แผนงานสอดคล้องกับศักยภาพทีม มีเวลาทดสอบระบบรวมอย่างน้อย 1 สัปดาห์\n5: มั่นใจว่าเสร็จสมบูรณ์ก่อนกำหนด มีต้นแบบที่ทำงานได้ในสัปดาห์ที่ 3 และมีเวลาปรับแต่งอย่างเต็มที่",
                "score": 2,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; integrating crawler chassis + LiDAR drivers + SLAM calibration inside symmetrical cylindrical pipe tunnels within 5 business weeks during exam blackout is highly compressed.",
                "descope": "Eliminate online SLAM mapping; log raw point clouds to bagfile and run offline reconstruction."
            },
            {
                "id": "SDG-01",
                "pillar": "ความยั่งยืน (SDGs 2.7)",
                "question": "ผลกระทบต่อสิ่งแวดล้อม สังคม และเศรษฐกิจตามกรอบ SDG Wedding Cake (Biosphere, Society, Economy)?",
                "rationale": "ประเมินคุณค่าที่แท้จริงต่อเป้าหมายการพัฒนาที่ยั่งยืน 3 ชั้น ป้องกันการสร้างภาพลักษณ์สีเขียว (Greenwashing)",
                "rubric": "1: สร้างภาพลักษณ์สีเขียวโดยไม่มีผลกระทบเชิงประจักษ์ (Greenwashing) หรือไม่ตอบโจทย์ SDG ชั้นใดเลย\n2: ตอบโจทย์เฉพาะชั้นเศรษฐกิจหรือสังคมอย่างผิวเผิน แต่ไม่มีผลกระทบต่อการอนุรักษ์ชีวมณฑล (Biosphere)\n3: มีผลกระทบเชิงบวกที่ชัดเจนใน 1 มิติ (เช่น ป้องกันน้ำท่วมในมิติสังคม หรือลดขยะในมิติชีวมณฑล)\n4: บูรณาการอย่างเข้มแข็งข้าม 2 มิติ (เช่น ชีวมณฑลด้านการจัดการน้ำ ร่วมกับสังคมเมืองที่ปลอดภัย)\n5: บูรณาการครบทั้ง 3 ชั้นของ SDG Wedding Cake: ชีวมณฑล (น้ำสะอาด) + สังคม (เมืองยั่งยืน) + เศรษฐกิจ (คุ้มค่า)",
                "score": 4,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 6-10; strongly integrates Biosphere (SDG 6.3 preventing drainage blockage) and Society (SDG 11.5 urban infrastructure protection and flood resilience).",
                "descope": "Quantify municipal infrastructure life extension from precision 3D deformation modeling."
            },
            {
                "id": "SDG-02",
                "pillar": "ความยั่งยืน (SDGs 2.7)",
                "question": "รอยเท้าสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และระบบเก็บกู้ที่ปลอดภัย (Environmental Footprint & E-Waste Safeguards)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 43; tethered crawler prevents hardware loss, but expensive LiDAR and embedded SBC risk electronic scrap loss if compromised by corrosive sewer humidity.",
                "descope": "Install moisture detection sensors inside the sealed crawler electronics pod to abort mission before water damage."
            }
        ]
    }
]

os.makedirs("feasibility-outcome", exist_ok=True)
json_path = os.path.join("feasibility-outcome", "jury_eval_data.json")

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[SUCCESS] Updated jury evaluation data saved with {len(data)} solutions (sorted by score):")
for s in data:
    tot = sum((q["score"]/5.0)*q["weight"]*100 for q in s["assessment_data"])
    rob = s.get("robotic_data", {}).get("score", 0)
    has_fatal = any(q["score"] == 1 for q in s["assessment_data"])
    print(f"  {s['sheet_title']} -> TELOS+S: {tot:.2f}% | Robotic: {rob:.1f}/12 | Fatal Flaw: {has_fatal}")
