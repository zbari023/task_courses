from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='course_category')
    duration = models.IntegerField()

    def __str__(self):
        return self.name


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews_course')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    review = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.course.name} by {self.user.username}"