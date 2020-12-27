#!/usr/bin/env python
# coding: utf-8

# In[43]:


ödev="Homework1"
print(f'{ödev} çözümü:')
ad_soyad="Burak demiralay"
yaş=25
boy=1.86
eğitim={"lise":"Bağcılar ATL", "Üniversite":"Dumlupınar Ünv."}
favori_renkler=["kırmızı,mavi,sarı"]
print(ad_soyad,yaş,boy,eğitim,favori_renkler)
Bilgiler=[ad_soyad,yaş,boy,eğitim,favori_renkler]
print("ad soyad: {}\nyaş: {}\nboy: {}\neğitim: {}\nfavori renkler: {}\n".format(Bilgiler[0],Bilgiler[1],Bilgiler[2],Bilgiler[3],Bilgiler[4]))
type(ad_soyad), type(yaş), type(boy), type(eğitim), type(favori_renkler)


# In[23]:


ödev="Homework2"
print(f'{ödev} çözümü:')
ad=input("First Name: ")
soyad=input("Last Name: ")
yas=int(input("Age :"))
tarih=input("Date of Birth: ")
user=[ad,soyad,yas,tarih]
print("First Name: {}, Last Name: {}, Age: {} ,Date of Birth: {}".format(user[0],user[1],user[2],user[3]))
if user[2] < 18:
    print("You can't go out because it's too dangerous!!")
else:
    print("you can go out to the street.")


# In[35]:


ödev="Homework3"
print(f'{ödev} çözümü:')
print("Welcome Player")
kelime=input("bir kelime gir :")
tahmin = []
while true:
    for i in enumerate(kelime):
        print("doğru" if i in tahmin else )
        


# In[50]:


ödev="proje"
print(f'{ödev} çözümü:')
ad=input("First Name: ")
soyad=input("Last Name: ")
print(f'Welcome {ad} {soyad}')
öğrenci=[ad,soyad]
exam=int(input("Midterm Exam :"))
final=int(input("Final :"))
Project=int(input("Project :"))
Notlar={"Midterm Exam":[exam], "final":[final], "Project":[Project]}
print(Notlar)
x=0.3
y=0.5
z=0.2
hesaplama=exam * x + final * y + Project * z
print(f'ortalma not = {hesaplama}')

if 90 < hesaplama <= 100:
    print("Öğrencinin harf notu AA")
elif 70 < hesaplama < 91:
    print("Öğrencinin harf notu BB")    
elif 50 < hesaplama < 71:    
    print("Öğrencinin harf notu CC")
elif 30 < hesaplama < 51:
    print("Öğrencinin harf notu DD")     
else:
    print("Öğrencinin harf notu FF")


# In[ ]:





# In[ ]:





# In[ ]:




