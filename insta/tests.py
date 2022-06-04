from msilib.schema import Class
from django.test import TestCase
from .models import Comment,Profile,Likes,Image
from django.contrib.auth.models import User
# Create your tests here.

class ImageTestCase(TestCase):
    
    def setUp(self):
        """
        
        """
        self.user=User(username='JOdero',email='odero@gmail.com',password='jko@2000')
        self.image=Image(image='blvck.jpg',name='black',caption='pretty awesome',user=self.user)
        self.comment=Comment(image=self.image,user=self.user,content='yeahh')
        self.like=Likes(image=self.image,user=self.user)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.comment,Comment))
        self.assertTrue(isinstance(self.like,Likes))
        
    def test_save(self):
        self.user.save()
        self.image.save_image()
        self.comment.save_comment()
        self.like.save_likes()
        users = User.objects.all()
        images = Image.objects.all()
        comments = Comment.objects.all()
        likes = Likes.objects.all()
        self.assertTrue(len(images) > 0)
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(comments) > 0)
        self.assertTrue(len(likes) > 0)
       #test for update 
    def test_update(self):
        self.user.save()
        self.image.save_image()
        self.image.update_caption('so pretty')
        caption_update=self.image.caption
        self.assertEqual(caption_update,'so pretty')
  #test todelete
    def test_delete(self):
        self.user.save()
        self.image.save_image()
        self.comment.save_comments()
        self.like.save_likes()
        Likes.objects.get(id =self.like.id).delete()
        Comment.objects.get(id =self.comment.id).delete()
        Image.objects.get(id =self.image.id).delete()
        User.objects.get(id =self.user.id).delete()
        likes=Likes.objects.all()
        comments=Comment.objects.all()
        images=Image.objects.all()
        users=User.objects.all()
        self.assertTrue(len(images) == 0)
        self.assertTrue(len(users) == 0)
        self.assertTrue(len(comments) == 0)
        self.assertTrue(len(likes) == 0)
    