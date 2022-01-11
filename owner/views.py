import json
from django.http import JsonResponse
from django.views import View

from owner.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name = data['name'],
            age = data['age'],
            email = data['email'],
        )
        return JsonResponse({'message': 'CREATED'}, status=201)
    def get(self, request):
        result = []
        owners = Owner.objects.all()
        dogs = Dog.objects.all()
        dog_list = []
        
        for dog in dogs:
                dog_info ={
                        'name' : dog.name,
                        'age' : dog.age,
                }
                dog_list.append(dog_info)
        for owner in owners:
            result.append(
                {
                    'name' : owner.name,
                    'age' : owner.age,
                    'email' : owner.email,
                    'dog_list' : dog_list,
                }
            )
        
        return  JsonResponse({'owners': result }, status=200)
class DogView(View):
    def post(self, request):
        
        data = json.loads(request.body)
        if not Owner.objects.filter(id=data['owner_id']).exists():
            return JsonResponse({'message': 'Need Owner Information'}, status=404)
        dog = Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner_id = data['owner_id'],
        )
        
        return JsonResponse({'message': 'CREATED'}, status=201)
    
    def get(self, request):
        result = []
        dogs = Dog.objects.all()
        
        for dog in dogs:
            result.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner_name' : dog.owner.name,
                }
            )
        return JsonResponse({'result' : result}, status=200)
