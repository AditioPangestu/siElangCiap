from django.contrib import admin
from .models import Produk, Bahan, Aksesoris, KebutuhanAksesoris, KebutuhanBahan, HistoriBahan, HistoriAksesoris, ProductionOrder, WIP, ProdukPesanan

class AksesorisProdukInline(admin.TabularInline):
    model = KebutuhanAksesoris.art.through
    extra = 1

class BahanProdukInline(admin.TabularInline):
    model = KebutuhanBahan.art.through
    extra = 1

class ProdukAdmin(admin.ModelAdmin):
    inlines = [
        AksesorisProdukInline,
        BahanProdukInline,
    ]

class ProdukPesananInline(admin.StackedInline):
    model = ProdukPesanan
    extra = 1

class ProductionOrderAdmin(admin.ModelAdmin):
    inlines = [
        ProdukPesananInline
    ]

class HistoriBahanInline(admin.StackedInline):
    model = HistoriBahan
    extra = 1

class HistoriAksesorisInline(admin.StackedInline):
    model = HistoriAksesoris
    extra = 1

class AksesorisAdmin(admin.ModelAdmin):
    inlines = [
        HistoriAksesorisInline,
    ]

class BahanAdmin(admin.ModelAdmin):
    inlines = [
        HistoriBahanInline,
    ]

admin.site.register(Produk,ProdukAdmin)
admin.site.register(ProductionOrder, ProductionOrderAdmin)
admin.site.register(WIP)
admin.site.register(Bahan,BahanAdmin)
admin.site.register(Aksesoris, AksesorisAdmin)

