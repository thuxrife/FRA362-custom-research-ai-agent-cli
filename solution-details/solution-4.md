# **Solution 4:** 

# Pipe Inspection Instrument using LiDAR SLAM attaching with Robot

# **Requirement**
For Pipe Maintanance
- ทำให้การทำความสะอาดท่อที่สะอาดเกิดขึ้นน้อยลง 

For Empty case (Where problem Naturally Receded)
- สามารถยืนยันได้ว่าบริเวณนั้นไม่มีน้ำท่วมอยู่

# **Constrains**
For Pipe Maintanance
- น้ำฝนและน้ำเสีย อยู่ในท่อเดียวกัน
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
1. ติดตั้ง 3D LiDAR ไว้ใน Inspection Robot
2. ลากจูง 3D LiDAR ด้วยหุ่นยนต์สำรวจท่อ
3. เก็บค่า Point Cloud
4. ทำ SLAM ให้ได้ pipe profiling

**Tech stack**
- 3D LiDAR
- Laser Scanning
- Point Cloud Processing

**Strong point**
- ได้ข้อมูลเป็น 3D
- วัดตะกอนและสภาพท่อเป็นข้อมูลเชิงปริมาณได้
- ตรวจ Buildup และ Debris ได้

**Weak point**
- ไม่สามาถใช้งานขณะมีน้ำเต็มท่อได้ (Point Cloud ไม่สามารถทะลุน้ำได้)
- ข้อมูลมีปริมาณมาก ต้องใช้เวลา Processing (Point Cloud ใช้ processing power เยอะ)
- ต้องจัดเรียงและประมวลผล Point Cloud