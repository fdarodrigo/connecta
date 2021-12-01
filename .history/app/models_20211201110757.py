# Django's imports
from django.db import models

# Developers' imports


"""
This class provides these three parameters for the other classes to inherit and in the django admin,
the superuser can manage the created models.
"""

# This class defines three parameters for easy viewing on the admin panel
class Base(models.Model):
    created = models.DateField("Creation Date", auto_now_add=True)
    modified = models.DateField("Modified Date", auto_now=True)
    active = models.BooleanField("Active?", default=True)

    class Meta:
        abstract = True


# In this class we can create the channel object
class Channel(Base):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("""Description", max_length=200, blank=True, null=True"")

    # Configuration for easy viewing of data on the admin panel
    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"

    def __str__(self):
        return self.name


# In this class we can create the channel content
class Content(Base):
    channel_name = models.ForeignKey(
        Channel, related_name="channel_name", on_delete=models.CASCADE
    )
    text = models.CharField("Text", max_length=500, blank=True)
    image = models.ImageField("Image", upload_to="images/", blank=True)
    file = models.FileField("File", upload_to="files/", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # Configuration for easy viewing of data on the admin panel
    class Meta:
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return self.text
