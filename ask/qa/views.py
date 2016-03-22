from django.http import HttpResponse

def test(reqest, *args, **kwargs):
	return HttpResponse('OK')
