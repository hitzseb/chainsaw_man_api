from django.db import models
from PIL import Image;

# Saga

class Saga(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=25, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Arc

class Arc(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    saga = models.ForeignKey(Saga, on_delete=models.SET_NULL, blank=True, null=True, related_name='arcs')

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Volume

class Volume(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    cover = models.ImageField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
        
    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')
        super().save(*args, **kwargs)
        if self.cover:
            self.resize_image()

    def resize_image(self):
        image = Image.open(self.cover.path)
        max_size = (600, 600)
        image.thumbnail(max_size)
        image.save(self.cover.path)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Manga

class Manga(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(blank=True, null=True,)
    cover = models.ImageField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, blank=True, null=True, related_name='chapters')
    arc = models.ForeignKey(Arc, on_delete=models.SET_NULL, blank=True, null=True, related_name='chapters')
    characters = models.ManyToManyField('Character', blank=True)
    
    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')
        super().save(*args, **kwargs)
        if self.cover:
            self.resize_image()

    def resize_image(self):
        image = Image.open(self.cover.path)
        max_size = (600, 600)
        image.thumbnail(max_size)
        image.save(self.cover.path)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Season

class Season(models.Model):
    number = models.IntegerField(unique=True)
    poster = models.ImageField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')
        super().save(*args, **kwargs)
        if self.poster:
            self.resize_image()

    def resize_image(self):
        image = Image.open(self.poster.path)
        max_size = (600, 600)
        image.thumbnail(max_size)
        image.save(self.poster.path)

    def __str__(self):
        return f'Season {self.number}'

# Anime

class Anime(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    still = models.ImageField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, blank=True, null=True, related_name='episodes')
    characters = models.ManyToManyField('Character', blank=True, related_name='characters')
    
    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')
        super().save(*args, **kwargs)
        if self.still:
            self.resize_image()

    def resize_image(self):
        image = Image.open(self.still.path)
        max_size = (400, 400)
        image.thumbnail(max_size)
        image.save(self.still.path)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Species

class Species(models.Model):
    name = models.CharField(unique=True, max_length=25)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.description = self.description.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Character

class Character(models.Model):
    name = models.CharField(unique=True, max_length=50)
    picture = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, blank=True, null=True, related_name='characters')
    manga_debut = models.ForeignKey(Manga, on_delete=models.SET_NULL, blank=True, null=True)
    anime_debut = models.ForeignKey(Anime, on_delete=models.SET_NULL, blank=True, null=True)
    seiyu = models.CharField(max_length=50, blank=True, null=True)
            
    def save(self, *args, **kwargs):
        self.description = self.description.replace('\r\n', '<br>')
        super().save(*args, **kwargs)
        if self.picture:
            self.resize_image()

    def resize_image(self):
        image = Image.open(self.picture.path)
        max_size = (400, 400)
        image.thumbnail(max_size)
        image.save(self.picture.path, format='WEBP', quality=100, save_all=True, optimize=True)

    def __str__(self):
        return self.name