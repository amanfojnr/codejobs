from django.db import models

# Create your models here.


class Listing(models.Model):
    """
    represent a job listing object
    """
    title = models.CharField(max_length=100)
    company = models.ForeignKey("Company", related_name="listings")
    location = models.CharField(max_length=100)
    job_description = models.TextField()
    application_link = models.URLField()
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        """ returns string representation of Listing """
        return "{}".format(self.title)


class Company(models.Model):
    """
    represents a company account
    """
    name = models.CharField(max_length=100)
    user = models.OneToOneField("auth.User")
    short_description = models.TextField()
    official_website = models.URLField()

    def __str__(self):
        """ returns string representation of Company """
        return "{}".format(self.name)