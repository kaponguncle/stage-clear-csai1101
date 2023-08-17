def discouter(price):
    if price >= 10000:
        discout = price*10/100
    elif price >= 3000:
        discout = price*5/100
    else:
        discout = 0
    return discout

# รายการที่ขาย
techNoDict = {
    "pc": 34990,
    "laptop": 23990,
    "smartphone": 9990,
    "printer": 3490,
    "tablet": 10900
}

# หน้าตาแสดงผล
print("***ยินดีต้อนรับเข้าสู่ร้าน TechNo Shopping***")
for product in techNoDict:
    print(" {} ------- {} บาท".format(product, techNoDict[product]))
print("*************************************")

try:
    selectMenu = str(input("กรุณาพิมพ์รายการที่ต้องการขาย: "))
    amountSelected = int(input("กรุณาใส่จำนวนสินค้าที่ซื้อ: "))
    print("*************************************")
    if selectMenu == "pc":
        pricePerUnit = techNoDict[selectMenu]
        price = pricePerUnit * amountSelected
        discouted = discouter(price)
        sumary = price-discouted
    elif selectMenu == "laptop":
        pricePerUnit = techNoDict[selectMenu]
        price = pricePerUnit * amountSelected
        discouted = discouter(price)
        sumary = price-discouted
    elif selectMenu == "smartphone":
        pricePerUnit = techNoDict[selectMenu]
        price = pricePerUnit * amountSelected
        discouted = discouter(price)
        sumary = price-discouted
    elif selectMenu == "printer":
        pricePerUnit = techNoDict[selectMenu]
        price = pricePerUnit * amountSelected
        discouted = discouter(price)
        sumary = price-discouted
    else:
        pricePerUnit = techNoDict[selectMenu]
        price = pricePerUnit * amountSelected
        discouted = discouter(price)
        sumary = price-discouted
    print("\n******สรุปรายการคำสั่งซื้อ******")
    print(f"สินค้าที่ซื้อ: {selectMenu}, {pricePerUnit} x {amountSelected}\nราคาก่อนได้รับส่วนลด: {price} บาท\nส่วนลดในการซื้อ: {round(discouted, 2)} บาท\nราคาที่ต้องชำระ: {sumary} บาท")
except IndexError:
    print("โปรแกรมหยุดการทำงาน!! ไม่พบรายการที่คุณป้อนเข้าไป ¯\_(ツ)_/¯")
    exit()
except KeyError:
    print("โปรแกรมหยุดการทำงาน!! ไม่พบรายการที่คุณป้อนเข้าไป ¯\_(ツ)_/¯")
    exit()
except ValueError:
    print("โปรแกรมหยุดการทำงาน!! กรุณาป้อนค่าให้ถูกต้อง ¯\_(ツ)_/¯")
    exit()
except KeyboardInterrupt:
    print("ขอบคุณสำหรับการใช้งานโปรแกรมของเรา _/|\_")
    exit()