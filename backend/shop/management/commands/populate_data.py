import os
import shutil
import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import transaction, connection
from shop.models import Category, Product, ProductImage
from shop.management.data.products import products
from shop.management.data.categories import categories

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Populate the database with initial product data'

    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            cursor.execute("SELECT to_regclass('shop_category')")
            category_table_exists = cursor.fetchone()[0]

            cursor.execute("SELECT to_regclass('shop_product')")
            product_table_exists = cursor.fetchone()[0]

            cursor.execute("SELECT to_regclass('shop_productimage')")
            product_image_table_exists = cursor.fetchone()[0]

        if not category_table_exists or not product_table_exists or not product_image_table_exists:
            self.stdout.write(self.style.ERROR('The necessary database tables do not exist. Run migrations first.'))
            return

        categories_media_dir = os.path.join(settings.MEDIA_ROOT, 'categories')
        if not os.path.exists(categories_media_dir):
            os.makedirs(categories_media_dir)

        products_media_dir = os.path.join(settings.MEDIA_ROOT, 'products')
        if not os.path.exists(products_media_dir):
            os.makedirs(products_media_dir)

        total_products_added = 0
        total_categories_added = 0

        for category_data in categories:
            try:
                with transaction.atomic():
                    if category_data['img']:
                        img_src_path = os.path.join(settings.BASE_DIR, 'shop', 'management', category_data['img'])
                        img_dst_path = os.path.join(categories_media_dir, os.path.basename(category_data['img']))
                        shutil.copy(img_src_path, img_dst_path)
                        category_data['img'] = 'categories/' + os.path.basename(category_data['img'])

                    category, created = Category.objects.get_or_create(
                        id=category_data['id'],
                        defaults={
                            'name': category_data['name'],
                            'code': category_data['code'],
                            'image': category_data['img'],
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created category: {category.name}"))
                        total_categories_added += 1
                    else:
                        self.stdout.write(self.style.WARNING(f"Category already exists: {category.name}"))

            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error adding category {category_data['name']}: {e}"))
                logger.error(f"Error adding category {category_data['name']}: {e}", exc_info=True)

        for product_data in products:
            try:
                with transaction.atomic():
                    if not product_data['img']:
                        raise ValueError("Product has not image")
                    img_src_path = os.path.join(settings.BASE_DIR, 'shop', 'management', product_data['img'])
                    img_dst_path = os.path.join(products_media_dir, os.path.basename(product_data['img']))
                    shutil.copy(img_src_path, img_dst_path)
                    product_data['img'] = 'products/' + os.path.basename(product_data['img'])

                    category_id = product_data.get('category_id')
                    category = Category.objects.get(id=category_id)

                    product, created = Product.objects.get_or_create(
                        id=product_data['id'],
                        defaults={
                            'category': category,
                            'name': product_data['description'],
                            'description': product_data['specs'],
                            'price': product_data['price'],
                            'image': product_data['img'],
                            'texture': product_data['texture'],
                            'weight': product_data['weight'],
                            'size': product_data['size'],
                            'is_proud_of': product_data.get('is_proud_of', False),
                            'is_trending_now': product_data.get('is_trending_now', False),
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Created product: {product.name}"))
                        total_products_added += 1
                    else:
                        self.stdout.write(self.style.WARNING(f"Product already exists: {product.name}"))

                    for img_path in product_data['other_imgs']:
                        other_img_src_path = os.path.join(settings.BASE_DIR, 'shop', 'management', img_path)
                        other_img_dst_path = os.path.join(products_media_dir, os.path.basename(img_path))
                        shutil.copy(other_img_src_path, other_img_dst_path)
                        ProductImage.objects.create(
                            product=product,
                            image='products/' + os.path.basename(img_path)
                        )

            except Category.DoesNotExist:
                self.stderr.write(self.style.ERROR(
                    f"Error adding product with cateogry ID {product_data['category_id']}: Category with specified ID does not exist."))
                logger.error(
                    f"Error adding product with cateogry ID {product_data['category_id']}: Category with specified ID does not exist.")
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Error adding product {product_data['description']}: {e}"))
                logger.error(f"Error adding product {product_data['description']}: {e}", exc_info=True)

        self.stdout.write(self.style.SUCCESS(f"Total products added: {total_products_added}"))
        self.stdout.write(self.style.SUCCESS(f"Total categories added: {total_categories_added}"))
