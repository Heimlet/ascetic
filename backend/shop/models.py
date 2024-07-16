from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    home_page_order = models.PositiveSmallIntegerField(verbose_name="Order at home page", null=True, default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    specs = models.TextField()
    texture = models.CharField(max_length=255)
    weight = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    is_proud_of = models.BooleanField(verbose_name="Product we are proud of", default=False)
    is_trending_now = models.BooleanField(verbose_name="Is trending now", default=False)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='other_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"


class Cart(models.Model):
    session_id = models.CharField(max_length=255, unique=True)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return self.session_id


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
