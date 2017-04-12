from django.contrib import admin
from .models import Produk, Bahan, Aksesoris, KebutuhanAksesoris, KebutuhanBahan, HistoriBahan, HistoriAksesoris, ProductionOrder, WIP, ProdukPesanan

class AksesorisProdukInline(admin.StackedInline):
    model = KebutuhanAksesoris
    extra = 1
    fk_name = 'art'

class BahanProdukInline(admin.StackedInline):
    model = KebutuhanBahan
    extra = 1
    fk_name = 'art'

class ProdukAdmin(admin.ModelAdmin):
    list_display = ('art','nama_produk', 'brand','image_thumb')
    inlines = [
        AksesorisProdukInline,
        BahanProdukInline,
    ]

class ProdukPesananInline(admin.StackedInline):
    model = ProdukPesanan
    fk_name = 'no_po'
    extra = 1


class ProductionOrderAdmin(admin.ModelAdmin):
    inlines = [
        ProdukPesananInline
    ]
    list_display = ('no_po', 'cust', 'tanggal')

class WIPAdmin(admin.ModelAdmin):
    list_display = ('no_po', 'art', 'qty_wip','delv_string')


admin.site.register(Produk,ProdukAdmin)
admin.site.register(ProductionOrder, ProductionOrderAdmin)
admin.site.register(WIP, WIPAdmin)
admin.site.register(Bahan)
admin.site.register(Aksesoris)
admin.site.register(HistoriBahan)
admin.site.register(HistoriAksesoris)

