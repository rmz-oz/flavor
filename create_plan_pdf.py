"""
Generate flavor project – 7-Day Team Plan PDF
Run: python3 create_plan_pdf.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

W, H = A4
OUTPUT = "/Users/ramiz/PycharmProjects/flavor/flavor_team_plan.pdf"

# ── Colors ──────────────────────────────────────────────────────────────────
ORANGE   = colors.HexColor("#ff6000")
DARK     = colors.HexColor("#1d1d1f")
GRAY     = colors.HexColor("#6e6e73")
LIGHT    = colors.HexColor("#f5f5f7")
WHITE    = colors.white
CODE_BG  = colors.HexColor("#1e1e2e")
CODE_FG  = colors.HexColor("#cdd6f4")
YAREN_C  = colors.HexColor("#ff6000")
ESIN_C   = colors.HexColor("#007aff")
RANA_C   = colors.HexColor("#34c759")
RAMIZ_C  = colors.HexColor("#af52de")

MEMBER_COLORS = {
    "Yaren": YAREN_C,
    "Esin":  ESIN_C,
    "Rana":  RANA_C,
    "Ramiz": RAMIZ_C,
}
MEMBER_HEX = {
    "Yaren": "#ff6000",
    "Esin":  "#007aff",
    "Rana":  "#34c759",
    "Ramiz": "#af52de",
}

# ── Styles ───────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, **kw)

sTitle = S("sTitle", fontSize=32, textColor=WHITE,
           fontName="Helvetica-Bold", leading=38, spaceAfter=6, alignment=TA_CENTER)
sSubtitle = S("sSubtitle", fontSize=14, textColor=colors.HexColor("#ffb380"),
              fontName="Helvetica", leading=20, spaceAfter=4, alignment=TA_CENTER)
sH1 = S("sH1", fontSize=18, textColor=DARK, fontName="Helvetica-Bold",
        leading=24, spaceBefore=18, spaceAfter=8)
sH2 = S("sH2", fontSize=13, textColor=DARK, fontName="Helvetica-Bold",
        leading=18, spaceBefore=12, spaceAfter=4)
sH3 = S("sH3", fontSize=11, textColor=GRAY, fontName="Helvetica-Bold",
        leading=16, spaceBefore=8, spaceAfter=4)
sBody = S("sBody", fontSize=10, textColor=DARK, fontName="Helvetica",
          leading=16, spaceAfter=4)
sBodyJ = S("sBodyJ", fontSize=10, textColor=DARK, fontName="Helvetica",
           leading=16, spaceAfter=4, alignment=TA_JUSTIFY)
sCode = S("sCode", fontSize=8.5, textColor=CODE_FG, fontName="Courier",
          leading=13, spaceAfter=2, backColor=CODE_BG,
          leftIndent=10, rightIndent=10)
sSmall = S("sSmall", fontSize=9, textColor=GRAY, fontName="Helvetica",
           leading=14, spaceAfter=2)
sBullet = S("sBullet", fontSize=10, textColor=DARK, fontName="Helvetica",
            leading=16, leftIndent=14, spaceAfter=3)

def member_style(name):
    c = MEMBER_COLORS.get(name, ORANGE)
    return S(f"sMember_{name}", fontSize=11, textColor=c,
             fontName="Helvetica-Bold", leading=16)

# ── Helpers ───────────────────────────────────────────────────────────────────
def hr(color=ORANGE, thickness=1.5):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=10, spaceBefore=4)

def code_block(*lines):
    els = []
    els.append(Spacer(1, 4))
    for line in lines:
        els.append(Paragraph(line.replace(" ", "&nbsp;").replace("<", "&lt;").replace(">", "&gt;"), sCode))
    els.append(Spacer(1, 6))
    return els

def member_badge_table(name, role, day_range):
    c = MEMBER_COLORS.get(name, ORANGE)
    hex_c = MEMBER_HEX.get(name, "#ff6000")
    data = [[
        Paragraph(f"<font color='{hex_c}'><b>{name}</b></font>", sH2),
        Paragraph(role, sBody),
        Paragraph(f"<b>{day_range}</b>", sSmall),
    ]]
    t = Table(data, colWidths=[4.5*cm, 9*cm, 3.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), LIGHT),
        ("ROUNDEDCORNERS", [6]),
        ("TOPPADDING",   (0,0),(-1,-1), 8),
        ("BOTTOMPADDING",(0,0),(-1,-1), 8),
        ("LEFTPADDING",  (0,0),(-1,-1), 12),
        ("RIGHTPADDING", (0,0),(-1,-1), 12),
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("LINEAFTER",    (0,0),(0,-1),  1, colors.HexColor("#e5e5ea")),
        ("LINEAFTER",    (1,0),(1,-1),  1, colors.HexColor("#e5e5ea")),
    ]))
    return t

def day_header(day_num, title, member):
    c = MEMBER_COLORS.get(member, ORANGE)
    hex_c = MEMBER_HEX.get(member, "#ff6000")
    data = [[
        Paragraph(f"<font color='{hex_c}'><b>DAY {day_num}</b></font>", sH2),
        Paragraph(f"<b>{title}</b>", sH2),
        Paragraph(f"<font color='{hex_c}'>{member}</font>", sH2),
    ]]
    t = Table(data, colWidths=[2.5*cm, 11*cm, 3.5*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND",   (0,0),(-1,-1), colors.HexColor("#f0f0f5")),
        ("TOPPADDING",   (0,0),(-1,-1), 7),
        ("BOTTOMPADDING",(0,0),(-1,-1), 7),
        ("LEFTPADDING",  (0,0),(-1,-1), 10),
        ("RIGHTPADDING", (0,0),(-1,-1), 10),
        ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
        ("LINEBELOW",    (0,0),(-1,-1), 2, c),
    ]))
    return t

# ── Document ──────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)

story = []

# ═══════════════════════════════════════════════════════════════════════════════
# COVER PAGE
# ═══════════════════════════════════════════════════════════════════════════════
cover_title = Table(
    [[Paragraph("flavor", sTitle)],
     [Paragraph("7-Day Team Development Plan", sSubtitle)],
     [Paragraph("CSE 220 Web Programming · Spring 2026", sSubtitle)]],
    colWidths=[17*cm],
)
cover_title.setStyle(TableStyle([
    ("BACKGROUND",   (0,0),(-1,-1), DARK),
    ("TOPPADDING",   (0,0),(-1,-1), 20),
    ("BOTTOMPADDING",(0,0),(-1,-1), 20),
    ("LEFTPADDING",  (0,0),(-1,-1), 20),
    ("RIGHTPADDING", (0,0),(-1,-1), 20),
    ("ROUNDEDCORNERS", [12]),
]))
story.append(cover_title)
story.append(Spacer(1, 20))

# Team table
team_data = [
    [Paragraph("<b>Member</b>", sH3), Paragraph("<b>Role</b>", sH3), Paragraph("<b>GitHub Username</b>", sH3)],
    [Paragraph("<font color='#ff6000'><b>Yaren</b></font>", sBody), Paragraph("Team Lead · Repo Owner", sBody), Paragraph("@yaren", sSmall)],
    [Paragraph("<font color='#007aff'><b>Esin</b></font>",  sBody), Paragraph("Models + Home/List Templates", sBody), Paragraph("@esin", sSmall)],
    [Paragraph("<font color='#34c759'><b>Rana</b></font>",  sBody), Paragraph("Admin + Detail Template", sBody), Paragraph("@rana", sSmall)],
    [Paragraph("<font color='#af52de'><b>Ramiz</b></font>", sBody), Paragraph("Views + URLs + CSS", sBody), Paragraph("@ramiz", sSmall)],
]
team_table = Table(team_data, colWidths=[4*cm, 8*cm, 5*cm])
team_table.setStyle(TableStyle([
    ("BACKGROUND",   (0,0),(-1,0),  ORANGE),
    ("TEXTCOLOR",    (0,0),(-1,0),  WHITE),
    ("BACKGROUND",   (0,1),(-1,-1), LIGHT),
    ("ROWBACKGROUNDS",(0,1),(-1,-1),[WHITE, LIGHT]),
    ("GRID",         (0,0),(-1,-1), 0.5, colors.HexColor("#e5e5ea")),
    ("TOPPADDING",   (0,0),(-1,-1), 8),
    ("BOTTOMPADDING",(0,0),(-1,-1), 8),
    ("LEFTPADDING",  (0,0),(-1,-1), 10),
    ("RIGHTPADDING", (0,0),(-1,-1), 10),
    ("VALIGN",       (0,0),(-1,-1), "MIDDLE"),
]))
story.append(Paragraph("Team Members", sH1))
story.append(hr())
story.append(team_table)
story.append(Spacer(1, 16))

# Overview schedule table
story.append(Paragraph("7-Day Overview", sH1))
story.append(hr())
sched_data = [
    [Paragraph("<b>Day</b>", sH3), Paragraph("<b>Task</b>", sH3), Paragraph("<b>Who</b>", sH3), Paragraph("<b>Files</b>", sH3)],
    ["Day 1", "Project setup, GitHub repo, Django init", Paragraph("<font color='#ff6000'>Yaren</font>", sBody), "settings.py, urls.py, requirements.txt"],
    ["Day 2", "Database models", Paragraph("<font color='#007aff'>Esin</font>", sBody),  "models.py"],
    ["Day 3", "Admin panel + seed data", Paragraph("<font color='#34c759'>Rana</font>",  sBody),  "admin.py, seed_acibadem.py"],
    ["Day 4", "Views and URL routing", Paragraph("<font color='#af52de'>Ramiz</font>", sBody), "views.py, restaurants/urls.py"],
    ["Day 5", "Base template + CSS", Paragraph("<font color='#ff6000'>Yaren</font>", sBody), "base.html, style.css"],
    ["Day 6", "Home + Restaurants list templates", Paragraph("<font color='#007aff'>Esin</font>", sBody),  "home.html, list.html"],
    ["Day 7", "Detail + About + Contact templates", Paragraph("<font color='#34c759'>Rana</font>",  sBody),  "detail.html, about.html, contact.html"],
]
for i, row in enumerate(sched_data[1:], 1):
    if not isinstance(row[0], Paragraph):
        sched_data[i][0] = Paragraph(f"<b>{row[0]}</b>", sBody)
    if not isinstance(row[3], Paragraph):
        sched_data[i][3] = Paragraph(f"<font face='Courier' size='8'>{row[3]}</font>", sSmall)

sched_table = Table(sched_data, colWidths=[1.8*cm, 6.5*cm, 3.2*cm, 5.5*cm])
sched_table.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0),  DARK),
    ("TEXTCOLOR",     (0,0),(-1,0),  WHITE),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT]),
    ("GRID",          (0,0),(-1,-1), 0.5, colors.HexColor("#e5e5ea")),
    ("TOPPADDING",    (0,0),(-1,-1), 7),
    ("BOTTOMPADDING", (0,0),(-1,-1), 7),
    ("LEFTPADDING",   (0,0),(-1,-1), 8),
    ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
]))
story.append(sched_table)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 1 — YAREN
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(1, "Project Setup & GitHub Repository", "Yaren"))
story.append(Spacer(1, 10))
story.append(Paragraph("What to do:", sH2))
story.append(Paragraph("1. Create a new GitHub repository named <b>flavor</b> (public, add README).", sBullet))
story.append(Paragraph("2. Invite Esin, Rana, and Ramiz as collaborators (Settings > Collaborators).", sBullet))
story.append(Paragraph("3. Create the Django project structure using the terminal commands below.", sBullet))
story.append(Paragraph("4. Push the initial project to GitHub.", sBullet))
story.append(Spacer(1, 6))

story.append(Paragraph("Terminal commands (run in order):", sH3))
story += code_block(
    "mkdir flavor && cd flavor",
    "python3 -m venv venv",
    "source venv/bin/activate",
    "pip install django",
    "pip freeze > requirements.txt",
    "django-admin startproject flavor .",
    "python manage.py startapp restaurants",
    "python manage.py migrate",
    "python manage.py createsuperuser",
)

story.append(Paragraph("File: <font face='Courier'>flavor/settings.py</font> — paste these additions at the bottom:", sH3))
story += code_block(
    "LANGUAGE_CODE = 'en-us'",
    "TIME_ZONE = 'Europe/Istanbul'",
    "",
    "TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']",
    "",
    "STATICFILES_DIRS = [BASE_DIR / 'static']",
    "STATIC_URL = '/static/'",
)
story.append(Paragraph(
    "Why: Django needs to know where to find HTML templates (templates/) and CSS/JS files (static/). "
    "Setting LANGUAGE_CODE and TIME_ZONE makes dates display correctly.",
    sBodyJ
))
story.append(Spacer(1, 8))

story.append(Paragraph("File: <font face='Courier'>flavor/urls.py</font> — main URL dispatcher:", sH3))
story += code_block(
    "from django.contrib import admin",
    "from django.urls import path, include",
    "",
    "urlpatterns = [",
    "    path('admin/', admin.site.urls),",
    "    path('', include('restaurants.urls')),",
    "]",
)
story.append(Paragraph(
    "Why: This file is Django's central router. The empty string '' means all non-admin URLs "
    "will be handled by the restaurants app's own urls.py.",
    sBodyJ
))

story.append(Paragraph("GitHub push:", sH3))
story += code_block(
    "git init",
    "git add .",
    "git commit -m 'Initial Django project setup'",
    "git branch -M main",
    "git remote add origin https://github.com/yaren/flavor.git",
    "git push -u origin main",
)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 2 — ESIN
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(2, "Database Models", "Esin"))
story.append(Spacer(1, 10))
story.append(Paragraph("Before starting:", sH2))
story.append(Paragraph("1. Clone the repo:  git clone https://github.com/yaren/flavor.git", sBullet))
story.append(Paragraph("2. Activate venv:   source venv/bin/activate", sBullet))
story.append(Paragraph("3. Install deps:    pip install -r requirements.txt", sBullet))
story.append(Spacer(1, 6))

story.append(Paragraph("File: <font face='Courier'>restaurants/models.py</font>", sH3))
story += code_block(
    "from django.db import models",
    "from django.db.models import Avg",
    "",
    "class Category(models.Model):",
    "    name = models.CharField(max_length=100)",
    "    class Meta:",
    "        verbose_name_plural = 'Categories'",
    "    def __str__(self):",
    "        return self.name",
    "",
    "class Location(models.Model):",
    "    city     = models.CharField(max_length=100)",
    "    district = models.CharField(max_length=100)",
    "    def __str__(self):",
    "        return f'{self.district}, {self.city}'",
    "",
    "PRICE_CHOICES = [('1','EUR'), ('2','EUR EUR'), ('3','EUR EUR EUR')]",
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
    "    def __str__(self): return self.name",
    "    def average_rating(self):",
    "        avg = self.reviews.aggregate(avg=Avg('rating'))['avg']",
    "        return round(avg, 1) if avg else None",
    "    def price_display(self):",
    "        return dict(PRICE_CHOICES).get(self.price_range, 'EUR EUR')",
    "",
    "class Review(models.Model):",
    "    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,",
    "                                   related_name='reviews')",
    "    author     = models.CharField(max_length=100)",
    "    rating     = models.IntegerField(choices=[(i,i) for i in range(1,6)])",
    "    text       = models.TextField()",
    "    created_at = models.DateTimeField(auto_now_add=True)",
    "    def __str__(self):",
    "        return f'{self.author} - {self.restaurant.name} ({self.rating})'",
)

story.append(Paragraph("After writing the file, run migrations:", sH3))
story += code_block(
    "python manage.py makemigrations",
    "python manage.py migrate",
)
story.append(Paragraph(
    "Why models.py matters: This file defines all the database tables. "
    "Category groups restaurants by cuisine type. Location stores city/district. "
    "Restaurant is the core table — it links to both Category and Location with ForeignKeys. "
    "Review belongs to a Restaurant (CASCADE delete = if restaurant deleted, reviews go too). "
    "average_rating() calculates the mean score using SQL Avg aggregation. "
    "price_display() converts the stored '1'/'2'/'3' code into a human-readable EUR symbol string.",
    sBodyJ
))

story.append(Paragraph("Push to GitHub:", sH3))
story += code_block(
    "git add restaurants/models.py restaurants/migrations/",
    "git commit -m 'Add Category, Location, Restaurant, Review models'",
    "git push",
)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 3 — RANA
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(3, "Admin Panel + Seed Data", "Rana"))
story.append(Spacer(1, 10))
story.append(Paragraph("Pull latest changes first:", sH3))
story += code_block("git pull origin main")

story.append(Paragraph("File: <font face='Courier'>restaurants/admin.py</font>", sH3))
story += code_block(
    "from django.contrib import admin",
    "from .models import Category, Location, Restaurant, Review",
    "",
    "@admin.register(Category)",
    "class CategoryAdmin(admin.ModelAdmin):",
    "    list_display  = ['name']",
    "    search_fields = ['name']",
    "",
    "@admin.register(Location)",
    "class LocationAdmin(admin.ModelAdmin):",
    "    list_display  = ['city', 'district']",
    "    list_filter   = ['city']",
    "    search_fields = ['city', 'district']",
    "",
    "@admin.register(Restaurant)",
    "class RestaurantAdmin(admin.ModelAdmin):",
    "    list_display  = ['name', 'category', 'location', 'price_range', 'created_at']",
    "    list_filter   = ['category', 'price_range', 'location__city']",
    "    search_fields = ['name', 'description', 'address']",
    "",
    "@admin.register(Review)",
    "class ReviewAdmin(admin.ModelAdmin):",
    "    list_display  = ['restaurant', 'author', 'rating', 'created_at']",
    "    list_filter   = ['rating', 'restaurant']",
    "    search_fields = ['author', 'text']",
)
story.append(Paragraph(
    "Why admin.py matters: The @admin.register decorator registers each model with Django's built-in "
    "admin panel at /admin/. list_display controls which columns appear in the table view. "
    "list_filter adds sidebar filter buttons. search_fields enables a search box. "
    "Without this file the admin panel exists but shows no models.",
    sBodyJ
))
story.append(Spacer(1, 8))

story.append(Paragraph("File: <font face='Courier'>seed_acibadem.py</font> — adds sample restaurants:", sH3))
story += code_block(
    "import os, django",
    "os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flavor.settings')",
    "django.setup()",
    "from restaurants.models import Category, Location, Restaurant, Review",
    "",
    "loc, _ = Location.objects.get_or_create(city='Istanbul', district='Acibadem')",
    "cafe, _ = Category.objects.get_or_create(name='Cafe')",
    "",
    "r = Restaurant.objects.create(",
    "    name='Starbucks Acibadem',",
    "    description='Cozy coffee shop near Acibadem University.',",
    "    address='Acibadem Cad. No:12', phone='+90 216 340 10 10',",
    "    price_range='2', category=cafe, location=loc)",
    "Review.objects.create(restaurant=r, author='Emily',",
    "    rating=5, text='Great coffee and fast wifi!')",
    "print('Done')",
)
story.append(Paragraph("Run the seed script:", sH3))
story += code_block("python3 seed_acibadem.py")

story.append(Paragraph("Push to GitHub:", sH3))
story += code_block(
    "git add restaurants/admin.py seed_acibadem.py",
    "git commit -m 'Add admin configuration and seed data script'",
    "git push",
)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 4 — RAMIZ
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(4, "Views & URL Routing", "Ramiz"))
story.append(Spacer(1, 10))
story.append(Paragraph("Pull latest changes first:", sH3))
story += code_block("git pull origin main")

story.append(Paragraph("File: <font face='Courier'>restaurants/views.py</font>", sH3))
story += code_block(
    "from django.shortcuts import render, get_object_or_404",
    "from .models import Restaurant, Category",
    "",
    "def home(request):",
    "    restaurants = Restaurant.objects.all().order_by('-created_at')[:6]",
    "    categories  = Category.objects.all()",
    "    return render(request, 'home.html',",
    "                  {'restaurants': restaurants, 'categories': categories})",
    "",
    "def restaurant_list(request):",
    "    restaurants  = Restaurant.objects.all().order_by('-created_at')",
    "    categories   = Category.objects.all()",
    "    q            = request.GET.get('q', '')",
    "    category_id  = request.GET.get('category', '')",
    "    price        = request.GET.get('price', '')",
    "    if q:",
    "        restaurants = restaurants.filter(name__icontains=q)",
    "    if category_id:",
    "        restaurants = restaurants.filter(category_id=category_id)",
    "    if price:",
    "        restaurants = restaurants.filter(price_range=price)",
    "    return render(request, 'restaurants/list.html',",
    "                  {'restaurants': restaurants, 'categories': categories})",
    "",
    "def restaurant_detail(request, pk):",
    "    restaurant = get_object_or_404(Restaurant, pk=pk)",
    "    reviews    = restaurant.reviews.all().order_by('-created_at')",
    "    return render(request, 'restaurants/detail.html',",
    "                  {'restaurant': restaurant, 'reviews': reviews})",
    "",
    "def about(request):",
    "    return render(request, 'about.html')",
    "",
    "def contact(request):",
    "    return render(request, 'contact.html')",
)

story.append(Paragraph("File: <font face='Courier'>restaurants/urls.py</font>", sH3))
story += code_block(
    "from django.urls import path",
    "from . import views",
    "",
    "urlpatterns = [",
    "    path('',                       views.home,              name='home'),",
    "    path('restaurants/',           views.restaurant_list,   name='restaurant_list'),",
    "    path('restaurants/int:pk/',    views.restaurant_detail, name='restaurant_detail'),",
    "    path('about/',                 views.about,             name='about'),",
    "    path('contact/',               views.contact,           name='contact'),",
    "]",
)
story.append(Paragraph(
    "Why views.py matters: Views are the bridge between the database and the templates. "
    "home() fetches the 6 newest restaurants and all categories, then passes them to the template. "
    "restaurant_list() reads optional GET parameters (q, category, price) from the URL and filters "
    "the queryset accordingly — this powers the search and filter functionality. "
    "restaurant_detail() uses get_object_or_404 which automatically returns a 404 page if the "
    "restaurant ID does not exist. All views call render() which combines the data with an HTML template.",
    sBodyJ
))

story.append(Paragraph("Push to GitHub:", sH3))
story += code_block(
    "git add restaurants/views.py restaurants/urls.py",
    "git commit -m 'Add views and URL routing'",
    "git push",
)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 5 — YAREN
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(5, "Base Template & CSS", "Yaren"))
story.append(Spacer(1, 10))
story.append(Paragraph("Pull latest changes first:", sH3))
story += code_block("git pull origin main")
story.append(Paragraph("Create these folders:", sH3))
story += code_block(
    "mkdir -p templates",
    "mkdir -p static/css",
)

story.append(Paragraph("File: <font face='Courier'>templates/base.html</font>", sH3))
story.append(Paragraph(
    "This is the master template that all other pages extend. It contains the nav bar, "
    "the Google Fonts Inter import, the CSS link, and the footer. Every page uses "
    "{% extends 'base.html' %} and {% block content %}...{% endblock %} to inject their own content.",
    sBodyJ
))
story += code_block(
    "{% load static %}",
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>",
    "  <title>{% block title %}flavor{% endblock %}</title>",
    "  <link rel='preconnect' href='https://fonts.googleapis.com'>",
    "  <link href='https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap'",
    "        rel='stylesheet'>",
    "  <link rel='stylesheet' href='{% static 'css/style.css' %}'>",
    "</head>",
    "<body>",
    "<nav class='nav'>",
    "  <div class='nav-inner'>",
    "    <a href='{% url 'home' %}' class='nav-brand'>fl<span>a</span>vor</a>",
    "    <div class='nav-links'>",
    "      <a href='{% url 'home' %}'>Home</a>",
    "      <a href='{% url 'restaurant_list' %}'>Restaurants</a>",
    "      <a href='{% url 'about' %}'>About</a>",
    "      <a href='{% url 'contact' %}'>Contact</a>",
    "    </div>",
    "  </div>",
    "</nav>",
    "<main>{% block content %}{% endblock %}</main>",
    "<footer>...(see project file)...</footer>",
    "</body></html>",
)

story.append(Paragraph("Key CSS variables in <font face='Courier'>static/css/style.css</font>:", sH3))
story += code_block(
    ":root {",
    "  --font:   'Inter', -apple-system, sans-serif;",
    "  --accent: #ff6000;   /* orange */",
    "  --text:   #1d1d1f;",
    "  --bg-2:   #f5f5f7;   /* light gray */",
    "  --border: #e5e5ea;",
    "}",
    "body { font-family: var(--font); min-height: 100vh;",
    "       display: flex; flex-direction: column; }",
    "main { flex: 1; }  /* pushes footer to bottom */",
)

story.append(Paragraph("Push to GitHub:", sH3))
story += code_block(
    "git add templates/base.html static/css/style.css",
    "git commit -m 'Add base template and CSS design system'",
    "git push",
)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 6 — ESIN
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(6, "Home Page + Restaurant List Template", "Esin"))
story.append(Spacer(1, 10))
story.append(Paragraph("Pull latest changes first:", sH3))
story += code_block("git pull origin main")

story.append(Paragraph("File: <font face='Courier'>templates/home.html</font>", sH3))
story.append(Paragraph(
    "The home page extends base.html and contains only the hero section — "
    "a large heading, subtitle, and a search form that submits to the restaurant_list URL. "
    "Keeping it minimal makes it look clean and professional.",
    sBodyJ
))
story += code_block(
    "{% extends 'base.html' %}",
    "{% block title %}flavor - Discover Restaurants{% endblock %}",
    "{% block content %}",
    "<div class='hero'>",
    "  <div class='hero-label'>Your Restaurant Guide</div>",
    "  <h1>YER<br><span>Routes</span></h1>",
    "  <p>Find the best restaurants in your city.</p>",
    "  <form class='hero-search' action='{% url 'restaurant_list' %}' method='get'>",
    "    <input type='text' name='q' placeholder='Search...'>",
    "    <button type='submit'>Search</button>",
    "  </form>",
    "</div>",
    "{% endblock %}",
)

story.append(Paragraph("File: <font face='Courier'>templates/restaurants/list.html</font>", sH3))
story.append(Paragraph(
    "The list page shows all restaurants in a card grid. It includes a filter bar "
    "with category and price dropdowns that auto-submit using onchange. "
    "The {% for r in restaurants %} loop renders one card per restaurant. "
    "The {{ restaurants|length }} tag counts results dynamically.",
    sBodyJ
))
story += code_block(
    "{% extends 'base.html' %}",
    "{% block content %}",
    "<div class='section'><div class='wrap'>",
    "  <form method='get'>",
    "    <div class='filter-bar'>",
    "      <select name='category' onchange='this.form.submit()'>",
    "        <option value=''>All Categories</option>",
    "        {% for cat in categories %}",
    "        <option value='{{ cat.id }}'>{{ cat.name }}</option>",
    "        {% endfor %}",
    "      </select>",
    "    </div>",
    "  </form>",
    "  <div class='cards'>",
    "    {% for r in restaurants %}",
    "    <a href='{% url 'restaurant_detail' r.pk %}' class='card'>",
    "      <div class='card-body'>",
    "        <div class='card-name'>{{ r.name }}</div>",
    "        <div class='card-loc'>{{ r.location }}</div>",
    "      </div>",
    "    </a>",
    "    {% endfor %}",
    "  </div>",
    "</div></div>",
    "{% endblock %}",
)

story.append(Paragraph("Create the restaurants template folder first:", sH3))
story += code_block("mkdir -p templates/restaurants")

story.append(Paragraph("Push to GitHub:", sH3))
story += code_block(
    "git add templates/home.html templates/restaurants/list.html",
    "git commit -m 'Add home page and restaurant list template'",
    "git push",
)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# DAY 7 — RANA + RAMIZ
# ═══════════════════════════════════════════════════════════════════════════════
story.append(day_header(7, "Detail, About & Contact Templates", "Rana"))
story.append(Spacer(1, 10))
story.append(Paragraph("Pull latest changes first:", sH3))
story += code_block("git pull origin main")

story.append(Paragraph("File: <font face='Courier'>templates/restaurants/detail.html</font> — Rana's task:", sH3))
story.append(Paragraph(
    "The detail page displays a single restaurant. It shows the restaurant name, category tag, "
    "description, address, phone, and a reviews section. The breadcrumb at the top (Home / Restaurants / Name) "
    "helps users navigate back. The sidebar shows the average rating as a large number.",
    sBodyJ
))
story += code_block(
    "{% extends 'base.html' %}",
    "{% block content %}",
    "<div class='detail-wrap'>",
    "  <div>",
    "    <div class='breadcrumb'>",
    "      <a href='{% url 'home' %}'>Home</a> /",
    "      <a href='{% url 'restaurant_list' %}'>Restaurants</a> /",
    "      {{ restaurant.name }}",
    "    </div>",
    "    <h1 class='detail-name'>{{ restaurant.name }}</h1>",
    "    <p class='detail-desc'>{{ restaurant.description }}</p>",
    "    <div class='reviews-section'>",
    "      <div class='reviews-title'>Reviews</div>",
    "      {% for review in reviews %}",
    "      <div class='review-card'>",
    "        <b>{{ review.author }}</b> rated {{ review.rating }}/5",
    "        <p>{{ review.text }}</p>",
    "      </div>",
    "      {% empty %}",
    "      <p>No reviews yet.</p>",
    "      {% endfor %}",
    "    </div>",
    "  </div>",
    "  <aside>",
    "    <div class='info-card'>",
    "      <div class='rating-num'>{{ restaurant.average_rating }}</div>",
    "    </div>",
    "  </aside>",
    "</div>",
    "{% endblock %}",
)

story.append(Spacer(1, 10))
story.append(Paragraph("Files: <font face='Courier'>templates/about.html</font> and <font face='Courier'>templates/contact.html</font> — also Rana:", sH3))
story += code_block(
    "{% extends 'base.html' %}",
    "{% block title %}About - flavor{% endblock %}",
    "{% block content %}",
    "<div class='section'><div class='wrap'>",
    "  <h1>Let's discover great food together.</h1>",
    "  <p>flavor is a restaurant discovery platform...</p>",
    "</div></div>",
    "{% endblock %}",
)

story.append(Spacer(1, 10))
story.append(Paragraph("Final test by all members:", sH2))
for step in [
    "Run:  python manage.py runserver",
    "Open: http://127.0.0.1:8000/ — hero page visible",
    "Open: http://127.0.0.1:8000/restaurants/ — restaurant cards visible",
    "Click a restaurant card — detail page opens",
    "Open: http://127.0.0.1:8000/admin/ — login with superuser, add data",
    "Test search and category/price filters on the list page",
]:
    story.append(Paragraph(f"• {step}", sBullet))

story.append(Spacer(1, 10))
story.append(Paragraph("Final push:", sH3))
story += code_block(
    "git add .",
    "git commit -m 'Complete Week 8 demo - all templates done'",
    "git push",
)

story.append(Spacer(1, 12))
story.append(hr(DARK, 1))
story.append(Paragraph(
    "flavor · CSE 220 Web Programming · 7-Day Team Plan  |  Generated 2026",
    S("foot", fontSize=9, textColor=GRAY, alignment=TA_CENTER)
))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF saved to: {OUTPUT}")
