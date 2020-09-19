
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Count
#from .serializers import *
from workspace.models import *
from users.models import *
from institutions.models import *
from groups.models import *
from courses.models import *
from secctions.models import *
from users.models import *

# ========== upload to Resource ===================================================================================


class AmountUserByInstitutio(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['codeIE']
        query = CustomUser.objects.filter(codeIE=ie).count()
        data = { 
            "IE": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)

class AmountTeachersByInstitutio(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['codeIE']
        query = TeacherUser.objects.filter(user__codeIE=ie).count()
        data = { 
            "IE": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)

class AmountStudentsByInstitutio(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['codeIE']
        query = StudentUser.objects.filter(user__codeIE=ie).count()
        data = { 
            "IE": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)


class AmountHeadquartersByIE(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['ieHeadquarters']
        query = Headquarters.objects.filter(ieHeadquarters=ie).count()
        data = { 
            "headquarter": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)




class AmountUserByHeadquarter(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['codeHeadquarters']
        query = CustomUser.objects.filter(codeHeadquarters=ie).count()
        data = { 
            "headquarter": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)

class AmountTeachersByHeadquarter(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['codeHeadquarters']
        query = TeacherUser.objects.filter(user__codeHeadquarters=ie).count()
        data = { 
            "headquarter": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)


class AmountStudentsByHeadquarter(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        ie = self.kwargs['codeHeadquarters']
        print(ie)
        query = StudentUser.objects.filter(user__codeHeadquarters=ie).count()
        data = { 
            "headquarter": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)

class AmountDictateCoursesByHead(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        #query = CustomUser.objects.values('codeIE').order_by('codeIE').annotate(count=Count('author'))
        ie = self.kwargs['head']
        query = AcademicCharge.objects.filter(groupDictate__headquarter=ie).count()
        data = { 
            "headquarter": ie,
            "amount": query 
        }
        return Response(data, status=status.HTTP_200_OK)

class TeacherAcademic_charge_Head(APIView):

    renderer_classes = [JSONRenderer]

    def post(self, request, *args, **kwargs):
        #query = CustomUser.objects.values('codeIE').order_by('codeIE').annotate(count=Count('author'))
        ie = self.kwargs['head']
        query = AcademicCharge.objects.filter(groupDictate__headquarter=ie).values('teacherDictate  ').order_by('teacherDictate').annotate(count=Count('teacherDictate'))
        return Response(query, status=status.HTTP_200_OK)

        