# **Solution 1:** 

# CCTV on the road (Visual water flow) \+ ultrasonic to measure the flow rate of the canal \+ alarm

พยายามใช้ local sensor ที่มีก่อน

**Leverage point fit**

- QRT  
- Maintenance Queue

# **Function**

- ดู flow น้ำบนถนนด้วย CCTV ภายในช่วงที่มีแสง  
- ดู ระดับความสูงน้ำบนคลอง ( มีอยู๋แล้วแต่ต้องดึงข้อมูลมา )  
- สามารถวิเคราะห์ได้ว่าตรงไหนท่วม เพราะฝนตกหนัก หรือ เพราะท่อตัน  
- เก็บ data เพื่อนำมาวิเคราะห์จัดคิวลอกท่อ  
- เก็บ sample น้ำท่วม  5 นาที และดูว่าน้ำท่วมหรือไม่ เพื่อ ให้เจ้าหน้าที่สwามารถ response ได้ และสามารถเก็บ

# **Operation flow**

- Input :  
  - flow การไหลของน้ำ ในคลอง (Flow Rate Meter at Canal)  
  - ภาพวิดีโอจาก CCTV  
  - ความสูงของน้ำในคลอง (ultrasonic)  
- Process :   
  - from CCTV optical Flow   
  -  วิเคราะห์ flow rate ของน้ำในคลองจาก ultrasonic sensors ที่มีอยู่แล้ว   
  - เก็บข้อมูล sample นาน  5 นาที  
  - วิเคราะห์ว่าท่วม เพราะอะไร  
    -  (1) ฝนตกหนักน้ำระบายไม่ทัน  
    -  (2) ท่อตันไม่มี flow ที่ท่อน้ำเล็ก น้ำเลยระบายลงคลองไม่ได้  
- Output : แจ้ง alert เข้าหน่วยงานที่เกี่ยวข้อง


**Tech stack**

- Particle Tracking Velocimetry ( For CCTV flow rate)  
- Particle Image Velocimetry (CCTV)  
- Optical Flow (CCTV)  
- Data of each canal and every sewer attached with each canal.

**Strong point**

- ถ้าทำได้จะสามารถรู้ได้ว่าแต่ละท่อท่วมเพราะอะไร ตรงไหนเป็นปัญหา

**Weak point**

- บางท่ออยู่นอกขอบเขตของ CCTV