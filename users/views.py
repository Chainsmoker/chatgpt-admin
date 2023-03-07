from django.shortcuts import render, HttpResponse
from .models import BlackListUsers
from django.http import JsonResponse

# Create your views here.
def ban_user(request):
    k = request.GET.get('k')
    username = request.GET.get('username')
    number = request.GET.get('number')
    reason = request.GET.get('reason')
    if k == "989855654" and number and reason:
        try:
            BlackListUsers(number=number, reason=reason).save()
            return JsonResponse(
                {
                    "query": "ban user",
                    "status": "user banned"
                }
            )
        except:
            return JsonResponse(
                {
                    "query": "ban user",
                    "status": "user is already banned or "
                }
            )
    else:
        return JsonResponse(
                {
                    "query": "ban user",
                    "status": "complete the fields"
                }
            )
    

def unban_user(request):
    k = request.GET.get('k')
    number = request.GET.get('number')

    if k == "989855654" and number != '':
        try:
            BlackListUsers.objects.get(number=number).delete()
            return JsonResponse(
                {
                    "query": "unban user",
                    "status": "user unbanned"
                }
            )
        except:
            return JsonResponse(
                {
                    "query": "unban user",
                    "status": "user not banned"
                }
            )
    else:
        return JsonResponse(
                {
                    "query": "unban user",
                    "status": "User not exist"
                }
            )

def check_user(request):
    k = request.GET.get('k')
    number = request.GET.get('number')

    if k == "989855654" and number != '':
        try:
            us = BlackListUsers.objects.get(number=number)
            return JsonResponse(
                {
                    "query": "check user",
                    "status": "banned",
                    "reason": us.reason
                }
            )
        except:
            return JsonResponse(
                {
                    "query": "check user",
                    "status": "User not banned"
                }
            )
    else:
        return JsonResponse(
                {
                    "query": "check user",
                    "status": "User not exist"
                }
            )
