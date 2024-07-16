from rest_framework import viewsets, status, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Sum, F
from .models import Category, Product, Cart, CartItem
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, CartItemSerializer


def normalize_boolean_param(param):
    if param is None or param == '':
        return None
    if isinstance(param, str):
        param = param.lower()
        if param in ['true', '1']:
            return True
        if param in ['false', '0']:
            return False
    return bool(int(param))


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        is_main_page = normalize_boolean_param(request.query_params.get('is_main_page', None)),

        if is_main_page is True:
            queryset = queryset.filter(home_page_order__isnull=False).order_by('home_page_order')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class OptionalPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    pagination_class = OptionalPagination

    def list(self, request, *args, **kwargs):
        queryset = self.queryset

        filters = {
            'category__code': request.query_params.get('category', None),
            'is_proud_of': normalize_boolean_param(request.query_params.get('is_proud_of', None)),
            'is_trending_now': normalize_boolean_param(request.query_params.get('is_trending_now', None)),
        }

        for key, value in filters.items():
            if value is not None:
                queryset = queryset.filter(**{key: value})

        page = request.query_params.get('page', None)
        page_size = request.query_params.get('page_size', None)
        if page and page_size:
            paginator = self.pagination_class()
            paginator.page_size = page_size
            paginated_queryset = paginator.paginate_queryset(queryset, request)
            serializer = self.get_serializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        product = Product.objects.get(id=product_id)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
        cart_item.save()
        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=['post'])
    def remove_product(self, request, pk=None):
        cart = self.get_object()
        product_id = request.data.get('product_id')
        product = Product.objects.get(id=product_id)
        CartItem.objects.filter(cart=cart, product=product).delete()
        return Response(CartSerializer(cart).data)

    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        cart = self.get_object()
        cart_items = CartItem.objects.filter(cart=cart)
        total_price = cart_items.aggregate(total_price=Sum(F('product__price') * F('quantity')))['total_price']
        response_data = {
            'products': CartItemSerializer(cart_items, many=True).data,
            'total_price': total_price
        }
        return Response(response_data)
