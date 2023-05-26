from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

class Author(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user_rating = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id_user.username}'

    def update_rating(self):
        rnews = self.object.aggregate(newsRating=Sum('rating_news'))
        rn = 0
        rn += rnews.get('newsRating')
        rcomment = self.id_user.object.aggregate(commentRating=Sum('rating_comment'))
        rc = 0
        rc += rcomment.get('commentRating')
        self.user_rating = rn*3 + rc
        self.save()



class Category(models.Model):
    name_cat = models.CharField(unique=True, max_length=64)


state = 'ST'
news = 'NW'

TYPE = [
    (state, 'Статья'),
    (news, 'Новость')
]


class Post(models.Model):
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    state_news = models.CharField(max_length=2, choices=TYPE, default=news)
    datetime_create = models.DateTimeField(auto_now_add=True)
    id_cat = models.ManyToManyField(Category, through='PostCategory')
    article = models.CharField(max_length=100)
    text = models.TextField()
    rating_news = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.article}:{self.datetime_create}: {self.text[:20]+"..."}'
        #return f'{self.article}:{self.datetime_create}'


    def like(self):
        self.rating_news += 1
        self.save()

    def dislike(self):
        self.rating_news -= 1
        self.save()

    def preview(self):
        viewtext = self.text
        return viewtext[:124]+"..."


class PostCategory(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text_comment = models.TextField()
    datetime_comment = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()