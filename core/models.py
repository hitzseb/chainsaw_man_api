from django.db import models

# Saga

class Saga(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=25, null=True, blank=True)
    plot = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Arc

class Arc(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    plot = models.TextField(null=True, blank=True)
    saga = models.ForeignKey(Saga, on_delete=models.SET_NULL, null=True, related_name='arcs')

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Volume

class Volume(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    cover = models.URLField(max_length=200, null=True, blank=True)
    plot = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Manga

class Manga(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    cover = models.URLField(max_length=200, null=True, blank=True)
    volume = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True, related_name='chapters')
    arc = models.ForeignKey(Arc, on_delete=models.SET_NULL, null=True, related_name='chapters')
    characters = models.ManyToManyField('Character', blank=True)

    def __str__(self):
        return f'{self.number} | {self.title}'

# Season

class Season(models.Model):
    number = models.IntegerField(unique=True)
    plot = models.TextField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.plot = self.plot.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return f'Season {self.number}'

# Anime

class Anime(models.Model):
    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, related_name='episodes')
    characters = models.ManyToManyField('Character', blank=True, related_name='characters')

    def __str__(self):
        return f'{self.number} | {self.title}'

# Species

class Species(models.Model):
    name = models.CharField(unique=True, max_length=25)
    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.description = self.description.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Character

class Character(models.Model):
    name = models.CharField(unique=True, max_length=50)
    picture = models.URLField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True, related_name='characters')
    manga_debut = models.ForeignKey(Manga, on_delete=models.SET_NULL, null=True, blank=True)
    anime_debut = models.ForeignKey(Anime, on_delete=models.SET_NULL, null=True, blank=True)
    seiyu = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.description = self.description.replace('\r\n', '<br>')

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name