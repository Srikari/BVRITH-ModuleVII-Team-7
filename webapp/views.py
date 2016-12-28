from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Login</h1><form>First name:<br><input type='text' name='firstname' ><br>Last name:<br><input type='text' name='lastname'><br><br><input type='submit' value='Submit'></form> ")
