# **Solution 3:** 

# Pipe Inspection Instrument using Sonar Frequency Profiling attaching with Robot

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
1. ติดตั้ง 360 Sonar Module ไว้ภายในท่อระบายน้ำ
2. ลากจูง 360 Sonar Module ด้วยหุ่นยนต์สำรวจท่อ
3. เก็บค่า 360 Sonar Signal ทำ Frequency Profiling ออกมาเป็น 3D Map ตามเส้นทางที่ผ่านไป
4. วิเคราะห์ความอุดตัน ความเสื่อมสภาพของท่อ ด้วยความละเอียด (สามารถเห็นภาพเปรียบเทียบ Cross Section เทียบกับขนาดท่อที่ Design ไว้)

**Tech stack**
- Sonar Frequency Profiling
- 360° Sonar Scan
- Profile Ring Processing

**Strong point**
- ตรวจตะกอนและ Debris ได้
- ได้ข้อมูล Profile รอบท่อ 360°
- ตรวจท่อที่มีน้ำอยู่ภายในได้

**Weak point**
- ต้องมีการลาก Sonar Head ผ่านภายในท่อ
- ต้องใช้ Float + Winching System
- ต้องใช้ Software Processing (ทำ Mapping ด้วยวิธีนี้มันยาก)