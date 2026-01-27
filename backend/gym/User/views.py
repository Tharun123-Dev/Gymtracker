from django.http import JsonResponse
from .models import *
from .utils import workout_suggestion

def member_api(request, member_id):
    member = MemberProfile.objects.get(id=member_id, is_approved=True)

    workouts = DailyWorkout.objects.filter(member=member)
    attendance = Attendance.objects.filter(member=member).count()

    return JsonResponse({
        "name": member.user.username,
        "age": member.age,
        "height": member.height,
        "weight": member.weight,
        "goal": member.goal,
        "trainer": member.assigned_trainer.username if member.assigned_trainer else "Not Assigned",
        "suggestion": workout_suggestion(member.goal),
        "attendance": attendance,
        "workouts": [
            {
                "date": w.date.strftime("%Y-%m-%d"),
                "details": w.workout_details
            } for w in workouts
        ]
    })
