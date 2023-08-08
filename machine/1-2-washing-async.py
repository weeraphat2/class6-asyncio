"""
ต้องการซักผ้า 2 ตะกร้า แบบ asynchronous io
กระบวนการซักผ้า 1 ตะกร้า คือ
1. หยอดเหรียญเพื่อซักผ้า
2. นำผ้าเข้าเครื่องซักผ้า
3. ซักผ้าเสร็จ (ใช้เวลา 5 วินาที)

เนื่องจากมีเครื่องซักผ้าที่สามารถพร้อมใช้งานได้ 2 เครื่องพร้อมกัน 

เปลี่ยนการทำงานเป็นแบบ asynchronous io 
"""

import time

import asyncio

async def wash(basket):
    

async def main():
    

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')