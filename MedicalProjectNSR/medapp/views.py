from django.shortcuts import render


from django.views import View

# Function Based View
def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
    print(email,password)
    return render(request,'login.html')

#End


#------Class Based View
class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(email, password)

        return render(request,'signup.html', {'email': email})

#End---------------

# Create your views here.
