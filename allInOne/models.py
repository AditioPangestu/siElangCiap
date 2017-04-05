from __future__ import unicode_literals
from django.urls import reverse
from django.db import models


class Produk(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    art = models.CharField(max_length=10, help_text="ART", primary_key=True)
    nama_produk = models.CharField(max_length=40, help_text="Nama Produk")
    serial = models.CharField(max_length=40, help_text="Serial")
    brand = models.CharField(max_length=40, help_text="Brand", default="Pineapple")
    jenis_tas = models.CharField(max_length=40, help_text="Jenis Tas", default="Ransel")
    keterangan = models.TextField(max_length=100, help_text="Keterangan", null=True)
    contoh_tas = models.CharField(max_length=100, help_text="Contoh Tas")

    # Metadata
    class Meta:
        ordering = ["art"]

    # Methods
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name

class Bahan(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id_bahan = models.CharField(max_length=10, help_text="ID Bahan", primary_key=True)
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
        return self.field_name

class Aksesoris(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    id_aksesoris = models.CharField(max_length=10, help_text="ID Aksesoris", primary_key=True)
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
        return self.field_name