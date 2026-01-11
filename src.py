import html   #escape kullanmak için kütüphane

ad= input("Adınız: ")
ad= html.escape(ad)   #kullanıcının girdiği özel karakterlerin komut yerine düz yazı olarak algılanması için

dersler=[] 
n=int(input("Kaç ders alıyorsunuz?: "))

for _ in range(n):   #alınan ders sayısı kadar girdi bekleyen döngü(Enter'la ayrılan)
 ders = input("Hangi dersleri alıyorsunuz?: ")
 dersler.append(ders)  #girdileri tek tek dersler listesine ekleme

biyografi=input("Biyografiniz: ")
biyografi= html.escape(biyografi)

html_parça=[]   #html dosyasına yazılacakları kapsayan liste
html_parça.append(f""" 
<!DOCTYPE html>
<head>
<title>Öğrenci Biyografi</title>
<style>
 body{{
   background-color: rgb(194, 154, 196);
   text-align: left;
 }}     
h1{{
   margin: 0;
   color: rgb(45, 19, 32)               
}}         
ol li, h2, p{{
  background: mistyrose;
  color: rgb(90, 19, 32);
  padding: 10px;
  margin-left: 20px;
}}
</style>
</head>
<body>
<h1>İsim: \n</h1>
<h2>{ad}</h2>
<h1>
<ol>Alınan dersler:""")

for ders in dersler:   #dersler listesindeki girdileri tek tek escapelemek için döngü
  esc_ders = html.escape(ders)
  html_parça.append(f"""<li>{esc_ders}</li>""")
html_parça.append(f"""
</ol>
</h1>
<h1>Biyografi: \n</h1>
<h2>{biyografi}</h2>
</body> """)

html = "\n".join(html_parça)   #html parçalarını aralarda satır atlayarak birleştirip tek değişkene atama


with open("index.html", "w", encoding="utf-8") as htmldos:   #write metoduyla açılan dosya oluşturma, Türkçe karakterlerin düzgün gözükmesi için utf-8 kodlaması
   htmldos.write(html)   #dosyanın içine html değişkeninin içeriğini yazdırma