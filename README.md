# ML_Project
โปรเจคนี้มีชื่อว่า "Is It Spam?" หรือ "อีเมลนี้เป็นสแปมหรือไม่?" ทำขึ้นเพื่อตรวจสอบว่าอีเมลนั้นๆ เป็นสแปมหรือไม่
โดยในโปรเจคนี้ จะใช้ dataset จาก kaggle 2 ชุด แบ่งเป็น train-test dataset และ validate dataset 
และใช้ model จาก sklearn 2 ตัว คือ MLPClassifier และ RandomForestClassifier

ใน Source จะมี 4 ไฟล์
- Create_test_dataset.ipynb คือ ไฟล์ที่จะทำการแปลง validate dataset ให้อยู่ในรูปแบบเดียวกับ train-test dataset
- Dataset Reference.txt คือ ที่มาของ dataset เนื่องจากไฟล์มีขนาดใหญ่เกินไปที่อัพโหลด จึงให้เป็นที่มาแทน
- IsItSpamMLP.ipynb คือ ไฟล์ที่ใช้ MLPClassifier ซึ่งจะมีการใช้ joblib เพื่อบันทึกสิ่งที่ต้องการไว้
- IsItSpamRF.ipynb คือ ไฟล์ที่ใช้ RandomForestClassifier

ใน Demo จะมี 6 ไฟล์
- COL.sav คือ ไฟล์ที่บันทึกชื่อ column ของ dataset ไว้ โดยใช้ joblib ในการโหลด
- Demo_Ans.xlsx คือ ไฟล์ excel ที่บันทึกตัวอย่างอีเมลพร้อมคำตอบไว้ (ใช้เพื่อนำเสนอ)
- Demo_emails.xlsx คือ ไฟล์ excel ที่บันทึกตัวอย่างอีเมลไว้ (ใช้เพื่อนำเสนอ)
- IsItSpam.py คือ ไฟล์ที่รันเพื่อทดลองใช้งานโปรเจค
- MLP.sav คือ ไฟล์ที่บันทึก model ที่พร้อมใช้งานไว้ โดยใช้ joblib ในการโหลด
- STD.sav คือ ไฟล์ที่บันทึก StandardScaler ที่พร้อมใช้งานไว้ โดยใช้ joblib ในการโหลด

Medium Draft:
https://medium.com/@GlitR/machine-learning-project-assignment-%E0%B8%AD%E0%B8%B5%E0%B9%80%E0%B8%A1%E0%B8%A5%E0%B8%99%E0%B8%B5%E0%B9%89%E0%B9%80%E0%B8%9B%E0%B9%87%E0%B8%99%E0%B8%AA%E0%B9%81%E0%B8%9B%E0%B8%A1%E0%B9%84%E0%B8%AB%E0%B8%A1-1c856196bd43

โปรเจคนี้เป็นส่วนหนึ่งของวิชา machine learning ภาควิชาวิศวกรรมคอมพิวเตอร์ คณะวิศวกรรมศาสตร์ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
