from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import status, generics

from .serializers import VisitorSerializer
from .models import Visitor
from .capture import Capture

import json

# Create your views here.
class CaptureView:

	@staticmethod
	@api_view(['POST'])
	@parser_classes((JSONParser,))
	def get_text_from_url(request):

		if request.method == "POST" :

			text = Capture.capture_text(request.data["url"])
			word_frequency = Capture.get_most_frequent_words(text)
			word_frequency_clean = [{"word" : word[0], "frequency" : word[1]} for word in word_frequency]

			return Response(data={
				"text": text,
				"topWords": word_frequency_clean
			}, status=status.HTTP_200_OK)

class ListVisitors(generics.ListCreateAPIView):
	queryset = Visitor.objects.all()
	serializer_class = VisitorSerializer

