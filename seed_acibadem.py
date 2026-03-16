#!/usr/bin/env python3
"""
Seed script: adds 10 restaurants near Acibadem University to the database.
Run with: python3 seed_acibadem.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flavor.settings')
django.setup()

from restaurants.models import Category, Location, Restaurant, Review

# --- Location ---
loc, _ = Location.objects.get_or_create(city='Istanbul', district='Acibadem')

# --- Categories ---
cafe,      _ = Category.objects.get_or_create(name='Café')
fastfood,  _ = Category.objects.get_or_create(name='Fast Food')
kebab,     _ = Category.objects.get_or_create(name='Kebab')
japanese,  _ = Category.objects.get_or_create(name='Japanese')
italian,   _ = Category.objects.get_or_create(name='Italian')
seafood,   _ = Category.objects.get_or_create(name='Seafood')
steakhouse,_ = Category.objects.get_or_create(name='Steakhouse')
bakery,    _ = Category.objects.get_or_create(name='Bakery')

# --- Restaurant data ---
restaurants_data = [
    {
        'name': 'Starbucks Acibadem',
        'description': 'A cozy Starbucks branch right next to Acibadem University — the perfect spot for studying or catching up with friends over your favorite coffee.',
        'address': 'Acibadem Cad. No:12, Kadikoy',
        'phone': '+90 216 340 10 10',
        'price_range': '2',
        'category': cafe,
        'reviews': [
            ('Emily', 5, 'Great coffee and very friendly staff. The wifi is fast — perfect for working between classes.'),
            ('James', 4, 'Always consistent quality. Gets a bit crowded during lunch hours.'),
        ],
    },
    {
        'name': "McDonald's Acibadem",
        'description': "Classic McDonald's burgers and fries. Conveniently located near the university with fast service.",
        'address': 'Acibadem Mah. Cevizlik Sok. No:3, Kadikoy',
        'phone': '+90 216 340 20 20',
        'price_range': '1',
        'category': fastfood,
        'reviews': [
            ('Tom', 3, 'Standard McDonald\'s. Nothing surprising but reliable and quick.'),
        ],
    },
    {
        'name': 'Durumcu Ahmet Usta',
        'description': 'A beloved local wrap shop famous for its spicy chicken doner and hand-stretched lavash bread. A must-try for any food lover in the area.',
        'address': 'Acibadem Cad. No:47, Kadikoy',
        'phone': '+90 216 341 55 55',
        'price_range': '1',
        'category': kebab,
        'reviews': [
            ('Mehmet', 5, 'Best doner wrap in the neighborhood. The bread is fresh every day.'),
            ('Sara', 5, 'Huge portions and amazing flavor. I come here every week.'),
        ],
    },
    {
        'name': 'Sushi Co Acibadem',
        'description': 'Modern Japanese restaurant serving fresh sushi rolls, sashimi platters and miso soup. A popular dinner destination for the university crowd.',
        'address': 'Mithatpasa Cad. No:22, Kadikoy',
        'phone': '+90 216 340 77 88',
        'price_range': '3',
        'category': japanese,
        'reviews': [
            ('Anna', 5, 'The salmon rolls are exceptional. Great atmosphere and attentive service.'),
            ('David', 4, 'Pricey but worth it for a special occasion. The omakase set was outstanding.'),
        ],
    },
    {
        'name': 'Pizza Express Acibadem',
        'description': 'Authentic Italian-style thin-crust pizzas baked in a stone oven, along with fresh pasta dishes and tiramisu.',
        'address': 'Acibadem Cad. No:61, Kadikoy',
        'phone': '+90 216 342 33 44',
        'price_range': '2',
        'category': italian,
        'reviews': [
            ('Laura', 4, 'Crispy thin crust and generous toppings. The margherita is simple perfection.'),
        ],
    },
    {
        'name': 'Balik Ekmek Corner',
        'description': 'Fresh grilled fish sandwiches made to order with crispy fish fillets, onion and parsley. A classic Istanbul street food experience.',
        'address': 'Acibadem Mah. Karanfil Sok. No:5, Kadikoy',
        'phone': '+90 216 341 11 22',
        'price_range': '1',
        'category': seafood,
        'reviews': [
            ('Chris', 5, 'The freshest fish sandwich I have had. Incredibly affordable too.'),
            ('Nadia', 4, 'Authentic Istanbul flavor. The queue moves fast and it is totally worth the wait.'),
        ],
    },
    {
        'name': 'Teras Cafe & Restaurant',
        'description': 'A charming rooftop café with views of the Bosphorus, serving all-day breakfast, salads and specialty coffees.',
        'address': 'Acibadem Cad. No:88, Kat:3, Kadikoy',
        'phone': '+90 216 343 66 77',
        'price_range': '2',
        'category': cafe,
        'reviews': [
            ('Sophie', 5, 'The rooftop view is stunning. Perfect for a relaxed weekend brunch.'),
            ('Ali', 4, 'Great coffee and a wonderful vibe. Service can be slow but the view makes up for it.'),
        ],
    },
    {
        'name': 'KFC Acibadem',
        'description': 'Crispy fried chicken, burgers and sides served fast. A reliable option near the university for a quick meal.',
        'address': 'Mithatpasa Cad. No:9, Kadikoy',
        'phone': '+90 216 340 40 40',
        'price_range': '1',
        'category': fastfood,
        'reviews': [
            ('Jake', 3, 'Good crispy chicken. The zinger burger is always satisfying.'),
        ],
    },
    {
        'name': 'Nusret Steakhouse Kadikoy',
        'description': 'Premium steakhouse known for its perfectly seasoned dry-aged cuts and theatrical salt-bae presentation. An unforgettable dining experience.',
        'address': 'Bahariye Cad. No:35, Kadikoy',
        'phone': '+90 216 344 00 00',
        'price_range': '3',
        'category': steakhouse,
        'reviews': [
            ('Michael', 5, 'The ribeye was absolutely incredible. Worth every penny for a special night out.'),
            ('Jessica', 5, 'Theatrical and delicious. The staff really know how to make the experience memorable.'),
        ],
    },
    {
        'name': 'Simit Sarayi Acibadem',
        'description': 'A beloved Turkish bakery chain offering freshly baked simit (sesame bagels), pastries and Turkish tea — ideal for a quick and affordable breakfast.',
        'address': 'Acibadem Cad. No:5, Kadikoy',
        'phone': '+90 216 341 00 99',
        'price_range': '1',
        'category': bakery,
        'reviews': [
            ('Zeynep', 5, 'Fresh simit every morning. The cheese borek is a must. Perfect before morning lectures.'),
            ('Can', 4, 'Classic Turkish breakfast stop. Cheap, fast and always fresh.'),
        ],
    },
]

created = 0
for data in restaurants_data:
    # Skip if restaurant with this name already exists
    if Restaurant.objects.filter(name=data['name']).exists():
        print(f'  SKIP (already exists): {data["name"]}')
        continue

    reviews = data.pop('reviews')
    r = Restaurant.objects.create(location=loc, **data)
    for author, rating, text in reviews:
        Review.objects.create(restaurant=r, author=author, rating=rating, text=text)
    print(f'  ADDED: {r.name}')
    created += 1

print(f'\nDone — {created} new restaurant(s) added.')
