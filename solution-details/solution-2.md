# **Solution 2 : Sewer Inspection by transmitter and receiver.Mapping Sewer profile มีตัวรับ ตัวส่ง แต่ยังไม่ confirm ตัวกลาง**

**Leverage point fit**

- QRT ( Data for make decision )  
- Maintenance Queue


# **Function**

- สามารถตรวจสอบสภาพของท่อได้ว่ามีสิ่งอุดตันท่อ   
- สามารถบอกได้ว่าท่อ segment นี้มีความสะอาดเท่าไหร่ใน Scale 0-10
- มีตัวส่งสัญญาณ และตัวรับสัญญาณ

# **Operation flow**

- Input :วาง Transmitter และ Receiver ไว้คนละฝั่งของช่วงท่อที่ต้องการตรวจสอบ  
-   
- Transmitter ส่งสัญญาณเสียงผ่านอากาศภายในท่อไปยัง Receiver  
-   
- Receiver รับสัญญาณเสียงที่ผ่านช่วงท่อ  
-   
- วิเคราะห์การลดลงของพลังงานเสียงที่เกิดขึ้นระหว่างการส่งและการรับสัญญาณ  
-   
- ประเมินระดับการอุดตันหรือสิ่งกีดขวางภายในช่วงท่อ  
-   
- จำแนกใน segment นี้ว่า good or bad ใน Scale (0-10)

  - ตำแหน่งLatitude and Longitude ของท่อ  
  - วางตัวส่งสัญญาณที่จุดต้น กับ ด้วยตัวรับสัญญาณที่จุดปลาย

- Process :   
  - วาง Transmitter และ Receiver ไว้คนละฝั่งของช่วงท่อที่ต้องการตรวจสอบ  
  - Transmitter ส่งสัญญาณเสียงผ่านอากาศภายในท่อไปยัง Receiver  
  - Receiver รับสัญญาณเสียงที่ผ่านช่วงท่อ  
  - วิเคราะห์การลดลงของพลังงานเสียงที่เกิดขึ้นระหว่างการส่งและการรับสัญญาณ  
  - ประเมินระดับการอุดตันหรือสิ่งกีดขวางภายในช่วงท่อ  
  - ประมวลผลออกมาเป็นมุมมองภาพตัดขวาว ของท่อ  
- Output :  
  - ผลการตรวจสอบของท่อในมุมมองภาพตัดขวางเพื่อดูเฉพาะความอุดตัน


**Tech stack**

- Airborne Acoustic Reflectometry  
- Signal Filtering.  

**Strong point**

- Fast  

**Weak point**

- Can’t use in high level water in pipe situation, low water height is still ok because high level of water implies that we operating in raining which is not corect.