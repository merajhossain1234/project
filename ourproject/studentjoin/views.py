from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    
    
    
    
class UpdateMemberStatusView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #lookup_field = 'user__username' 

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_member = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)




class DeleteStudentView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    #lookup_field = 'user'  # Use 'pk' to lookup by primary key

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)  # No Content