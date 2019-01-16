from django.shortcuts import render

def index(request):
    context = {
        "employees": [
            {
                "first_name": "Raoof",
                "last_name": "Arakkal"
            },
            {
                "first_name": "Emp1 First Name",
                "last_name": "Emp2 Last Name"
            }
        ]
    }
    return render(request, 'app1/index.html', context)
