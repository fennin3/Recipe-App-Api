from django.db import models



class Comment(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    text = models.CharField(max_length=50000)
    date_posted = models.DateTimeField(auto_now_add=True)



class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField("community_category/")



class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/community_post/")
    author = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    read_time = models.DurationField()
    body = models.CharField(max_length=1000000)
    comments = models.ManyToManyField(Comment, null=True, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)