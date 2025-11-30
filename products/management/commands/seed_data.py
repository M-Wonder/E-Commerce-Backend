"""
Django management command to seed the database with sample data
Place this file at: products/management/commands/seed_data.py
"""
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds the database with sample categories and products'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Create admin user if doesn't exist
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('✅ Created admin user (username: admin, password: admin123)'))
        else:
            admin_user = User.objects.get(username='admin')
            self.stdout.write(self.style.WARNING('⚠️  Admin user already exists'))

        # Create demo user if doesn't exist
        if not User.objects.filter(username='demo').exists():
            demo_user = User.objects.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123',
                first_name='Demo',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('✅ Created demo user (username: demo, password: demo123)'))
        else:
            demo_user = User.objects.get(username='demo')
            self.stdout.write(self.style.WARNING('⚠️  Demo user already exists'))

        # Create categories
        categories_data = [
            {
                'name': 'Electronics',
                'slug': 'electronics',
                'description': 'Electronic devices and gadgets'
            },
            {
                'name': 'Laptops',
                'slug': 'laptops',
                'description': 'Portable computers and accessories'
            },
            {
                'name': 'Smartphones',
                'slug': 'smartphones',
                'description': 'Mobile phones and accessories'
            },
            {
                'name': 'Accessories',
                'slug': 'accessories',
                'description': 'Tech accessories and peripherals'
            },
            {
                'name': 'Audio',
                'slug': 'audio',
                'description': 'Headphones, speakers, and audio equipment'
            }
        ]

        created_categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'description': cat_data['description']
                }
            )
            created_categories.append(category)
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Created category: {category.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️  Category already exists: {category.name}'))

        # Get categories for products
        electronics = Category.objects.get(slug='electronics')
        laptops = Category.objects.get(slug='laptops')
        smartphones = Category.objects.get(slug='smartphones')
        accessories = Category.objects.get(slug='accessories')
        audio = Category.objects.get(slug='audio')

        # Create products
        products_data = [
            # Laptops
            {
                'name': 'MacBook Pro 16"',
                'description': 'Powerful laptop with M2 Max chip, 32GB RAM, 1TB SSD. Perfect for professionals.',
                'price': '2499.99',
                'stock_quantity': 25,
                'sku': 'MBP-16-2024',
                'category': laptops,
                'rating': 4.8,
                'is_active': True
            },
            {
                'name': 'Dell XPS 15',
                'description': 'High-performance laptop with Intel i9, 16GB RAM, 512GB SSD.',
                'price': '1899.99',
                'stock_quantity': 30,
                'sku': 'DELL-XPS-15',
                'category': laptops,
                'rating': 4.6,
                'is_active': True
            },
            {
                'name': 'ThinkPad X1 Carbon',
                'description': 'Business laptop with excellent keyboard and 14" display.',
                'price': '1599.99',
                'stock_quantity': 8,
                'sku': 'TP-X1C-GEN11',
                'category': laptops,
                'rating': 4.7,
                'is_active': True
            },
            # Smartphones
            {
                'name': 'iPhone 15 Pro',
                'description': 'Latest flagship smartphone with A17 Pro chip, 256GB storage.',
                'price': '999.99',
                'stock_quantity': 50,
                'sku': 'IPH-15-PRO-256',
                'category': smartphones,
                'rating': 4.9,
                'is_active': True
            },
            {
                'name': 'Samsung Galaxy S24 Ultra',
                'description': 'Premium Android phone with S Pen, 512GB storage.',
                'price': '1199.99',
                'stock_quantity': 35,
                'sku': 'SGS24U-512',
                'category': smartphones,
                'rating': 4.8,
                'is_active': True
            },
            {
                'name': 'Google Pixel 8 Pro',
                'description': 'AI-powered camera phone with Tensor G3 chip.',
                'price': '899.99',
                'stock_quantity': 6,
                'sku': 'GPX8P-128',
                'category': smartphones,
                'rating': 4.5,
                'is_active': True
            },
            # Audio
            {
                'name': 'AirPods Pro 2',
                'description': 'Wireless earbuds with active noise cancellation.',
                'price': '249.99',
                'stock_quantity': 100,
                'sku': 'APP-GEN2',
                'category': audio,
                'rating': 4.7,
                'is_active': True
            },
            {
                'name': 'Sony WH-1000XM5',
                'description': 'Industry-leading noise canceling headphones.',
                'price': '399.99',
                'stock_quantity': 45,
                'sku': 'SONY-WH1000XM5',
                'category': audio,
                'rating': 4.9,
                'is_active': True
            },
            {
                'name': 'Bose QuietComfort 45',
                'description': 'Premium wireless headphones with legendary noise cancellation.',
                'price': '329.99',
                'stock_quantity': 9,
                'sku': 'BOSE-QC45',
                'category': audio,
                'rating': 4.6,
                'is_active': True
            },
            # Accessories
            {
                'name': 'Magic Mouse',
                'description': 'Wireless rechargeable mouse with Multi-Touch surface.',
                'price': '79.99',
                'stock_quantity': 60,
                'sku': 'MAGIC-MOUSE-2',
                'category': accessories,
                'rating': 4.2,
                'is_active': True
            },
            {
                'name': 'USB-C Hub 7-in-1',
                'description': 'Multiport adapter with HDMI, USB 3.0, SD card reader.',
                'price': '49.99',
                'stock_quantity': 5,
                'sku': 'USBC-HUB-7IN1',
                'category': accessories,
                'rating': 4.4,
                'is_active': True
            },
            {
                'name': 'Laptop Stand Aluminum',
                'description': 'Ergonomic laptop stand for better posture.',
                'price': '39.99',
                'stock_quantity': 3,
                'sku': 'LPTP-STAND-ALU',
                'category': accessories,
                'rating': 4.3,
                'is_active': True
            },
            # Electronics
            {
                'name': 'iPad Air 5th Gen',
                'description': 'Versatile tablet with M1 chip, 256GB storage.',
                'price': '749.99',
                'stock_quantity': 40,
                'sku': 'IPAD-AIR-M1-256',
                'category': electronics,
                'rating': 4.8,
                'is_active': True
            },
            {
                'name': 'Apple Watch Series 9',
                'description': 'Advanced health and fitness smartwatch.',
                'price': '429.99',
                'stock_quantity': 55,
                'sku': 'AW-S9-45MM',
                'category': electronics,
                'rating': 4.7,
                'is_active': True
            },
            {
                'name': 'Kindle Paperwhite',
                'description': 'E-reader with 6.8" display and adjustable warm light.',
                'price': '139.99',
                'stock_quantity': 7,
                'sku': 'KINDLE-PW-11',
                'category': electronics,
                'rating': 4.6,
                'is_active': True
            },
        ]

        created_count = 0
        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                sku=product_data['sku'],
                defaults={
                    **product_data,
                    'created_by': admin_user
                }
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'✅ Created product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'⚠️  Product already exists: {product.name}'))

        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('DATABASE SEEDING COMPLETED!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(self.style.SUCCESS(f'Categories: {Category.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Products: {Product.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('\nTest Accounts:'))
        self.stdout.write(self.style.SUCCESS('  Admin: username=admin, password=admin123'))
        self.stdout.write(self.style.SUCCESS('  Demo:  username=demo, password=demo123'))
        self.stdout.write(self.style.SUCCESS('='*50))
