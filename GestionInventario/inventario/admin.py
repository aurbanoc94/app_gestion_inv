from django.contrib import admin
from .models import Categoria, Proveedor, Producto, Cliente, Orden, DetalleOrden

admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Orden)
admin.site.register(DetalleOrden)
