from django.http import HttpResponse
import json

def index(request):
	format_str = "URL:\n{url}\n\nURL with querystring:\n{full_url}\n\nMETHOD:\n{method}\n\nHEADERS:\n{headers}\n\nBODY:\n{body}\n\nCOOKIES:\n{cookies}\n\nQUERYSTRING:\n{qstr}\n\nPOST DATA:\n{post}\n"

	http_headers = {}
	for key,value in request.META.items():
		if key.startswith("HTTP_"):
			http_headers[key] = value
	keys = ('CONTENT_TYPE','REMOTE_ADDR',)
	for key in keys:
		if key in request.META:
			http_headers[key] = request.META[key]
	headers_str = json.dumps(http_headers, indent=2)
#	headers_str = request.META

	qstr = json.dumps(request.GET,indent=2)
	post = json.dumps(request.POST,indent=2)
	cookies = json.dumps(request.COOKIES,indent=2)

	response_str = format_str.format(url=request.path, full_url=request.get_full_path(), method=request.method,
		headers=headers_str, body=request.body, cookies=cookies, qstr=qstr, post=post)
	return HttpResponse(response_str, content_type='text/plain')
