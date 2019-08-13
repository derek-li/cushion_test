from rest_framework import serializers
from .models import Visitor

class VisitorSerializer(serializers.ModelSerializer):
	class Meta: 
		fields = (
			'address',
			'date'
		)
		
		model = Visitor