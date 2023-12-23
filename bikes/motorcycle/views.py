import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import MotorcycleForm

JSON_FILE_PATH = 'bike.json'  # Change the file path accordingly

def read_json_data():
    with open(JSON_FILE_PATH, 'r') as file:
        return json.load(file)

def write_json_data(data):
    with open(JSON_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=2)

def motorcycle_list(request):
    motorcycles = read_json_data()
    return render(request, 'motorcycles/motorcycle_list.html', {'motorcycles': motorcycles})

def motorcycle_detail(request, motorcycle_id):
    motorcycles = read_json_data()
    motorcycle = next((m for m in motorcycles if m['id'] == motorcycle_id), None)

    if motorcycle:
        return render(request, 'motorcycles/motorcycle_detail.html', {'motorcycle': motorcycle})
    else:
        return JsonResponse({'error': 'Motorcycle not found'}, status=404)

@csrf_exempt
def create_motorcycle(request):
    if request.method == 'POST':
        form = MotorcycleForm(request.POST)
        if form.is_valid():
            motorcycles = read_json_data()
            new_motorcycle = {
                'id': len(motorcycles) + 1,
                'brand': form.cleaned_data['brand'],
                'model': form.cleaned_data['model'],
                'year': form.cleaned_data['year'],
                'max_speed': form.cleaned_data['max_speed'],
            }
            motorcycles.append(new_motorcycle)
            write_json_data(motorcycles)

            return JsonResponse({'message': 'Motorcycle created successfully'})
        else:
            return JsonResponse({'error': 'Invalid form data'})
    else:
        form = MotorcycleForm()
    return render(request, 'motorcycles/motorcycle_form.html', {'form': form})

# views.py
@csrf_exempt
def delete_motorcycle(request, motorcycle_id):
    motorcycles = read_json_data()
    motorcycle_index = next((index for index, m in enumerate(motorcycles) if m['id'] == motorcycle_id), None)

    if motorcycle_index is not None:
        deleted_motorcycle = motorcycles.pop(motorcycle_index)
        write_json_data(motorcycles)
        return JsonResponse({'message': 'Motorcycle deleted successfully'})
    else:
        return JsonResponse({'error': 'Motorcycle not found'}, status=404)

@csrf_exempt
def update_motorcycle(request, motorcycle_id):
    motorcycles = read_json_data()
    motorcycle = next((m for m in motorcycles if m['id'] == motorcycle_id), None)

    if not motorcycle:
        return JsonResponse({'error': 'Motorcycle not found'}, status=404)

    if request.method == 'POST':
        form = MotorcycleForm(request.POST)
        if form.is_valid():
            updated_data = form.cleaned_data
            # Update the existing motorcycle data
            motorcycle.update(updated_data)
            write_json_data(motorcycles)
            return JsonResponse({'message': 'Motorcycle updated successfully'})
    else:
        # Pre-fill the form with existing data
        form = MotorcycleForm(initial=motorcycle)

    return render(request, 'motorcycles/motorcycle_detail.html', {'motorcycle': motorcycle, 'form': form})
