from __future__ import unicode_literals
from django.urls import reverse
from django.db import models


class Produk(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    art = models.CharField(max_length=10, help_text="ART")
    nama_produk = models.CharField(max_length=40, help_text="Nama Produk")
    serial = models.CharField(max_length=40, help_text="Serial")
    brand = models.CharField(max_length=40, help_text="Brand", default="Pineapple")
    jenis_tas = models.CharField(max_length=40, help_text="Jenis Tas", default="Ransel")
    keterangan = models.TextField(max_length=100, help_text="Keterangan", null=True)
    contoh_tas = models.ImageField(upload_to='uploads/%Y/%m/%d/')

    # Metadata
    class Meta:
        ordering = ["art"]

    # Methods
    def image_thumb(self):
        return '<img src="%s" width="100" height="100" />' % (self.contoh_tas)
    image_thumb.allow_tags = True
    image_thumb.short_description = 'image_thumb'

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return "cek"

class Bahan(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    nama_bahan = models.CharField(max_length=40, help_text="Nama Bahan")
    satuan_barang = models.CharField(max_length=40, help_text="Satuan Bahan", default="Meter")
    warna = models.CharField(max_length=20, help_text="Warna")
    stok_akhir = models.IntegerField(help_text="Stok Akhir", default=0)
    harga_per_meter = models.IntegerField(help_text="Harga/Meter", default=0)
    keterangan = models.TextField(max_length=100, help_text="Keterangan", null=True)
    last_update = models.DateField(help_text="Terakhir Di-update")

    # Metadata
    class Meta:
        ordering = ["nama_bahan"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.nama_bahan

class KebutuhanBahan(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    art = models.ForeignKey(Produk)
    id_bahan = models.ForeignKey(Bahan)
    pemakaian_untuk = models.TextField(max_length=100, help_text="Pemakaian untuk")
    jumlah_per_lusin = models.IntegerField(help_text="Jumlah/Lusin")
    x = models.IntegerField(help_text="Faktor Pengali(X)", default=1)
    marker = models.FloatField(help_text="Marker", default=1)
    lembar_bahan = models.IntegerField(help_text="Lembar Bahan", default=12)

    # Metadata
    class Meta:
        ordering = ["id_bahan"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return str(self.art)

class HistoriBahan(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id_bahan = models.ForeignKey(Bahan)
    tanggal = models.DateField(help_text="Tanggal")
    nomor_bukti = models.CharField(max_length=10, help_text="Nomor Bukti")
    masuk = models.IntegerField(help_text="Masuk",default=0)
    keluar = models.IntegerField(help_text="Keluar",default=0)

    # Metadata
    class Meta:
        ordering = ["tanggal"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

class Aksesoris(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    nama_aksesoris = models.CharField(max_length=40, help_text="Nama Aksesoris")
    satuan_barang = models.CharField(max_length=40, help_text="Satuan Aksesoris", default="Pieces")
    warna = models.CharField(max_length=20, help_text="Warna")
    stok_akhir = models.IntegerField(help_text="Stok Akhir", default=0)
    harga_per_satuan = models.IntegerField(help_text="Harga/Meter", default=0)
    keterangan = models.TextField(max_length=100, help_text="Keterangan", null=True)
    last_update = models.DateField(help_text="Terakhir Di-update")

    # Metadata
    class Meta:
        ordering = ["nama_aksesoris"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.nama_aksesoris

class KebutuhanAksesoris(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    art = models.ForeignKey(Produk)
    id_aksesoris = models.ForeignKey(Aksesoris)
    pemakaian_di = models.TextField(max_length=100, help_text="Pemakaian di")
    jumlah_per_lusin = models.IntegerField(help_text="Jumlah/Lusin")
    x = models.IntegerField(help_text="Faktor Pengali(X)", default=1)
    marker = models.FloatField(help_text="Marker", default=1)
    lembar_bahan = models.IntegerField(help_text="Lembar Bahan", default=12)

    # Metadata
    class Meta:
        ordering = ["id_aksesoris"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return str(self.art)

class HistoriAksesoris(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id_aksesoris = models.ForeignKey(Aksesoris)
    tanggal = models.DateField(help_text="Tanggal")
    nomor_bukti = models.CharField(max_length=10, help_text="Nomor Bukti")
    masuk = models.IntegerField(help_text="Masuk",default=0)
    keluar = models.IntegerField(help_text="Keluar",default=0)

    # Metadata
    class Meta:
        ordering = ["tanggal"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.id_aksesoris

class ProductionOrder(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    no_po = models.IntegerField(help_text="Production Order Number", default=0)
    cust = models.CharField(max_length=40, help_text="Cust")
    tanggal = models.DateField(help_text="Tanggal")

    # Metadata
    class Meta:
        ordering = ["tanggal"]

    # Methods
    def tanggal_string(self):
        return self.tanggal.strftime('%y-%m-%d')
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.cust

    tanggal_string.short_description = 'tgl'

class ProdukPesanan(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    no_po = models.ForeignKey(ProductionOrder)
    art = models.ForeignKey(Produk)
    qty = models.IntegerField(help_text="Qty")
    delv = models.DateField(help_text="Delv")
    ket = models.TextField(max_length=100, help_text="Ket")

    # Metadata
    class Meta:
        ordering = ["delv"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return str(self.no_po)

class WIP(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    no_po = models.ForeignKey(ProductionOrder)
    art = models.ForeignKey(Produk)
    qty_wip = models.IntegerField(help_text="Qty WIP")
    delivery = models.DateField(help_text="Delivery")
    acc = models.DateField(help_text="ACC", null=True)
    cutt = models.DateField(help_text="CUTT", null=True)
    log = models.DateField(help_text="LOG", null=True)
    tanggal_kirim = models.DateField(help_text="Tanggal Kirim")
    makloon = models.CharField(max_length=20, help_text="Makloon", default="NN")
    sewing_setor = models.IntegerField(help_text="Sewing Setor", default=0)
    wip_sewing = models.IntegerField(help_text="WIP sewing", default=0)
    sisa = models.IntegerField(help_text="Sisa", default=0)
    keterangan = models.TextField(max_length=100, help_text="Keterangan")
    reps = models.IntegerField(help_text="Reps", default=0)

    # Metadata
    class Meta:
        ordering = ["tanggal_kirim"]

    # Methods
    def delv_string(self):
        return self.delivery.strftime('%y-%m-%d')
    def acc_string(self):
        return self.acc.strftime('%y-%m-%d')
    def cutt_string(self):
        return self.cutt.strftime('%y-%m-%d')
    def log_string(self):
        return self.log.strftime('%y-%m-%d')
    def tanggal_kirim_string(self):
        return self.tanggal_kirim.strftime('%y-%m-%d')

    delv_string.short_description = 'delv'
    acc_string.short_description = 'acc'
    cutt_string.short_description = 'cutt'
    log_string.short_description = 'log'
    tanggal_kirim_string.short_description = 'tanggal_kirim'

    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return "cek"

