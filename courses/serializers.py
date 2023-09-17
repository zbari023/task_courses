from rest_framework import serializers
from .models import *



class ReviewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'



class CourseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    review_count = serializers.SerializerMethodField()
    reviews = ReviewsSerializers(source='reviews_course',many=True)
    class Meta:
        model = Course
        fields = '__all__'  
    def get_review_count(self,object):
        review = object.reviews_course.all().count()
        return review


    