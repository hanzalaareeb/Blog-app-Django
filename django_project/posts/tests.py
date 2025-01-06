from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Add a user and a post to the database before each test
        """
        
        cls.user = get_user_model().object.createuser(
            username = "testuser",
            email = "testuser@example.com",
            password = "testpassword"
            
        )
        cls.post = Post.objects.create(
            author = cls.user,
            title = "Test Post",
            body = "test body",
        )
    def Test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.body, "test body")
        self.assertEqual(str(self.post), "Test Post")
        