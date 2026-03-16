"""
flavor – 7 Günlük Takım Planı PDF (Türkçe)
Run: python3 create_plan_pdf_tr.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

OUTPUT = "/Users/ramiz/PycharmProjects/flavor/flavor_takim_plani.pdf"

ORANGE = colors.HexColor("#ff6000")
DARK   = colors.HexColor("#1d1d1f")
GRAY   = colors.HexColor("#6e6e73")
LIGHT  = colors.HexColor("#f5f5f7")
WHITE  = colors.white
BLUE   = colors.HexColor("#007aff")
GREEN  = colors.HexColor("#34c759")
PURPLE = colors.HexColor("#af52de")
BORDER = colors.HexColor("#e5e5ea")

MEMBER_HEX = {"Yaren": "#ff6000", "Esin": "#007aff", "Rana": "#34c759", "Ramiz": "#af52de"}
MEMBER_CLR = {"Yaren": ORANGE, "Esin": BLUE, "Rana": GREEN, "Ramiz": PURPLE}

def S(name, **kw):
    return ParagraphStyle(name, **kw)

sCover  = S("sCover",  fontSize=36, textColor=WHITE, fontName="Helvetica-Bold", leading=42, alignment=TA_CENTER)
sCoverS = S("cSub",    fontSize=13, textColor=colors.HexColor("#ffb380"), fontName="Helvetica", leading=20, alignment=TA_CENTER)
sH1     = S("sH1",     fontSize=20, textColor=DARK,  fontName="Helvetica-Bold", leading=26, spaceBefore=20, spaceAfter=6)
sH2     = S("sH2",     fontSize=14, textColor=DARK,  fontName="Helvetica-Bold", leading=20, spaceBefore=14, spaceAfter=5)
sH3     = S("sH3",     fontSize=11, textColor=GRAY,  fontName="Helvetica-Bold", leading=16, spaceBefore=10, spaceAfter=4)
sBody   = S("sBody",   fontSize=10, textColor=DARK,  fontName="Helvetica", leading=16, spaceAfter=4)
sBodyJ  = S("sBodyJ",  fontSize=10, textColor=DARK,  fontName="Helvetica", leading=17, spaceAfter=5, alignment=TA_JUSTIFY)
sQ      = S("sQ",      fontSize=10, textColor=ORANGE, fontName="Helvetica-Bold", leading=16, spaceBefore=10, spaceAfter=3)
sA      = S("sA",      fontSize=10, textColor=DARK,  fontName="Helvetica", leading=17, spaceAfter=6, leftIndent=12, alignment=TA_JUSTIFY)
sBullet = S("sBullet", fontSize=10, textColor=DARK,  fontName="Helvetica", leading=16, leftIndent=14, spaceAfter=3)
sSmall  = S("sSmall",  fontSize=9,  textColor=GRAY,  fontName="Helvetica", leading=13, spaceAfter=2)
sCenter = S("sCenter", fontSize=9,  textColor=GRAY,  fontName="Helvetica", leading=14, alignment=TA_CENTER)
sTableH = S("sTableH", fontSize=10, textColor=WHITE, fontName="Helvetica-Bold", leading=14, alignment=TA_CENTER)

def hr(c=ORANGE, t=1.5):
    return HRFlowable(width="100%", thickness=t, color=c, spaceAfter=10, spaceBefore=4)

def qa(soru, cevap):
    return [Paragraph(f"S: {soru}", sQ), Paragraph(cevap, sA)]

def gun_baslik(num, baslik, uye):
    hx = MEMBER_HEX.get(uye, "#ff6000")
    mc = MEMBER_CLR.get(uye, ORANGE)
    row = [[
        Paragraph(f"<font color='{hx}'><b>GUN {num}</b></font>", sH2),
        Paragraph(f"<b>{baslik}</b>", sH2),
        Paragraph(f"<font color='{hx}'><b>{uye}</b></font>", sH2),
    ]]
    t = Table(row, colWidths=[2.8*cm, 10.5*cm, 3.7*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), LIGHT),
        ("TOPPADDING",   (0,0),(-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
        ("LEFTPADDING",  (0,0),(-1,-1), 10),
        ("RIGHTPADDING", (0,0),(-1,-1), 10),
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("LINEBELOW",    (0,0),(-1,-1), 2.5, mc),
    ]))
    return t

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2.2*cm, rightMargin=2.2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)
story = []

# ── KAPAK ───────────────────────────────────────────────────────────────────
kapak = Table(
    [[Paragraph("flavor", sCover)],
     [Paragraph("7 Gunluk Takim Gelistirme Plani", sCoverS)],
     [Paragraph("CSE 220 Web Programlama  -  Bahar 2026", sCoverS)]],
    colWidths=[16.6*cm],
)
kapak.setStyle(TableStyle([
    ("BACKGROUND",   (0,0),(-1,-1), DARK),
    ("TOPPADDING",   (0,0),(-1,-1), 22),
    ("BOTTOMPADDING",(0,0),(-1,-1), 22),
    ("LEFTPADDING",  (0,0),(-1,-1), 20),
    ("RIGHTPADDING", (0,0),(-1,-1), 20),
]))
story.append(kapak)
story.append(Spacer(1, 18))

# Takim tablosu
story.append(Paragraph("Takim Uyeleri", sH1))
story.append(hr())
takim_data = [
    [Paragraph("<b>Ad</b>", sTableH), Paragraph("<b>Gorev</b>", sTableH),
     Paragraph("<b>Admin Kullanici</b>", sTableH), Paragraph("<b>Sifre</b>", sTableH)],
    [Paragraph("<font color='#ff6000'><b>Yaren</b></font>", sBody),
     Paragraph("Takim Lideri - Repo Sahibi - Temel Sablon + CSS", sBody),
     Paragraph("Yaren", sSmall), Paragraph("123456", sSmall)],
    [Paragraph("<font color='#007aff'><b>Esin</b></font>", sBody),
     Paragraph("Modeller - Ana Sayfa ve Liste Sablonlari", sBody),
     Paragraph("Esin", sSmall), Paragraph("123456", sSmall)],
    [Paragraph("<font color='#34c759'><b>Rana</b></font>", sBody),
     Paragraph("Admin Paneli - Ornek Veri - Detay Sablonu", sBody),
     Paragraph("Rana", sSmall), Paragraph("123456", sSmall)],
    [Paragraph("<font color='#af52de'><b>Ramiz</b></font>", sBody),
     Paragraph("View Fonksiyonlari - URL Yonlendirme - Hakkinda ve Iletisim", sBody),
     Paragraph("Ramiz", sSmall), Paragraph("123456", sSmall)],
]
tt = Table(takim_data, colWidths=[3*cm, 8.2*cm, 3*cm, 2.4*cm])
tt.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0),  DARK),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT]),
    ("GRID",          (0,0),(-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0),(-1,-1), 7),
    ("BOTTOMPADDING", (0,0),(-1,-1), 7),
    ("LEFTPADDING",   (0,0),(-1,-1), 9),
    ("RIGHTPADDING",  (0,0),(-1,-1), 9),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
]))
story.append(tt)
story.append(Spacer(1, 16))

# 7 gunluk plan tablosu
story.append(Paragraph("7 Gunluk Program", sH1))
story.append(hr())
program = [
    [Paragraph("<b>Gun</b>", sTableH), Paragraph("<b>Gorev</b>", sTableH),
     Paragraph("<b>Kim</b>", sTableH), Paragraph("<b>Dosyalar</b>", sTableH)],
    ["Gun 1", "Proje kurulumu ve GitHub",
     Paragraph("<font color='#ff6000'>Yaren</font>", sBody), "settings.py, urls.py"],
    ["Gun 2", "Veritabani modelleri",
     Paragraph("<font color='#007aff'>Esin</font>",  sBody), "models.py"],
    ["Gun 3", "Admin paneli ve ornek veri",
     Paragraph("<font color='#34c759'>Rana</font>",  sBody), "admin.py, seed.py"],
    ["Gun 4", "View fonksiyonlari ve URL yonlendirme",
     Paragraph("<font color='#af52de'>Ramiz</font>", sBody), "views.py, urls.py"],
    ["Gun 5", "Temel sablon ve CSS tasarim sistemi",
     Paragraph("<font color='#ff6000'>Yaren</font>", sBody), "base.html, style.css"],
    ["Gun 6", "Ana sayfa ve restoran liste sablonlari",
     Paragraph("<font color='#007aff'>Esin</font>",  sBody), "home.html, list.html"],
    ["Gun 7", "Detay, Hakkinda ve Iletisim sablonlari",
     Paragraph("<font color='#34c759'>Rana</font>",  sBody), "detail.html, about.html"],
]
for i, row in enumerate(program[1:], 1):
    if not isinstance(row[0], Paragraph):
        program[i][0] = Paragraph(f"<b>{row[0]}</b>", sBody)
    if not isinstance(row[3], Paragraph):
        program[i][3] = Paragraph(row[3], sSmall)

pt = Table(program, colWidths=[1.8*cm, 7*cm, 3*cm, 4.8*cm])
pt.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0),  DARK),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT]),
    ("GRID",          (0,0),(-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0),(-1,-1), 7),
    ("BOTTOMPADDING", (0,0),(-1,-1), 7),
    ("LEFTPADDING",   (0,0),(-1,-1), 8),
    ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
]))
story.append(pt)
story.append(PageBreak())

# ── settings.py ─────────────────────────────────────────────────────────────
story.append(Paragraph("settings.py — Detayli Aciklama", sH1))
story.append(hr())
story.append(Paragraph(
    "settings.py, Django projesinin merkezi yapilandirma dosyasidir. "
    "Django'ya nasil davranacagini anlatir: dosyalarin nerede oldugunu, "
    "hangi veritabaninin kullanilacagini, hangi uygulamalarin aktif oldugunu ve daha fazlasini. "
    "Buradaki her ayar tum projeyi etkiler.", sBodyJ))
story.append(Spacer(1, 8))

for s, c in [
    ("settings.py nedir ve neden vardir?",
     "Django'nun tum proje yapilandirmasini tek bir yerde saklamasi gerekir. "
     "Yollar, veritabani adlari veya gizli anahtarlar her dosyaya ayri ayri yazilmak yerine "
     "hepsi bir kez settings.py'de tanimlanir. Django'nun diger tum parcalari sunucu baslarken "
     "bu dosyayi otomatik olarak okur."),

    ("SECRET_KEY nedir ve neden gizli tutulmalidir?",
     "SECRET_KEY, Django'nun cerezleri, oturumları ve CSRF token'larini sifrelediginde kullandigi "
     "uzun bir rastgele dizedir. Birisi bu anahtari ele gecirirse kullanici oturumlarini taklit edebilir "
     "ve guvenlik onlemlerini atlayabilir. Gercek bir projede bu anahtar asla GitHub'a yuklenmemeli, "
     "ortam degiskeni olarak saklanmalidir. Bu demo projede sadece basitlik acisindan settings.py icindedir."),

    ("DEBUG = True ne yapar, ne zaman False olmalidir?",
     "DEBUG True oldugunda bir hata olursa Django; kod parcaciklari ve degisken degerlerini iceren "
     "ayrintili bir hata sayfasi gosterir. Gelistirme sirasinda son derece kullanislidir. "
     "Ancak internete yayinlamadan once mutlaka False yapilmalidir; cunku bu hata sayfalari "
     "ic kod yollarini ve hassas bilgileri herkesin gorebilecegi sekilde ifsa eder."),

    ("INSTALLED_APPS nedir, uygulamamizi eklemezsek ne olur?",
     "INSTALLED_APPS, projede aktif olan tum Django uygulamalarinin listesidir. "
     "Django bu listeyi sablonlari, statik dosyalari, modelleri ve yonetim komutlarini bulmak icin kullanir. "
     "'restaurants' buraya eklenmezse makemigrations calistirildiginda modeller bulunamaz "
     "ve veritabani tablolari olusturulamaz."),

    ("TEMPLATES ve DIRS ne ise yarar?",
     "TEMPLATES, Django'ya HTML dosyalarini nerede bulacagini ve nasil isleyecegini anlatir. "
     "DIRS anahtari, Django'nun sablon arayacagi klasorlerin listesidir. "
     "Biz bunu [BASE_DIR / 'templates'] olarak ayarladik; boylece en ust duzeydeki templates/ "
     "klasorundeki tum .html dosyalari otomatik olarak bulunur. "
     "Bu olmadan Django yalnizca her uygulamanin kendi templates/ alt klasorune bakar."),

    ("STATICFILES_DIRS nedir, CSS nasil yuklenir?",
     "Statik dosyalar; istek basina degismeyen CSS, JavaScript ve resimlerdir. "
     "STATICFILES_DIRS, Django'ya bu dosyalarin diskte nerede oldugunu soyler (static/ klasorumuz). "
     "STATIC_URL URL onekini belirler; style.css'e /static/css/style.css adresiyle ulasilir. "
     "Sablonlarda dogru URL'yi otomatik uretmek icin {% load static %} ve "
     "{% static 'css/style.css' %} yazariz."),

    ("DATABASES nedir, neden SQLite kullaniyoruz?",
     "DATABASES hangi veritabani motorunun kullanilacagini ve nasil baglanilacagini tanimlar. "
     "SQLite tum veritabanini sunucu gerektirmeden tek bir dosyada (db.sqlite3) saklar. "
     "Gelistirme ve kucuk demo projeleri icin idealdir. Gercek bir uretim sitesi icin "
     "PostgreSQL veya MySQL'e gecilir; settings.py degisikligi minimaldir, Python kodumuzun hicbiri degismez."),

    ("LANGUAGE_CODE ve TIME_ZONE ne anlama gelir?",
     "LANGUAGE_CODE, form dogrulama hatalari gibi yerlesik mesajlar icin varsayilan insan dilini ayarlar. "
     "TIME_ZONE, tarihlerin ve saatlerin nasil saklanip gosterilecegini kontrol eder. "
     "Europe/Istanbul olarak ayarladik; boylece yorum zaman damgalari UTC yerine yerel Turkiye saatinde gosterilir."),

    ("settings.py projenin geri kalaniyla nasil baglanti kurar?",
     "python manage.py runserver calistirildiginda Django, settings.py'yi bulmak icin "
     "DJANGO_SETTINGS_MODULE ortam degiskenini okur. Modeller, view'lar, sablonlar, admin ve "
     "migration'lar gibi tum bilesenler bu dosyadan otomatik olarak import eder. "
     "En ustteki BASE_DIR degiskeni, proje kok klasorune isaret eden bir pathlib.Path nesnesidir; "
     "diger tum mutlak yollar bu degisken uzerinden guvenli bicimde olusturulur."),
]:
    story += qa(s, c)

story.append(PageBreak())

# ── urls.py ──────────────────────────────────────────────────────────────────
story.append(Paragraph("urls.py — Detayli Aciklama", sH1))
story.append(hr())
story.append(Paragraph(
    "urls.py, Django'nun yonlendirme sistemidir. Bir kullanici URL'yi ziyaret ettiginde Django, "
    "urlpatterns listesini yukari'dan asagiya okur, ilk eslesen deseni bulur ve "
    "ilgili view fonksiyonunu cagirir. Bu projede iki urls.py dosyasi vardir.", sBodyJ))
story.append(Spacer(1, 8))

for s, c in [
    ("Neden iki urls.py dosyasi var?",
     "Ana urls.py, flavor/ yapilandirma klasorundedir ve gelen tum istekler icin giris noktasidir. "
     "Restoran ile ilgili URL'leri include() kullanarak restaurants uygulamasinin kendi urls.py'sine "
     "devreder. Bu her uygulamanin kendi icinde bagimsiz olmasini saglar; restaurants uygulamasi "
     "teorik olarak baska bir projeye degistirilmeden aktarilabilir."),

    ("path('', include('restaurants.urls')) ne anlama gelir?",
     "Bos dize '' 'ek bir seyle baslamayan herhangi bir URL'yi eslestir' anlamina gelir; yani sitenin koku. "
     "include(), Django'ya URL'nin geri kalanini daha fazla eslestirme icin restaurants/urls.py'ye "
     "gecirmesini soyler. Yani /restaurants/ istegi once ana urls.py'ye gelir, oradan "
     "restaurants/urls.py'ye iletilir ve 'restaurants/' deseni restaurant_list view'iyla eslestir."),

    ("urlpatterns sirasi onemli midir?",
     "Evet, sira cok onemlidir. Django desenleri yukari'dan asagiya kontrol eder ve ilk eslestiginde durur. "
     "Admin URL'si yanlistikla gecersiz kilinmasin diye genel desenlerden once gelmelidir. "
     "restaurants/urls.py'de restaurants/<int:pk>/ yolu restaurants/'den sonra listelenmelidir; "
     "eger daha genel bir desen once gelirse spesifik olana hic ulasilamaz. "
     "Her zaman daha spesifik yollari daha genel olanlardan once yazin."),

    ("<int:pk> URL deseninde ne anlama gelir?",
     "Bu bir URL donusturucusudur. <int:pk> URL'nin tam sayi gibi gorunen bir bolumunu yakalar "
     "ve pk (primary key, birincil anahtar) anahtar kelime argumani olarak view'a iletir. "
     "Kullanici /restaurants/7/ adresini ziyaret ettiginde Django 7 sayisini cikarir, Python int'ine "
     "donusturur ve restaurant_detail(request, pk=7) fonksiyonunu cagirir. "
     "Bolum bir sayi degilse Django view'u cagirmadan otomatik 404 dondurur."),

    ("Her path() icindeki name= parametresi neden onemlidir?",
     "name parametresi her URL desenine benzersiz bir etiket verir. URL'leri sablonlarda "
     "sabit dize olarak yazmak yerine (href='/restaurants/') {% url 'restaurant_list' %} yazariz. "
     "Django bu etiketi sablonu islerken gercek URL ile degistirir. Buyuk avantaji: "
     "URL yapisini degistirirsek (ornegin /restaurants/'den /mekanlar/'a) yalnizca urls.py'yi "
     "guncellememiz yeter, tum sablonlar otomatik guncellenir, hicbir sey bozulmaz."),

    ("Hicbir URL deseni eslesmezse ne olur?",
     "urlpatterns icindeki hicbir desen istenen URL ile eslesmezse Django bir Http404 istisna "
     "firlatir ve 404 Bulunamadi yaniti dondurur. DEBUG modunda Django'nun denedigi tum desenleri "
     "listeleyen sari bir hata sayfasi gosterilir. Uretimde (DEBUG=False) varsa ozel bir 404.html "
     "sablonunun icerigi gosterilir, yoksa duz metin hata mesaji verilir."),

    ("Bir URL istegi tarayicidan ekrana nasil gider?",
     "Adim 1: Tarayici sunucuya GET /restaurants/?q=pizza gonderir. "
     "Adim 2: Django ROOT_URLCONF'u settings.py'den okur ve flavor/urls.py'yi yukler. "
     "Adim 3: '' eslestigi icin Django tam URL'yi restaurants/urls.py'ye iletir. "
     "Adim 4: 'restaurants/' deseni restaurant_list view'iyla eslestir. "
     "Adim 5: Django request.GET'in {'q': 'pizza'} icerdiginde restaurant_list(request)'i cagirir. "
     "Adim 6: View veritabanini sorgular, bir context sozlugu olusturur ve render() cagirir. "
     "Adim 7: Django templates/ klasorunde list.html'i bulur, context ile doldurur "
     "ve bitirmis HTML'i tarayiciya gonderir."),
]:
    story += qa(s, c)

story.append(PageBreak())

# ── Admin Paneli ─────────────────────────────────────────────────────────────
story.append(Paragraph("Django Admin Paneli — Detayli Aciklama", sH1))
story.append(hr())
story.append(Paragraph(
    "Django'nun admin paneli, Django'nun otomatik olarak olusturdugu tam ozellikli bir yonetim "
    "arabirimidir. Tek bir satir SQL yazmadan web tarayicisi araciligiyla veritabani kayitlarini "
    "eklemenizi, duzenlemenizi, silmenizi ve aramanizi saglar.", sBodyJ))
story.append(Spacer(1, 8))

for s, c in [
    ("Admin paneline nasil girilir?",
     "python manage.py runserver komutuyla gelistirme sunucusunu baslatin, ardindan tarayicinizi "
     "acin ve http://127.0.0.1:8000/admin/ adresine gidin. Asagidaki superuser hesaplarinden "
     "biriyle giris yapin. Tum kayitli modelleri listeleyen bir kontrol paneli goreceksiniz."),

    ("Bu proje icin dort superuser hesabi hangileridir?",
     "Dort takim uyesinin de ayni sifreyle superuser erisimi vardir:\n"
     "  Yaren   /   sifre: 123456\n"
     "  Esin    /   sifre: 123456\n"
     "  Rana    /   sifre: 123456\n"
     "  Ramiz   /   sifre: 123456\n"
     "Bir superuser admin panelindeki her seye tam erisime sahiptir. "
     "Gercek bir uygulamada her kisi benzersiz ve guclu bir sifre kullanir."),

    ("Superuser, staff kullanici ve normal kullanici arasindaki fark nedir?",
     "Normal bir kullanici ana siteye giris yapabilir (giris formu varsa) ancak /admin/'e erisemez. "
     "Staff kullanici (is_staff=True) admin paneline giris yapabilir, ancak yalnizca izin verilen "
     "modelleri gorebilir. Superuser (is_superuser=True) tum izin kontrollerini atlar; her kaydi "
     "olusturabilir, duzenleyebilir, silebilir ve diger kullanicilari yonetebilir."),

    ("Admin uzerinden yeni bir restoran nasil eklenir?",
     "1. http://127.0.0.1:8000/admin/ adresine gidin ve giris yapin. "
     "2. Restaurants bolumunden 'Restaurants'a tiklayin. "
     "3. Sag ustteki '+ Ekle' dugmesine tiklayin. "
     "4. Ad, Aciklama, Adres, Telefon, Fiyat Aralig alanlarini doldurun. "
     "5. Acilir menuden bir Kategori ve Konum secin (yoksa once onlari ekleyin). "
     "6. Kaydet'e tiklayin. Restoran aninda web sitesinde gozukur."),

    ("Once Kategori veya Konum nasil eklenir?",
     "Admin kontrol panelinde Kategoriler ve Konumlar ayri ayri listelenir. "
     "Her birinin yanindaki '+ Ekle'ye tiklayin, ad veya sehir/ilce girin ve kaydedin. "
     "Kaydedildikten sonra restoran eklerken acilir menulerde gorununurler. "
     "Bir restorani kaydetmeden once en az bir Kategori ve bir Konum eklenmis olmalidir."),

    ("Bir restoran icin yorum nasil eklenir?",
     "Admin kenar cubugundan 'Yorumlar'a tiklayin, ardindan '+ Ekle' secin. "
     "Acilir menuden restorani secin, yazar adini girin, 1 ile 5 arasinda bir puan secin, "
     "yorum metnini yazin ve Kaydet'e tiklayin. Yorum aninda o restoranin detay sayfasinda gosterilir."),

    ("admin.py'deki list_display ne ise yarar?",
     "list_display, admin liste gorunumunde sutun olarak gorulecek alan adlarinin bir demetidir. "
     "RestaurantAdmin icin list_display = ['name', 'category', 'location', 'price_range', 'created_at'] "
     "ayarladik. Bu demek oluyor ki Restaurants'a tikladiginda her restoran icin bu bes sutunlu "
     "bir tablo gorursun. list_display olmadan Django tek sutunda yalnizca __str__ temsilini gosterir."),

    ("list_filter ne ise yarar?",
     "list_filter, liste gorunumunun sag tarafinda tiklanabilir filtre duge ekler. "
     "Restoranlar icin kategori, fiyat araligii ve konum sehrine gore filtreleme yapiyoruz. "
     "'Cafe'ye tiklayinca liste aninda yalnizca kafeleri gosterir. "
     "Cok sayida kayit oldugunda kayit bulmak cok daha hizli hale gelir."),

    ("search_fields ne ise yarar?",
     "search_fields, admin listesinin en ustune bir arama kutusu ekler. Bir sey yazip Enter'a "
     "bastiginda Django belirtilen alanlarda SQL LIKE sorgusu calistirir. Restoranlar icin "
     "isim, aciklama ve adreste arama yapiyoruz. 'Acibadem' yazinca adi, aciklamasi veya "
     "adresi bu kelimeyi iceren tum restoranlar bulunur."),

    ("Admin paneli bu proje icin neden onemlidir?",
     "8. hafta demosu icin admin paneli birincil veri yonetim araci. Ayri olustur/duzenle formlari "
     "yazmadan restoran, kategori, konum ve yorum eklememizi ve gostermemizi saglar. "
     "Ayrica odev gereksinimlerindeki CRUD (Olustur, Oku, Guncelle, Sil) islemlerini karsilar. "
     "Ogretim gorevlisi giris yapip verilerin veritabaninda dogru sekilde saklandigini dogrulayabilir."),

    ("@admin.register nedir, neden admin.site.register()'dan daha iyidir?",
     "@admin.register(Category), CategoryAdmin sinifini Category modeli icin admin sitesine "
     "kaydeden bir Python dekoratoru. Dosyanin sonuna admin.site.register(Category, CategoryAdmin) "
     "yazmakla tamamen aynidir, ancak model ile admin sinifi taniminin en ustunde gorsel olarak "
     "iliskilendirilmesi acisindan daha temizdir. Iki yontem de calisir; dekorator sadece modern konvansiyondur."),
]:
    story += qa(s, c)

story.append(Spacer(1, 10))

story.append(Paragraph("Hizli Referans — Admin Giris Bilgileri", sH2))
giris_data = [
    [Paragraph("<b>Kullanici Adi</b>", sTableH), Paragraph("<b>Sifre</b>", sTableH),
     Paragraph("<b>Rol</b>", sTableH), Paragraph("<b>Erisim Seviyesi</b>", sTableH)],
    [Paragraph("<font color='#ff6000'>Yaren</font>", sBody),  Paragraph("123456", sBody), Paragraph("Takim Lideri", sBody),  Paragraph("Superuser", sBody)],
    [Paragraph("<font color='#007aff'>Esin</font>",  sBody),  Paragraph("123456", sBody), Paragraph("Gelistirici", sBody),  Paragraph("Superuser", sBody)],
    [Paragraph("<font color='#34c759'>Rana</font>",  sBody),  Paragraph("123456", sBody), Paragraph("Gelistirici", sBody),  Paragraph("Superuser", sBody)],
    [Paragraph("<font color='#af52de'>Ramiz</font>", sBody),  Paragraph("123456", sBody), Paragraph("Gelistirici", sBody),  Paragraph("Superuser", sBody)],
]
ct = Table(giris_data, colWidths=[4*cm, 3.5*cm, 5*cm, 4.1*cm])
ct.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0),  DARK),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT]),
    ("GRID",          (0,0),(-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0),(-1,-1), 8),
    ("BOTTOMPADDING", (0,0),(-1,-1), 8),
    ("LEFTPADDING",   (0,0),(-1,-1), 10),
    ("RIGHTPADDING",  (0,0),(-1,-1), 10),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
]))
story.append(ct)
story.append(PageBreak())

# ── Gun gun gorev dagilimi ───────────────────────────────────────────────────
story.append(Paragraph("Gunluk Gorev Dagilimi", sH1))
story.append(hr())

gunler = [
    (1, "Proje Kurulumu ve GitHub", "Yaren", [
        ("GitHub deposu olustur", "Yaren GitHub'da 'flavor' adinda yeni bir public depo olusturur. Settings > Collaborators bolumune gidip Esin, Rana ve Ramiz'i GitHub kullanici adlariyla davet eder; boylece herkes kod gonderebilir."),
        ("Django projesini baslat", "Klonlanan klasorde: Python sanal ortami olustur, aktive et, Django'yu kur, pip freeze > requirements.txt ile bagimlilik kaydet. Ardindan django-admin startproject flavor . ile proje yapisini olustur. Sondaki nokta onemlidir; projeyi alt klasorde degil mevcut klasorde olusturur."),
        ("Restaurants uygulamasini olustur", "python manage.py startapp restaurants komutunu calistir. Ardindan settings.py dosyasindaki INSTALLED_APPS listesine 'restaurants' ekle. Bu Django'ya uygulamanin varligini bildirir."),
        ("settings.py'yi yapilandir", "TEMPLATES DIRS'i templates/ klasorune, STATICFILES_DIRS'i static/'e yonlendir. LANGUAGE_CODE'u en-us, TIME_ZONE'u Europe/Istanbul olarak ayarla. templates/ ve static/css/ klasorlerini elle olustur."),
        ("Ana urls.py'yi ayarla", "flavor/urls.py'yi duzenleyerek restaurants.urls'i include et. Bu ana yonlendiriciyi uygulamanin rotalariyla baglar. Ayrica bos bir restaurants/urls.py dosyasi olustur; aksi halde Python import hatasi verir."),
        ("Ilk commit ve push", "Tum dosyalari stage'e ekle, aciklayici bir commit mesaji yaz ve main dala gonder. Tum takim uyeleri depoyu klonlar."),
    ]),
    (2, "Veritabani Modelleri", "Esin", [
        ("Son kodu cek", "Baslamadan once Yaren'in kurulumunu almak icin git pull origin main calistir."),
        ("models.py'yi yaz", "Dort model sinifi tanimla: Category (name alani), Location (city + district), Restaurant (name, description, address, phone, price_range, Category'ye ForeignKey, Location'a ForeignKey, created_at) ve Review (Restaurant'a ForeignKey, author, rating 1-5, text, created_at). Restaurant modeline average_rating() ve price_display() yardimci metodlarini ekle."),
        ("Migration'lari calistir", "python manage.py makemigrations ile migration dosyasini (veritabani tablolarini aciklayan Python scripti) olustur. Ardindan python manage.py migrate ile tablolari db.sqlite3 icinde gercekten olustur."),
        ("Commit ve push", "models.py ve yeni migrations/ klasorunu commit'le. Migration dosyalarini asla silme; veritabani degisikliklerinin gecmisini temsil ederler."),
    ]),
    (3, "Admin Paneli ve Ornek Veri", "Rana", [
        ("Son kodu cek", "Esin'in modellerini almak icin git pull origin main calistir."),
        ("admin.py'yi yaz", "@admin.register kullanarak dort modelin tumunu kaydet. Her model sinifi icin list_display, list_filter ve search_fields'i yapilandir; boylece admin panelinde gezinmek kolaylasir."),
        ("Superuser olustur", "python manage.py createsuperuser calistir ve ilk admin hesabini kur. Diger uc takim uyesi seed scripti araciligiyla veya admin panelinden eklenecektir."),
        ("seed_acibadem.py'yi yaz", "Django ORM'ini kullanarak ornek restoran, kategori, konum ve yorum ekleyen bagimsiz bir Python scripti olustur. Scripti birkac kez calistirmak veri tekrarina yol acmasin diye get_or_create() kullan. python3 seed_acibadem.py ile calistir."),
        ("Admin'de dogrula", "Sunucuyu baslat, /admin/'i ac, giris yap ve tum tohumlanan verinin her modelin liste gorunumunde dogru sekilde gozuktugundan emin ol."),
        ("Commit ve push", "admin.py ve seed_acibadem.py'yi commit'le."),
    ]),
    (4, "View Fonksiyonlari ve URL Yonlendirme", "Ramiz", [
        ("Son kodu cek", "git pull origin main calistir."),
        ("views.py'yi yaz", "Bes view fonksiyonu yaz: home() en yeni 6 restorani ve tum kategorileri getirir. restaurant_list() GET parametrelerini (q, category, price) okur ve ORM filtreleri uygular. restaurant_detail() get_object_or_404 ile pk'ya gore bir restoran getirir. about() ve contact() sadece statik sayfalari render eder."),
        ("restaurants/urls.py'yi yaz", "Aciklayici adlarla bes URL deseni tanimla: home, restaurant_list, restaurant_detail (<int:pk> ile), about, contact. Bu adlar sablonlarda {% url 'ad' %} ile link olusturmak icin kullanilir."),
        ("Tarayicida test et", "Sunucuyu baslat. Sablonlar olmasa bile her URL'yi ziyaret etmek 'sablon bulunamadi' hatasi vermeli (iyi — view calisiyordur), asla 'URL bulunamadi' hatasi vermemeli."),
        ("Commit ve push", "views.py ve restaurants/urls.py'yi commit'le."),
    ]),
    (5, "Temel Sablon ve CSS", "Yaren", [
        ("Son kodu cek", "git pull origin main calistir."),
        ("base.html'i yaz", "templates/base.html olustur. Bu dosya ana duzeni tanimlar. Google Fonts'tan Inter fontunu yukler, CSS dosyasini baglar, navigasyon cubugu ve footer icerir. {% block content %}{% endblock %} yer tutucu her sayfanin kendi icerigini buraya eklemesini saglar. <main> etiketi blogu sarar; boylece CSS footer'i her zaman en alta iter."),
        ("style.css'i yaz", "static/css/style.css olustur. En uste :root icinde renkler, fontlar, bosluklar ve golge efektleri icin CSS degiskenleri (custom properties) tanimla. Navigasyon, hero, kartlar, filtre cubugu, detay sayfasi, footer ve responsive kircilma noktalarini stile donustur. body'ye display:flex, main'e flex:1 uygula; boylece footer her zaman en altta kalir."),
        ("Commit ve push", "templates/base.html ve static/css/style.css'i commit'le."),
    ]),
    (6, "Ana Sayfa ve Liste Sablonlari", "Esin", [
        ("Son kodu cek", "git pull origin main calistir."),
        ("home.html'i yaz", "templates/home.html olustur. {% extends 'base.html' %} ile basla. {% block content %} icine hero bolumunu ekle: bir etiket rozeti, buyuk YER / Routes basligi, alt baslik paragraf ve q parametresiyle GET istegi gonderen, restaurant_list URL'sine yonelen arama formu."),
        ("list.html'i yaz", "templates/restaurants/list.html olustur (once restaurants alt klasorunu olustur). En uste kategori seridini ekle (kategori id'ye gore filtreleyen linkler). Degistiginde otomatik gonderen kategori ve fiyat acilir menulu filtre cubugu formunu ekle. Restoran kartlarini render etmek icin {% for r in restaurants %} ile don. Bos durumu {% empty %} veya {% if restaurants %}...{% else %} bloguyla isle."),
        ("Commit ve push", "Iki sablon dosyasini da commit'le."),
    ]),
    (7, "Detay, Hakkinda ve Iletisim Sablonlari", "Rana", [
        ("Son kodu cek", "git pull origin main calistir."),
        ("detail.html'i yaz", "templates/restaurants/detail.html olustur. Ekmek kirtisi navigasyon, restoran adi, kategori etiketi, fiyat etiketi, aciklama ve adres + sehir + telefon iceren bir bilgi karti goster. Altinda yazar, tarih, yildiz puan ve yorum metnini gosteren {% for review in reviews %} dongusuyle yorumlar bolumu ekle. Kenarda average_rating() degerini goster."),
        ("about.html'i yaz", "templates/about.html olustur. Bir baslik ve CSS grid ile dizilmis uc ozellik karti (Kesfet, Degerlendirin, Konumlandir) iceren sade bir sayfa."),
        ("contact.html'i yaz", "templates/contact.html olustur. Proje e-postasi ve sehri iceren minimal bir sayfa."),
        ("Son takim testi", "Dort uye de son kodu ceker, sunucuyu baslatir ve her sayfayi test eder. Aramanin calismasi, kategori filtrelerinin calismasi, restoran kartina tiklandiktan sonra detay sayfasinin acilmasi ve admin panelinin tum verileri dogru gostermesi kontrol edilir."),
        ("Son commit", "Bir kisi (Yaren) son git pull'u yapar, ardindan kalan duzeltmeleri 'Week 8 demosu tamamlandi - tum sablonlar hazir' mesajiyla commit'ler ve gonderir."),
    ]),
]

for gun_num, baslik, uye, gorevler in gunler:
    story.append(gun_baslik(gun_num, baslik, uye))
    story.append(Spacer(1, 8))
    for gorev_baslik, gorev_aciklamasi in gorevler:
        story.append(Paragraph(f"<b>{gorev_baslik}</b>", sH3))
        story.append(Paragraph(gorev_aciklamasi, sBodyJ))
    story.append(Spacer(1, 10))

story.append(HRFlowable(width="100%", thickness=1, color=DARK, spaceAfter=8, spaceBefore=4))
story.append(Paragraph("flavor  -  CSE 220 Web Programlama  -  7 Gunluk Takim Plani  -  Bahar 2026", sCenter))

doc.build(story)
print(f"PDF kaydedildi: {OUTPUT}")
