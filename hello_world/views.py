import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.debug("Request data: %s", request.GET)
    return HttpResponse("Hello, world!")
