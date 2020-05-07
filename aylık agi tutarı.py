
       
print("arac türü : \n (1)-Binek araç \n (2)-Ticari araç")      
arac=input("araç türünü seçiniz(1)/(2)?")
if arac=="1":
     yas=input("araç yaşı: \n (1) 1-3 yaş \n (2) 4-7 yaş \n (3) 7 yaş üzeri \n araç yaşını giriniz:")
     if yas=="1":
         t=100*1.75
         h=float(input("Motor hacmi değerini giriniz"))
         if h<=1300:
             x=float(t)*2
             print("Vergi ücretiniz:",x)
         elif h<=1600:
             y=int(t)*3
             print("Vergi ücretiniz:",y)
             
         elif h<=2000:
             xx=int(t)*4
             print("Vergi ücretiniz:",xx)
             
         elif h>2000:
             yy=int(t)*5
             print("Vergi ücretiniz:",yy)
             
         else :
             print("Bir şeyleri yanlış girdiniz lütfen tekrar deneyiniz")
             
                           
     elif yas=="2":
         y=100*1.50
         h=float(input("Motor hacmi değerini giriniz:"))
         if h<=1300:
             x=float(y)*2
             print("Vergi ücretiniz:",x)
         elif h<=1600:
             y=float(y)*3
             print("Vergi ücretiniz:",y)
             
         elif h<=2000:
             xx=float(y)*4
             print("Vergi ücretiniz:",xx)
             
         elif h>2000:
             yy=float(y)*5
             print("Vergi ücretiniz:",yy)
             
         else :
             print("Bir şeyleri yanlış girdiniz lütfen tekrar deneyiniz")
                      
     elif yas=="3":
         z=100*1.25
         h=float(input("Motor hacmi değerini giriniz"))
         if h<=1300:
             x=float(z)*2
             print("Vergi ücretiniz:",x)
         elif h<=1600:
             y=float(z)*3
             print("Vergi ücretiniz:",y)
             
         elif h<=2000:
             xx=float(z)*4
             print("Vergi ücretiniz:",xx)
             
         elif h>2000:
             yy=float(z)*5
             print("Vergi ücretiniz:",yy)
             
         else :
             print("Bir şeyleri yanlış girdiniz lütfen tekrar deneyiniz")         

             
elif arac=="2":
    yas=input("araç yaşı: \n (1) 1-3 yaş \n (2) 4-7 yaş \n (3) 7 yaş üzeri \n araç yaşını giriniz:")
    if yas=="1":
         t=150*1.75
         h=float(input("Motor hacmi değerini giriniz"))
         if h<=1300:
             x=float(t)*2
             print("Vergi ücretiniz:",x)
         elif h<=1600:
             y=int(t)*3
             print("Vergi ücretiniz:",y)
             
         elif h<=2000:
             xx=int(t)*4
             print("Vergi ücretiniz:",xx)
             
         elif h>2000:
             yy=int(t)*5
             print("Vergi ücretiniz:",yy)
             
         else :
             print("Bir şeyleri yanlış girdiniz lütfen tekrar deneyiniz")
             
                           
    elif yas=="2":
         y=150*1.50
         h=float(input("Motor hacmi değerini giriniz"))
         if h<=1300:
             x=float(y)*2
             print("Vergi ücretiniz:",x)
         elif h<=1600:
             y=float(y)*3
             print("Vergi ücretiniz:",y)
             
         elif h<=2000:
             xx=float(y)*4
             print("Vergi ücretiniz:",xx)
             
         elif h>2000:
             yy=float(y)*5
             print("Vergi ücretiniz:",yy)
             
         else :
             print("Bir şeyleri yanlış girdiniz lütfen tekrar deneyiniz")
                      
    elif yas=="3":
         z=150*1.25
         h=float(input("Motor hacmi değerini giriniz"))
         if h<=1300:
             x=float(z)*2
             print("Vergi ücretiniz:",x)
         elif h<=1600:
             y=float(z)*3
             print("Vergi ücretiniz:",y)
             
         elif h<=2000:
             xx=float(z)*4
             print("Vergi ücretiniz:",xx)
             
         elif h>2000:
             yy=float(z)*5
             print("Vergi ücretiniz:",yy)
             
         else :
             print("Bir şeyleri yanlış girdiniz lütfen tekrar deneyiniz")         
   
    else :
        print("aracın yaşını yanlış girdiniz.Lütfen tekrar deneyiniz")
        
else:
    print("araç türünü yanlış seçtiniz..")     