# **Solution 1:** 

# Pipe Inspection Robot using CCTV for profiling pipe

# **Requirement**
For Pipe Maintanance
- ทำให้การทำความสะอาดท่อที่สะอาดเกิดขึ้นน้อยลง 

For Empty case (Where problem Naturally Receded)
- สามารถยืนยันได้ว่าบริเวณนั้นไม่มีน้ำท่วมอยู่

# **Constrains**
For Pipe Maintanance
- น้ำฝนและน้ำเสีย อยู่ในท่อเดียวกัน
- มีน้ำอยู่ในท่อไม่เกิน 20%
- การวางท่ออยู่ใต้ดินทั้งหมด
- ท่อมี เส้นผ่านศูนย์กลาง ความยาว และความลึก ไม่เท่ากันในแต่ละพื้นที่
- สิ่งที่อุดตันท่อในแต่ละพื้นที่่ต่างกัน
- ขนาดปากท่อบนพื้นผิวถนนของแต่ละพื้นที่่ไม่เท่ากัน

For Empty case (Where problem Naturally Receded)
- แต่ละพื้นที่มีเซนเซอร์ติดอยู่แล้วเพื่อดูน้ำท่วมบนถนนไม่เท่ากัน
- กล้อง CCTV ของแต่ละพื้นที่มีไม่เท่ากัน และไม่สามารถดูครอบคลุมได้ทุกพื้นที่
- ท่อหลายท่อเชืื่อมกับคลองเดียวกัน
- ขนาดปากท่อบนผิวถนนของแต่ละพื้นที่ไม่เท่ากัน.

# **Operation flow**
1. ปล่อยหุ่นยนต์ลงท่อ
2. ใช้ CCTV streaming สภาพภายในของท่อระบายน้ำ
3. ใช้ภาพ Video ที่รับมาจาก CCTV ทำ Object Detection หารอยรั่ว ร่องรอยความเสียหายของท่อ และ สิ่งอุดตัน
4. ทำเป็น Map Profile ออกมา ด้วยการปักหมุดตำแหน่ง object ภายในท่อ

**Tech stack**
- 4K PTZ Camera
- High-Power LED Array
- YOLOv8 AI Detection 
- Real-time Video Streaming
- Wheeled Crawler Platform (ส่วนล้อของหุ่นยนต์)

**Strong point**
- เห็นภาพจริงภายในท่อ HD
- AI ตรวจหาความเสียหายอัตโนมัติ
- ไม่ต้องระบายน้ำออกจากท่อ
- ราคาต่ำกว่า Sonar System 3–10 เท่า

**Weak point**
- ต้องการน้ำใสสำหรับกล้อง
- สาย Tether จำกัดระยะทาง (สาย Data)
- ไม่ได้ข้อมูล 3D Profile ท่อ
- ต้องใช้ AI Software Processing