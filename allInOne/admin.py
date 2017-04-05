from django.contrib import admin
from .models import Produk, Bahan, Aksesoris, KebutuhanAksesoris, KebutuhanBahan, HistoriBahan, HistoriAksesoris, ProductionOrder, WIP, ProdukPesanan

admin.site.register(Produk)
admin.site.register(Bahan)
admin.site.register(Aksesoris)
admin.site.register(KebutuhanBahan)
admin.site.register(KebutuhanAksesoris)
admin.site.register(HistoriAksesoris)
admin.site.register(HistoriBahan)
admin.site.register(ProdukPesanan)
admin.site.register(ProductionOrder)
admin.site.register(WIP)
