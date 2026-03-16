"""
flavor – 7-Day Team Plan PDF (v2)
Run: python3 create_plan_pdf.py
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

OUTPUT = "/Users/ramiz/PycharmProjects/flavor/flavor_team_plan.pdf"

# ── Colors ──────────────────────────────────────────────────────────────────
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

# ── Styles ───────────────────────────────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

sCover   = S("sCover",  fontSize=36, textColor=WHITE, fontName="Helvetica-Bold",
             leading=42, alignment=TA_CENTER)
sCoverSub= S("cSub",   fontSize=13, textColor=colors.HexColor("#ffb380"),
             fontName="Helvetica", leading=20, alignment=TA_CENTER)
sH1      = S("sH1",    fontSize=20, textColor=DARK,  fontName="Helvetica-Bold",
             leading=26, spaceBefore=20, spaceAfter=6)
sH2      = S("sH2",    fontSize=14, textColor=DARK,  fontName="Helvetica-Bold",
             leading=20, spaceBefore=14, spaceAfter=5)
sH3      = S("sH3",    fontSize=11, textColor=GRAY,  fontName="Helvetica-Bold",
             leading=16, spaceBefore=10, spaceAfter=4)
sBody    = S("sBody",  fontSize=10, textColor=DARK,  fontName="Helvetica",
             leading=16, spaceAfter=4)
sBodyJ   = S("sBodyJ", fontSize=10, textColor=DARK,  fontName="Helvetica",
             leading=17, spaceAfter=5, alignment=TA_JUSTIFY)
sQ       = S("sQ",     fontSize=10, textColor=ORANGE, fontName="Helvetica-Bold",
             leading=16, spaceBefore=10, spaceAfter=3)
sA       = S("sA",     fontSize=10, textColor=DARK,  fontName="Helvetica",
             leading=17, spaceAfter=6, leftIndent=12, alignment=TA_JUSTIFY)
sBullet  = S("sBullet",fontSize=10, textColor=DARK,  fontName="Helvetica",
             leading=16, leftIndent=14, spaceAfter=3)
sSmall   = S("sSmall", fontSize=9,  textColor=GRAY,  fontName="Helvetica",
             leading=13, spaceAfter=2)
sCenter  = S("sCenter",fontSize=9,  textColor=GRAY,  fontName="Helvetica",
             leading=14, alignment=TA_CENTER)
sTableH  = S("sTableH",fontSize=10, textColor=WHITE, fontName="Helvetica-Bold",
             leading=14, alignment=TA_CENTER)
sTableB  = S("sTableB",fontSize=10, textColor=DARK,  fontName="Helvetica",
             leading=14)

def hr(c=ORANGE, t=1.5):
    return HRFlowable(width="100%", thickness=t, color=c, spaceAfter=10, spaceBefore=4)

def qa(question, answer):
    return [Paragraph(f"Q: {question}", sQ), Paragraph(answer, sA)]

def day_bar(num, title, member):
    hx = MEMBER_HEX.get(member, "#ff6000")
    mc = MEMBER_CLR.get(member, ORANGE)
    row = [[
        Paragraph(f"<font color='{hx}'><b>DAY {num}</b></font>", sH2),
        Paragraph(f"<b>{title}</b>", sH2),
        Paragraph(f"<font color='{hx}'><b>{member}</b></font>", sH2),
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

# ── Document ──────────────────────────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2.2*cm, rightMargin=2.2*cm,
    topMargin=2*cm, bottomMargin=2*cm,
)
story = []

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 1 — COVER
# ═══════════════════════════════════════════════════════════════════════════════
cover = Table(
    [[Paragraph("flavor", sCover)],
     [Paragraph("7-Day Team Development Plan", sCoverSub)],
     [Paragraph("CSE 220 Web Programming  ·  Spring 2026", sCoverSub)]],
    colWidths=[16.6*cm],
)
cover.setStyle(TableStyle([
    ("BACKGROUND",   (0,0),(-1,-1), DARK),
    ("TOPPADDING",   (0,0),(-1,-1), 22),
    ("BOTTOMPADDING",(0,0),(-1,-1), 22),
    ("LEFTPADDING",  (0,0),(-1,-1), 20),
    ("RIGHTPADDING", (0,0),(-1,-1), 20),
]))
story.append(cover)
story.append(Spacer(1, 18))

# Team table (no GitHub column)
story.append(Paragraph("Team Members", sH1))
story.append(hr())
team_data = [
    [Paragraph("<b>Name</b>", sTableH), Paragraph("<b>Role</b>", sTableH),
     Paragraph("<b>Admin Login</b>", sTableH), Paragraph("<b>Password</b>", sTableH)],
    [Paragraph("<font color='#ff6000'><b>Yaren</b></font>", sBody),
     Paragraph("Team Lead · Repo Owner · Base Template + CSS", sBody),
     Paragraph("Yaren", sSmall), Paragraph("123456", sSmall)],
    [Paragraph("<font color='#007aff'><b>Esin</b></font>", sBody),
     Paragraph("Models · Home &amp; List Templates", sBody),
     Paragraph("Esin", sSmall), Paragraph("123456", sSmall)],
    [Paragraph("<font color='#34c759'><b>Rana</b></font>", sBody),
     Paragraph("Admin Panel · Seed Data · Detail Template", sBody),
     Paragraph("Rana", sSmall), Paragraph("123456", sSmall)],
    [Paragraph("<font color='#af52de'><b>Ramiz</b></font>", sBody),
     Paragraph("Views · URL Routing · About &amp; Contact", sBody),
     Paragraph("Ramiz", sSmall), Paragraph("123456", sSmall)],
]
tt = Table(team_data, colWidths=[3*cm, 8.2*cm, 3*cm, 2.4*cm])
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

# 7-day schedule
story.append(Paragraph("7-Day Schedule", sH1))
story.append(hr())
sched = [
    [Paragraph("<b>Day</b>", sTableH), Paragraph("<b>Task</b>", sTableH),
     Paragraph("<b>Who</b>", sTableH), Paragraph("<b>Key Files</b>", sTableH)],
    ["Day 1", "Project setup, GitHub repo, Django init",
     Paragraph("<font color='#ff6000'>Yaren</font>", sBody), "settings.py, urls.py"],
    ["Day 2", "Database models",
     Paragraph("<font color='#007aff'>Esin</font>", sBody), "models.py"],
    ["Day 3", "Admin panel + seed data",
     Paragraph("<font color='#34c759'>Rana</font>", sBody), "admin.py, seed.py"],
    ["Day 4", "Views and URL routing",
     Paragraph("<font color='#af52de'>Ramiz</font>", sBody), "views.py, urls.py"],
    ["Day 5", "Base template + CSS design system",
     Paragraph("<font color='#ff6000'>Yaren</font>", sBody), "base.html, style.css"],
    ["Day 6", "Home + Restaurant list templates",
     Paragraph("<font color='#007aff'>Esin</font>", sBody), "home.html, list.html"],
    ["Day 7", "Detail + About + Contact templates",
     Paragraph("<font color='#34c759'>Rana</font>", sBody), "detail.html, about.html"],
]
for i, row in enumerate(sched[1:], 1):
    if not isinstance(row[0], Paragraph):
        sched[i][0] = Paragraph(f"<b>{row[0]}</b>", sBody)
    if not isinstance(row[3], Paragraph):
        sched[i][3] = Paragraph(row[3], sSmall)
st = Table(sched, colWidths=[1.8*cm, 7*cm, 3*cm, 4.8*cm])
st.setStyle(TableStyle([
    ("BACKGROUND",    (0,0),(-1,0),  DARK),
    ("ROWBACKGROUNDS",(0,1),(-1,-1), [WHITE, LIGHT]),
    ("GRID",          (0,0),(-1,-1), 0.5, BORDER),
    ("TOPPADDING",    (0,0),(-1,-1), 7),
    ("BOTTOMPADDING", (0,0),(-1,-1), 7),
    ("LEFTPADDING",   (0,0),(-1,-1), 8),
    ("RIGHTPADDING",  (0,0),(-1,-1), 8),
    ("VALIGN",        (0,0),(-1,-1), "MIDDLE"),
]))
story.append(st)
story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 2 — settings.py
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("settings.py — Explained", sH1))
story.append(hr())
story.append(Paragraph(
    "settings.py is the configuration file for the entire Django project. "
    "It tells Django how to behave: where to find files, which database to use, "
    "which apps are active, and much more. Every setting here affects the whole project.",
    sBodyJ))
story.append(Spacer(1, 8))

for q, a in [
    ("What is settings.py and why does it exist?",
     "Django needs a central place to store all project configuration. Instead of hardcoding "
     "paths, database names, or secret keys inside every file, they are all defined once in "
     "settings.py. Every other part of Django reads from this file automatically when the server starts."),

    ("What is SECRET_KEY and why must it be kept private?",
     "SECRET_KEY is a long random string used by Django to cryptographically sign cookies, "
     "sessions, and CSRF tokens. If someone steals this key they can forge user sessions and "
     "bypass security. In a real production project it must never be committed to GitHub — "
     "it should be stored in an environment variable. In our demo project we keep it in "
     "settings.py for simplicity only."),

    ("What does DEBUG = True do and when should it be False?",
     "When DEBUG is True, Django shows a full error page with code snippets and variable values "
     "whenever something goes wrong. This is extremely useful during development. "
     "However, it must be set to False before deploying to the internet, because those error "
     "pages reveal internal code paths and sensitive information to anyone who visits a broken URL."),

    ("What is INSTALLED_APPS and what happens if we forget to add our app?",
     "INSTALLED_APPS is a list of all Django applications that are active in the project. "
     "Django uses this list to find templates, static files, models, and management commands. "
     "If we forget to add 'restaurants' here, Django will not find our models when we run "
     "makemigrations and the database tables will never be created."),

    ("What do TEMPLATES and DIRS do?",
     "TEMPLATES tells Django how to find and render HTML files. The DIRS key is a list of "
     "folders where Django should look for templates. We set it to [BASE_DIR / 'templates'] "
     "so that all our .html files inside the top-level templates/ folder are found automatically. "
     "Without this, Django would only look inside each app's own templates/ subfolder."),

    ("What is STATICFILES_DIRS and how does CSS get loaded?",
     "Static files are CSS, JavaScript, and images — files that do not change per request. "
     "STATICFILES_DIRS tells Django where to find them on disk (our static/ folder). "
     "STATIC_URL sets the URL prefix, so style.css becomes accessible at /static/css/style.css. "
     "In templates we write {% load static %} and {% static 'css/style.css' %} to generate "
     "the correct URL automatically."),

    ("What is DATABASES and why are we using SQLite?",
     "DATABASES defines which database engine to use and how to connect to it. "
     "SQLite stores the entire database in a single file (db.sqlite3) on disk with no server needed. "
     "It is perfect for development and small demo projects. For a real production site we would "
     "switch to PostgreSQL or MySQL, but the settings.py change is minimal — only the ENGINE "
     "and connection parameters change, not any of our Python code."),

    ("What are LANGUAGE_CODE and TIME_ZONE?",
     "LANGUAGE_CODE sets the default human language for built-in messages like form validation "
     "errors. TIME_ZONE controls how dates and times are stored and displayed. We set it to "
     "Europe/Istanbul so that review timestamps appear in local Turkish time instead of UTC."),

    ("How does settings.py connect to the rest of the project?",
     "When you run python manage.py runserver, Django reads the environment variable "
     "DJANGO_SETTINGS_MODULE to find settings.py. Every component — models, views, templates, "
     "admin, migrations — automatically imports from this file. The BASE_DIR variable "
     "at the top is a pathlib.Path pointing to the project root folder, used to build "
     "all other absolute paths safely across different operating systems."),
]:
    story += qa(q, a)

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 3 — urls.py
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("urls.py — Explained", sH1))
story.append(hr())
story.append(Paragraph(
    "urls.py is Django's routing system. When a user visits a URL, Django reads through the "
    "urlpatterns list from top to bottom, finds the first pattern that matches, and calls the "
    "corresponding view function. There are two urls.py files in this project.",
    sBodyJ))
story.append(Spacer(1, 8))

for q, a in [
    ("Why are there two urls.py files?",
     "The main urls.py lives inside the flavor/ config folder and is the entry point for all "
     "incoming requests. It delegates restaurant-related URLs to the restaurants app's own urls.py "
     "using include(). This keeps each app self-contained — the restaurants app owns its own routes "
     "and can theoretically be reused in another project without changes."),

    ("What does path('', include('restaurants.urls')) mean?",
     "The empty string '' means 'match any URL that starts with nothing extra' — in other words, "
     "the root of the site. include() tells Django to pass the rest of the URL to restaurants/urls.py "
     "for further matching. So a request to /restaurants/ hits the main urls.py first, which "
     "passes it to restaurants/urls.py, which matches 'restaurants/' to the restaurant_list view."),

    ("What is the order of urlpatterns and does it matter?",
     "Yes, order matters. Django checks patterns from top to bottom and stops at the first match. "
     "The admin URL must come before catch-all patterns to avoid being accidentally overridden. "
     "In our restaurants/urls.py the specific path restaurants/<int:pk>/ must be listed "
     "after restaurants/ — if a more general pattern came first, the specific one would never "
     "be reached. Always place more specific paths before more general ones."),

    ("What does <int:pk> mean in a URL pattern?",
     "This is a URL converter. <int:pk> captures a segment of the URL that looks like an integer "
     "and passes it to the view as a keyword argument named pk (short for primary key). "
     "When a user visits /restaurants/7/, Django extracts the number 7, converts it to a Python int, "
     "and calls restaurant_detail(request, pk=7). If the segment is not a number, Django returns "
     "a 404 automatically without even calling the view."),

    ("What is the name= parameter in each path() and why is it important?",
     "The name parameter gives each URL pattern a unique label. Instead of hardcoding URLs as "
     "strings in templates (like href='/restaurants/') we write {% url 'restaurant_list' %}. "
     "Django replaces this tag with the actual URL at render time. The huge benefit is that "
     "if we ever change the URL structure (e.g. from /restaurants/ to /places/), "
     "we only update urls.py and every template updates automatically — nothing breaks."),

    ("What happens when no URL pattern matches?",
     "If no pattern in urlpatterns matches the requested URL, Django raises a Http404 exception "
     "and returns a 404 Not Found response. In DEBUG mode this shows a yellow error page listing "
     "all patterns Django tried. In production (DEBUG=False) it shows the contents of a "
     "custom 404.html template if one exists, otherwise a plain text error."),

    ("How does a URL request travel from the browser to the screen?",
     "Step 1: Browser sends GET /restaurants/?q=pizza to the server. "
     "Step 2: Django reads ROOT_URLCONF from settings.py and loads flavor/urls.py. "
     "Step 3: '' matches, so Django passes the full URL to restaurants/urls.py. "
     "Step 4: 'restaurants/' matches restaurant_list view. "
     "Step 5: Django calls restaurant_list(request) where request.GET contains {'q': 'pizza'}. "
     "Step 6: The view queries the database, builds a context dictionary, and calls render(). "
     "Step 7: Django finds list.html in the templates/ folder, fills it with the context, "
     "and sends the finished HTML back to the browser."),
]:
    story += qa(q, a)

story.append(PageBreak())

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 4 — Admin Panel
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Django Admin Panel — Explained", sH1))
story.append(hr())
story.append(Paragraph(
    "Django's admin panel is a fully featured management interface that Django generates "
    "automatically. It lets you add, edit, delete, and search database records through a "
    "web browser without writing a single line of SQL.",
    sBodyJ))
story.append(Spacer(1, 8))

for q, a in [
    ("How do I access the admin panel?",
     "Start the development server with python manage.py runserver, then open your browser "
     "and go to http://127.0.0.1:8000/admin/. Log in with one of the superuser accounts below. "
     "You will see a dashboard listing all registered models."),

    ("What are the four superuser accounts for this project?",
     "All four team members have superuser access with the same password:\n"
     "  Yaren   /   password: 123456\n"
     "  Esin    /   password: 123456\n"
     "  Rana    /   password: 123456\n"
     "  Ramiz   /   password: 123456\n"
     "A superuser has full access to everything in the admin panel. In a real application "
     "each person would have a unique strong password."),

    ("What is the difference between a superuser, staff user, and regular user?",
     "A regular user can log into the main site (if login exists) but cannot access /admin/. "
     "A staff user (is_staff=True) can log into the admin panel but only sees models they "
     "have explicit permissions for. A superuser (is_superuser=True) bypasses all permission "
     "checks and can do everything — create, edit, delete any record and manage other users."),

    ("How do I add a new restaurant through the admin?",
     "1. Go to http://127.0.0.1:8000/admin/ and log in. "
     "2. Click 'Restaurants' under the Restaurants section. "
     "3. Click the '+ Add' button in the top right. "
     "4. Fill in the Name, Description, Address, Phone, Price Range fields. "
     "5. Select a Category and Location from the dropdowns (add them first if needed). "
     "6. Click Save. The restaurant immediately appears on the website."),

    ("How do I add a Category or Location first?",
     "In the admin dashboard you will see Categories and Locations listed separately. "
     "Click '+ Add' next to each one, enter the name or city/district, and save. "
     "Once saved they appear in the dropdown menus when adding a restaurant. "
     "You must add at least one Category and one Location before you can add a restaurant."),

    ("How do I add a review for a restaurant?",
     "Click 'Reviews' in the admin sidebar, then '+ Add'. Select the restaurant from the "
     "dropdown, enter the author name, choose a rating from 1 to 5, write the review text, "
     "and click Save. The review will appear immediately on that restaurant's detail page."),

    ("What does list_display do in admin.py?",
     "list_display is a tuple of field names that appear as columns in the admin list view. "
     "For RestaurantAdmin we set list_display = ['name', 'category', 'location', 'price_range', "
     "'created_at']. This means when you click Restaurants in the admin, you see a table with "
     "those five columns for every restaurant. Without list_display, Django only shows the "
     "__str__ representation in a single column."),

    ("What does list_filter do?",
     "list_filter adds a sidebar on the right side of the list view with clickable filter "
     "buttons. For restaurants we filter by category, price_range, and location city. "
     "Clicking 'Cafe' instantly filters the list to show only cafes. "
     "It makes finding records much faster when there are many entries."),

    ("What does search_fields do?",
     "search_fields enables a search box at the top of the admin list. When you type something "
     "and press Enter, Django runs a SQL LIKE query on the specified fields. For restaurants we "
     "search in name, description, and address. So typing 'Acibadem' finds all restaurants "
     "whose name, description, or address contains that word."),

    ("Why is the admin panel important for this project?",
     "For the Week 8 demo the admin panel is our primary data management tool. It lets us "
     "add and demonstrate restaurants, categories, locations, and reviews without building "
     "separate create/edit forms. It also satisfies the assignment requirement for CRUD "
     "(Create, Read, Update, Delete) operations. The instructor can log in and verify data "
     "is stored correctly in the database."),

    ("What is @admin.register and why is it better than admin.site.register()?",
     "@admin.register(Category) is a Python decorator that registers the CategoryAdmin class "
     "with the admin site for the Category model. It is exactly equivalent to writing "
     "admin.site.register(Category, CategoryAdmin) at the end of the file, but is cleaner "
     "because the model and its admin class are visually connected at the top of the class "
     "definition. Both approaches work — the decorator is simply the modern convention."),
]:
    story += qa(q, a)

story.append(Spacer(1, 10))

# Login credentials table
story.append(Paragraph("Quick Reference — Admin Login Credentials", sH2))
cred_data = [
    [Paragraph("<b>Username</b>", sTableH), Paragraph("<b>Password</b>", sTableH),
     Paragraph("<b>Role</b>", sTableH), Paragraph("<b>Access Level</b>", sTableH)],
    [Paragraph("<font color='#ff6000'>Yaren</font>", sBody),  "123456", "Team Lead",   "Superuser"],
    [Paragraph("<font color='#007aff'>Esin</font>",  sBody),  "123456", "Developer",  "Superuser"],
    [Paragraph("<font color='#34c759'>Rana</font>",  sBody),  "123456", "Developer",  "Superuser"],
    [Paragraph("<font color='#af52de'>Ramiz</font>", sBody),  "123456", "Developer",  "Superuser"],
]
for i, row in enumerate(cred_data[1:], 1):
    for j in [1, 2, 3]:
        if not isinstance(row[j], Paragraph):
            cred_data[i][j] = Paragraph(str(row[j]), sBody)

ct = Table(cred_data, colWidths=[4*cm, 3.5*cm, 5*cm, 4.1*cm])
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

# ═══════════════════════════════════════════════════════════════════════════════
# PAGE 5 — Day-by-Day Plan
# ═══════════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Day-by-Day Task Breakdown", sH1))
story.append(hr())

days = [
    (1, "Project Setup & GitHub Repository", "Yaren", [
        ("Create GitHub repo", "Yaren creates a new public repository named 'flavor' on GitHub. She goes to Settings > Collaborators and invites Esin, Rana, and Ramiz by their GitHub usernames so everyone can push code."),
        ("Initialize Django project", "Inside the cloned folder: create a Python virtual environment, activate it, install Django, run pip freeze > requirements.txt to record the dependency, then run django-admin startproject flavor . to create the project structure. The dot at the end is important — it means create the project in the current folder, not in a new subfolder."),
        ("Create the restaurants app", "Run python manage.py startapp restaurants to generate the app folder. Then open INSTALLED_APPS in settings.py and add 'restaurants' to the list. This tells Django the app exists."),
        ("Configure settings.py", "Add TEMPLATES DIRS pointing to the templates/ folder, add STATICFILES_DIRS pointing to static/, set LANGUAGE_CODE to en-us and TIME_ZONE to Europe/Istanbul. Create the templates/ and static/css/ folders manually."),
        ("Set up main urls.py", "Edit flavor/urls.py to include restaurants.urls. This connects the main router to the app's routes. Also create an empty restaurants/urls.py file so Python does not throw an import error."),
        ("First commit and push", "Stage all files, write a clear commit message, and push to the main branch. All team members then clone the repository."),
    ]),
    (2, "Database Models", "Esin", [
        ("Pull latest code", "Run git pull origin main to get Yaren's setup before starting."),
        ("Write models.py", "Define four model classes: Category (name field), Location (city + district), Restaurant (name, description, address, phone, price_range, ForeignKey to Category, ForeignKey to Location, created_at), and Review (ForeignKey to Restaurant, author, rating 1-5, text, created_at). Add average_rating() and price_display() helper methods to Restaurant."),
        ("Run migrations", "Run python manage.py makemigrations to generate the migration file (a Python script that describes the database tables). Then run python manage.py migrate to actually create the tables in db.sqlite3."),
        ("Commit and push", "Commit models.py and the new migrations/ folder. Never delete migration files — they are the history of database changes."),
    ]),
    (3, "Admin Panel + Seed Data", "Rana", [
        ("Pull latest code", "Run git pull origin main to get Esin's models."),
        ("Write admin.py", "Register all four models using @admin.register. Configure list_display, list_filter, and search_fields for each model class so the admin panel is easy to navigate."),
        ("Create superuser", "Run python manage.py createsuperuser and set up the first admin account. The other three team members will be added by running the seed script or through the admin panel."),
        ("Write seed_acibadem.py", "Create a standalone Python script that uses Django's ORM to insert sample restaurants, categories, locations, and reviews. Use get_or_create() so running the script multiple times does not duplicate data. Run it with python3 seed_acibadem.py."),
        ("Verify in admin", "Start the server, open /admin/, log in, and confirm that all seeded data appears correctly in each model's list view."),
        ("Commit and push", "Commit admin.py and seed_acibadem.py."),
    ]),
    (4, "Views & URL Routing", "Ramiz", [
        ("Pull latest code", "Run git pull origin main."),
        ("Write views.py", "Write five view functions: home() fetches the 6 newest restaurants and all categories. restaurant_list() reads GET parameters (q, category, price) and applies ORM filters. restaurant_detail() fetches one restaurant by pk using get_object_or_404. about() and contact() simply render static pages."),
        ("Write restaurants/urls.py", "Define five URL patterns with descriptive names: home, restaurant_list, restaurant_detail (with <int:pk>), about, contact. The names are used in templates with {% url 'name' %} to generate links."),
        ("Test in browser", "Start the server. Even without templates yet, visiting each URL should either show an error about a missing template (good — the view ran) or a TemplateDoesNotExist error — never a URL not found error."),
        ("Commit and push", "Commit views.py and restaurants/urls.py."),
    ]),
    (5, "Base Template & CSS", "Yaren", [
        ("Pull latest code", "Run git pull origin main."),
        ("Write base.html", "Create templates/base.html. This file is the master layout. It loads the Inter font from Google Fonts, links the CSS file, and contains the nav bar and footer. The {% block content %}{% endblock %} placeholder is where each page injects its own content. The <main> tag wraps the block so CSS can push the footer to the bottom."),
        ("Write style.css", "Create static/css/style.css. Define CSS custom properties (variables) at the top inside :root for colors, fonts, spacing, and shadows. Style the nav, hero, cards, filter bar, detail page, footer, and responsive breakpoints. Use display:flex on body and flex:1 on main so the footer always sits at the very bottom."),
        ("Commit and push", "Commit templates/base.html and static/css/style.css."),
    ]),
    (6, "Home & Restaurant List Templates", "Esin", [
        ("Pull latest code", "Run git pull origin main."),
        ("Write home.html", "Create templates/home.html. Start with {% extends 'base.html' %}. Inside {% block content %} add the hero section: a label badge, the large YER / Routes heading, a subtitle paragraph, and the search form that submits a GET request with parameter q to the restaurant_list URL."),
        ("Write list.html", "Create templates/restaurants/list.html (create the restaurants subfolder). Add the category strip at the top (links that filter by category id). Add the filter bar form with category and price dropdowns that auto-submit on change. Loop over restaurants with {% for r in restaurants %} to render restaurant cards. Handle the empty case with {% empty %} or an {% if restaurants %}...{% else %} block."),
        ("Commit and push", "Commit both template files."),
    ]),
    (7, "Detail, About & Contact Templates", "Rana", [
        ("Pull latest code", "Run git pull origin main."),
        ("Write detail.html", "Create templates/restaurants/detail.html. Show the breadcrumb navigation, restaurant name, category tag, price tag, description, and an info card with address, city, and phone. Below that add the reviews section with a {% for review in reviews %} loop showing author, date, star rating, and review text. In the sidebar show the average_rating() value."),
        ("Write about.html", "Create templates/about.html. A simple page with a headline and three feature cards (Discover, Review, Locate) arranged in a CSS grid."),
        ("Write contact.html", "Create templates/contact.html. A minimal page with the project email and city."),
        ("Final team test", "All four members pull the latest code, start the server, and test every page. Check that search works, category filters work, clicking a restaurant card opens the detail page, and the admin panel shows all data correctly."),
        ("Final commit", "One person (Yaren) does a final git pull, then commits any last fixes with message 'Complete Week 8 demo — all templates done' and pushes."),
    ]),
]

for day_num, title, member, tasks in days:
    story.append(day_bar(day_num, title, member))
    story.append(Spacer(1, 8))
    for task_title, task_desc in tasks:
        story.append(Paragraph(f"<b>{task_title}</b>", sH3))
        story.append(Paragraph(task_desc, sBodyJ))
    story.append(Spacer(1, 10))

story.append(hr(DARK, 1))
story.append(Paragraph("flavor  ·  CSE 220 Web Programming  ·  7-Day Team Plan  ·  Spring 2026", sCenter))

# ── Build ─────────────────────────────────────────────────────────────────────
doc.build(story)
print(f"PDF saved: {OUTPUT}")
