from django import forms
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import ModelForm, widgets
from django.dispatch import receiver
from django.db.models.signals import post_save




# Create your models here.
class Image(models.Model):
    image = CloudinaryField('pictures')
    image_date = models.DateTimeField(auto_now_add=True ,null=True)
    name = models.CharField(max_length =30)
    caption = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.user
    # save image
    def save_image(self):
        self.save()

    # delete image
    def delete_image(self):
        self.delete()
    # get all images
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images
    # update image caption
    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    # search images by name
    @classmethod
    def search_images(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term).all()
        return images
class Profile(models.Model):
   
    profile_photo=CloudinaryField('pictures')
    bio=models.TextField()
    first_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20,null=True)
    user_name=models.CharField(max_length=20,null=True)
   
    def __str__(self):
        return f'{self.user_name} Profile'

    def save_profile(self):
        self.save()

    # update profile
    def update_profile(self, name):
        self.name = name
        self.save()

     # delete profile from database
    def delete_profile(self):
        self.delete()
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

  
    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    content=models.TextField(null=True)
    
    def __str__(self):
        return (self.image)
    def save_comment(self):
        self.save()

    # update comments
    def update_comment(self, name):
        self.name = name
        self.save()

     # delete comments from database
    def delete_comments(self):
        self.delete()
class Likes(models.Model):
    image = models.ForeignKey(Image,related_name='like_count', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.image
    def save_likes(self):
        self.save()

    # update like
    def update_likes(self, name):
        self.name = name
 
     # delete like from database
    def delete_likes(self):
        self.delete()
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'image'], name="unique_like"),
        ]
class AddImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image','caption','name']
class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_photo']
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['content']
        widgets= {
            'content':forms.Textarea(attrs={'rows':2,})
        }
        
        
        
class Follow(models.Model):
    users=models.ManyToManyField(User,related_name='follow')
    current_user=models.ForeignKey(User,related_name='c_user',null=True, on_delete=models.CASCADE)

    @classmethod
    def follow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.add(new)

    @classmethod
    def unfollow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.remove(new)

       