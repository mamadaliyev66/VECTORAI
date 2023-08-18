from django.db import models


class About(models.Model):
        title=models.CharField(max_length=255,null=False,blank=False)
        text=models.TextField(blank=False,null=False)
        image=models.ImageField(upload_to='page_images',blank=True,null=True)

        def __str__(self):
                return self.title

class HomePage(models.Model):
        main_title=models.CharField(max_length=255,null=False,blank=False)
        text=models.TextField(max_length=255,null=False)

        def __str__(self):
                return self.main_title

        class Meta:
                ordering = ('main_title',)
                verbose_name_plural=("HomePageItems")

class HomePageCard(models.Model):
        card_title = models.CharField(max_length=100, null=False)
        card_image=models.ImageField(upload_to='page_images',blank=False,null=False)

        def __str__(self):
                return self.card_title

class HomePageAbout(models.Model):
        top_main_title=models.CharField(max_length=30)
        title=models.CharField(max_length=50)
        text=models.TextField(blank=True,null=True)
        image=models.ImageField(upload_to='page_images',blank=False,null=False)

        def __str__(self):
                return self.title

class HomePageServicesTitle(models.Model):
        main_title=models.CharField(max_length=255,null=False,blank=False)
        second_title=models.CharField(max_length=255,null=False,blank=False)
        def __str__(self):
                return self.main_title

class HomePageServices(models.Model):
        image=models.ImageField(upload_to='page_images/service_images',null=False,blank=False)
        title=models.CharField(max_length=255,null=False,blank=False)
        text=models.TextField(max_length=255,null=False,blank=False)
        def __str__(self):
                return self.title


class HomePageTeamTitle(models.Model):
        main_title=models.CharField(max_length=100,null=False,blank=False)
        text=models.CharField(max_length=255,null=True,blank=True)
        def __str__(self):
                return self.main_title
class HomePageTeam(models.Model):
        image=models.ImageField(upload_to='page_images/team',null=False,blank=False)
        full_name=models.CharField(max_length=255,null=False,blank=False)
        subject=models.CharField(max_length=30,null=True,blank=True)
        telegram_link=models.CharField(max_length=255,null=True)
        facebook_link=models.CharField(max_length=255,null=True)
        linkedin_link=models.CharField(max_length=255,null=True)
        twitter_link=models.CharField(max_length=255,null=True)

        def __str__(self):
                return self.full_name

class HomePageContact(models.Model):
        main_title=models.CharField(max_length=255,null=False)
        text=models.TextField(max_length=300,null=False)
        location=models.CharField(max_length=255,null=False)
        phone_number=models.CharField(max_length=50,null=False)
        email_address=models.CharField(max_length=50,null=False)

        def __str__(self):
                return self.main_title