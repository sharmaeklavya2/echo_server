from __future__ import print_function

from django.http import HttpResponse
from django.utils import timezone
import json

def index(request):
	format_str = """URL:
{url}

URL with querystring:
{full_url}

METHOD:
{method}

HEADERS:
{headers}

BODY:
{body}

COOKIES:
{cookies}

QUERYSTRING:
{qstr}

POST DATA:
{post}

SERVER TIME in UTC:
{sutime}
"""

	http_headers = {}
	for key, value in request.META.items():
		if key.startswith("HTTP_"):
			http_headers[key] = value
	keys = ('CONTENT_TYPE', 'REMOTE_ADDR',)
	for key in keys:
		if key in request.META:
			http_headers[key] = request.META[key]
	headers_str = json.dumps(http_headers, indent=2)
#	headers_str = request.META

	qstr = json.dumps(request.GET, indent=2)
	post = json.dumps(request.POST, indent=2)
	cookies = json.dumps(request.COOKIES, indent=2)

	response_str = format_str.format(url=request.path, full_url=request.get_full_path(), method=request.method,
		headers=headers_str, body=request.body, cookies=cookies, qstr=qstr, post=post, sutime=timezone.now())
	return HttpResponse(response_str, content_type='text/plain')
