"""
flavor – Adim Adim Takim Rehberi (Turkce, kod vurgulama yok)
Run: python3 create_stepbystep_pdf.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

OUTPUT = "/Users/ramiz/PycharmProjects/flavor/flavor_adim_adim.pdf"

ORANGE = colors.HexColor("#ff6000")
DARK   = colors.HexColor("#1d1d1f")
GRAY   = colors.HexColor("#6e6e73")
LIGHT  = colors.HexColor("#f5f5f7")
WHITE  = colors.white
BLUE   = colors.HexColor("#007aff")
GREEN  = colors.HexColor("#34c759")
PURPLE = colors.HexColor("#af52de")
BORDER = colors.HexColor("#e5e5ea")
CODEBG = colors.HexColor("#f8f8f8")

MEMBER_HEX = {"Yaren":"#ff6000","Esin":"#007aff","Rana":"#34c759","Ramiz":"#af52de"}
MEMBER_CLR = {"Yaren":ORANGE,"Esin":BLUE,"Rana":GREEN,"Ramiz":PURPLE}

def S(name,**kw): return ParagraphStyle(name,**kw)

sCover  = S("sCover", fontSize=34,textColor=WHITE,fontName="Helvetica-Bold",leading=40,alignment=TA_CENTER)
sCoverS = S("cS",     fontSize=13,textColor=colors.HexColor("#ffb380"),fontName="Helvetica",leading=20,alignment=TA_CENTER)
sH1     = S("sH1",    fontSize=18,textColor=DARK, fontName="Helvetica-Bold",leading=24,spaceBefore=18,spaceAfter=6)
sH2     = S("sH2",    fontSize=13,textColor=DARK, fontName="Helvetica-Bold",leading=18,spaceBefore=12,spaceAfter=4)
sH3     = S("sH3",    fontSize=10,textColor=GRAY, fontName="Helvetica-Bold",leading=15,spaceBefore=8, spaceAfter=3)
sBody   = S("sBody",  fontSize=10,textColor=DARK, fontName="Helvetica",leading=16,spaceAfter=3)
sNote   = S("sNote",  fontSize=9, textColor=GRAY, fontName="Helvetica",leading=14,spaceAfter=3,leftIndent=8)
sCode   = S("sCode",  fontSize=8, textColor=DARK, fontName="Courier",leading=12,spaceAfter=0,
            leftIndent=6,rightIndent=4,backColor=CODEBG)
sCmd    = S("sCmd",   fontSize=8.5,textColor=colors.HexColor("#003d99"),fontName="Courier-Bold",
            leading=13,spaceAfter=0,leftIndent=6,backColor=colors.HexColor("#eef4ff"))
sStep   = S("sStep",  fontSize=10,textColor=ORANGE,fontName="Helvetica-Bold",leading=15,spaceBefore=8,spaceAfter=2)
sCenter = S("sCtr",   fontSize=9, textColor=GRAY, fontName="Helvetica",leading=13,alignment=TA_CENTER)
sTH     = S("sTH",    fontSize=10,textColor=WHITE,fontName="Helvetica-Bold",leading=14,alignment=TA_CENTER)

def hr(c=ORANGE,t=1.2):
    return HRFlowable(width="100%",thickness=t,color=c,spaceAfter=8,spaceBefore=3)

def gun_bar(num, baslik, uye):
    hx = MEMBER_HEX.get(uye,"#ff6000")
    mc = MEMBER_CLR.get(uye,ORANGE)
    row = [[
        Paragraph(f"<font color='{hx}'><b>GUN {num}</b></font>", sH1),
        Paragraph(f"<b>{baslik}</b>", sH1),
        Paragraph(f"<font color='{hx}'><b>{uye}</b></font>", sH1),
    ]]
    t = Table(row, colWidths=[2.6*cm,10.5*cm,4.0*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), LIGHT),
        ("TOPPADDING",   (0,0),(-1,-1), 9),
        ("BOTTOMPADDING",(0,0),(-1,-1), 9),
        ("LEFTPADDING",  (0,0),(-1,-1), 10),
        ("RIGHTPADDING", (0,0),(-1,-1), 10),
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("LINEBELOW",    (0,0),(-1,-1), 3, mc),
    ]))
    return t

def adim(num, metin):
    return Paragraph(f"<b>Adim {num}:</b>  {metin}", sStep)

def terminal(*satirlar):
    """Mavi tonlu terminal komut blogu"""
    els = [Spacer(1,3)]
    for s in satirlar:
        els.append(Paragraph(
            s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"),
            sCmd
        ))
    els.append(Spacer(1,6))
    return els

def kod(*satirlar):
    """Acik gri arka planli kod blogu"""
    els = [Spacer(1,3)]
    for s in satirlar:
        els.append(Paragraph(
            s.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"),
            sCode
        ))
    els.append(Spacer(1,6))
    return els

def dosya_baslik(isim):
    return Paragraph(f"Dosya: <b>{isim}</b>", sH3)

# ─── BELGE ────────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)
story = []

# ══ KAPAK ════════════════════════════════════════════════════════════════════
kapak = Table(
    [[Paragraph("flavor", sCover)],
     [Paragraph("Adim Adim Gelistirme Rehberi", sCoverS)],
     [Paragraph("CSE 220 Web Programlama  -  Bahar 2026", sCoverS)]],
    colWidths=[17*cm],
)
kapak.setStyle(TableStyle([
    ("BACKGROUND",   (0,0),(-1,-1), DARK),
    ("TOPPADDING",   (0,0),(-1,-1), 24),
    ("BOTTOMPADDING",(0,0),(-1,-1), 24),
    ("LEFTPADDING",  (0,0),(-1,-1), 20),
    ("RIGHTPADDING", (0,0),(-1,-1), 20),
]))
story.append(kapak)
story.append(Spacer(1,16))

# Renk aciklamasi
story.append(Paragraph("Renk Kodu", sH2))
story.append(hr())
renk_data = [
    [Paragraph("<b>Uye</b>",sTH), Paragraph("<b>Gorev Ozeti</b>",sTH),
     Paragraph("<b>Admin</b>",sTH), Paragraph("<b>Sifre</b>",sTH)],
    [Paragraph("<font color='#ff6000'><b>Yaren</b></font>",sBody),
     Paragraph("Takim Lideri - Kurulum - Temel Sablon - CSS",sBody),
     Paragraph("Yaren",sNote), Paragraph("123456",sNote)],
    [Paragraph("<font color='#007aff'><b>Esin</b></font>",sBody),
     Paragraph("Modeller - Ana Sayfa - Liste Sablonu",sBody),
     Paragraph("Esin",sNote), Paragraph("123456",sNote)],
    [Paragraph("<font color='#34c759'><b>Rana</b></font>",sBody),
     Paragraph("Admin - Ornek Veri - Detay Sablonu",sBody),
     Paragraph("Rana",sNote), Paragraph("123456",sNote)],
    [Paragraph("<font color='#af52de'><b>Ramiz</b></font>",sBody),
     Paragraph("View'lar - URL - Hakkinda - Iletisim",sBody),
     Paragraph("Ramiz",sNote), Paragraph("123456",sNote)],
]
rt = Table(renk_data, colWidths=[3*cm,8*cm,3*cm,3*cm])
rt.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,0),DARK),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE,LIGHT]),
    ("GRID",(0,0),(-1,-1),0.5,BORDER),
    ("TOPPADDING",(0,0),(-1,-1),7),
    ("BOTTOMPADDING",(0,0),(-1,-1),7),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("RIGHTPADDING",(0,0),(-1,-1),8),
    ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
]))
story.append(rt)
story.append(Spacer(1,10))
story.append(Paragraph("Mavi kutular = Terminal komutu     Gri kutular = Yazilacak kod", sNote))
story.append(PageBreak())

# ══ GUN 1 — YAREN ════════════════════════════════════════════════════════════
story.append(gun_bar(1,"Proje Kurulumu ve GitHub","Yaren"))
story.append(Spacer(1,10))

story.append(adim(1,"GitHub'da 'flavor' adinda public depo olustur. Settings > Collaborators'dan Esin, Rana ve Ramiz'i davet et."))
story.append(Spacer(1,6))

story.append(adim(2,"PyCharm terminalini ac ve su komutlari sirayla yaz:"))
story += terminal(
    "mkdir flavor",
    "cd flavor",
    "python3 -m venv venv",
    "source venv/bin/activate",
    "pip install django",
    "pip freeze > requirements.txt",
    "django-admin startproject flavor .",
    "python manage.py startapp restaurants",
    "python manage.py migrate",
)

story.append(adim(3,"PyCharm'da sol panelden flavor/settings.py dosyasini ac. Dosyanin EN ALTINA su satirlari ekle:"))
story += kod(
    "LANGUAGE_CODE = 'en-us'",
    "TIME_ZONE = 'Europe/Istanbul'",
    "",
    "TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']",
    "",
    "STATICFILES_DIRS = [BASE_DIR / 'static']",
    "STATIC_URL = '/static/'",
)
story.append(Paragraph("Ayrica INSTALLED_APPS listesine 'restaurants' satirini ekle:", sNote))
story += kod(
    "INSTALLED_APPS = [",
    "    'django.contrib.admin',",
    "    'django.contrib.auth',",
    "    'django.contrib.contenttypes',",
    "    'django.contrib.sessions',",
    "    'django.contrib.messages',",
    "    'django.contrib.staticfiles',",
    "    'restaurants',    # <-- bu satiri ekle",
    "]",
)

story.append(adim(4,"flavor/urls.py dosyasini tamamen asagidakiyle degistir:"))
story += kod(
    "from django.contrib import admin",
    "from django.urls import path, include",
    "",
    "urlpatterns = [",
    "    path('admin/', admin.site.urls),",
    "    path('', include('restaurants.urls')),",
    "]",
)

story.append(adim(5,"templates/ ve static/css/ klasorlerini olustur:"))
story += terminal(
    "mkdir templates",
    "mkdir -p static/css",
)

story.append(adim(6,"Superuser (admin) hesabi olustur:"))
story += terminal("python manage.py createsuperuser")
story.append(Paragraph("Kullanici adi: Yaren   E-posta: yaren@flavor.com   Sifre: 123456", sNote))

story.append(adim(7,"GitHub'a gonder:"))
story += terminal(
    "git init",
    "git add .",
    "git commit -m 'Gun 1: Django kurulumu tamamlandi'",
    "git branch -M main",
    "git remote add origin https://github.com/KULLANICI_ADI/flavor.git",
    "git push -u origin main",
)
story.append(Paragraph("Diger uc kisi depoyu klonlar: git clone https://github.com/.../flavor.git", sNote))
story.append(PageBreak())

# ══ GUN 2 — ESIN ════════════════════════════════════════════════════════════
story.append(gun_bar(2,"Veritabani Modelleri","Esin"))
story.append(Spacer(1,10))

story.append(adim(1,"Son kodu cek ve gerekli kurulumu yap:"))
story += terminal(
    "git pull origin main",
    "source venv/bin/activate",
    "pip install -r requirements.txt",
)

story.append(adim(2,"restaurants/models.py dosyasini tamamen asagidakiyle degistir:"))
story += kod(
    "from django.db import models",
    "from django.db.models import Avg",
    "",
    "",
    "class Category(models.Model):",
    "    name = models.CharField(max_length=100)",
    "",
    "    class Meta:",
    "        verbose_name_plural = 'Categories'",
    "",
    "    def __str__(self):",
    "        return self.name",
    "",
    "",
    "class Location(models.Model):",
    "    city     = models.CharField(max_length=100)",
    "    district = models.CharField(max_length=100)",
    "",
    "    def __str__(self):",
    "        return f'{self.district}, {self.city}'",
    "",
    "",
    "PRICE_CHOICES = [",
    "    ('1', 'EUR'),",
    "    ('2', 'EUR EUR'),",
    "    ('3', 'EUR EUR EUR'),",
    "]",
    "",
    "",
    "class Restaurant(models.Model):",
    "    name        = models.CharField(max_length=200)",
    "    description = models.TextField()",
    "    address     = models.CharField(max_length=300)",
    "    phone       = models.CharField(max_length=20)",
    "    price_range = models.CharField(max_length=1, choices=PRICE_CHOICES, default='2')",
    "    category    = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)",
    "    location    = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)",
    "    created_at  = models.DateTimeField(auto_now_add=True)",
    "",
    "    def __str__(self):",
    "        return self.name",
    "",
    "    def average_rating(self):",
    "        avg = self.reviews.aggregate(avg=Avg('rating'))['avg']",
    "        return round(avg, 1) if avg else None",
    "",
    "    def price_display(self):",
    "        return dict(PRICE_CHOICES).get(self.price_range, 'EUR EUR')",
    "",
    "",
    "class Review(models.Model):",
    "    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,",
    "                                   related_name='reviews')",
    "    author     = models.CharField(max_length=100)",
    "    rating     = models.IntegerField(choices=[(i, i) for i in range(1, 6)])",
    "    text       = models.TextField()",
    "    created_at = models.DateTimeField(auto_now_add=True)",
    "",
    "    def __str__(self):",
    "        return f'{self.author} - {self.restaurant.name} ({self.rating})'",
)

story.append(adim(3,"Migration'lari olustur ve calistir:"))
story += terminal(
    "python manage.py makemigrations",
    "python manage.py migrate",
)

story.append(adim(4,"GitHub'a gonder:"))
story += terminal(
    "git add restaurants/models.py restaurants/migrations/",
    "git commit -m 'Gun 2: Veritabani modelleri eklendi'",
    "git push",
)
story.append(PageBreak())

# ══ GUN 3 — RANA ════════════════════════════════════════════════════════════
story.append(gun_bar(3,"Admin Paneli ve Ornek Veri","Rana"))
story.append(Spacer(1,10))

story.append(adim(1,"Son kodu cek:"))
story += terminal("git pull origin main","source venv/bin/activate")

story.append(adim(2,"restaurants/admin.py dosyasini tamamen asagidakiyle degistir:"))
story += kod(
    "from django.contrib import admin",
    "from .models import Category, Location, Restaurant, Review",
    "",
    "",
    "@admin.register(Category)",
    "class CategoryAdmin(admin.ModelAdmin):",
    "    list_display  = ['name']",
    "    search_fields = ['name']",
    "",
    "",
    "@admin.register(Location)",
    "class LocationAdmin(admin.ModelAdmin):",
    "    list_display  = ['city', 'district']",
    "    list_filter   = ['city']",
    "    search_fields = ['city', 'district']",
    "",
    "",
    "@admin.register(Restaurant)",
    "class RestaurantAdmin(admin.ModelAdmin):",
    "    list_display  = ['name', 'category', 'location', 'price_range', 'created_at']",
    "    list_filter   = ['category', 'price_range', 'location__city']",
    "    search_fields = ['name', 'description', 'address']",
    "",
    "",
    "@admin.register(Review)",
    "class ReviewAdmin(admin.ModelAdmin):",
    "    list_display  = ['restaurant', 'author', 'rating', 'created_at']",
    "    list_filter   = ['rating', 'restaurant']",
    "    search_fields = ['author', 'text']",
)

story.append(adim(3,"Proje kok klasorunde (flavor/ ile ayni seviyede) seed_acibadem.py dosyasini olustur ve asagidaki kodu yaz:"))
story += kod(
    "import os",
    "import django",
    "",
    "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flavor.settings')",
    "django.setup()",
    "",
    "from restaurants.models import Category, Location, Restaurant, Review",
    "",
    "# Konum olustur",
    "loc, _ = Location.objects.get_or_create(city='Istanbul', district='Acibadem')",
    "",
    "# Kategoriler",
    "cafe,      _ = Category.objects.get_or_create(name='Cafe')",
    "fastfood,  _ = Category.objects.get_or_create(name='Fast Food')",
    "kebab,     _ = Category.objects.get_or_create(name='Kebab')",
    "japanese,  _ = Category.objects.get_or_create(name='Japanese')",
    "italian,   _ = Category.objects.get_or_create(name='Italian')",
    "seafood,   _ = Category.objects.get_or_create(name='Seafood')",
    "bakery,    _ = Category.objects.get_or_create(name='Bakery')",
    "turkish,   _ = Category.objects.get_or_create(name='Turkish Cuisine')",
    "",
    "# Restoranlar",
    "restaurants_data = [",
    "    {'name': 'Starbucks Acibadem',",
    "     'description': 'Acibadem Universitesi yaninda rahat kafe.',",
    "     'address': 'Acibadem Cad. No:12', 'phone': '+90 216 340 10 10',",
    "     'price_range': '2', 'category': cafe, 'location': loc},",
    "    {'name': 'McDonalds Acibadem',",
    "     'description': 'Hizli servis burger restorani.',",
    "     'address': 'Acibadem Mah. Cevizlik Sok. No:3', 'phone': '+90 216 340 20 20',",
    "     'price_range': '1', 'category': fastfood, 'location': loc},",
    "    {'name': 'Durumcu Ahmet Usta',",
    "     'description': 'El yapimi tavuk durum ve lavas.',",
    "     'address': 'Acibadem Cad. No:47', 'phone': '+90 216 341 55 55',",
    "     'price_range': '1', 'category': kebab, 'location': loc},",
    "    {'name': 'Sushi Co Acibadem',",
    "     'description': 'Modern Japon mutfagi, taze sushi.',",
    "     'address': 'Mithatpasa Cad. No:22', 'phone': '+90 216 340 77 88',",
    "     'price_range': '3', 'category': japanese, 'location': loc},",
    "    {'name': 'Pizza Express Acibadem',",
    "     'description': 'Tas firinda ince hamur pizza.',",
    "     'address': 'Acibadem Cad. No:61', 'phone': '+90 216 342 33 44',",
    "     'price_range': '2', 'category': italian, 'location': loc},",
    "    {'name': 'Balik Ekmek Corner',",
    "     'description': 'Taze izgara balik ekmek.',",
    "     'address': 'Acibadem Mah. Karanfil Sok. No:5', 'phone': '+90 216 341 11 22',",
    "     'price_range': '1', 'category': seafood, 'location': loc},",
    "    {'name': 'Teras Cafe Restaurant',",
    "     'description': 'Bogaz manzarali cati kati kafe.',",
    "     'address': 'Acibadem Cad. No:88 Kat:3', 'phone': '+90 216 343 66 77',",
    "     'price_range': '2', 'category': cafe, 'location': loc},",
    "    {'name': 'KFC Acibadem',",
    "     'description': 'Crispy tavuk ve burger.',",
    "     'address': 'Mithatpasa Cad. No:9', 'phone': '+90 216 340 40 40',",
    "     'price_range': '1', 'category': fastfood, 'location': loc},",
    "    {'name': 'Simit Sarayi Acibadem',",
    "     'description': 'Taze simit, borek ve cay.',",
    "     'address': 'Acibadem Cad. No:5', 'phone': '+90 216 341 00 99',",
    "     'price_range': '1', 'category': bakery, 'location': loc},",
    "    {'name': 'Ciya Sofrasi',",
    "     'description': 'Anadolu mutfagindan geleneksel yemekler.',",
    "     'address': 'Guneslibahce Sok. No:43', 'phone': '+90 216 330 31 90',",
    "     'price_range': '2', 'category': turkish, 'location': loc},",
    "]",
    "",
    "for data in restaurants_data:",
    "    r, created = Restaurant.objects.get_or_create(",
    "        name=data['name'],",
    "        defaults={k: v for k, v in data.items() if k != 'name'}",
    "    )",
    "    if created:",
    "        print(f'Eklendi: {r.name}')",
    "    else:",
    "        print(f'Zaten var: {r.name}')",
    "",
    "print('Tamamlandi!')",
)

story.append(adim(4,"Seed scriptini calistir:"))
story += terminal("python3 seed_acibadem.py")

story.append(adim(5,"Diger takim uyelerinin superuser hesaplarini olustur:"))
story += terminal(
    "python manage.py shell",
)
story.append(Paragraph("Shell acildiktan sonra asagidaki Python kodunu yaz ve Enter'a bas:", sNote))
story += kod(
    "from django.contrib.auth.models import User",
    "for name, email in [('Esin','esin@flavor.com'),('Rana','rana@flavor.com'),('Ramiz','ramiz@flavor.com')]:",
    "    User.objects.create_superuser(username=name, email=email, password='123456')",
    "    print(f'Olusturuldu: {name}')",
    "exit()",
)

story.append(adim(6,"GitHub'a gonder:"))
story += terminal(
    "git add restaurants/admin.py seed_acibadem.py",
    "git commit -m 'Gun 3: Admin paneli ve ornek veri eklendi'",
    "git push",
)
story.append(PageBreak())

# ══ GUN 4 — RAMIZ ════════════════════════════════════════════════════════════
story.append(gun_bar(4,"View Fonksiyonlari ve URL Yonlendirme","Ramiz"))
story.append(Spacer(1,10))

story.append(adim(1,"Son kodu cek:"))
story += terminal("git pull origin main","source venv/bin/activate")

story.append(adim(2,"restaurants/views.py dosyasini tamamen asagidakiyle degistir:"))
story += kod(
    "from django.shortcuts import render, get_object_or_404",
    "from .models import Restaurant, Category",
    "",
    "",
    "def home(request):",
    "    restaurants = Restaurant.objects.all().order_by('-created_at')[:6]",
    "    categories  = Category.objects.all()",
    "    return render(request, 'home.html',",
    "                  {'restaurants': restaurants, 'categories': categories})",
    "",
    "",
    "def restaurant_list(request):",
    "    restaurants = Restaurant.objects.all().order_by('-created_at')",
    "    categories  = Category.objects.all()",
    "",
    "    q           = request.GET.get('q', '')",
    "    category_id = request.GET.get('category', '')",
    "    price       = request.GET.get('price', '')",
    "",
    "    if q:",
    "        restaurants = restaurants.filter(name__icontains=q) | \\",
    "                      restaurants.filter(description__icontains=q)",
    "    if category_id:",
    "        restaurants = restaurants.filter(category_id=category_id)",
    "    if price:",
    "        restaurants = restaurants.filter(price_range=price)",
    "",
    "    return render(request, 'restaurants/list.html',",
    "                  {'restaurants': restaurants, 'categories': categories})",
    "",
    "",
    "def restaurant_detail(request, pk):",
    "    restaurant = get_object_or_404(Restaurant, pk=pk)",
    "    reviews    = restaurant.reviews.all().order_by('-created_at')",
    "    return render(request, 'restaurants/detail.html',",
    "                  {'restaurant': restaurant, 'reviews': reviews})",
    "",
    "",
    "def about(request):",
    "    return render(request, 'about.html')",
    "",
    "",
    "def contact(request):",
    "    return render(request, 'contact.html')",
)

story.append(adim(3,"restaurants/urls.py dosyasini tamamen asagidakiyle degistir:"))
story += kod(
    "from django.urls import path",
    "from . import views",
    "",
    "urlpatterns = [",
    "    path('',                        views.home,              name='home'),",
    "    path('restaurants/',            views.restaurant_list,   name='restaurant_list'),",
    "    path('restaurants/<int:pk>/',   views.restaurant_detail, name='restaurant_detail'),",
    "    path('about/',                  views.about,             name='about'),",
    "    path('contact/',                views.contact,           name='contact'),",
    "]",
)

story.append(adim(4,"Sunucuyu test et — her URL 200 donmeli:"))
story += terminal(
    "python manage.py runserver",
)
story.append(Paragraph("Tarayicida su adresleri kontrol et: /  /restaurants/  /restaurants/1/  /about/  /contact/", sNote))
story.append(Paragraph("Cikis icin: CTRL+C", sNote))

story.append(adim(5,"GitHub'a gonder:"))
story += terminal(
    "git add restaurants/views.py restaurants/urls.py",
    "git commit -m 'Gun 4: View fonksiyonlari ve URL yonlendirme eklendi'",
    "git push",
)
story.append(PageBreak())

# ══ GUN 5 — YAREN ════════════════════════════════════════════════════════════
story.append(gun_bar(5,"Temel Sablon ve CSS","Yaren"))
story.append(Spacer(1,10))

story.append(adim(1,"Son kodu cek:"))
story += terminal("git pull origin main")

story.append(adim(2,"templates/base.html dosyasini olustur ve asagidaki kodu yaz:"))
story += kod(
    "{% load static %}",
    "<!DOCTYPE html>",
    "<html lang=\"en\">",
    "<head>",
    "  <meta charset=\"UTF-8\">",
    "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">",
    "  <title>{% block title %}flavor{% endblock %}</title>",
    "  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">",
    "  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>",
    "  <link href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap\" rel=\"stylesheet\">",
    "  <link rel=\"stylesheet\" href=\"{% static 'css/style.css' %}\">",
    "</head>",
    "<body>",
    "",
    "<nav class=\"nav\">",
    "  <div class=\"nav-inner\">",
    "    <a href=\"{% url 'home' %}\" class=\"nav-brand\">fl<span>a</span>vor</a>",
    "    <div class=\"nav-links\">",
    "      <a href=\"{% url 'home' %}\">Home</a>",
    "      <a href=\"{% url 'restaurant_list' %}\">Restaurants</a>",
    "      <a href=\"{% url 'about' %}\">About</a>",
    "      <a href=\"{% url 'contact' %}\">Contact</a>",
    "    </div>",
    "    <div class=\"nav-search\">",
    "      <svg width=\"15\" height=\"15\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2.5\">",
    "        <circle cx=\"11\" cy=\"11\" r=\"8\"/><path d=\"m21 21-4.35-4.35\"/>",
    "      </svg>",
    "      <form action=\"{% url 'restaurant_list' %}\" method=\"get\">",
    "        <input type=\"text\" name=\"q\" placeholder=\"Search restaurants...\"",
    "               value=\"{{ request.GET.q|default:'' }}\">",
    "      </form>",
    "    </div>",
    "  </div>",
    "</nav>",
    "",
    "<main>{% block content %}{% endblock %}</main>",
    "",
    "<footer>",
    "  <div class=\"footer-inner\">",
    "    <span class=\"footer-brand\">fl<span>a</span>vor</span>",
    "    <div class=\"footer-links\">",
    "      <a href=\"{% url 'home' %}\">Home</a>",
    "      <a href=\"{% url 'restaurant_list' %}\">Restaurants</a>",
    "      <a href=\"{% url 'about' %}\">About</a>",
    "      <a href=\"{% url 'contact' %}\">Contact</a>",
    "      <a href=\"/admin/\">Admin</a>",
    "    </div>",
    "    <span class=\"footer-copy\">2026 flavor</span>",
    "  </div>",
    "</footer>",
    "",
    "</body>",
    "</html>",
)

story.append(adim(3,"static/css/style.css dosyasini olustur ve asagidaki kodu yaz:"))
story.append(Paragraph("(Uzun bir dosyadir, tamamen kopyala)", sNote))
story += kod(
    "/* flavor - Apple-inspired design */",
    "",
    ":root {",
    "  --font: \"Inter\", -apple-system, BlinkMacSystemFont, \"Helvetica Neue\", Arial, sans-serif;",
    "  --text: #1d1d1f;",
    "  --text-2: #6e6e73;",
    "  --text-3: #adadb8;",
    "  --bg: #ffffff;",
    "  --bg-2: #f5f5f7;",
    "  --bg-3: #fafafa;",
    "  --border: #e5e5ea;",
    "  --accent: #ff6000;",
    "  --accent-dk: #e05500;",
    "  --green: #34c759;",
    "  --nav-h: 56px;",
    "  --r: 14px;",
    "  --r-lg: 20px;",
    "  --shadow: 0 2px 12px rgba(0,0,0,0.07);",
    "  --shadow-lg: 0 8px 32px rgba(0,0,0,0.10);",
    "}",
    "",
    "*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }",
    "html { scroll-behavior: smooth; height: 100%; }",
    "body {",
    "  font-family: var(--font);",
    "  color: var(--text);",
    "  background: var(--bg);",
    "  -webkit-font-smoothing: antialiased;",
    "  line-height: 1.5;",
    "  min-height: 100vh;",
    "  display: flex;",
    "  flex-direction: column;",
    "}",
    "main { flex: 1; }",
    "a { text-decoration: none; color: inherit; }",
    "img { display: block; width: 100%; object-fit: cover; }",
    "",
    "/* NAV */",
    ".nav {",
    "  position: sticky;",
    "  top: 0;",
    "  z-index: 100;",
    "  height: var(--nav-h);",
    "  background: rgba(255,255,255,0.88);",
    "  backdrop-filter: blur(20px) saturate(180%);",
    "  -webkit-backdrop-filter: blur(20px) saturate(180%);",
    "  border-bottom: 1px solid var(--border);",
    "}",
    ".nav-inner {",
    "  max-width: 1180px;",
    "  margin: 0 auto;",
    "  padding: 0 20px;",
    "  height: 100%;",
    "  display: flex;",
    "  align-items: center;",
    "  gap: 32px;",
    "}",
    ".nav-brand { font-size: 22px; font-weight: 700; letter-spacing: -0.5px; color: var(--text); flex-shrink: 0; }",
    ".nav-brand span { color: var(--accent); }",
    ".nav-links { display: flex; gap: 4px; }",
    ".nav-links a {",
    "  font-size: 14px; font-weight: 500; color: var(--text-2);",
    "  padding: 6px 12px; border-radius: 8px;",
    "  transition: background 0.18s, color 0.18s;",
    "}",
    ".nav-links a:hover { background: var(--bg-2); color: var(--text); }",
    ".nav-search { flex: 1; max-width: 320px; margin-left: auto; position: relative; }",
    ".nav-search input {",
    "  width: 100%; height: 36px; border: none; background: var(--bg-2);",
    "  border-radius: 50px; padding: 0 16px 0 38px; font-size: 14px;",
    "  font-family: var(--font); color: var(--text); outline: none; transition: box-shadow 0.2s;",
    "}",
    ".nav-search input:focus { box-shadow: 0 0 0 3px rgba(255,96,0,0.18); }",
    ".nav-search svg { position: absolute; left: 12px; top: 50%; transform: translateY(-50%); color: var(--text-3); }",
    "",
    "/* HERO */",
    ".hero { background: var(--bg-2); padding: 72px 20px 64px; text-align: center; }",
    ".hero-label {",
    "  display: inline-block; background: rgba(255,96,0,0.1); color: var(--accent);",
    "  font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase;",
    "  padding: 5px 14px; border-radius: 50px; margin-bottom: 20px; border: 1px solid rgba(255,96,0,0.2);",
    "}",
    ".hero h1 {",
    "  font-size: clamp(36px, 6vw, 68px); font-weight: 700; letter-spacing: -2px;",
    "  line-height: 1.05; color: var(--text); margin-bottom: 16px;",
    "}",
    ".hero h1 span { color: var(--accent); }",
    ".hero p { font-size: 18px; color: var(--text-2); max-width: 520px; margin: 0 auto 36px; }",
    ".hero-search {",
    "  display: flex; max-width: 560px; margin: 0 auto; background: #fff;",
    "  border-radius: 50px; padding: 6px 6px 6px 20px;",
    "  box-shadow: 0 4px 20px rgba(0,0,0,0.08); border: 1px solid var(--border);",
    "}",
    ".hero-search input { flex: 1; border: none; outline: none; font-size: 15px; font-family: var(--font); color: var(--text); background: transparent; }",
    ".hero-search input::placeholder { color: var(--text-3); }",
    ".hero-search button {",
    "  background: var(--accent); color: #fff; border: none; border-radius: 50px;",
    "  padding: 10px 22px; font-size: 14px; font-weight: 600; font-family: var(--font);",
    "  cursor: pointer; transition: background 0.18s; white-space: nowrap;",
    "}",
    ".hero-search button:hover { background: var(--accent-dk); }",
    "",
    "/* CATEGORY STRIP */",
    ".cat-strip { background: var(--bg); border-bottom: 1px solid var(--border); overflow-x: auto; scrollbar-width: none; }",
    ".cat-strip::-webkit-scrollbar { display: none; }",
    ".cat-inner { max-width: 1180px; margin: 0 auto; padding: 0 20px; display: flex; gap: 4px; align-items: center; height: 52px; }",
    ".cat-btn {",
    "  display: inline-flex; align-items: center; gap: 6px; padding: 6px 16px;",
    "  border-radius: 50px; border: 1.5px solid var(--border); background: var(--bg);",
    "  font-size: 13px; font-weight: 500; font-family: var(--font); color: var(--text-2);",
    "  cursor: pointer; white-space: nowrap; transition: all 0.18s; flex-shrink: 0;",
    "}",
    ".cat-btn:hover, .cat-btn.active { border-color: var(--accent); color: var(--accent); background: rgba(255,96,0,0.06); }",
    "",
    "/* SECTION */",
    ".section { padding: 56px 20px; }",
    ".wrap { max-width: 1180px; margin: 0 auto; }",
    ".section-top { display: flex; align-items: flex-end; justify-content: space-between; margin-bottom: 28px; gap: 12px; flex-wrap: wrap; }",
    ".section-title { font-size: clamp(22px, 3vw, 30px); font-weight: 700; letter-spacing: -0.5px; }",
    ".section-sub { font-size: 14px; color: var(--text-2); margin-top: 4px; }",
    ".see-all { font-size: 14px; font-weight: 600; color: var(--accent); white-space: nowrap; }",
    ".see-all:hover { text-decoration: underline; }",
    "",
    "/* CARDS */",
    ".cards { display: grid; grid-template-columns: repeat(auto-fill, minmax(268px, 1fr)); gap: 18px; }",
    ".card { background: var(--bg); border: 1px solid var(--border); border-radius: var(--r-lg); overflow: hidden; transition: transform 0.22s, box-shadow 0.22s; cursor: pointer; }",
    ".card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: transparent; }",
    ".card-img { height: 180px; background: linear-gradient(135deg, #f5f5f7, #ebebeb); display: flex; align-items: center; justify-content: center; font-size: 52px; overflow: hidden; position: relative; }",
    ".card-badge { position: absolute; top: 10px; left: 10px; background: rgba(255,255,255,0.92); backdrop-filter: blur(8px); border-radius: 50px; padding: 3px 10px; font-size: 11px; font-weight: 700; color: var(--text); }",
    ".card-body { padding: 14px 16px 16px; }",
    ".card-cat { font-size: 11px; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 4px; }",
    ".card-name { font-size: 16px; font-weight: 700; letter-spacing: -0.2px; margin-bottom: 4px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }",
    ".card-loc { font-size: 13px; color: var(--text-2); margin-bottom: 10px; }",
    ".card-foot { display: flex; align-items: center; justify-content: space-between; padding-top: 10px; border-top: 1px solid var(--border); }",
    ".stars { color: #ff9f0a; font-size: 13px; letter-spacing: 1px; }",
    ".rating { font-size: 13px; font-weight: 700; margin-left: 5px; }",
    ".rev-cnt { font-size: 12px; color: var(--text-3); }",
    ".price-tag { font-size: 13px; color: var(--text-2); }",
    "",
    "/* FILTER BAR */",
    ".filter-bar { background: var(--bg-2); border-radius: var(--r); padding: 14px 18px; display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin-bottom: 28px; }",
    ".filter-label { font-size: 13px; color: var(--text-2); font-weight: 500; }",
    "select.filter-sel { font-family: var(--font); font-size: 13px; color: var(--text); background: var(--bg); border: 1px solid var(--border); border-radius: 8px; padding: 7px 10px; outline: none; cursor: pointer; transition: border-color 0.18s; }",
    "select.filter-sel:focus { border-color: var(--accent); }",
    "",
    "/* DETAIL */",
    ".detail-hero { height: 380px; background: var(--bg-2); overflow: hidden; position: relative; }",
    ".detail-hero-ph { height: 100%; display: flex; align-items: center; justify-content: center; font-size: 80px; background: linear-gradient(135deg, #f5f5f7, #e5e5ea); }",
    ".detail-wrap { max-width: 1180px; margin: 0 auto; padding: 40px 20px 80px; display: grid; grid-template-columns: 1fr 320px; gap: 40px; align-items: start; }",
    ".breadcrumb { font-size: 13px; color: var(--text-3); margin-bottom: 14px; }",
    ".breadcrumb a { color: var(--accent); }",
    ".detail-name { font-size: clamp(26px, 4vw, 40px); font-weight: 700; letter-spacing: -1px; margin-bottom: 12px; }",
    ".detail-tags { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }",
    ".tag { display: inline-flex; align-items: center; gap: 4px; padding: 4px 12px; border-radius: 50px; font-size: 13px; font-weight: 600; }",
    ".tag-cat { background: rgba(255,96,0,0.1); color: var(--accent); }",
    ".tag-price { background: var(--bg-2); color: var(--text-2); }",
    ".detail-desc { font-size: 16px; color: var(--text-2); line-height: 1.7; margin-bottom: 32px; }",
    ".info-card { background: var(--bg-2); border-radius: var(--r-lg); padding: 22px; margin-bottom: 16px; }",
    ".info-card h4 { font-size: 15px; font-weight: 700; margin-bottom: 14px; }",
    ".info-row { display: flex; gap: 10px; font-size: 14px; color: var(--text-2); margin-bottom: 10px; align-items: flex-start; }",
    ".info-row:last-child { margin-bottom: 0; }",
    ".info-icon { flex-shrink: 0; color: var(--text-3); }",
    ".rating-box { text-align: center; padding: 24px; }",
    ".rating-num { font-size: 56px; font-weight: 700; letter-spacing: -2px; color: var(--text); line-height: 1; }",
    ".rating-stars { font-size: 22px; color: #ff9f0a; margin: 6px 0; }",
    ".rating-cnt { font-size: 14px; color: var(--text-3); }",
    ".reviews-section { margin-top: 40px; }",
    ".reviews-title { font-size: 20px; font-weight: 700; margin-bottom: 20px; }",
    ".review-card { border: 1px solid var(--border); border-radius: var(--r); padding: 18px; margin-bottom: 12px; }",
    ".review-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }",
    ".reviewer { display: flex; align-items: center; gap: 10px; }",
    ".avatar { width: 38px; height: 38px; border-radius: 50%; background: linear-gradient(135deg, var(--accent), #ff9a5c); color: #fff; font-weight: 700; font-size: 15px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }",
    ".reviewer-name { font-size: 14px; font-weight: 700; }",
    ".reviewer-date { font-size: 12px; color: var(--text-3); }",
    ".review-stars { color: #ff9f0a; font-size: 14px; }",
    ".review-text { font-size: 14px; color: var(--text-2); line-height: 1.6; }",
    "",
    "/* FOOTER */",
    "footer { background: #1a1a1a; color: rgba(255,255,255,0.45); padding: 20px 20px; }",
    ".footer-inner { max-width: 1180px; margin: 0 auto; display: flex; align-items: center; gap: 16px; }",
    ".footer-brand { font-size: 14px; font-weight: 700; color: #fff; flex-shrink: 0; }",
    ".footer-brand span { color: var(--accent); }",
    ".footer-links { display: flex; gap: 14px; flex-wrap: wrap; flex: 1; }",
    ".footer-links a { font-size: 12px; color: rgba(255,255,255,0.4); transition: color 0.18s; }",
    ".footer-links a:hover { color: #fff; }",
    ".footer-copy { font-size: 12px; white-space: nowrap; }",
    "",
    "/* EMPTY */",
    ".empty { text-align: center; padding: 80px 20px; }",
    ".empty-icon { font-size: 56px; margin-bottom: 12px; }",
    ".empty h3 { font-size: 20px; font-weight: 700; margin-bottom: 6px; }",
    ".empty p { font-size: 15px; color: var(--text-2); }",
    "",
    "/* RESPONSIVE */",
    "@media (max-width: 860px) {",
    "  .detail-wrap { grid-template-columns: 1fr; }",
    "  .hero h1 { letter-spacing: -1px; }",
    "  .nav-links { display: none; }",
    "}",
    "@media (max-width: 540px) {",
    "  .cards { grid-template-columns: 1fr; }",
    "  .hero-search { flex-direction: column; gap: 8px; border-radius: 16px; }",
    "  .hero-search input { padding: 10px 16px; }",
    "  .hero-search button { border-radius: 10px; }",
    "}",
)

story.append(adim(4,"GitHub'a gonder:"))
story += terminal(
    "git add templates/base.html static/css/style.css",
    "git commit -m 'Gun 5: Temel sablon ve CSS eklendi'",
    "git push",
)
story.append(PageBreak())

# ══ GUN 6 — ESIN ════════════════════════════════════════════════════════════
story.append(gun_bar(6,"Ana Sayfa ve Liste Sablonlari","Esin"))
story.append(Spacer(1,10))

story.append(adim(1,"Son kodu cek:"))
story += terminal("git pull origin main")

story.append(adim(2,"templates/home.html dosyasini olustur ve asagidaki kodu yaz:"))
story += kod(
    "{% extends 'base.html' %}",
    "{% block title %}flavor - Discover Restaurants{% endblock %}",
    "",
    "{% block content %}",
    "",
    "<!-- HERO -->",
    "<div class=\"hero\">",
    "  <div class=\"hero-label\">Your Restaurant Guide</div>",
    "  <h1>YER<br><span>Routes</span></h1>",
    "  <p>Find the best restaurants in your city, read reviews and save your favorites.</p>",
    "  <form class=\"hero-search\" action=\"{% url 'restaurant_list' %}\" method=\"get\">",
    "    <input type=\"text\" name=\"q\" placeholder=\"Search by restaurant, cuisine or neighborhood...\">",
    "    <button type=\"submit\">Search</button>",
    "  </form>",
    "</div>",
    "",
    "{% endblock %}",
)

story.append(adim(3,"templates/restaurants/ klasorunu olustur:"))
story += terminal("mkdir -p templates/restaurants")

story.append(adim(4,"templates/restaurants/list.html dosyasini olustur ve asagidaki kodu yaz:"))
story += kod(
    "{% extends 'base.html' %}",
    "{% block title %}Restaurants - flavor{% endblock %}",
    "",
    "{% block content %}",
    "",
    "<!-- CATEGORY STRIP -->",
    "{% if categories %}",
    "<div class=\"cat-strip\">",
    "  <div class=\"cat-inner\">",
    "    <a href=\"{% url 'restaurant_list' %}\"",
    "       class=\"cat-btn {% if not request.GET.category %}active{% endif %}\">All</a>",
    "    {% for cat in categories %}",
    "    <a href=\"?category={{ cat.id }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}\"",
    "       class=\"cat-btn {% if request.GET.category == cat.id|stringformat:'s' %}active{% endif %}\">",
    "      {{ cat.name }}",
    "    </a>",
    "    {% endfor %}",
    "  </div>",
    "</div>",
    "{% endif %}",
    "",
    "<div class=\"section\">",
    "  <div class=\"wrap\">",
    "",
    "    <!-- FILTER BAR -->",
    "    <form method=\"get\">",
    "      <div class=\"filter-bar\">",
    "        <span class=\"filter-label\">Filter:</span>",
    "        <select name=\"category\" class=\"filter-sel\" onchange=\"this.form.submit()\">",
    "          <option value=\"\">All Categories</option>",
    "          {% for cat in categories %}",
    "          <option value=\"{{ cat.id }}\"",
    "            {% if request.GET.category == cat.id|stringformat:'s' %}selected{% endif %}>",
    "            {{ cat.name }}",
    "          </option>",
    "          {% endfor %}",
    "        </select>",
    "        <select name=\"price\" class=\"filter-sel\" onchange=\"this.form.submit()\">",
    "          <option value=\"\">All Prices</option>",
    "          <option value=\"1\" {% if request.GET.price == '1' %}selected{% endif %}>EUR Budget</option>",
    "          <option value=\"2\" {% if request.GET.price == '2' %}selected{% endif %}>EUR EUR Mid-range</option>",
    "          <option value=\"3\" {% if request.GET.price == '3' %}selected{% endif %}>EUR EUR EUR Luxury</option>",
    "        </select>",
    "        {% if request.GET.q or request.GET.category or request.GET.price %}",
    "        <a href=\"{% url 'restaurant_list' %}\" style=\"font-size:13px;color:#ff3b30;font-weight:600;\">Clear</a>",
    "        {% endif %}",
    "        <span style=\"margin-left:auto;font-size:13px;color:#6e6e73;\">",
    "          {{ restaurants|length }} restaurant{{ restaurants|length|pluralize }}",
    "        </span>",
    "      </div>",
    "    </form>",
    "",
    "    {% if restaurants %}",
    "    <div class=\"cards\">",
    "      {% for r in restaurants %}",
    "      <a href=\"{% url 'restaurant_detail' r.pk %}\" class=\"card\">",
    "        <div class=\"card-img\">",
    "          <span class=\"card-badge\">{{ r.price_display }}</span>",
    "          🍽️",
    "        </div>",
    "        <div class=\"card-body\">",
    "          <div class=\"card-cat\">{{ r.category }}</div>",
    "          <div class=\"card-name\">{{ r.name }}</div>",
    "          <div class=\"card-loc\">{{ r.location }}</div>",
    "          <div class=\"card-foot\">",
    "            {% with avg=r.average_rating cnt=r.reviews.count %}",
    "            {% if avg %}",
    "            <div style=\"display:flex;align-items:center;gap:4px\">",
    "              <span class=\"stars\">★</span>",
    "              <span class=\"rating\">{{ avg }}</span>",
    "              <span class=\"rev-cnt\">({{ cnt }} review{{ cnt|pluralize }})</span>",
    "            </div>",
    "            {% else %}",
    "            <span class=\"rev-cnt\">No reviews yet</span>",
    "            {% endif %}",
    "            {% endwith %}",
    "            <span class=\"price-tag\">{{ r.price_display }}</span>",
    "          </div>",
    "        </div>",
    "      </a>",
    "      {% endfor %}",
    "    </div>",
    "    {% else %}",
    "    <div class=\"empty\">",
    "      <div class=\"empty-icon\">🔍</div>",
    "      <h3>No results found</h3>",
    "      <p>Try different filters.</p>",
    "    </div>",
    "    {% endif %}",
    "",
    "  </div>",
    "</div>",
    "{% endblock %}",
)

story.append(adim(5,"GitHub'a gonder:"))
story += terminal(
    "git add templates/home.html templates/restaurants/list.html",
    "git commit -m 'Gun 6: Ana sayfa ve liste sablonlari eklendi'",
    "git push",
)
story.append(PageBreak())

# ══ GUN 7 — RANA ════════════════════════════════════════════════════════════
story.append(gun_bar(7,"Detay, Hakkinda ve Iletisim Sablonlari","Rana"))
story.append(Spacer(1,10))

story.append(adim(1,"Son kodu cek:"))
story += terminal("git pull origin main")

story.append(adim(2,"templates/restaurants/detail.html dosyasini olustur:"))
story += kod(
    "{% extends 'base.html' %}",
    "{% block title %}{{ restaurant.name }} - flavor{% endblock %}",
    "",
    "{% block content %}",
    "",
    "<div class=\"detail-hero\">",
    "  <div class=\"detail-hero-ph\">🍽️</div>",
    "</div>",
    "",
    "<div class=\"detail-wrap\">",
    "",
    "  <!-- SOL SUTUN -->",
    "  <div>",
    "    <div class=\"breadcrumb\">",
    "      <a href=\"{% url 'home' %}\">Home</a> /",
    "      <a href=\"{% url 'restaurant_list' %}\">Restaurants</a> /",
    "      {{ restaurant.name }}",
    "    </div>",
    "",
    "    <h1 class=\"detail-name\">{{ restaurant.name }}</h1>",
    "",
    "    <div class=\"detail-tags\">",
    "      <span class=\"tag tag-cat\">{{ restaurant.category }}</span>",
    "      <span class=\"tag tag-price\">{{ restaurant.price_display }}</span>",
    "    </div>",
    "",
    "    <p class=\"detail-desc\">{{ restaurant.description }}</p>",
    "",
    "    <div class=\"info-card\">",
    "      <h4>Details</h4>",
    "      <div class=\"info-row\"><span class=\"info-icon\">📍</span> {{ restaurant.address }}</div>",
    "      <div class=\"info-row\"><span class=\"info-icon\">🏙️</span> {{ restaurant.location }}</div>",
    "      <div class=\"info-row\"><span class=\"info-icon\">📞</span> {{ restaurant.phone }}</div>",
    "      <div class=\"info-row\"><span class=\"info-icon\">💰</span> Price range: {{ restaurant.price_display }}</div>",
    "    </div>",
    "",
    "    <!-- YORUMLAR -->",
    "    <div class=\"reviews-section\">",
    "      <div class=\"reviews-title\">Reviews</div>",
    "      {% if reviews %}",
    "        {% for review in reviews %}",
    "        <div class=\"review-card\">",
    "          <div class=\"review-top\">",
    "            <div class=\"reviewer\">",
    "              <div class=\"avatar\">{{ review.author|first|upper }}</div>",
    "              <div>",
    "                <div class=\"reviewer-name\">{{ review.author }}</div>",
    "                <div class=\"reviewer-date\">{{ review.created_at|date:'d M Y' }}</div>",
    "              </div>",
    "            </div>",
    "            <div class=\"review-stars\">",
    "              {% for i in '12345' %}{% if forloop.counter <= review.rating %}★{% else %}☆{% endif %}{% endfor %}",
    "            </div>",
    "          </div>",
    "          <p class=\"review-text\">{{ review.text }}</p>",
    "        </div>",
    "        {% endfor %}",
    "      {% else %}",
    "        <div class=\"empty\" style=\"padding:40px 0\">",
    "          <div class=\"empty-icon\">💬</div>",
    "          <h3>No reviews yet</h3>",
    "          <p>Be the first to review this restaurant.</p>",
    "        </div>",
    "      {% endif %}",
    "    </div>",
    "  </div>",
    "",
    "  <!-- SAG KENAR CUBUGU -->",
    "  <aside>",
    "    <div class=\"info-card\">",
    "      <div class=\"rating-box\">",
    "        {% with avg=restaurant.average_rating cnt=restaurant.reviews.count %}",
    "        {% if avg %}",
    "        <div class=\"rating-num\">{{ avg }}</div>",
    "        <div class=\"rating-stars\">★★★★★</div>",
    "        <div class=\"rating-cnt\">{{ cnt }} review{{ cnt|pluralize }}</div>",
    "        {% else %}",
    "        <div style=\"font-size:15px;color:#adadb8;padding:12px 0\">Not rated yet</div>",
    "        {% endif %}",
    "        {% endwith %}",
    "      </div>",
    "    </div>",
    "",
    "    <div class=\"info-card\">",
    "      <h4>Location</h4>",
    "      <div class=\"info-row\"><span class=\"info-icon\">📍</span> {{ restaurant.address }}</div>",
    "      <div class=\"info-row\"><span class=\"info-icon\">🏙️</span> {{ restaurant.location }}</div>",
    "      <div class=\"info-row\"><span class=\"info-icon\">📞</span> {{ restaurant.phone }}</div>",
    "    </div>",
    "  </aside>",
    "",
    "</div>",
    "{% endblock %}",
)

story.append(adim(3,"templates/about.html dosyasini olustur:"))
story += kod(
    "{% extends 'base.html' %}",
    "{% block title %}About - flavor{% endblock %}",
    "{% block content %}",
    "<div class=\"section\">",
    "  <div class=\"wrap\" style=\"max-width:720px\">",
    "    <h1 style=\"font-size:clamp(32px,5vw,52px);font-weight:700;letter-spacing:-1.5px;margin-bottom:16px\">",
    "      Let's discover<br>great food together.",
    "    </h1>",
    "    <p style=\"font-size:18px;color:#6e6e73;line-height:1.7;margin-bottom:40px\">",
    "      flavor is a restaurant discovery platform that helps you find the best dining spots in your city.",
    "      Browse by category, read authentic reviews, and explore new places to eat.",
    "    </p>",
    "    <div style=\"display:grid;grid-template-columns:repeat(3,1fr);gap:20px\">",
    "      <div style=\"background:#f5f5f7;border-radius:16px;padding:28px;text-align:center\">",
    "        <div style=\"font-size:36px;margin-bottom:10px\">🍽️</div>",
    "        <div style=\"font-weight:700;margin-bottom:6px\">Discover</div>",
    "        <div style=\"font-size:14px;color:#6e6e73\">Find your next favorite restaurant from thousands of options.</div>",
    "      </div>",
    "      <div style=\"background:#f5f5f7;border-radius:16px;padding:28px;text-align:center\">",
    "        <div style=\"font-size:36px;margin-bottom:10px\">⭐</div>",
    "        <div style=\"font-weight:700;margin-bottom:6px\">Review</div>",
    "        <div style=\"font-size:14px;color:#6e6e73\">Share your experience and help the community.</div>",
    "      </div>",
    "      <div style=\"background:#f5f5f7;border-radius:16px;padding:28px;text-align:center\">",
    "        <div style=\"font-size:36px;margin-bottom:10px\">📍</div>",
    "        <div style=\"font-weight:700;margin-bottom:6px\">Locate</div>",
    "        <div style=\"font-size:14px;color:#6e6e73\">Find the nearest great food spots around you.</div>",
    "      </div>",
    "    </div>",
    "  </div>",
    "</div>",
    "{% endblock %}",
)

story.append(adim(4,"templates/contact.html dosyasini olustur:"))
story += kod(
    "{% extends 'base.html' %}",
    "{% block title %}Contact - flavor{% endblock %}",
    "{% block content %}",
    "<div class=\"section\">",
    "  <div class=\"wrap\" style=\"max-width:560px\">",
    "    <h1 style=\"font-size:40px;font-weight:700;letter-spacing:-1px;margin-bottom:8px\">Contact</h1>",
    "    <p style=\"font-size:16px;color:#6e6e73;margin-bottom:36px\">Have a question or suggestion? Get in touch.</p>",
    "    <div class=\"info-card\">",
    "      <div class=\"info-row\"><span class=\"info-icon\">📧</span> hello@flavor.com</div>",
    "      <div class=\"info-row\"><span class=\"info-icon\">📍</span> Istanbul, Turkey</div>",
    "    </div>",
    "  </div>",
    "</div>",
    "{% endblock %}",
)

story.append(adim(5,"Son test — tum sayfalar calisiyor mu kontrol et:"))
story += terminal("python manage.py runserver")
story.append(Paragraph("Kontrol edilecek adresler:", sNote))
story.append(Paragraph("http://127.0.0.1:8000/                      Ana sayfa", sNote))
story.append(Paragraph("http://127.0.0.1:8000/restaurants/          Restoran listesi", sNote))
story.append(Paragraph("http://127.0.0.1:8000/restaurants/1/        Detay sayfasi", sNote))
story.append(Paragraph("http://127.0.0.1:8000/about/                Hakkinda", sNote))
story.append(Paragraph("http://127.0.0.1:8000/contact/              Iletisim", sNote))
story.append(Paragraph("http://127.0.0.1:8000/admin/                Admin paneli (Yaren / 123456)", sNote))
story.append(Spacer(1,8))

story.append(adim(6,"Son commit ve push (Yaren yapar):"))
story += terminal(
    "git pull origin main",
    "git add .",
    "git commit -m 'Gun 7: Tum sablonlar tamamlandi - Week 8 demo hazir'",
    "git push",
)

story.append(Spacer(1,10))
story.append(HRFlowable(width="100%",thickness=1,color=DARK,spaceAfter=8,spaceBefore=4))
story.append(Paragraph("flavor  -  CSE 220 Web Programlama  -  Adim Adim Takim Rehberi  -  Bahar 2026", sCenter))

doc.build(story)
print(f"PDF kaydedildi: {OUTPUT}")
