from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
import string ,random 
# Create your views here.
def random_password(request : HttpRequest):
    source = string.ascii_letters + string.digits+string.punctuation
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(source) for i in range(16))
    context={
        "random_pass": result_str
    }
    
    return render(request,"password/index.html",context)


    '''def random_password(request : HttpRequest):
        random_pass_list=random.choice("ijrhgbkjflworeiwru1234321!@#$%"k=15)
        random_pass_str="".join(random_pass_list)
    
    return render(request,"password/index.html",{"pass":random_pass_str})'''