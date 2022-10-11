from cgitb import text
from http import client
from tabnanny import verbose
from typing_extensions import Self
from django.db import models
from clientes.models import Cliente
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import format_html


