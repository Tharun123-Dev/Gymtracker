from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import GymUser

@csrf_exempt
def gym_users(request):

    # Handle OPTIONS (CORS preflight)
    if request.method == "OPTIONS":
        response = JsonResponse({"message": "OK"})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # GET: Fetch users
    if request.method == "GET":
        users = list(GymUser.objects.values())
        return JsonResponse(users, safe=False)

    # POST: Save user
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8"))

            name = data.get("name")
            age = data.get("age")
            weight = data.get("weight")
            workout = data.get("workout")

            # Validation
            if not all([name, age, weight, workout]):
                return JsonResponse(
                    {"error": "All fields are required"},
                    status=400
                )

            GymUser.objects.create(
                name=name,
                age=age,
                weight=weight,
                workout=workout
            )

            return JsonResponse({"message": "User added successfully"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    # Fallback (never return None)
    return JsonResponse({"error": "Method not allowed"}, status=405)
