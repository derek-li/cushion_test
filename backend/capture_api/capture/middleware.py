from .models import Visitor
from django.utils import timezone

class LogMiddleware:

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		visit = Visitor(address=request.get_host(), date=timezone.now())
		visit.save()
		response = self.get_response(request)
		return response
