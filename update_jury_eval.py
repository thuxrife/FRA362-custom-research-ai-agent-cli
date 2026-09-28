import os
import json

data = [
    {
        "sheet_title": "Solution_1_CCTV_Crawler",
        "concept": "Pipe Inspection Robot using CCTV for profiling pipe (4K PTZ Camera + YOLOv8 Wheeled Crawler)",
        "strength": "ให้ภาพวิดีโอความละเอียดสูง (HD/4K) ภายในท่อจริง พร้อมโมเดล AI (YOLOv8) ตรวจจับรอยแตกร้าว รอยรั่ว และสิ่งอุดตันได้โดยอัตโนมัติ",
        "bottleneck": "ต้องใช้หุ่นยนต์ลงไปสัมผัสน้ำเสียในท่อจริง การกันน้ำระดับ IP68 ทำได้ยาก มีความเสี่ยงหุ่นยนต์ติดค้าง/สาย Tether พันกันในท่อ (O-01=3), และต้องใช้เวลาสร้างระบบกลไกกันน้ำสูงเกินกรอบเวลา 5 สัปดาห์ (S-01=2)",
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
                "evidence": "solution-details/solution-1.md lines 40-49; CCTV pipe crawling is established commercially (TRL 8-9), but custom student crawler with YOLOv8 in murky sewer conditions operates at TRL 5-6 (prototype in simulated pipe).",
                "descope": "Conduct bench testing in a dry simulated 300mm PVC pipe before advancing to damp mock-up drainage channels."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความพร้อมและกำลังคนสำรองของทีมงาน (Team Compatibility & Redundancy / Anti-SPOF)?",
                "rationale": "ตรวจสอบความเสี่ยงคอขวดบุคลากร (Single Point of Failure) ป้องกันไม่ให้โครงการหยุดชะงักหากผู้รับผิดชอบหลักไม่ว่าง",
                "rubric": "1: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (SPOF) หากไม่อยู่ โครงการหยุดชะงัก 100%\n2: มีหัวหน้าโครงการ 1 คน และมีผู้ช่วยเข้าใจทฤษฎีแต่แก้โค้ดหรือซ่อมฮาร์ดแวร์แทนไม่ได้\n3: มีคู่หลัก-รอง (Primary + Secondary) สามารถแก้ไขปัญหาและดูแลระบบแทนกันได้\n4: สมาชิกตั้งแต่ 3 คนขึ้นไปสามารถร่วมพัฒนา ประกอบ และแก้ไขปัญหาระบบได้โดยตรง\n5: สมาชิกทุกคนในทีมมีความเชี่ยวชาญเต็มรูปแบบ สามารถสลับงานแทนกันได้ทันทีอย่างไร้รอยต่อ",
                "score": 3,
                "weight": 0.04,
                "evidence": "team-skills/due.md, fifa.md, jk.md, kin.md; Fifa and Due form a primary/secondary mechanical/chassis pair, while JK and Kin form a primary/secondary AI/streaming pair.",
                "descope": "Standardize motor driver pinouts and ROS2 messaging so that Due and JK can cross-debug embedded code seamlessly."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันในการเรียนรู้และเวลาปรับตัวของทีมงาน (Learning Curve & Ramp-up Time)?",
                "rationale": "ประเมินเวลาที่ทีมต้องใช้ในการเรียนรู้เครื่องมือหรือทฤษฎีใหม่ เพื่อไม่ให้กระทบต่อกำหนดการส่งมอบ 5 สัปดาห์",
                "rubric": "1: ต้องเริ่มเรียนรู้ใหม่จากศูนย์ 100% ทั้งเครื่องมือ ภาษา และฮาร์ดแวร์ที่ไม่เคยใช้งานมาก่อน\n2: มีพื้นฐานทฤษฎีแต่ขาดประสบการณ์จริง การติดตั้งและแก้บั๊กเบื้องต้นใช้เวลานานและติดขัด\n3: มีความเชี่ยวชาญในเทคโนโลยีใกล้เคียง สามารถปรับตัวและเรียนรู้เพิ่มเติมได้ภายใน 1 สัปดาห์\n4: คุ้นเคยกับเทคโนโลยีหลักอยู่แล้ว เพียงแค่เรียนรู้ไลบรารีหรือการตั้งค่าเฉพาะเพิ่มเติมเล็กน้อย\n5: สามารถดึงโค้ดเก่า วงจรที่เคยทำ และประสบการณ์เดิมมาใช้งานได้ทันทีโดยไม่ต้องเรียนรู้ใหม่",
                "score": 3,
                "weight": 0.04,
                "evidence": "team-skills/fifa.md, jk.md; team has proven experience in ROS2, OpenCV, and 3D CAD, but waterproofing dynamic rotary wheel shafts and tuning long tether signal integrity requires a 1-week learning ramp-up.",
                "descope": "Use off-the-shelf industrial magnetic rotary couplers or pre-sealed brushless underwater thrusters/motors."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (ROI / Payback Period) เทียบกับการขุดลอกแบบสุ่ม?",
                "rationale": "วัดความคุ้มค่าทางการเงินและการประหยัดงบประมาณการลอกท่อของหน่วยงานภาครัฐเทียบกับ Baseline เดิม",
                "rubric": "1: ระยะเวลาคืนทุนนานมาก (≥ 10 ปี) ต้นทุนเริ่มแรกสูงมากและแทบไม่มีผลประหยัดค่าใช้จ่าย\n2: ระยะเวลาคืนทุนช้า (6–9 ปี) ใช้เงินลงทุนสูง ต้องอาศัยเงินอุดหนุนระยะยาวจึงจะคุ้มทุน\n3: ระยะเวลาคืนทุนปานกลาง (3–5 ปี) ช่วยประหยัดค่าใช้จ่ายการปฏิบัติการในรอบปีงบประมาณปกติ\n4: ระยะเวลาคืนทุนเร็ว (2–3 ปี) ลดค่าใช้จ่ายปฏิบัติการ (ค่าน้ำมัน แรงงาน เครื่องจักร) ได้อย่างมีนัยสำคัญ\n5: คืนทุนทันที (≤ 1–2 ปี) ลดความสูญเสียจากน้ำท่วมและตัดรอบการลอกท่อที่ไม่จำเป็นได้ตั้งแต่ปีแรก",
                "score": 3,
                "weight": 0.0667,
                "evidence": "solution-details/solution-1.md lines 6-7, 43; condition-based visual inspection prevents unneeded jetting of 30-40% clean pipes, delivering moderate 3-5 year payback across municipal sewer maintenance cycles.",
                "descope": "Focus reporting on high-priority clogged segments to maximize fuel and labor savings per inspection run."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "การพึ่งพาผู้จำหน่ายและการผูกขาดชิ้นส่วนเฉพาะ (Component Dependency & Vendor Lock-in)?",
                "rationale": "ตรวจสอบความเสี่ยงจากการพึ่งพาผู้ขายรายเดียว การผูกขาดชิ้นส่วนนำเข้า หรือค่าลิขสิทธิ์ซอฟต์แวร์รายปี",
                "rubric": "1: ผูกขาดกับระบบปิด 100% ต้องใช้คลาวด์ หัวต่อ หรือเซนเซอร์เฉพาะจากผู้ผลิตรายเดียวเท่านั้น\n2: พึ่งพาผู้ผลิตสูง ต้องใช้เครื่องมือตรวจวินิจฉัยเฉพาะหรือเสียค่าธรรมเนียมรายปีเพื่อใช้งาน\n3: กึ่งอิสระ ฮาร์ดแวร์หลักเป็นระบบปิดแต่รองรับการส่งออกข้อมูลแบบเปิดและใช้อินเทอร์เฟซมาตรฐาน\n4: มีความเป็นอิสระสูง ใช้โปรโตคอลสื่อสารมาตรฐาน (Modbus, MQTT, CAN) หาอะไหล่เทียบได้ง่าย\n5: เป็นอิสระสมบูรณ์ 100% ใช้อุปกรณ์มาตรฐานทั่วไป สามารถซ่อมบำรุงและเปลี่ยนอะไหล่ได้เอง",
                "score": 4,
                "weight": 0.0667,
                "evidence": "solution-details/solution-1.md lines 32-38; uses standard COTS DC gearmotors, standard USB/IP camera modules, generic LED drivers, and open communication protocols.",
                "descope": "Avoid proprietary camera protocols; use open standard RTSP/UVC drivers for camera interchangeability."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "วงเงินงบประมาณสำรองความเสียหายและการทำซ้ำ (Scrap Margin & Iteration Allowance)?",
                "rationale": "ประเมินขีดความสามารถในการรับมือกับความเสียหายของอุปกรณ์และชิปที่อาจช็อตหรือเสียหายระหว่างการพัฒนา",
                "rubric": "1: งบประมาณสำรอง 0% (ซื้อชุดเดียวพอดี) หากชิปไหม้หรืออุปกรณ์เสียหาย โครงการจะหยุดชะงักทันที\n2: งบประมาณสำรอง 20–30% สำรองได้เฉพาะชิ้นส่วนพาสซีฟราคาถูก ไม่มีอะไหล่สำหรับเซนเซอร์หลัก\n3: งบประมาณสำรอง 50% มีชิ้นส่วนพาสซีฟสำรองครบ และมีบอร์ดควบคุมหลักสำรอง 1 ชุด\n4: งบประมาณสำรอง 80% มีอะไหล่สำรองเกือบครบทุกชิ้นส่วน รองรับการทดสอบพัง (Burn-in) ได้หลายรอบ\n5: มีความพร้อมสำรองสมบูรณ์ (≥ 100%) งบประมาณครอบคลุมการสร้างตัวต้นแบบที่ทำงานได้ 2 ชุดพร้อมกัน",
                "score": 2,
                "weight": 0.0666,
                "evidence": "team-skills/due.md, fifa.md; waterproof crawler chassis, 4K PTZ camera, and high-spec tether cable are relatively costly; budget buffer for spare cameras or fried motor drivers is limited to 20-30%.",
                "descope": "Use lower-cost 1080p wide-angle camera modules (~800 THB) during initial testing to preserve spare budget."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามกฎหมายจราจร ความปลอดภัยในที่อับอากาศ และระเบียบพื้นที่สาธารณะ (Felony, Traffic & Confined Space Compliance)?",
                "rationale": "ตรวจสอบความเสี่ยงต่อการละเมิดกฎหมายจราจร กฎหมายความปลอดภัยในที่อับอากาศ และการปิดกั้นทางสัญจร",
                "rubric": "1: ละเมิดกฎหมายโดยตรง (กีดขวางการจราจรสาธารณะร้ายแรง, ละเมิด PDPA รุนแรง, ส่งคลื่นรบกวนผิดกฎหมาย)\n2: สุ่มเสี่ยงทางกฎหมายสูง อาจถูกร้องเรียนเรื่องปิดกั้นการจราจรหรือความปลอดภัย ต้องขอผ่อนผันซับซ้อน\n3: มีเงื่อนไขทางกฎหมาย ต้องขออนุญาตเปิดฝาท่อและปิดช่องทางจราจรตามระเบียบของหน่วยงานเทศบาล\n4: ผลกระทบทางกฎหมายต่ำ ปฏิบัติตามข้อยกเว้นงานวิศวกรรมสาธารณะทั่วไป ใช้เพียงการแจ้งเตือนความปลอดภัย\n5: ได้รับการยกเว้นสมบูรณ์ 100% ไม่กีดขวางการจราจร ไม่เข้าข่ายที่อับอากาศ ไม่มีการเก็บข้อมูลส่วนบุคคล (Zero PII)",
                "score": 2,
                "weight": 0.075,
                "evidence": "solution-details/solution-1.md lines 18, 27; deploying wheeled crawler requires opening street manhole covers and setting up a stationary tether station on public roads, creating traffic blockage risks requiring municipal permits.",
                "descope": "Deploy strictly on pedestrian sidewalk drainage gutters or campus drainage testbeds to bypass public road traffic permit requirements."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามสัญญาอนุญาต ทรัพย์สินทางปัญญา และโอเพนซอร์ส (IP & Software Licensing Compliance)?",
                "rationale": "ตรวจสอบสิทธิ์การใช้งานซอฟต์แวร์ ไลบรารี และสิทธิบัตร ป้องกันการฟ้องร้องละเมิดลิขสิทธิ์",
                "rubric": "1: ติดสัญญาอนุญาตเชิงพาณิชย์แบบปิด ไม่สามารถคอมไพล์ รัน หรือแจกจ่ายได้หากไม่จ่ายค่าลิขสิทธิ์ราคาแพง\n2: สถานะทรัพย์สินทางปัญญาคลุมเครือ ไม่มีสัญญาอนุญาตระบุชัดเจน เสี่ยงต่อการถูกระงับเมื่อเปิดเผยต่อสาธารณะ\n3: สัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น GPLv3) บังคับให้ต้องเปิดเผยโค้ดทั้งหมดหากมีการแจกจ่าย\n4: สัญญาอนุญาตแบบผ่อนปรน (เช่น LGPL, CC-BY) ใช้งานและห่อหุ้มซอฟต์แวร์ได้โดยมีเงื่อนไขอ้างอิงแหล่งที่มา\n5: โอเพนซอร์สสมบูรณ์ (MIT, Apache 2.0, BSD) หรือ Public Domain ใช้งานและต่อยอดได้อย่างอิสระ 100%",
                "score": 5,
                "weight": 0.075,
                "evidence": "solution-details/solution-1.md lines 35-36; YOLOv8 educational license, OpenCV (Apache 2.0), and ROS2 (Apache 2.0) are fully permissive with zero commercial barrier for academic project delivery.",
                "descope": "Document all open-source licenses in repository attribution headers."
            },
            {
                "id": "O-01",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบและความรุนแรงเมื่อระบบเกิดความขัดข้องหรือติดค้าง (User — Failure Impact & Stuck Hazards)?",
                "rationale": "ประเมินความเสียหายต่อโครงสร้างพื้นฐาน ความปลอดภัยของเจ้าหน้าที่ และการกลายเป็นสิ่งกีดขวางในท่อระบายน้ำ",
                "rubric": "1: เป็นอันตรายต่อชีวิต (ไฟฟ้าดูด เพลิงไหม้ อุบัติเหตุทางถนน สารพิษ หรือโครงสร้างท่อพังทลาย)\n2: ก่อให้เกิดอันตรายทางกายภาพร้ายแรง อุปกรณ์ติดค้างกลายเป็นสิ่งอุดตันท่อ หรือระบบน้ำล้นฉับพลัน\n3: เกิดความสับสนในการปฏิบัติงาน อุปกรณ์ขัดข้องต้องใช้เวลาหลายชั่วโมงในการกู้คืนหรือส่งทีมไปช่วย\n4: เกิดความล่าช้าเล็กน้อย อุปกรณ์ตัดการทำงานอย่างปลอดภัย สามารถกู้คืนได้ตามขั้นตอนมาตรฐาน\n5: ความเสียหายจำกัดเฉพาะงบประมาณ ไม่ส่งผลต่อความปลอดภัยหรือการไหลของน้ำ กู้คืนได้ทันที",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 46-49; if the crawler flips over, gets entangled on tree roots/sludge, or loses power, the tether cable serves as a mechanical tow-line for recovery, but retrieval stalls operations for several hours.",
                "descope": "Integrate a high-tensile steel wire safety core inside the tether cable with a manual emergency hand-winch."
            },
            {
                "id": "O-02",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมเจ้าหน้าที่และขั้นตอนการทำงานเดิม (User — Workflow Friction & Adoption)?",
                "rationale": "ประเมินภาระการฝึกอบรม ความสะดวกในการพกพา และแรงต้านจากเจ้าหน้าที่ภาคสนามของ กทม.",
                "rubric": "1: ขัดขวางขั้นตอนเดิมอย่างรุนแรง บังคับให้เจ้าหน้าที่ต้องเปลี่ยนวิธีทำงานทั้งหมดและกรอกเอกสารเพิ่มมากมาย\n2: มีความฝืดสูง เพิ่มขั้นตอนการทำงานและต้องใช้อุปกรณ์เทอะทะ เจ้าหน้าที่มีแนวโน้มหลีกเลี่ยงการใช้งาน\n3: ต้องปรับตัวปานกลาง ปรับเปลี่ยนขั้นตอนประจำวันเล็กน้อย ต้องฝึกอบรม 1–2 ครั้ง แต่ได้ผลลัพธ์คุ้มค่า\n4: ความฝืดต่ำ บูรณาการเข้ากับเครื่องมือเดิมได้โดยตรง (ส่งค่าเข้า LINE/Dashboard) ปรับพฤติกรรมน้อยมาก\n5: ราบรื่นไร้รอยต่อ 100% ทำงานอัตโนมัติในพื้นหลัง ลดภาระงานเอกสารและการลอกท่อเดิมของเจ้าหน้าที่",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 6-7, 27-30; operators must carry crawler and heavy cable reel, wash sewage off robot after deployment, but benefit from direct visual evidence for work verification.",
                "descope": "Package the system into a ruggedized portable rolling case with an automated one-button cable reel."
            },
            {
                "id": "O-03",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนการขออนุมัติของนักพัฒนา (Developer — Lab & Administrative Gatekeeping)?",
                "rationale": "ประเมินอุปสรรคการเข้าถึงเครื่องมือ ช็อปเครื่องกล หรือการต้องรอคิวอนุมัติเอกสารของมหาวิทยาลัย",
                "rubric": "1: ติดคอขวดขั้นตอนอนุมัติหนัก ห้องแล็บปิด ต้องลงนาม NDA หรือรอจัดซื้ออุปกรณ์หลายสัปดาห์\n2: มีขั้นตอนราชการปานกลาง ต้องส่งแบบฟอร์มจองเครื่องมือล่วงหน้า และรออนุมัติ 3–5 วันทำการ\n3: เข้าถึงได้ตามเวลาทำการปกติของมหาวิทยาลัย มีความล่าช้าเล็กน้อยในการเบิกใช้เครื่องมือเฉพาะทาง\n4: มีอิสระสูง ทีมงานเข้าแล็บได้ตลอด มีสิทธิ์เขียนโค้ดลงบอร์ด และมีงบประมาณย่อยพร้อมใช้งานทันที\n5: พัฒนาได้อย่างอิสระสมบูรณ์ 100% มีระบบ CI/CD บนคลาวด์และพัฒนาชิ้นงานได้เองที่บ้าน/หอพัก",
                "score": 3,
                "weight": 0.05,
                "evidence": "team-skills/due.md, fifa.md; mechanical chassis fabrication requires FIBO workshop 3D printers and water test tank during standard university opening hours.",
                "descope": "Use standard modular 3D printed PETG enclosures assembled with off-the-shelf silicone O-rings."
            },
            {
                "id": "O-04",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประกอบ ติดตั้ง และโปรแกรม (Developer — Setup Steps & Pipeline Friction)?",
                "rationale": "ประเมินจำนวนขั้นตอนและความเปราะบางของเครื่องมือพัฒนา ป้องกันข้อผิดพลาดจากการตั้งค่าระบบที่ซับซ้อนเกินไป",
                "rubric": "1: ซับซ้อนมาก มีขั้นตอนคอมไพล์และตั้งค่าหลายสิบขั้นตอน เสี่ยงต่อข้อผิดพลาดสูงมาก\n2: ความซับซ้อนสูง ต้องใช้เครื่องมือหลายระดับ มีปัญหาความเข้ากันได้ของไลบรารีและแฟลชบอร์ดได้ยาก\n3: ความซับซ้อนปานกลาง มีขั้นตอนประกอบและทดสอบตามคู่มือมาตรฐานที่บันทึกไว้ ทำซ้ำได้ไม่ยาก\n4: ความซับซ้อนต่ำ ใช้สคริปต์อัตโนมัติ IDE มาตรฐาน หรือแฟลชเฟิร์มแวร์ด้วยคำสั่งเดียว\n5: เรียบง่ายและตรงไปตรงมา เป็นระบบ Plug-and-Play ตั้งค่าขั้นตอนเดียวเสร็จสมบูรณ์",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 27-38; multi-stage pipeline involves sealed mechanical assembly, waterproof wiring, high-bandwidth video tethering, and deep learning model inference setup.",
                "descope": "Containerize YOLOv8 and streaming server inside a single Docker image with a 1-click startup script."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงานและเวลา (Schedule 2.6)",
                "question": "วุฒิภาวะของการออกแบบทางวิศวรรกรรมภายในกรอบเวลา 5 สัปดาห์ทำงาน (Engineering Design Maturity by 5 Weeks)?",
                "rationale": "ทดสอบความเป็นไปได้ในการสร้างชิ้นงานให้สำเร็จตามเป้าหมาย TRL โดยหักสัปดาห์สอบมิดเทอมและไฟนอลออกแล้ว",
                "rubric": "1: ระดับแนวคิดเท่านั้น (แบบ 0%) มีเพียงภาพสเก็ตช์ ยังไม่มีโมเดล 3D วงจร หรือเฟิร์มแวร์ใดๆ\n2: แบบร่างเบื้องต้น (แบบ 25%) มีบล็อกไดอะแกรม วงจรร่างมือ รายการชิ้นส่วนที่ยังไม่ยืนยัน และกล่อง 3D คร่าวๆ\n3: วุฒิภาวะปานกลาง (แบบ 50%) แอสเซมบลี CAD ครบ วาดวงจรเสร็จ และวางโครงสร้างเฟิร์มแวร์แล้ว\n4: พร้อมผลิตเบื้องต้น (แบบ 75–80%) ไฟล์ CAD พร้อมพิมพ์ 3D/CNC และไฟล์ PCB Gerber ผ่านการตรวจ DRC\n5: แบบสมบูรณ์พร้อมผลิต 100% มีเอกสารสั่งผลิตครบ พิกัดความเผื่อ CAD แน่นอน และสคริปต์แฟลชพร้อมทำงาน",
                "score": 2,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; designing, machining, waterproofing, and debugging an IP68 motorized crawler chassis with tether winch within 5 active business weeks under university exam blackout constraints represents extreme schedule pressure.",
                "descope": "Adopt a modular COTS chassis baseline immediately in Week 9 to freeze mechanical dimensions before midterm."
            },
            {
                "id": "SDG-01",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "การบูรณาการตามกรอบ Stockholm Wedding Cake (Biosphere, Society, Economy Integration)?",
                "rationale": "ประเมินผลกระทบเชิงบวกที่ครอบคลุมทั้งด้านชีวมณฑล (SDG 6/14), สังคม (SDG 11) และเศรษฐกิจ (SDG 8/12)",
                "rubric": "1: หลุดจากกรอบ Wedding Cake หรือสร้างผลกระทบเชิงลบอย่างรุนแรงต่อสิ่งแวดล้อมหรือสุขอนามัย\n2: สัมผัสเพียง 1 เสาหลักอย่างผิวเผิน ขาดการเชื่อมโยงเชิงประจักษ์ไปยังสังคมหรือสิ่งแวดล้อมจริง\n3: ครอบคลุม 1 เสาหลักอย่างเป็นรูปธรรม หรือเริ่มแตะ 2 เสาหลักแบบมีข้อจำกัดเฉพาะจุด\n4: บูรณาการ 2 เสาหลักสำคัญอย่างมีนัยสำคัญ (เช่น Biosphere + Society) พร้อมตัวชี้วัดรองรับ\n5: บูรณาการครบทั้ง 3 เสาหลักของ Wedding Cake อย่างสมบูรณ์ (Biosphere, Society, Economy)",
                "score": 4,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 6-10; strongly addresses Biosphere (SDG 6.3 preventing sewage backup into urban canals) and Society (SDG 11.5 urban flood resilience and pedestrian road safety).",
                "descope": "Incorporate automated reporting of plastic debris volume to support circular waste collection metrics."
            },
            {
                "id": "SDG-02",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "ผลกระทบสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และหลักเศรษฐกิจหมุนเวียน (E-Waste & 'Do No Harm' — SDG 6.3/12.4)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-1.md lines 47; physical tether prevents total hardware loss, but sewage moisture, grease, and H2S gas cause rapid wear and electronic corrosion over repeated deployments.",
                "descope": "Conformal coat all internal electronics with silicone/polyurethane moisture barrier to extend hardware lifespan."
            }
        ]
    },
    {
        "sheet_title": "Solution_2_Acoustic_Reflectometry",
        "concept": "Pipe Inspection Instrument using Acoustic Reflectometry (Airborne Acoustic Inversion + SL-RAT EPA USA Cleanliness Scale)",
        "strength": "ตรวจประเมินท่อจากผิวดินได้อย่างรวดเร็ว (3–5 นาทีต่อช่วงท่อ) โดยไม่ต้องปล่อยหุ่นยนต์ลงไปสัมผัสน้ำเสีย ใช้พลังงานต่ำ ต้นทุนอุปกรณ์ต่ำมาก และไม่มีความเสี่ยงเรื่องอุปกรณ์ติดค้างในท่อ",
        "bottleneck": "ไม่สามารถทำงานได้ในสภาวะที่น้ำท่วมเต็มท่อระบายน้ำ (Airspace ปิดกั้น) และไม่ได้ภาพ 3D เรขาคณิตของผิวท่อ",
        "advice": "พัฒนาท่อส่งคลื่นเสียงแบบ Telescoping Pole ที่สามารถปรับระดับความลึกตามปากท่อได้ พร้อมบันทึกพิกัด GPS อัตโนมัติเพื่อเชื่อมต่อแผนที่ระบบท่อของ กทม.",
        "robotic_compatibility": {
            "score": 8.5,
            "domains": {
                "perception": "Score 3.5/4.0: Active airborne acoustic reflectometry transducer, swept-sine/chirp acoustic wave excitation, and precision condenser microphone array capturing acoustic impulse response.",
                "control_algorithms": "Score 3.5/4.0: Digital signal processing (DSP), acoustic energy attenuation deconvolution, spectral bandpass filtering, and automated 0-10 EPA SL-RAT cleanliness score generation.",
                "actuation_mechanics": "Score 1.5/4.0: High-output acoustic compression driver transducer with telescoping manhole deployment rig; non-mobile surface-operated payload."
            },
            "fibo_alignment_rationale": "Solution 2 represents an advanced non-destructive testing (NDT) acoustic instrumentation payload with deep digital signal processing, acoustic wave physics modeling, and automated scoring classification, closely aligning with FIBO instrumentation and embedded DSP curriculum."
        },
        "robotic_data": {
            "score": 8.5,
            "domains": {
                "perception": "Score 3.5/4.0: Active airborne acoustic reflectometry transducer, swept-sine/chirp acoustic wave excitation, and precision condenser microphone array capturing acoustic impulse response.",
                "control_algorithms": "Score 3.5/4.0: Digital signal processing (DSP), acoustic energy attenuation deconvolution, spectral bandpass filtering, and automated 0-10 EPA SL-RAT cleanliness score generation.",
                "actuation_mechanics": "Score 1.5/4.0: High-output acoustic compression driver transducer with telescoping manhole deployment rig; non-mobile surface-operated payload."
            },
            "fibo_alignment_rationale": "Solution 2 represents an advanced non-destructive testing (NDT) acoustic instrumentation payload with deep digital signal processing, acoustic wave physics modeling, and automated scoring classification, closely aligning with FIBO instrumentation and embedded DSP curriculum."
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
                "descope": "Use 3D printed acoustic waveguide horns and standard off-the-shelf portable telescoping painter poles."
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
                "descope": "Implement standard swept-sine excitation and bandpass filtering using open-source Python SciPy signal libraries."
            },
            {
                "id": "T-03",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับความพร้อมทางเทคโนโลยี (Base Performance / TRL) ในสภาพแวดล้อมจริงของท่อระบายน้ำใต้ดิน?",
                "rationale": "วัดวุฒิภาวะของเทคโนโลยีว่าผ่านการพิสูจน์ในสภาพแวดล้อมใต้ดินที่มีความชื้น สารกัดกร่อน หรือน้ำขังจริงแล้วหรือไม่",
                "rubric": "1: ระดับแนวคิด/สมการคณิตศาสตร์ (TRL 2–3) ทดสอบเฉพาะในห้องทดลองที่ควบคุมสภาพแวดล้อมได้\n2: เบรดบอร์ดทำงานได้ในแล็บ (TRL 4) สายไฟเปราะบาง ยังไม่ผ่านการสอบเทียบในสภาพแวดล้อมจริง\n3: ตัวต้นแบบประกอบลงกล่อง (TRL 5–6) ผ่านการทดสอบในสภาพแวดล้อมจำลอง ต้องมีคนคอยดูแล\n4: ต้นแบบระดับพรีโปรดักชัน (TRL 7) ทำงานได้อย่างมีเสถียรภาพในสภาพแวดล้อมปฏิบัติงานจริง\n5: ผลิตภัณฑ์เชิงพาณิชย์สมบูรณ์ (TRL 8–9) ผ่านการรับรองมาตรฐาน มีค่า MTBF ยืนยันความทนทาน",
                "score": 3,
                "weight": 0.04,
                "evidence": "solution-details/solution-2.md lines 31, 38-42; Acoustic inspection (SL-RAT) is an EPA-verified commercial standard (TRL 7-8) worldwide. However, in Bangkok's combined sewer system with permanent 10-30% dry-weather standing water, custom student prototype operates at TRL 5-6 requiring water-level compensation baseline calibration.",
                "descope": "Calibrate swept-sine frequency band (500 Hz - 4 kHz) with water surface boundary reflection baseline in simulated pipe test rig."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความพร้อมและกำลังคนสำรองของทีมงาน (Team Compatibility & Redundancy / Anti-SPOF)?",
                "rationale": "ตรวจสอบความเสี่ยงคอขวดบุคลากร (Single Point of Failure) ป้องกันไม่ให้โครงการหยุดชะงักหากผู้รับผิดชอบหลักไม่ว่าง",
                "rubric": "1: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (SPOF) หากไม่อยู่ โครงการหยุดชะงัก 100%\n2: มีหัวหน้าโครงการ 1 คน และมีผู้ช่วยเข้าใจทฤษฎีแต่แก้โค้ดหรือซ่อมฮาร์ดแวร์แทนไม่ได้\n3: มีคู่หลัก-รอง (Primary + Secondary) สามารถแก้ไขปัญหาและดูแลระบบแทนกันได้\n4: สมาชิกตั้งแต่ 3 คนขึ้นไปสามารถร่วมพัฒนา ประกอบ และแก้ไขปัญหาระบบได้โดยตรง\n5: สมาชิกทุกคนในทีมมีความเชี่ยวชาญเต็มรูปแบบ สามารถสลับงานแทนกันได้ทันทีอย่างไร้รอยต่อ",
                "score": 4,
                "weight": 0.04,
                "evidence": "team-skills/due.md, jk.md, kin.md; Due has verified hardware experience building MAX98357 audio amp & ESP32 circuits; JK handles DSP math & Fourier analysis; Kin handles data ingestion & scoring backend.",
                "descope": "Due leads hardware assembly while JK and Kin develop audio playback and signal processing scripts in parallel."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันในการเรียนรู้และเวลาปรับตัวของทีมงาน (Learning Curve & Ramp-up Time)?",
                "rationale": "ประเมินเวลาที่ทีมต้องใช้ในการเรียนรู้เครื่องมือหรือทฤษฎีใหม่ เพื่อไม่ให้กระทบต่อกำหนดการส่งมอบ 5 สัปดาห์",
                "rubric": "1: ต้องเริ่มเรียนรู้ใหม่จากศูนย์ 100% ทั้งเครื่องมือ ภาษา และฮาร์ดแวร์ที่ไม่เคยใช้งานมาก่อน\n2: มีพื้นฐานทฤษฎีแต่ขาดประสบการณ์จริง การติดตั้งและแก้บั๊กเบื้องต้นใช้เวลานานและติดขัด\n3: มีความเชี่ยวชาญในเทคโนโลยีใกล้เคียง สามารถปรับตัวและเรียนรู้เพิ่มเติมได้ภายใน 1 สัปดาห์\n4: คุ้นเคยกับเทคโนโลยีหลักอยู่แล้ว เพียงแค่เรียนรู้ไลบรารีหรือการตั้งค่าเฉพาะเพิ่มเติมเล็กน้อย\n5: สามารถดึงโค้ดเก่า วงจรที่เคยทำ และประสบการณ์เดิมมาใช้งานได้ทันทีโดยไม่ต้องเรียนรู้ใหม่",
                "score": 4,
                "weight": 0.04,
                "evidence": "team-skills/due.md, jk.md; team has built audio amplifiers and implemented DSP bandpass filtering in previous projects; ramp-up only requires configuring I2S audio sampling and attenuation lookup tables.",
                "descope": "Reuse Due's verified ESP32 I2S audio driver code from past embedded projects directly."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (ROI / Payback Period) เทียบกับการขุดลอกแบบสุ่ม?",
                "rationale": "วัดความคุ้มค่าทางการเงินและการประหยัดงบประมาณการลอกท่อของหน่วยงานภาครัฐเทียบกับ Baseline เดิม",
                "rubric": "1: ระยะเวลาคืนทุนนานมาก (≥ 10 ปี) ต้นทุนเริ่มแรกสูงมากและแทบไม่มีผลประหยัดค่าใช้จ่าย\n2: ระยะเวลาคืนทุนช้า (6–9 ปี) ใช้เงินลงทุนสูง ต้องอาศัยเงินอุดหนุนระยะยาวจึงจะคุ้มทุน\n3: ระยะเวลาคืนทุนปานกลาง (3–5 ปี) ช่วยประหยัดค่าใช้จ่ายการปฏิบัติการในรอบปีงบประมาณปกติ\n4: ระยะเวลาคืนทุนเร็ว (2–3 ปี) ลดค่าใช้จ่ายปฏิบัติการ (ค่าน้ำมัน แรงงาน เครื่องจักร) ได้อย่างมีนัยสำคัญ\n5: คืนทุนทันที (≤ 1–2 ปี) ลดความสูญเสียจากน้ำท่วมและตัดรอบการลอกท่อที่ไม่จำเป็นได้ตั้งแต่ปีแรก",
                "score": 4,
                "weight": 0.0667,
                "evidence": "solution-details/solution-2.md lines 6-7, 38; 2-person crew inspects 2–3 km/day in under 3 minutes per segment. In Bangkok context, covers ~65-75% of gravity lateral drainage networks (excluding 100% submerged siphon lines), achieving fast payback in 2-3 years.",
                "descope": "Prioritize deployment on roadside gravity laterals to maximize ROI before storm season."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "การพึ่งพาผู้จำหน่ายและการผูกขาดชิ้นส่วนเฉพาะ (Component Dependency & Vendor Lock-in)?",
                "rationale": "ตรวจสอบความเสี่ยงจากการพึ่งพาผู้ขายรายเดียว การผูกขาดชิ้นส่วนนำเข้า หรือค่าลิขสิทธิ์ซอฟต์แวร์รายปี",
                "rubric": "1: ผูกขาดกับระบบปิด 100% ต้องใช้คลาวด์ หัวต่อ หรือเซนเซอร์เฉพาะจากผู้ผลิตรายเดียวเท่านั้น\n2: พึ่งพาผู้ผลิตสูง ต้องใช้เครื่องมือตรวจวินิจฉัยเฉพาะหรือเสียค่าธรรมเนียมรายปีเพื่อใช้งาน\n3: กึ่งอิสระ ฮาร์ดแวร์หลักเป็นระบบปิดแต่รองรับการส่งออกข้อมูลแบบเปิดและใช้อินเทอร์เฟซมาตรฐาน\n4: มีความเป็นอิสระสูง ใช้โปรโตคอลสื่อสารมาตรฐาน (Modbus, MQTT, CAN) หาอะไหล่เทียบได้ง่าย\n5: เป็นอิสระสมบูรณ์ 100% ใช้อุปกรณ์มาตรฐานทั่วไป สามารถซ่อมบำรุงและเปลี่ยนอะไหล่ได้เอง",
                "score": 5,
                "weight": 0.0667,
                "evidence": "solution-details/solution-2.md lines 33-36; 100% generic electronic and acoustic components (compression driver speaker, condenser mic, ESP32); self-serviceable by any engineer with zero proprietary vendor lock-in.",
                "descope": "Maintain bill of materials strictly with generic electronic parts purchasable across multiple local vendors."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "วงเงินงบประมาณสำรองความเสียหายและการทำซ้ำ (Scrap Margin & Iteration Allowance)?",
                "rationale": "ประเมินขีดความสามารถในการรับมือกับความเสียหายของอุปกรณ์และชิปที่อาจช็อตหรือเสียหายระหว่างการพัฒนา",
                "rubric": "1: งบประมาณสำรอง 0% (ซื้อชุดเดียวพอดี) หากชิปไหม้หรืออุปกรณ์เสียหาย โครงการจะหยุดชะงักทันที\n2: งบประมาณสำรอง 20–30% สำรองได้เฉพาะชิ้นส่วนพาสซีฟราคาถูก ไม่มีอะไหล่สำหรับเซนเซอร์หลัก\n3: งบประมาณสำรอง 50% มีชิ้นส่วนพาสซีฟสำรองครบ และมีบอร์ดควบคุมหลักสำรอง 1 ชุด\n4: งบประมาณสำรอง 80% มีอะไหล่สำรองเกือบครบทุกชิ้นส่วน รองรับการทดสอบพัง (Burn-in) ได้หลายรอบ\n5: มีความพร้อมสำรองสมบูรณ์ (≥ 100%) งบประมาณครอบคลุมการสร้างตัวต้นแบบที่ทำงานได้ 2 ชุดพร้อมกัน",
                "score": 4,
                "weight": 0.0666,
                "evidence": "team-skills/due.md; total hardware BOM for audio driver, mic capsule, amplifier, and ESP32 is very low (< 3,000 THB total), allowing the team to purchase 3x full sets of backup components comfortably.",
                "descope": "Order 3 sets of ESP32 and audio breakout boards in a single batch to safeguard against bench testing mishaps."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามกฎหมายจราจร ความปลอดภัยในที่อับอากาศ และระเบียบพื้นที่สาธารณะ (Felony, Traffic & Confined Space Compliance)?",
                "rationale": "ตรวจสอบความเสี่ยงต่อการละเมิดกฎหมายจราจร กฎหมายความปลอดภัยในที่อับอากาศ และการปิดกั้นทางสัญจร",
                "rubric": "1: ละเมิดกฎหมายโดยตรง (กีดขวางการจราจรสาธารณะร้ายแรง, ละเมิด PDPA รุนแรง, ส่งคลื่นรบกวนผิดกฎหมาย)\n2: สุ่มเสี่ยงทางกฎหมายสูง อาจถูกร้องเรียนเรื่องปิดกั้นการจราจรหรือความปลอดภัย ต้องขอผ่อนผันซับซ้อน\n3: มีเงื่อนไขทางกฎหมาย ต้องขออนุญาตเปิดฝาท่อและปิดช่องทางจราจรตามระเบียบของหน่วยงานเทศบาล\n4: ผลกระทบทางกฎหมายต่ำ ปฏิบัติตามข้อยกเว้นงานวิศวกรรมสาธารณะทั่วไป ใช้เพียงการแจ้งเตือนความปลอดภัย\n5: ได้รับการยกเว้นสมบูรณ์ 100% ไม่กีดขวางการจราจร ไม่เข้าข่ายที่อับอากาศ ไม่มีการเก็บข้อมูลส่วนบุคคล (Zero PII)",
                "score": 3,
                "weight": 0.075,
                "evidence": "solution-details/solution-2.md lines 27-29; requires opening manhole covers for 3 minutes from sidewalk/road edge; rapid turnaround substantially lowers traffic impact compared to rovers, but requires standard municipal maintenance protocol.",
                "descope": "Conduct initial field verification on university campus manholes with faculty permission."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามสัญญาอนุญาต ทรัพย์สินทางปัญญา และโอเพนซอร์ส (IP & Software Licensing Compliance)?",
                "rationale": "ตรวจสอบสิทธิ์การใช้งานซอฟต์แวร์ ไลบรารี และสิทธิบัตร ป้องกันการฟ้องร้องละเมิดลิขสิทธิ์",
                "rubric": "1: ติดสัญญาอนุญาตเชิงพาณิชย์แบบปิด ไม่สามารถคอมไพล์ รัน หรือแจกจ่ายได้หากไม่จ่ายค่าลิขสิทธิ์ราคาแพง\n2: สถานะทรัพย์สินทางปัญญาคลุมเครือ ไม่มีสัญญาอนุญาตระบุชัดเจน เสี่ยงต่อการถูกระงับเมื่อเปิดเผยต่อสาธารณะ\n3: สัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น GPLv3) บังคับให้ต้องเปิดเผยโค้ดทั้งหมดหากมีการแจกจ่าย\n4: สัญญาอนุญาตแบบผ่อนปรน (เช่น LGPL, CC-BY) ใช้งานและห่อหุ้มซอฟต์แวร์ได้โดยมีเงื่อนไขอ้างอิงแหล่งที่มา\n5: โอเพนซอร์สสมบูรณ์ (MIT, Apache 2.0, BSD) หรือ Public Domain ใช้งานและต่อยอดได้อย่างอิสระ 100%",
                "score": 5,
                "weight": 0.075,
                "evidence": "solution-details/solution-2.md lines 31, 34-36; EPA SL-RAT acoustic inspection methodology and mathematical attenuation formulations are in the public domain and widely published in academic literature; open-source SciPy algorithms.",
                "descope": "Cite EPA research documentation and standard acoustic wave attenuation references in the project report."
            },
            {
                "id": "O-01",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบและความรุนแรงเมื่อระบบเกิดความขัดข้องหรือติดค้าง (User — Failure Impact & Stuck Hazards)?",
                "rationale": "ประเมินความเสียหายต่อโครงสร้างพื้นฐาน ความปลอดภัยของเจ้าหน้าที่ และการกลายเป็นสิ่งกีดขวางในท่อระบายน้ำ",
                "rubric": "1: เป็นอันตรายต่อชีวิต (ไฟฟ้าดูด เพลิงไหม้ อุบัติเหตุทางถนน สารพิษ หรือโครงสร้างท่อพังทลาย)\n2: ก่อให้เกิดอันตรายทางกายภาพร้ายแรง อุปกรณ์ติดค้างกลายเป็นสิ่งอุดตันท่อ หรือระบบน้ำล้นฉับพลัน\n3: เกิดความสับสนในการปฏิบัติงาน อุปกรณ์ขัดข้องต้องใช้เวลาหลายชั่วโมงในการกู้คืนหรือส่งทีมไปช่วย\n4: เกิดความล่าช้าเล็กน้อย อุปกรณ์ตัดการทำงานอย่างปลอดภัย สามารถกู้คืนได้ตามขั้นตอนมาตรฐาน\n5: ความเสียหายจำกัดเฉพาะงบประมาณ ไม่ส่งผลต่อความปลอดภัยหรือการไหลของน้ำ กู้คืนได้ทันที",
                "score": 5,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 27-29, 39; system operates strictly from the surface above the wastewater line; if battery dies or audio fails, the operator simply pulls up the pole; zero risk of blocking pipe.",
                "descope": "Add a simple LED status indicator and battery voltage buzzer to alert operators when battery is low."
            },
            {
                "id": "O-02",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมเจ้าหน้าที่และขั้นตอนการทำงานเดิม (User — Workflow Friction & Adoption)?",
                "rationale": "ประเมินภาระการฝึกอบรม ความสะดวกในการพกพา และแรงต้านจากเจ้าหน้าที่ภาคสนามของ กทม.",
                "rubric": "1: ขัดขวางขั้นตอนเดิมอย่างรุนแรง บังคับให้เจ้าหน้าที่ต้องเปลี่ยนวิธีทำงานทั้งหมดและกรอกเอกสารเพิ่มมากมาย\n2: มีความฝืดสูง เพิ่มขั้นตอนการทำงานและต้องใช้อุปกรณ์เทอะทะ เจ้าหน้าที่มีแนวโน้มหลีกเลี่ยงการใช้งาน\n3: ต้องปรับตัวปานกลาง ปรับเปลี่ยนขั้นตอนประจำวันเล็กน้อย ต้องฝึกอบรม 1–2 ครั้ง แต่ได้ผลลัพธ์คุ้มค่า\n4: ความฝืดต่ำ บูรณาการเข้ากับเครื่องมือเดิมได้โดยตรง (ส่งค่าเข้า LINE/Dashboard) ปรับพฤติกรรมน้อยมาก\n5: ราบรื่นไร้รอยต่อ 100% ทำงานอัตโนมัติในพื้นหลัง ลดภาระงานเอกสารและการลอกท่อเดิมของเจ้าหน้าที่",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 27-31, 41-42; Lightweight handheld poles take < 3 minutes per manhole pair, but field crews must follow a simple triage protocol: deploy on gravity pipes with air headspace and avoid 100% submerged inverted siphons.",
                "descope": "Include a 1-page visual decision chart for field crews to verify manhole water level before acoustic transmission."
            },
            {
                "id": "O-03",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนการขออนุมัติของนักพัฒนา (Developer — Lab & Administrative Gatekeeping)?",
                "rationale": "ประเมินอุปสรรคการเข้าถึงเครื่องมือ ช็อปเครื่องกล หรือการต้องรอคิวอนุมัติเอกสารของมหาวิทยาลัย",
                "rubric": "1: ติดคอขวดขั้นตอนอนุมัติหนัก ห้องแล็บปิด ต้องลงนาม NDA หรือรอจัดซื้ออุปกรณ์หลายสัปดาห์\n2: มีขั้นตอนราชการปานกลาง ต้องส่งแบบฟอร์มจองเครื่องมือล่วงหน้า และรออนุมัติ 3–5 วันทำการ\n3: เข้าถึงได้ตามเวลาทำการปกติของมหาวิทยาลัย มีความล่าช้าเล็กน้อยในการเบิกใช้เครื่องมือเฉพาะทาง\n4: มีอิสระสูง ทีมงานเข้าแล็บได้ตลอด มีสิทธิ์เขียนโค้ดลงบอร์ด และมีงบประมาณย่อยพร้อมใช้งานทันที\n5: พัฒนาได้อย่างอิสระสมบูรณ์ 100% มีระบบ CI/CD บนคลาวด์และพัฒนาชิ้นงานได้เองที่บ้าน/หอพัก",
                "score": 5,
                "weight": 0.05,
                "evidence": "team-skills/due.md, jk.md; audio circuitry and DSP code development can be tested entirely on dorm/lab bench using PVC pipe sections with zero machine shop gatekeeping.",
                "descope": "Construct a 6-meter PVC pipe test rig on bench for rapid acoustic calibration."
            },
            {
                "id": "O-04",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประกอบ ติดตั้ง และโปรแกรม (Developer — Setup Steps & Pipeline Friction)?",
                "rationale": "ประเมินจำนวนขั้นตอนและความเปราะบางของเครื่องมือพัฒนา ป้องกันข้อผิดพลาดจากการตั้งค่าระบบที่ซับซ้อนเกินไป",
                "rubric": "1: ซับซ้อนมาก มีขั้นตอนคอมไพล์และตั้งค่าหลายสิบขั้นตอน เสี่ยงต่อข้อผิดพลาดสูงมาก\n2: ความซับซ้อนสูง ต้องใช้เครื่องมือหลายระดับ มีปัญหาความเข้ากันได้ของไลบรารีและแฟลชบอร์ดได้ยาก\n3: ความซับซ้อนปานกลาง มีขั้นตอนประกอบและทดสอบตามคู่มือมาตรฐานที่บันทึกไว้ ทำซ้ำได้ไม่ยาก\n4: ความซับซ้อนต่ำ ใช้สคริปต์อัตโนมัติ IDE มาตรฐาน หรือแฟลชเฟิร์มแวร์ด้วยคำสั่งเดียว\n5: เรียบง่ายและตรงไปตรงมา เป็นระบบ Plug-and-Play ตั้งค่าขั้นตอนเดียวเสร็จสมบูรณ์",
                "score": 4,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 27-36; straightforward transmitter-receiver setup with standard ESP32 Arduino/PlatformIO toolchain and automated signal analysis script.",
                "descope": "Use a single PlatformIO configuration file with automated library dependency management."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงานและเวลา (Schedule 2.6)",
                "question": "วุฒิภาวะของการออกแบบทางวิศวกรรมภายในกรอบเวลา 5 สัปดาห์ทำงาน (Engineering Design Maturity by 5 Weeks)?",
                "rationale": "ทดสอบความเป็นไปได้ในการสร้างชิ้นงานให้สำเร็จตามเป้าหมาย TRL โดยหักสัปดาห์สอบมิดเทอมและไฟนอลออกแล้ว",
                "rubric": "1: ระดับแนวคิดเท่านั้น (แบบ 0%) มีเพียงภาพสเก็ตช์ ยังไม่มีโมเดล 3D วงจร หรือเฟิร์มแวร์ใดๆ\n2: แบบร่างเบื้องต้น (แบบ 25%) มีบล็อกไดอะแกรม วงจรร่างมือ รายการชิ้นส่วนที่ยังไม่ยืนยัน และกล่อง 3D คร่าวๆ\n3: วุฒิภาวะปานกลาง (แบบ 50%) แอสเซมบลี CAD ครบ วาดวงจรเสร็จ และวางโครงสร้างเฟิร์มแวร์แล้ว\n4: พร้อมผลิตเบื้องต้น (แบบ 75–80%) ไฟล์ CAD พร้อมพิมพ์ 3D/CNC และไฟล์ PCB Gerber ผ่านการตรวจ DRC\n5: แบบสมบูรณ์พร้อมผลิต 100% มีเอกสารสั่งผลิตครบ พิกัดความเผื่อ CAD แน่นอน และสคริปต์แฟลชพร้อมทำงาน",
                "score": 4,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; electronic schematics and acoustic software can be finalized in 2 weeks; breadboard PoC achievable before midterm with production testing in Weeks 11-13.",
                "descope": "Lock acoustic horn 3D print dimensions by Week 9 to allow parallel firmware and DSP development."
            },
            {
                "id": "SDG-01",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "การบูรณาการตามกรอบ Stockholm Wedding Cake (Biosphere, Society, Economy Integration)?",
                "rationale": "ประเมินผลกระทบเชิงบวกที่ครอบคลุมทั้งด้านชีวมณฑล (SDG 6/14), สังคม (SDG 11) และเศรษฐกิจ (SDG 8/12)",
                "rubric": "1: หลุดจากกรอบ Wedding Cake หรือสร้างผลกระทบเชิงลบอย่างรุนแรงต่อสิ่งแวดล้อมหรือสุขอนามัย\n2: สัมผัสเพียง 1 เสาหลักอย่างผิวเผิน ขาดการเชื่อมโยงเชิงประจักษ์ไปยังสังคมหรือสิ่งแวดล้อมจริง\n3: ครอบคลุม 1 เสาหลักอย่างเป็นรูปธรรม หรือเริ่มแตะ 2 เสาหลักแบบมีข้อจำกัดเฉพาะจุด\n4: บูรณาการ 2 เสาหลักสำคัญอย่างมีนัยสำคัญ (เช่น Biosphere + Society) พร้อมตัวชี้วัดรองรับ\n5: บูรณาการครบทั้ง 3 เสาหลักของ Wedding Cake อย่างสมบูรณ์ (Biosphere, Society, Economy)",
                "score": 5,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 6-10; completely unites Biosphere (SDG 6.3 preventing sewer blockages and dirty overflow), Society (SDG 11.5 urban flood mitigation), and Economy (SDG 8.2 & 12.2 optimizing municipal maintenance resources).",
                "descope": "Include carbon footprint reduction calculation resulting from avoided diesel jetting truck runs."
            },
            {
                "id": "SDG-02",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "ผลกระทบสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และหลักเศรษฐกิจหมุนเวียน (E-Waste & 'Do No Harm' — SDG 6.3/12.4)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 5,
                "weight": 0.05,
                "evidence": "solution-details/solution-2.md lines 38-40; 100% fail-safe surface retrieval; zero electronic components or toxic batteries enter wastewater; ultra-low power consumption with rechargeable lithium cells.",
                "descope": "Use recyclable PETG casing and standardized rechargeable 18650 battery cells."
            }
        ]
    },
    {
        "sheet_title": "Solution_3_Sonar_Profiling",
        "concept": "Pipe Inspection Instrument using Sonar Frequency Profiling attaching with Robot (360° Underwater Sonar Scan + Floater/Crawler)",
        "strength": "สามารถส่งคลื่นความถี่อัลตราโซนิกทะลุน้ำเสียและโคลนตม เพื่อสแกนโครงสร้างหน้าตัดท่อแบบ 360 องศา และตรวจวัดปริมาณตะกอนใต้ผิวน้ำได้โดยตรง",
        "bottleneck": "ต้องสร้างหรือจัดซื้อหัว Sonar 360° สำหรับสแกนใต้น้ำที่มีราคาสูงมาก (> 100,000 THB) เกินงบประมาณ (E-03=1), ไม่มีสมาชิกที่มีทักษะสร้างวงจรขับ Piezo ใต้น้ำ (T-04=1), ต้องเรียนรู้ใหม่จากศูนย์ (T-05=1), และใช้เวลาสร้างเกินกรอบเวลา 5 สัปดาห์ (S-01=1)",
        "advice": "ยกเลิกการพัฒนาหัวสแกน Sonar 360° ใต้น้ำขึ้นเองชั่วคราว หรือเปลี่ยนไปใช้ระบบ Acoustic Reflectometry ผ่านช่องว่างอากาศ (Solution 2) หรือเซนเซอร์วัดระยะแบบจุดเดียวบนทุ่นลอย",
        "robotic_compatibility": {
            "score": 10.5,
            "domains": {
                "perception": "Score 4.0/4.0: High-frequency 360° rotating underwater acoustic transducer scanning polar cross-sections through turbid slurry with millimeter time-of-flight resolution.",
                "control_algorithms": "Score 3.5/4.0: Acoustic backscatter signal processing, polar-to-Cartesian scan conversion, and 3D geometric cross-section loss calculation.",
                "actuation_mechanics": "Score 3.0/4.0: Continuous 360° rotating transducer scan head paired with motorized winch cable rig or submersible crawler platform."
            },
            "fibo_alignment_rationale": "Solution 3 represents an exemplary deep robotics sensing system with rotating acoustic transducers and underwater cross-sectional profiling, but exceeds student fabrication and budget reality."
        },
        "robotic_data": {
            "score": 10.5,
            "domains": {
                "perception": "Score 4.0/4.0: High-frequency 360° rotating underwater acoustic transducer scanning polar cross-sections through turbid slurry with millimeter time-of-flight resolution.",
                "control_algorithms": "Score 3.5/4.0: Acoustic backscatter signal processing, polar-to-Cartesian scan conversion, and 3D geometric cross-section loss calculation.",
                "actuation_mechanics": "Score 3.0/4.0: Continuous 360° rotating transducer scan head paired with motorized winch cable rig or submersible crawler platform."
            },
            "fibo_alignment_rationale": "Solution 3 represents an exemplary deep robotics sensing system with rotating acoustic transducers and underwater cross-sectional profiling, but exceeds student fabrication and budget reality."
        },
        "assessment_data": [
            {
                "id": "T-01",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับการสร้างเองเทียบกับการซื้อสำเร็จรูป (Build vs. Buy Burden) ของสถาปัตยกรรมระบบตรวจประเมินท่อระบายน้ำ?",
                "rationale": "ประเมินภาระการวิจัยและพัฒนาชิ้นส่วนกลไก อิเล็กทรอนิกส์ และอัลกอริทึม ป้องกันการเสียเวลากับงานประดิษฐ์ขึ้นใหม่โดยไม่จำเป็น",
                "rubric": "1: ต้องวิจัยและสร้างขึ้นเองทั้งหมด 100% (ไม่มีพิมพ์เขียว อัลกอริทึม หรือไลบรารีอ้างอิง)\n2: มีชิ้นส่วนหลักในท้องตลาด แต่ต้องดัดแปลงโครงสร้างอย่างหนักและเขียนโค้ดเชื่อมต่อเองทั้งหมด\n3: บูรณาการชิ้นส่วน COTS เข้ากับแท่นยึดแบบกำหนดเอง และเขียนโค้ดเชื่อมต่อบางส่วน\n4: ประกอบจากโมดูลมาตรฐานสำเร็จรูป (DIN-rail, I2C/CAN shields) มีงานประกอบกลไกเล็กน้อย\n5: ซื้อมาติดตั้งใช้งานได้ทันที (Plug-and-Play) ไม่ต้องตัดกลึงหรือบัดกรีวงจรเพิ่มเติม",
                "score": 1,
                "weight": 0.04,
                "evidence": "solution-details/solution-3.md lines 27-36, 43-45; 360° underwater scanning sonar heads require custom waterproof acoustic matching layers, high-voltage piezo pulse generators, slip-rings, and TGC analog frontends with zero open reference designs, triggering a fatal flaw VETO.",
                "descope": "Descope from continuous rotating underwater sonar to fixed single-point ultrasonic depth echo sounders."
            },
            {
                "id": "T-02",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "สิทธิ์ในการเข้าถึงเทคโนโลยี ซอฟต์แวร์ และระบบนิเวศข้อมูล (Access & Permissions) ของระบบตรวจประเมินท่อ?",
                "rationale": "ตรวจสอบข้อจำกัดด้านกรรมสิทธิ์ การล็อกสิทธิ์ใช้งาน และการอนุญาตเข้าถึง เพื่อป้องกันการพัฒนาระบบบนฐานข้อมูลที่ไม่สามารถเข้าถึงได้จริง",
                "rubric": "1: ล็อกสิทธิ์ภายใต้สัญญา NDA ระบบปิด ติดไฟร์วอลล์องค์กร หรือไม่มีสิทธิ์เข้าถึงฝั่งนักพัฒนา\n2: ซอฟต์แวร์หรือเฟิร์มแวร์กรรมสิทธิ์ปิด ทำงานแบบ Black-box โดยไม่มี Source Code หรือ Telemetry\n3: บัญชีเพื่อการศึกษา/ทดลองใช้ที่มีโควตาหรือ Rate Limit เข้มงวด ต้องรอการอนุมัติอย่างเป็นทางการ\n4: มี SDK หรือ Open API สาธารณะพร้อมเอกสารครบถ้วน แต่ไม่สามารถแก้ไขสถาปัตยกรรมระดับล่างได้\n5: สถาปัตยกรรมเปิดสมบูรณ์ (Open Source/Open HW) ทีมงานมีสิทธิ์ระดับ Root/Admin เต็มรูปแบบ",
                "score": 2,
                "weight": 0.04,
                "evidence": "solution-details/solution-3.md lines 33-36; commercial sewer sonar profilers operate on closed binary telemetry protocols with encrypted raw backscatter logs; open drivers are nonexistent.",
                "descope": "Use generic analog hydrophones with open ADC logging on microcontrollers."
            },
            {
                "id": "T-03",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับความพร้อมทางเทคโนโลยี (Base Performance / TRL) ในสภาพแวดล้อมจริงของท่อระบายน้ำใต้ดิน?",
                "rationale": "วัดวุฒิภาวะของเทคโนโลยีว่าผ่านการพิสูจน์ในสภาพแวดล้อมใต้ดินที่มีความชื้น สารกัดกร่อน หรือน้ำขังจริงแล้วหรือไม่",
                "rubric": "1: ระดับแนวคิด/สมการคณิตศาสตร์ (TRL 2–3) ทดสอบเฉพาะในห้องทดลองที่ควบคุมสภาพแวดล้อมได้\n2: เบรดบอร์ดทำงานได้ในแล็บ (TRL 4) สายไฟเปราะบาง ยังไม่ผ่านการสอบเทียบในสภาพแวดล้อมจริง\n3: ตัวต้นแบบประกอบลงกล่อง (TRL 5–6) ผ่านการทดสอบในสภาพแวดล้อมจำลอง ต้องมีคนคอยดูแล\n4: ต้นแบบระดับพรีโปรดักชัน (TRL 7) ทำงานได้อย่างมีเสถียรภาพในสภาพแวดล้อมปฏิบัติงานจริง\n5: ผลิตภัณฑ์เชิงพาณิชย์สมบูรณ์ (TRL 8–9) ผ่านการรับรองมาตรฐาน มีค่า MTBF ยืนยันความทนทาน",
                "score": 2,
                "weight": 0.04,
                "evidence": "solution-details/solution-3.md lines 40, 45; high acoustic attenuation, suspended organic matter, grease layers, and multi-path reflections inside dirty wastewater create substantial signal degradation at breadboard level (TRL 4).",
                "descope": "Test sonar transducers strictly in clean water bench tanks with artificial sediment steps."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความพร้อมและกำลังคนสำรองของทีมงาน (Team Compatibility & Redundancy / Anti-SPOF)?",
                "rationale": "ตรวจสอบความเสี่ยงคอขวดบุคลากร (Single Point of Failure) ป้องกันไม่ให้โครงการหยุดชะงักหากผู้รับผิดชอบหลักไม่ว่าง",
                "rubric": "1: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (SPOF) หากไม่อยู่ โครงการหยุดชะงัก 100%\n2: มีหัวหน้าโครงการ 1 คน และมีผู้ช่วยเข้าใจทฤษฎีแต่แก้โค้ดหรือซ่อมฮาร์ดแวร์แทนไม่ได้\n3: มีคู่หลัก-รอง (Primary + Secondary) สามารถแก้ไขปัญหาและดูแลระบบแทนกันได้\n4: สมาชิกตั้งแต่ 3 คนขึ้นไปสามารถร่วมพัฒนา ประกอบ และแก้ไขปัญหาระบบได้โดยตรง\n5: สมาชิกทุกคนในทีมมีความเชี่ยวชาญเต็มรูปแบบ สามารถสลับงานแทนกันได้ทันทีอย่างไร้รอยต่อ",
                "score": 1,
                "weight": 0.04,
                "evidence": "team-skills/due.md, fifa.md, jk.md, kin.md; zero team members have experience in underwater acoustic transducer design, piezoelectric matching circuits, or submersible slip-ring mechanisms, creating a fatal manpower deficit.",
                "descope": "Engage faculty acoustic research labs or pivot to airborne reflectometry where Due and JK have verified competence."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันในการเรียนรู้และเวลาปรับตัวของทีมงาน (Learning Curve & Ramp-up Time)?",
                "rationale": "ประเมินเวลาที่ทีมต้องใช้ในการเรียนรู้เครื่องมือหรือทฤษฎีใหม่ เพื่อไม่ให้กระทบต่อกำหนดการส่งมอบ 5 สัปดาห์",
                "rubric": "1: ต้องเริ่มเรียนรู้ใหม่จากศูนย์ 100% ทั้งเครื่องมือ ภาษา และฮาร์ดแวร์ที่ไม่เคยใช้งานมาก่อน\n2: มีพื้นฐานทฤษฎีแต่ขาดประสบการณ์จริง การติดตั้งและแก้บั๊กเบื้องต้นใช้เวลานานและติดขัด\n3: มีความเชี่ยวชาญในเทคโนโลยีใกล้เคียง สามารถปรับตัวและเรียนรู้เพิ่มเติมได้ภายใน 1 สัปดาห์\n4: คุ้นเคยกับเทคโนโลยีหลักอยู่แล้ว เพียงแค่เรียนรู้ไลบรารีหรือการตั้งค่าเฉพาะเพิ่มเติมเล็กน้อย\n5: สามารถดึงโค้ดเก่า วงจรที่เคยทำ และประสบการณ์เดิมมาใช้งานได้ทันทีโดยไม่ต้องเรียนรู้ใหม่",
                "score": 1,
                "weight": 0.04,
                "evidence": "team-skills/due.md, jk.md; designing an underwater rotating sonar head, impedance matching circuitry, and polar-to-Cartesian reconstruction from scratch requires starting from total reset (Score 1).",
                "descope": "Pivot to standard open-source audio DSP architectures."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (ROI / Payback Period) เทียบกับการขุดลอกแบบสุ่ม?",
                "rationale": "วัดความคุ้มค่าทางการเงินและการประหยัดงบประมาณการลอกท่อของหน่วยงานภาครัฐเทียบกับ Baseline เดิม",
                "rubric": "1: ระยะเวลาคืนทุนนานมาก (≥ 10 ปี) ต้นทุนเริ่มแรกสูงมากและแทบไม่มีผลประหยัดค่าใช้จ่าย\n2: ระยะเวลาคืนทุนช้า (6–9 ปี) ใช้เงินลงทุนสูง ต้องอาศัยเงินอุดหนุนระยะยาวจึงจะคุ้มทุน\n3: ระยะเวลาคืนทุนปานกลาง (3–5 ปี) ช่วยประหยัดค่าใช้จ่ายการปฏิบัติการในรอบปีงบประมาณปกติ\n4: ระยะเวลาคืนทุนเร็ว (2–3 ปี) ลดค่าใช้จ่ายปฏิบัติการ (ค่าน้ำมัน แรงงาน เครื่องจักร) ได้อย่างมีนัยสำคัญ\n5: คืนทุนทันที (≤ 1–2 ปี) ลดความสูญเสียจากน้ำท่วมและตัดรอบการลอกท่อที่ไม่จำเป็นได้ตั้งแต่ปีแรก",
                "score": 2,
                "weight": 0.0667,
                "evidence": "solution-details/solution-3.md lines 43-45; extremely high capital equipment cost for underwater sonar scan heads and winch rigs results in slow 6-9 year payback horizon for municipal drainage agencies.",
                "descope": "Use sonar profiler strictly as a specialized secondary diagnostic tool on suspected severely damaged pipe segments."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "การพึ่งพาผู้จำหน่ายและการผูกขาดชิ้นส่วนเฉพาะ (Component Dependency & Vendor Lock-in)?",
                "rationale": "ตรวจสอบความเสี่ยงจากการพึ่งพาผู้ขายรายเดียว การผูกขาดชิ้นส่วนนำเข้า หรือค่าลิขสิทธิ์ซอฟต์แวร์รายปี",
                "rubric": "1: ผูกขาดกับระบบปิด 100% ต้องใช้คลาวด์ หัวต่อ หรือเซนเซอร์เฉพาะจากผู้ผลิตรายเดียวเท่านั้น\n2: พึ่งพาผู้ผลิตสูง ต้องใช้เครื่องมือตรวจวินิจฉัยเฉพาะหรือเสียค่าธรรมเนียมรายปีเพื่อใช้งาน\n3: กึ่งอิสระ ฮาร์ดแวร์หลักเป็นระบบปิดแต่รองรับการส่งออกข้อมูลแบบเปิดและใช้อินเทอร์เฟซมาตรฐาน\n4: มีความเป็นอิสระสูง ใช้โปรโตคอลสื่อสารมาตรฐาน (Modbus, MQTT, CAN) หาอะไหล่เทียบได้ง่าย\n5: เป็นอิสระสมบูรณ์ 100% ใช้อุปกรณ์มาตรฐานทั่วไป สามารถซ่อมบำรุงและเปลี่ยนอะไหล่ได้เอง",
                "score": 1,
                "weight": 0.0667,
                "evidence": "solution-details/solution-3.md lines 33-36; commercial sewer profiling sonar transducers, waterproof rotary slip rings, and acoustic matching lenses are proprietary single-source imports with 4-8 week lead times, triggering a fatal vendor lock-in flaw.",
                "descope": "Replace proprietary commercial sonar modules with generic open piezoelectric transducer discs."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "วงเงินงบประมาณสำรองความเสียหายและการทำซ้ำ (Scrap Margin & Iteration Allowance)?",
                "rationale": "ประเมินขีดความสามารถในการรับมือกับความเสียหายของอุปกรณ์และชิปที่อาจช็อตหรือเสียหายระหว่างการพัฒนา",
                "rubric": "1: งบประมาณสำรอง 0% (ซื้อชุดเดียวพอดี) หากชิปไหม้หรืออุปกรณ์เสียหาย โครงการจะหยุดชะงักทันที\n2: งบประมาณสำรอง 20–30% สำรองได้เฉพาะชิ้นส่วนพาสซีฟราคาถูก ไม่มีอะไหล่สำหรับเซนเซอร์หลัก\n3: งบประมาณสำรอง 50% มีชิ้นส่วนพาสซีฟสำรองครบ และมีบอร์ดควบคุมหลักสำรอง 1 ชุด\n4: งบประมาณสำรอง 80% มีอะไหล่สำรองเกือบครบทุกชิ้นส่วน รองรับการทดสอบพัง (Burn-in) ได้หลายรอบ\n5: มีความพร้อมสำรองสมบูรณ์ (≥ 100%) งบประมาณครอบคลุมการสร้างตัวต้นแบบที่ทำงานได้ 2 ชุดพร้อมกัน",
                "score": 1,
                "weight": 0.0666,
                "evidence": "team-skills/due.md, fifa.md; a single commercial 360 sonar transducer module exceeds the entire student project budget (> 50,000 THB), leaving 0% margin for cracked piezo elements or flooded waterproof enclosures.",
                "descope": "Cap experimental hardware spending to < 3,000 THB using DIY low-voltage acoustic elements."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามกฎหมายจราจร ความปลอดภัยในที่อับอากาศ และระเบียบพื้นที่สาธารณะ (Felony, Traffic & Confined Space Compliance)?",
                "rationale": "ตรวจสอบความเสี่ยงต่อการละเมิดกฎหมายจราจร กฎหมายความปลอดภัยในที่อับอากาศ และการปิดกั้นทางสัญจร",
                "rubric": "1: ละเมิดกฎหมายโดยตรง (กีดขวางการจราจรสาธารณะร้ายแรง, ละเมิด PDPA รุนแรง, ส่งคลื่นรบกวนผิดกฎหมาย)\n2: สุ่มเสี่ยงทางกฎหมายสูง อาจถูกร้องเรียนเรื่องปิดกั้นการจราจรหรือความปลอดภัย ต้องขอผ่อนผันซับซ้อน\n3: มีเงื่อนไขทางกฎหมาย ต้องขออนุญาตเปิดฝาท่อและปิดช่องทางจราจรตามระเบียบของหน่วยงานเทศบาล\n4: ผลกระทบทางกฎหมายต่ำ ปฏิบัติตามข้อยกเว้นงานวิศวกรรมสาธารณะทั่วไป ใช้เพียงการแจ้งเตือนความปลอดภัย\n5: ได้รับการยกเว้นสมบูรณ์ 100% ไม่กีดขวางการจราจร ไม่เข้าข่ายที่อับอากาศ ไม่มีการเก็บข้อมูลส่วนบุคคล (Zero PII)",
                "score": 2,
                "weight": 0.075,
                "evidence": "solution-details/solution-3.md lines 27-28, 44; stringing winching cables between consecutive manholes across public roadways requires blocking traffic lanes for hours, necessitating formal municipal road closure permits.",
                "descope": "Perform winching trials exclusively inside closed university campus culverts."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามสัญญาอนุญาต ทรัพย์สินทางปัญญา และโอเพนซอร์ส (IP & Software Licensing Compliance)?",
                "rationale": "ตรวจสอบสิทธิ์การใช้งานซอฟต์แวร์ ไลบรารี และสิทธิบัตร ป้องกันการฟ้องร้องละเมิดลิขสิทธิ์",
                "rubric": "1: ติดสัญญาอนุญาตเชิงพาณิชย์แบบปิด ไม่สามารถคอมไพล์ รัน หรือแจกจ่ายได้หากไม่จ่ายค่าลิขสิทธิ์ราคาแพง\n2: สถานะทรัพย์สินทางปัญญาคลุมเครือ ไม่มีสัญญาอนุญาตระบุชัดเจน เสี่ยงต่อการถูกระงับเมื่อเปิดเผยต่อสาธารณะ\n3: สัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น GPLv3) บังคับให้ต้องเปิดเผยโค้ดทั้งหมดหากมีการแจกจ่าย\n4: สัญญาอนุญาตแบบผ่อนปรน (เช่น LGPL, CC-BY) ใช้งานและห่อหุ้มซอฟต์แวร์ได้โดยมีเงื่อนไขอ้างอิงแหล่งที่มา\n5: โอเพนซอร์สสมบูรณ์ (MIT, Apache 2.0, BSD) หรือ Public Domain ใช้งานและต่อยอดได้อย่างอิสระ 100%",
                "score": 3,
                "weight": 0.075,
                "evidence": "solution-details/solution-3.md lines 35, 45; sewer sonar mapping software and polar reconstruction suites are often proprietary and protected by commercial dongles or restrictive licenses.",
                "descope": "Write custom open-source Python NumPy/Matplotlib scripts for polar backscatter plotting."
            },
            {
                "id": "O-01",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบและความรุนแรงเมื่อระบบเกิดความขัดข้องหรือติดค้าง (User — Failure Impact & Stuck Hazards)?",
                "rationale": "ประเมินความเสียหายต่อโครงสร้างพื้นฐาน ความปลอดภัยของเจ้าหน้าที่ และการกลายเป็นสิ่งกีดขวางในท่อระบายน้ำ",
                "rubric": "1: เป็นอันตรายต่อชีวิต (ไฟฟ้าดูด เพลิงไหม้ อุบัติเหตุทางถนน สารพิษ หรือโครงสร้างท่อพังทลาย)\n2: ก่อให้เกิดอันตรายทางกายภาพร้ายแรง อุปกรณ์ติดค้างกลายเป็นสิ่งอุดตันท่อ หรือระบบน้ำล้นฉับพลัน\n3: เกิดความสับสนในการปฏิบัติงาน อุปกรณ์ขัดข้องต้องใช้เวลาหลายชั่วโมงในการกู้คืนหรือส่งทีมไปช่วย\n4: เกิดความล่าช้าเล็กน้อย อุปกรณ์ตัดการทำงานอย่างปลอดภัย สามารถกู้คืนได้ตามขั้นตอนมาตรฐาน\n5: ความเสียหายจำกัดเฉพาะงบประมาณ ไม่ส่งผลต่อความปลอดภัยหรือการไหลของน้ำ กู้คืนได้ทันที",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-3.md lines 43-44; if the submerged sonar pod or float gets snagged on submerged debris or the winch line snaps under tension, the expensive equipment becomes a permanent pipe obstruction.",
                "descope": "Implement a mechanical shear-pin release with a secondary redundant floating retrieval tether."
            },
            {
                "id": "O-02",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมเจ้าหน้าที่และขั้นตอนการทำงานเดิม (User — Workflow Friction & Adoption)?",
                "rationale": "ประเมินภาระการฝึกอบรม ความสะดวกในการพกพา และแรงต้านจากเจ้าหน้าที่ภาคสนามของ กทม.",
                "rubric": "1: ขัดขวางขั้นตอนเดิมอย่างรุนแรง บังคับให้เจ้าหน้าที่ต้องเปลี่ยนวิธีทำงานทั้งหมดและกรอกเอกสารเพิ่มมากมาย\n2: มีความฝืดสูง เพิ่มขั้นตอนการทำงานและต้องใช้อุปกรณ์เทอะทะ เจ้าหน้าที่มีแนวโน้มหลีกเลี่ยงการใช้งาน\n3: ต้องปรับตัวปานกลาง ปรับเปลี่ยนขั้นตอนประจำวันเล็กน้อย ต้องฝึกอบรม 1–2 ครั้ง แต่ได้ผลลัพธ์คุ้มค่า\n4: ความฝืดต่ำ บูรณาการเข้ากับเครื่องมือเดิมได้โดยตรง (ส่งค่าเข้า LINE/Dashboard) ปรับพฤติกรรมน้อยมาก\n5: ราบรื่นไร้รอยต่อ 100% ทำงานอัตโนมัติในพื้นหลัง ลดภาระงานเอกสารและการลอกท่อเดิมของเจ้าหน้าที่",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-3.md lines 43-44; requires setting up winches on two consecutive manholes, threading pull-ropes through sewage, and washing contaminated cables after every inspection run.",
                "descope": "Mount sonar on a self-propelled crawler to eliminate the two-manhole winch threading procedure."
            },
            {
                "id": "O-03",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนการขออนุมัติของนักพัฒนา (Developer — Lab & Administrative Gatekeeping)?",
                "rationale": "ประเมินอุปสรรคการเข้าถึงเครื่องมือ ช็อปเครื่องกล หรือการต้องรอคิวอนุมัติเอกสารของมหาวิทยาลัย",
                "rubric": "1: ติดคอขวดขั้นตอนอนุมัติหนัก ห้องแล็บปิด ต้องลงนาม NDA หรือรอจัดซื้ออุปกรณ์หลายสัปดาห์\n2: มีขั้นตอนราชการปานกลาง ต้องส่งแบบฟอร์มจองเครื่องมือล่วงหน้า และรออนุมัติ 3–5 วันทำการ\n3: เข้าถึงได้ตามเวลาทำการปกติของมหาวิทยาลัย มีความล่าช้าเล็กน้อยในการเบิกใช้เครื่องมือเฉพาะทาง\n4: มีอิสระสูง ทีมงานเข้าแล็บได้ตลอด มีสิทธิ์เขียนโค้ดลงบอร์ด และมีงบประมาณย่อยพร้อมใช้งานทันที\n5: พัฒนาได้อย่างอิสระสมบูรณ์ 100% มีระบบ CI/CD บนคลาวด์และพัฒนาชิ้นงานได้เองที่บ้าน/หอพัก",
                "score": 2,
                "weight": 0.05,
                "evidence": "team-skills/due.md, fifa.md; underwater acoustic testing requires access to deep water testing tanks, high-voltage pulse generators, and hydrophone calibration facilities.",
                "descope": "Use a small portable water tank container for bench testing."
            },
            {
                "id": "O-04",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประกอบ ติดตั้ง และโปรแกรม (Developer — Setup Steps & Pipeline Friction)?",
                "rationale": "ประเมินจำนวนขั้นตอนและความเปราะบางของเครื่องมือพัฒนา ป้องกันข้อผิดพลาดจากการตั้งค่าระบบที่ซับซ้อนเกินไป",
                "rubric": "1: ซับซ้อนมาก มีขั้นตอนคอมไพล์และตั้งค่าหลายสิบขั้นตอน เสี่ยงต่อข้อผิดพลาดสูงมาก\n2: ความซับซ้อนสูง ต้องใช้เครื่องมือหลายระดับ มีปัญหาความเข้ากันได้ของไลบรารีและแฟลชบอร์ดได้ยาก\n3: ความซับซ้อนปานกลาง มีขั้นตอนประกอบและทดสอบตามคู่มือมาตรฐานที่บันทึกไว้ ทำซ้ำได้ไม่ยาก\n4: ความซับซ้อนต่ำ ใช้สคริปต์อัตโนมัติ IDE มาตรฐาน หรือแฟลชเฟิร์มแวร์ด้วยคำสั่งเดียว\n5: เรียบง่ายและตรงไปตรงมา เป็นระบบ Plug-and-Play ตั้งค่าขั้นตอนเดียวเสร็จสมบูรณ์",
                "score": 1,
                "weight": 0.05,
                "evidence": "solution-details/solution-3.md lines 27-36, 45; highly convoluted multi-stage toolchain: waterproof rotary mechanics, high-voltage piezo pulsing, low-noise analog TGC filtering, and complex polar SLAM mapping software, triggering a fatal complexity flaw.",
                "descope": "Descope mapping software into simple 2D polar scatter plots."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงานและเวลา (Schedule 2.6)",
                "question": "วุฒิภาวะของการออกแบบทางวิศวกรรมภายในกรอบเวลา 5 สัปดาห์ทำงาน (Engineering Design Maturity by 5 Weeks)?",
                "rationale": "ทดสอบความเป็นไปได้ในการสร้างชิ้นงานให้สำเร็จตามเป้าหมาย TRL โดยหักสัปดาห์สอบมิดเทอมและไฟนอลออกแล้ว",
                "rubric": "1: ระดับแนวคิดเท่านั้น (แบบ 0%) มีเพียงภาพสเก็ตช์ ยังไม่มีโมเดล 3D วงจร หรือเฟิร์มแวร์ใดๆ\n2: แบบร่างเบื้องต้น (แบบ 25%) มีบล็อกไดอะแกรม วงจรร่างมือ รายการชิ้นส่วนที่ยังไม่ยืนยัน และกล่อง 3D คร่าวๆ\n3: วุฒิภาวะปานกลาง (แบบ 50%) แอสเซมบลี CAD ครบ วาดวงจรเสร็จ และวางโครงสร้างเฟิร์มแวร์แล้ว\n4: พร้อมผลิตเบื้องต้น (แบบ 75–80%) ไฟล์ CAD พร้อมพิมพ์ 3D/CNC และไฟล์ PCB Gerber ผ่านการตรวจ DRC\n5: แบบสมบูรณ์พร้อมผลิต 100% มีเอกสารสั่งผลิตครบ พิกัดความเผื่อ CAD แน่นอน และสคริปต์แฟลชพร้อมทำงาน",
                "score": 1,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; developing custom underwater rotating sonar hardware, transducer matching, and float winching mechanisms from 0% baseline within 5 business weeks under exam blackout constraints is mathematically unfeasible, triggering a fatal schedule flaw.",
                "descope": "Halt hardware development of 360 sonar and pivot team resources to viable acoustic reflectometry."
            },
            {
                "id": "SDG-01",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "การบูรณาการตามกรอบ Stockholm Wedding Cake (Biosphere, Society, Economy Integration)?",
                "rationale": "ประเมินผลกระทบเชิงบวกที่ครอบคลุมทั้งด้านชีวมณฑล (SDG 6/14), สังคม (SDG 11) และเศรษฐกิจ (SDG 8/12)",
                "rubric": "1: หลุดจากกรอบ Wedding Cake หรือสร้างผลกระทบเชิงลบอย่างรุนแรงต่อสิ่งแวดล้อมหรือสุขอนามัย\n2: สัมผัสเพียง 1 เสาหลักอย่างผิวเผิน ขาดการเชื่อมโยงเชิงประจักษ์ไปยังสังคมหรือสิ่งแวดล้อมจริง\n3: ครอบคลุม 1 เสาหลักอย่างเป็นรูปธรรม หรือเริ่มแตะ 2 เสาหลักแบบมีข้อจำกัดเฉพาะจุด\n4: บูรณาการ 2 เสาหลักสำคัญอย่างมีนัยสำคัญ (เช่น Biosphere + Society) พร้อมตัวชี้วัดรองรับ\n5: บูรณาการครบทั้ง 3 เสาหลักของ Wedding Cake อย่างสมบูรณ์ (Biosphere, Society, Economy)",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-3.md lines 6-10; addresses Biosphere (SDG 6.3 water infrastructure integrity) but lacks direct socio-economic scalability due to extreme equipment cost.",
                "descope": "Map sediment clearance volume directly to local flood hazard reduction metrics."
            },
            {
                "id": "SDG-02",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "ผลกระทบสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และหลักเศรษฐกิจหมุนเวียน (E-Waste & 'Do No Harm' — SDG 6.3/12.4)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-3.md lines 43-44; submerged electronic pod and cables in sewage risk chemical degradation, wire snapping, and accidental abandonment as hazardous e-waste in drainage culverts.",
                "descope": "Install dual redundant stainless steel mechanical recovery tethers."
            }
        ]
    },
    {
        "sheet_title": "Solution_4_LiDAR_SLAM",
        "concept": "Pipe Inspection Instrument using LiDAR SLAM attaching with Robot (3D LiDAR + Laser SLAM Point Cloud Profiling)",
        "strength": "สร้างแผนที่ 3 มิติ (3D Point Cloud) ของท่อระบายน้ำได้อย่างแม่นยำระดับมิลลิเมตร สามารถตรวจวัดปริมาตรตะกอน (Buildup/Debris) และตรวจจับการเสียรูปเชิงเรขาคณิตของท่อได้อย่างชัดเจน",
        "bottleneck": "เซนเซอร์ 3D LiDAR และบอร์ดประมวลผล GPU/SBC มีราคาสูงมากเกินงบประมาณ (E-03=1: ไม่มีงบสำรองกรณีเซนเซอร์ตกน้ำ), เลเซอร์ไม่สามารถทะลุน้ำเสียหรือหมอกควันได้ (T-03=2), และต้องใช้เวลาประมวลผล Point Cloud สูง",
        "advice": "ลดสโคปจากการใช้ 3D LiDAR ราคาแพง มาใช้ 2D LiDAR ติดตั้งบนแกนหมุน หรือใช้ Depth Camera / Structured Light ในท่อแห้งเพื่อควบคุมต้นทุนไม่ให้เกินงบประมาณ",
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
                "descope": "Use a modular 2D LiDAR with a 1-DOF servo rotation pitch axis instead of a costly monolithic 3D LiDAR."
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
                "descope": "Deploy open-source FAST-LIO2 or Cartographer ROS2 nodes directly."
            },
            {
                "id": "T-03",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ระดับความพร้อมทางเทคโนโลยี (Base Performance / TRL) ในสภาพแวดล้อมจริงของท่อระบายน้ำใต้ดิน?",
                "rationale": "วัดวุฒิภาวะของเทคโนโลยีว่าผ่านการพิสูจน์ในสภาพแวดล้อมใต้ดินที่มีความชื้น สารกัดกร่อน หรือน้ำขังจริงแล้วหรือไม่",
                "rubric": "1: ระดับแนวคิด/สมการคณิตศาสตร์ (TRL 2–3) ทดสอบเฉพาะในห้องทดลองที่ควบคุมสภาพแวดล้อมได้\n2: เบรดบอร์ดทำงานได้ในแล็บ (TRL 4) สายไฟเปราะบาง ยังไม่ผ่านการสอบเทียบในสภาพแวดล้อมจริง\n3: ตัวต้นแบบประกอบลงกล่อง (TRL 5–6) ผ่านการทดสอบในสภาพแวดล้อมจำลอง ต้องมีคนคอยดูแล\n4: ต้นแบบระดับพรีโปรดักชัน (TRL 7) ทำงานได้อย่างมีเสถียรภาพในสภาพแวดล้อมปฏิบัติงานจริง\n5: ผลิตภัณฑ์เชิงพาณิชย์สมบูรณ์ (TRL 8–9) ผ่านการรับรองมาตรฐาน มีค่า MTBF ยืนยันความทนทาน",
                "score": 2,
                "weight": 0.04,
                "evidence": "solution-details/solution-4.md lines 43-45; laser beams suffer total optical absorption and refraction on dirty standing water surfaces, and high humidity/fog creates backscatter noise; works at TRL 4 in dry lab pipes only.",
                "descope": "Restrict LiDAR SLAM inspection strictly to dry sewer pipe segments or pre-drained culverts."
            },
            {
                "id": "T-04",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความพร้อมและกำลังคนสำรองของทีมงาน (Team Compatibility & Redundancy / Anti-SPOF)?",
                "rationale": "ตรวจสอบความเสี่ยงคอขวดบุคลากร (Single Point of Failure) ป้องกันไม่ให้โครงการหยุดชะงักหากผู้รับผิดชอบหลักไม่ว่าง",
                "rubric": "1: พึ่งพาผู้เชี่ยวชาญเพียงคนเดียว (SPOF) หากไม่อยู่ โครงการหยุดชะงัก 100%\n2: มีหัวหน้าโครงการ 1 คน และมีผู้ช่วยเข้าใจทฤษฎีแต่แก้โค้ดหรือซ่อมฮาร์ดแวร์แทนไม่ได้\n3: มีคู่หลัก-รอง (Primary + Secondary) สามารถแก้ไขปัญหาและดูแลระบบแทนกันได้\n4: สมาชิกตั้งแต่ 3 คนขึ้นไปสามารถร่วมพัฒนา ประกอบ และแก้ไขปัญหาระบบได้โดยตรง\n5: สมาชิกทุกคนในทีมมีความเชี่ยวชาญเต็มรูปแบบ สามารถสลับงานแทนกันได้ทันทีอย่างไร้รอยต่อ",
                "score": 3,
                "weight": 0.04,
                "evidence": "team-skills/jk.md, fifa.md, due.md; JK is highly competent in ROS2, Linux, C++, and linear algebra for SLAM; Fifa and Due provide mechanical crawler support.",
                "descope": "JK packages SLAM nodes with clear ROS2 launch files so team members can run inspection recordings without tuning parameters."
            },
            {
                "id": "T-05",
                "pillar": "ด้านเทคนิค (Technical 2.2)",
                "question": "ความชันในการเรียนรู้และเวลาปรับตัวของทีมงาน (Learning Curve & Ramp-up Time)?",
                "rationale": "ประเมินเวลาที่ทีมต้องใช้ในการเรียนรู้เครื่องมือหรือทฤษฎีใหม่ เพื่อไม่ให้กระทบต่อกำหนดการส่งมอบ 5 สัปดาห์",
                "rubric": "1: ต้องเริ่มเรียนรู้ใหม่จากศูนย์ 100% ทั้งเครื่องมือ ภาษา และฮาร์ดแวร์ที่ไม่เคยใช้งานมาก่อน\n2: มีพื้นฐานทฤษฎีแต่ขาดประสบการณ์จริง การติดตั้งและแก้บั๊กเบื้องต้นใช้เวลานานและติดขัด\n3: มีความเชี่ยวชาญในเทคโนโลยีใกล้เคียง สามารถปรับตัวและเรียนรู้เพิ่มเติมได้ภายใน 1 สัปดาห์\n4: คุ้นเคยกับเทคโนโลยีหลักอยู่แล้ว เพียงแค่เรียนรู้ไลบรารีหรือการตั้งค่าเฉพาะเพิ่มเติมเล็กน้อย\n5: สามารถดึงโค้ดเก่า วงจรที่เคยทำ และประสบการณ์เดิมมาใช้งานได้ทันทีโดยไม่ต้องเรียนรู้ใหม่",
                "score": 2,
                "weight": 0.04,
                "evidence": "team-skills/jk.md; while JK knows ROS2 and differential equations, tuning 3D LiDAR SLAM in feature-degenerate cylindrical pipe tunnels requires extensive point cloud filtering and IMU tightly-coupled odometry.",
                "descope": "Use wheel encoder odometry fusion to constrain the longitudinal translation axis inside symmetric pipes."
            },
            {
                "id": "E-01",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "ระยะเวลาคืนทุนและความคุ้มค่าในการลงทุน (ROI / Payback Period) เทียบกับการขุดลอกแบบสุ่ม?",
                "rationale": "วัดความคุ้มค่าทางการเงินและการประหยัดงบประมาณการลอกท่อของหน่วยงานภาครัฐเทียบกับ Baseline เดิม",
                "rubric": "1: ระยะเวลาคืนทุนนานมาก (≥ 10 ปี) ต้นทุนเริ่มแรกสูงมากและแทบไม่มีผลประหยัดค่าใช้จ่าย\n2: ระยะเวลาคืนทุนช้า (6–9 ปี) ใช้เงินลงทุนสูง ต้องอาศัยเงินอุดหนุนระยะยาวจึงจะคุ้มทุน\n3: ระยะเวลาคืนทุนปานกลาง (3–5 ปี) ช่วยประหยัดค่าใช้จ่ายการปฏิบัติการในรอบปีงบประมาณปกติ\n4: ระยะเวลาคืนทุนเร็ว (2–3 ปี) ลดค่าใช้จ่ายปฏิบัติการ (ค่าน้ำมัน แรงงาน เครื่องจักร) ได้อย่างมีนัยสำคัญ\n5: คืนทุนทันที (≤ 1–2 ปี) ลดความสูญเสียจากน้ำท่วมและตัดรอบการลอกท่อที่ไม่จำเป็นได้ตั้งแต่ปีแรก",
                "score": 3,
                "weight": 0.0667,
                "evidence": "solution-details/solution-4.md lines 6-10, 38-40; produces millimeter-accurate 3D CAD models of pipe deformation and sediment volume, delivering moderate 3-5 year payback for specialized structural asset management.",
                "descope": "Focus value proposition on structural defect quantification to justify CapEx."
            },
            {
                "id": "E-02",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "การพึ่งพาผู้จำหน่ายและการผูกขาดชิ้นส่วนเฉพาะ (Component Dependency & Vendor Lock-in)?",
                "rationale": "ตรวจสอบความเสี่ยงจากการพึ่งพาผู้ขายรายเดียว การผูกขาดชิ้นส่วนนำเข้า หรือค่าลิขสิทธิ์ซอฟต์แวร์รายปี",
                "rubric": "1: ผูกขาดกับระบบปิด 100% ต้องใช้คลาวด์ หัวต่อ หรือเซนเซอร์เฉพาะจากผู้ผลิตรายเดียวเท่านั้น\n2: พึ่งพาผู้ผลิตสูง ต้องใช้เครื่องมือตรวจวินิจฉัยเฉพาะหรือเสียค่าธรรมเนียมรายปีเพื่อใช้งาน\n3: กึ่งอิสระ ฮาร์ดแวร์หลักเป็นระบบปิดแต่รองรับการส่งออกข้อมูลแบบเปิดและใช้อินเทอร์เฟซมาตรฐาน\n4: มีความเป็นอิสระสูง ใช้โปรโตคอลสื่อสารมาตรฐาน (Modbus, MQTT, CAN) หาอะไหล่เทียบได้ง่าย\n5: เป็นอิสระสมบูรณ์ 100% ใช้อุปกรณ์มาตรฐานทั่วไป สามารถซ่อมบำรุงและเปลี่ยนอะไหล่ได้เอง",
                "score": 3,
                "weight": 0.0667,
                "evidence": "solution-details/solution-4.md lines 33-36; dependent on specialized solid-state 3D LiDAR hardware (Livox/Velodyne) and high-performance embedded GPU SBCs.",
                "descope": "Use standardized ROS2 point cloud drivers to maintain compatibility across different LiDAR hardware vendors."
            },
            {
                "id": "E-03",
                "pillar": "ด้านเศรษฐศาสตร์ (Economic 2.3)",
                "question": "วงเงินงบประมาณสำรองความเสียหายและการทำซ้ำ (Scrap Margin & Iteration Allowance)?",
                "rationale": "ประเมินขีดความสามารถในการรับมือกับความเสียหายของอุปกรณ์และชิปที่อาจช็อตหรือเสียหายระหว่างการพัฒนา",
                "rubric": "1: งบประมาณสำรอง 0% (ซื้อชุดเดียวพอดี) หากชิปไหม้หรืออุปกรณ์เสียหาย โครงการจะหยุดชะงักทันที\n2: งบประมาณสำรอง 20–30% สำรองได้เฉพาะชิ้นส่วนพาสซีฟราคาถูก ไม่มีอะไหล่สำหรับเซนเซอร์หลัก\n3: งบประมาณสำรอง 50% มีชิ้นส่วนพาสซีฟสำรองครบ และมีบอร์ดควบคุมหลักสำรอง 1 ชุด\n4: งบประมาณสำรอง 80% มีอะไหล่สำรองเกือบครบทุกชิ้นส่วน รองรับการทดสอบพัง (Burn-in) ได้หลายรอบ\n5: มีความพร้อมสำรองสมบูรณ์ (≥ 100%) งบประมาณครอบคลุมการสร้างตัวต้นแบบที่ทำงานได้ 2 ชุดพร้อมกัน",
                "score": 1,
                "weight": 0.0666,
                "evidence": "team-skills/due.md, fifa.md; 3D LiDAR sensor (25,000–35,000 THB) + Jetson SBC exhausts 100% of student team funding; zero budget exists for replacement if the sensor is damaged or dropped into sewage, triggering a fatal scrap margin flaw.",
                "descope": "Borrow an evaluation LiDAR unit from FIBO robotics labs with signed academic liability waivers."
            },
            {
                "id": "L-01",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามกฎหมายจราจร ความปลอดภัยในที่อับอากาศ และระเบียบพื้นที่สาธารณะ (Felony, Traffic & Confined Space Compliance)?",
                "rationale": "ตรวจสอบความเสี่ยงต่อการละเมิดกฎหมายจราจร กฎหมายความปลอดภัยในที่อับอากาศ และการปิดกั้นทางสัญจร",
                "rubric": "1: ละเมิดกฎหมายโดยตรง (กีดขวางการจราจรสาธารณะร้ายแรง, ละเมิด PDPA รุนแรง, ส่งคลื่นรบกวนผิดกฎหมาย)\n2: สุ่มเสี่ยงทางกฎหมายสูง อาจถูกร้องเรียนเรื่องปิดกั้นการจราจรหรือความปลอดภัย ต้องขอผ่อนผันซับซ้อน\n3: มีเงื่อนไขทางกฎหมาย ต้องขออนุญาตเปิดฝาท่อและปิดช่องทางจราจรตามระเบียบของหน่วยงานเทศบาล\n4: ผลกระทบทางกฎหมายต่ำ ปฏิบัติตามข้อยกเว้นงานวิศวกรรมสาธารณะทั่วไป ใช้เพียงการแจ้งเตือนความปลอดภัย\n5: ได้รับการยกเว้นสมบูรณ์ 100% ไม่กีดขวางการจราจร ไม่เข้าข่ายที่อับอากาศ ไม่มีการเก็บข้อมูลส่วนบุคคล (Zero PII)",
                "score": 2,
                "weight": 0.075,
                "evidence": "solution-details/solution-4.md lines 18, 27-28; requires opening public road manhole covers and deploying crawler tether stations, necessitating formal municipal permits and safety lane closures.",
                "descope": "Perform SLAM scanning trials strictly on pedestrian campus walkways."
            },
            {
                "id": "L-02",
                "pillar": "ด้านกฎหมายและสถาบัน (Legal 2.4)",
                "question": "การปฏิบัติตามสัญญาอนุญาต ทรัพย์สินทางปัญญา และโอเพนซอร์ส (IP & Software Licensing Compliance)?",
                "rationale": "ตรวจสอบสิทธิ์การใช้งานซอฟต์แวร์ ไลบรารี และสิทธิบัตร ป้องกันการฟ้องร้องละเมิดลิขสิทธิ์",
                "rubric": "1: ติดสัญญาอนุญาตเชิงพาณิชย์แบบปิด ไม่สามารถคอมไพล์ รัน หรือแจกจ่ายได้หากไม่จ่ายค่าลิขสิทธิ์ราคาแพง\n2: สถานะทรัพย์สินทางปัญญาคลุมเครือ ไม่มีสัญญาอนุญาตระบุชัดเจน เสี่ยงต่อการถูกระงับเมื่อเปิดเผยต่อสาธารณะ\n3: สัญญาอนุญาตแบบ Copyleft เข้มงวด (เช่น GPLv3) บังคับให้ต้องเปิดเผยโค้ดทั้งหมดหากมีการแจกจ่าย\n4: สัญญาอนุญาตแบบผ่อนปรน (เช่น LGPL, CC-BY) ใช้งานและห่อหุ้มซอฟต์แวร์ได้โดยมีเงื่อนไขอ้างอิงแหล่งที่มา\n5: โอเพนซอร์สสมบูรณ์ (MIT, Apache 2.0, BSD) หรือ Public Domain ใช้งานและต่อยอดได้อย่างอิสระ 100%",
                "score": 5,
                "weight": 0.075,
                "evidence": "solution-details/solution-4.md lines 33-36; ROS2 (Apache 2.0), Point Cloud Library (BSD), and FAST-LIO2 (GPL/BSD) are completely open source for academic research and prototyping.",
                "descope": "Adhere to open-source repository documentation guidelines."
            },
            {
                "id": "O-01",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ผลกระทบและความรุนแรงเมื่อระบบเกิดความขัดข้องหรือติดค้าง (User — Failure Impact & Stuck Hazards)?",
                "rationale": "ประเมินความเสียหายต่อโครงสร้างพื้นฐาน ความปลอดภัยของเจ้าหน้าที่ และการกลายเป็นสิ่งกีดขวางในท่อระบายน้ำ",
                "rubric": "1: เป็นอันตรายต่อชีวิต (ไฟฟ้าดูด เพลิงไหม้ อุบัติเหตุทางถนน สารพิษ หรือโครงสร้างท่อพังทลาย)\n2: ก่อให้เกิดอันตรายทางกายภาพร้ายแรง อุปกรณ์ติดค้างกลายเป็นสิ่งอุดตันท่อ หรือระบบน้ำล้นฉับพลัน\n3: เกิดความสับสนในการปฏิบัติงาน อุปกรณ์ขัดข้องต้องใช้เวลาหลายชั่วโมงในการกู้คืนหรือส่งทีมไปช่วย\n4: เกิดความล่าช้าเล็กน้อย อุปกรณ์ตัดการทำงานอย่างปลอดภัย สามารถกู้คืนได้ตามขั้นตอนมาตรฐาน\n5: ความเสียหายจำกัดเฉพาะงบประมาณ ไม่ส่งผลต่อความปลอดภัยหรือการไหลของน้ำ กู้คืนได้ทันที",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 43-45; crawler stuck in sewage requires manual recovery; laser optical glass easily smudged by splashing wastewater slurry, requiring aborting scan run.",
                "descope": "Equip LiDAR with a protective clear acrylic splash shield and rubber wiper."
            },
            {
                "id": "O-02",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความสอดคล้องกับพฤติกรรมเจ้าหน้าที่และขั้นตอนการทำงานเดิม (User — Workflow Friction & Adoption)?",
                "rationale": "ประเมินภาระการฝึกอบรม ความสะดวกในการพกพา และแรงต้านจากเจ้าหน้าที่ภาคสนามของ กทม.",
                "rubric": "1: ขัดขวางขั้นตอนเดิมอย่างรุนแรง บังคับให้เจ้าหน้าที่ต้องเปลี่ยนวิธีทำงานทั้งหมดและกรอกเอกสารเพิ่มมากมาย\n2: มีความฝืดสูง เพิ่มขั้นตอนการทำงานและต้องใช้อุปกรณ์เทอะทะ เจ้าหน้าที่มีแนวโน้มหลีกเลี่ยงการใช้งาน\n3: ต้องปรับตัวปานกลาง ปรับเปลี่ยนขั้นตอนประจำวันเล็กน้อย ต้องฝึกอบรม 1–2 ครั้ง แต่ได้ผลลัพธ์คุ้มค่า\n4: ความฝืดต่ำ บูรณาการเข้ากับเครื่องมือเดิมได้โดยตรง (ส่งค่าเข้า LINE/Dashboard) ปรับพฤติกรรมน้อยมาก\n5: ราบรื่นไร้รอยต่อ 100% ทำงานอัตโนมัติในพื้นหลัง ลดภาระงานเอกสารและการลอกท่อเดิมของเจ้าหน้าที่",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 44-45; generates massive 3D point cloud files (.pcd/.ply) requiring GIS/CAD engineering expertise to interpret, creating operational workflow friction for field maintenance crews.",
                "descope": "Develop an automated Python script that converts 3D point clouds into a single 1-page PDF cross-section summary."
            },
            {
                "id": "O-03",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "การพึ่งพาห้องปฏิบัติการและขั้นตอนการขออนุมัติของนักพัฒนา (Developer — Lab & Administrative Gatekeeping)?",
                "rationale": "ประเมินอุปสรรคการเข้าถึงเครื่องมือ ช็อปเครื่องกล หรือการต้องรอคิวอนุมัติเอกสารของมหาวิทยาลัย",
                "rubric": "1: ติดคอขวดขั้นตอนอนุมัติหนัก ห้องแล็บปิด ต้องลงนาม NDA หรือรอจัดซื้ออุปกรณ์หลายสัปดาห์\n2: มีขั้นตอนราชการปานกลาง ต้องส่งแบบฟอร์มจองเครื่องมือล่วงหน้า และรออนุมัติ 3–5 วันทำการ\n3: เข้าถึงได้ตามเวลาทำการปกติของมหาวิทยาลัย มีความล่าช้าเล็กน้อยในการเบิกใช้เครื่องมือเฉพาะทาง\n4: มีอิสระสูง ทีมงานเข้าแล็บได้ตลอด มีสิทธิ์เขียนโค้ดลงบอร์ด และมีงบประมาณย่อยพร้อมใช้งานทันที\n5: พัฒนาได้อย่างอิสระสมบูรณ์ 100% มีระบบ CI/CD บนคลาวด์และพัฒนาชิ้นงานได้เองที่บ้าน/หอพัก",
                "score": 3,
                "weight": 0.05,
                "evidence": "team-skills/due.md, jk.md; requires access to FIBO robotics lab GPU workstations for point cloud processing and mechanical workshop for crawler chassis mounting.",
                "descope": "Record raw ROS2 rosbag files on SBC and perform offline SLAM mapping on personal laptops."
            },
            {
                "id": "O-04",
                "pillar": "ด้านการปฏิบัติการ (Operational 2.5)",
                "question": "ความซับซ้อนของขั้นตอนการประกอบ ติดตั้ง และโปรแกรม (Developer — Setup Steps & Pipeline Friction)?",
                "rationale": "ประเมินจำนวนขั้นตอนและความเปราะบางของเครื่องมือพัฒนา ป้องกันข้อผิดพลาดจากการตั้งค่าระบบที่ซับซ้อนเกินไป",
                "rubric": "1: ซับซ้อนมาก มีขั้นตอนคอมไพล์และตั้งค่าหลายสิบขั้นตอน เสี่ยงต่อข้อผิดพลาดสูงมาก\n2: ความซับซ้อนสูง ต้องใช้เครื่องมือหลายระดับ มีปัญหาความเข้ากันได้ของไลบรารีและแฟลชบอร์ดได้ยาก\n3: ความซับซ้อนปานกลาง มีขั้นตอนประกอบและทดสอบตามคู่มือมาตรฐานที่บันทึกไว้ ทำซ้ำได้ไม่ยาก\n4: ความซับซ้อนต่ำ ใช้สคริปต์อัตโนมัติ IDE มาตรฐาน หรือแฟลชเฟิร์มแวร์ด้วยคำสั่งเดียว\n5: เรียบง่ายและตรงไปตรงมา เป็นระบบ Plug-and-Play ตั้งค่าขั้นตอนเดียวเสร็จสมบูรณ์",
                "score": 2,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 27-36, 44-45; multi-stage setup: ROS2 network configuration, high-bandwidth sensor tethering, IMU extrinsic calibration, and point cloud registration pipeline.",
                "descope": "Provide a pre-built Docker container with all PCL and SLAM dependencies pre-compiled."
            },
            {
                "id": "S-01",
                "pillar": "ด้านแผนงานและเวลา (Schedule 2.6)",
                "question": "วุฒิภาวะของการออกแบบทางวิศวกรรมภายในกรอบเวลา 5 สัปดาห์ทำงาน (Engineering Design Maturity by 5 Weeks)?",
                "rationale": "ทดสอบความเป็นไปได้ในการสร้างชิ้นงานให้สำเร็จตามเป้าหมาย TRL โดยหักสัปดาห์สอบมิดเทอมและไฟนอลออกแล้ว",
                "rubric": "1: ระดับแนวคิดเท่านั้น (แบบ 0%) มีเพียงภาพสเก็ตช์ ยังไม่มีโมเดล 3D วงจร หรือเฟิร์มแวร์ใดๆ\n2: แบบร่างเบื้องต้น (แบบ 25%) มีบล็อกไดอะแกรม วงจรร่างมือ รายการชิ้นส่วนที่ยังไม่ยืนยัน และกล่อง 3D คร่าวๆ\n3: วุฒิภาวะปานกลาง (แบบ 50%) แอสเซมบลี CAD ครบ วาดวงจรเสร็จ และวางโครงสร้างเฟิร์มแวร์แล้ว\n4: พร้อมผลิตเบื้องต้น (แบบ 75–80%) ไฟล์ CAD พร้อมพิมพ์ 3D/CNC และไฟล์ PCB Gerber ผ่านการตรวจ DRC\n5: แบบสมบูรณ์พร้อมผลิต 100% มีเอกสารสั่งผลิตครบ พิกัดความเผื่อ CAD แน่นอน และสคริปต์แฟลชพร้อมทำงาน",
                "score": 2,
                "weight": 0.15,
                "evidence": "schedule-details/schedule.md lines 8-15; integrating crawler chassis + LiDAR drivers + SLAM calibration inside symmetrical cylindrical pipe tunnels within 5 business weeks during exam blackout is highly compressed.",
                "descope": "Focus demonstration strictly on a 3-meter indoor PVC pipe section with pre-placed geometric obstacles."
            },
            {
                "id": "SDG-01",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "การบูรณาการตามกรอบ Stockholm Wedding Cake (Biosphere, Society, Economy Integration)?",
                "rationale": "ประเมินผลกระทบเชิงบวกที่ครอบคลุมทั้งด้านชีวมณฑล (SDG 6/14), สังคม (SDG 11) และเศรษฐกิจ (SDG 8/12)",
                "rubric": "1: หลุดจากกรอบ Wedding Cake หรือสร้างผลกระทบเชิงลบอย่างรุนแรงต่อสิ่งแวดล้อมหรือสุขอนามัย\n2: สัมผัสเพียง 1 เสาหลักอย่างผิวเผิน ขาดการเชื่อมโยงเชิงประจักษ์ไปยังสังคมหรือสิ่งแวดล้อมจริง\n3: ครอบคลุม 1 เสาหลักอย่างเป็นรูปธรรม หรือเริ่มแตะ 2 เสาหลักแบบมีข้อจำกัดเฉพาะจุด\n4: บูรณาการ 2 เสาหลักสำคัญอย่างมีนัยสำคัญ (เช่น Biosphere + Society) พร้อมตัวชี้วัดรองรับ\n5: บูรณาการครบทั้ง 3 เสาหลักของ Wedding Cake อย่างสมบูรณ์ (Biosphere, Society, Economy)",
                "score": 4,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 6-10; strongly integrates Biosphere (SDG 6.3 preventing drainage blockage) and Society (SDG 11.5 urban infrastructure protection and flood resilience).",
                "descope": "Add automated reporting of sediment volume for environmental municipal dashboards."
            },
            {
                "id": "SDG-02",
                "pillar": "ด้านความยั่งยืน (SDGs Feasibility 2.7)",
                "question": "ผลกระทบสิ่งแวดล้อม ขยะอิเล็กทรอนิกส์ และหลักเศรษฐกิจหมุนเวียน (E-Waste & 'Do No Harm' — SDG 6.3/12.4)?",
                "rationale": "ตรวจสอบการป้องกันขยะอิเล็กทรอนิกส์ตกค้างในท่อระบายน้ำ สารพิษรั่วไหล และระบบกู้คืนอุปกรณ์ที่ปลอดภัย 100%",
                "rubric": "1: ก่อให้เกิดอันตรายจากสารพิษ แบตเตอรี่รั่วไหล หรืออุปกรณ์หลุดลอยลงสู่แหล่งน้ำสาธารณะเป็นขยะมลพิษ\n2: อายุการใช้งานสั้น เซนเซอร์สึกกร่อนหรือเสียหายภายใน 2–3 สัปดาห์ และยากต่อการเก็บกู้คืน\n3: มีขยะอิเล็กทรอนิกส์ตามมาตรฐาน ต้องเปลี่ยนแบตเตอรี่เป็นรอบๆ แต่มีสายโยงป้องกันการสูญหายในท่อ\n4: ตัวกล่องทนทาน ใช้พลังงานต่ำ ใช้วัสดุรีไซเคิลได้ และมีสลิงสแตนเลสคู่ป้องกันการหลุดหาย\n5: หมุนเวียนสมบูรณ์และไร้รอยเท้าสิ่งแวดล้อม กู้คืนได้ 100% จากผิวดิน ใช้วัสดุไม่เป็นพิษและไม่ทิ้งขยะตกค้าง",
                "score": 3,
                "weight": 0.05,
                "evidence": "solution-details/solution-4.md lines 43; tethered crawler prevents hardware loss, but expensive LiDAR and embedded SBC risk electronic scrap loss if compromised by corrosive sewer humidity.",
                "descope": "Enclose the SBC in an IP67 sealed pelican-style enclosure with desiccant packs."
            }
        ]
    }
]

def main():
    os.makedirs("feasibility-outcome", exist_ok=True)
    out_path = os.path.join("feasibility-outcome", "jury_eval_data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote {len(data)} solutions to {out_path}")

if __name__ == "__main__":
    main()
