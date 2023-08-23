from django.urls import path
from .views import StudentListCreateView, StudentRetrieveUpdateDestroy,UpdateMemberStatusView,DeleteStudentView

urlpatterns = [
    #you can use get(for admin) and post(for user) method here
    path("studentdetailspostorget/", StudentListCreateView.as_view(), name='post_custom_student'),
    #you can find by id.and its (for admin);
    path("studentdetailsget/<int:pk>/", StudentRetrieveUpdateDestroy.as_view(), name='get_custom_students'),
    #give permission to user for membership and use patch method here.
    path("addmember/<int:pk>/", UpdateMemberStatusView.as_view(), name='member_create'),
    #admin are able to delete student request or not allow to be a member
    path('delete-student/<int:pk>/', DeleteStudentView.as_view(), name='delete-student'),
]
