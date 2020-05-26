# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password

"""para responder los usuarios en el login"""

from .models import CustomUser, TeacherUser, StudentUser, StaffUser, RelativeUser
from institutions.models import EducationalInstitution, Headquarters


from .serializers import (
    UserSerializer,
    InactivateUserSerializer,
    UpdateUserSerializer,
    CreateUserSerializer,
    TeacherSerializer,
    CreateTeacherSerializer,
    UpdateTeacherSerializer,
    StudentSerializer,
    CreateStudentSerializer,
    UpdateStudentSerializer,
    RelativeSerializer,
    CreateRelativeSerializer,
    UpdateRelativeSerializer,
    StaffSerializer,
    CreateStaffSerializer,
    UpdateStaffSerializer,
    UserEncoder,
)
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

""" ===================================================
Las siguientes clases verifican si quien consulta una ruta
tiene el cargo para poder hacer dicha consulta.
"""


class AllowPrincipal(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 1)
        else:
            return False


class AllowSubprincipal(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 2)
        else:
            return False


class AllowPayer(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 3)
        else:
            return False


class AllowAssistant(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 4)
        else:
            return False


class AllowAssistantSIMAT(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = StaffUser.objects.filter(
                user=request.user.codeUser).values('ocupationStaff')
            return bool(quey[1]['ocupationStaff'] == 5)
        else:
            return False


# ============== Metodo del login ===================================================================
class Login(APIView):
    def post(self, request):
        documentIdUser = request.data.get('documentIdUser', None)
        passwordUser = request.data.get('passwordUser', None)
        """si el se reciben bien los parametros busca el usuario"""
        if documentIdUser and passwordUser:
            user_querysets = CustomUser.objects.filter(documentIdUser__iexact=documentIdUser).values(
                'documentIdUser',
                'typeIdeUser',
                'firstNameUser',
                'lastNameUser',
                'emailUser',
                'phoneUser',
                'addressUser',
                'passwordUser',
                'dateOfBirthUser',
                'dateLastAccessUser',
                'genderUser',
                'rhUser',
                'codeHeadquarters',
                'codeIE',
                'is_active'
            )

            """Si lo encuentra y esta activo elimna los campos sencibiles y crea el token"""
            if (user_querysets.exists() and user_querysets[0]['is_active']):
                user = user_querysets[0]
                if(check_password(passwordUser, user['passwordUser'])):
                    user.pop('passwordUser')
                    user.pop('is_active')
                    userC = CustomUser.objects.filter(
                        documentIdUser__iexact=documentIdUser)
                    token, created = Token.objects.get_or_create(user=userC[0])
                    """revisa si es usuario estaff | teacher | student | relative"""
                    staff_querysets = StaffUser.objects.filter(user__documentIdUser__iexact=documentIdUser).values(
                        'codeStaff',
                        'ocupationStaff')
                    if (staff_querysets.exists()):
                        staff = staff_querysets[0]
                        return Response({"message": "Login exitoso",
                                         "code": 200,
                                         "data":  {
                                                    "token": token.key,
                                                    "user_data": {"staff": staff,
                                                                  "user": user}
                                         }})
                    teacher_querysets = TeacherUser.objects.filter(user__documentIdUser__iexact=documentIdUser).values(
                        'codeTeacher',
                        'degreesTeacher')
                    if (teacher_querysets.exists()):
                        teacher = teacher_querysets[0]
                        return Response({"message": "Login exitoso",
                                         "code": 200,
                                         "data":  {
                                             "token": token.key,
                                             "user_data": {"teacher": teacher,
                                                           "user": user}
                                         }})
                    student_querysets = StudentUser.objects.filter(user__documentIdUser__iexact=documentIdUser).values(
                        'codeStudent')
                    if (student_querysets.exists()):
                        student = student_querysets[0]
                        return Response({"message": "Login exitoso",
                                         "code": 200,
                                         "data":  {
                                                    "token": token.key,
                                                    "user_data": {"student": student,
                                                                  "user": user}
                                         }})
                    relative_querysets = RelativeUser.objects.filter(user__documentIdUser__iexact=documentIdUser).values(
                        'codeRelative',
                        'typeRelative',
                        'student')
                    if (relative_querysets.exists()):
                        relative = relative_querysets[0]
                        return Response({"message": "Login exitoso",
                                         "code": 200,
                                         "data":  {
                                                    "token": token.key,
                                                    "user_data": {"relative": relative,
                                                                  "user": user}
                                         }})
                    # Si el usuario existe pero no tiene perfil no puede acceder
                    else:
                        message = "Usuario no tiene un rol asignado"
                        return Response({"message": message,
                                         "code": 204,
                                         "data":  {}})
                else:
                    message = "Contraseña incorrecta"
                    return Response({"message": message, "code": 204, 'data': {}})

            else:
                message = "El id proporcionado no existe o el usuario no está activo"
                return Response({"message": message, "code": 204, 'data': {}})
        else:
            message = "No ha proporciando datos validos"
            return Response({"message": message, "code": 204, 'data': {}})


# ========== CRUD para la informacion basica del usuario ================================================================
# Listar todos los usuarios
class UserList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Listar un usuario por id


class UserDetail(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# Crear un usuario


class UserCreate(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer

# Actualizar datos de un usuario por id


class UserUpdate(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer

# Eliminar usuario


class UserDelete(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

# ========== CRUD para la informacion del Teacher==============================================
# Listar todos los teacher (anida info basica de usuario)


class TeacherList(ListAPIView):
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherSerializer


class TeacherListByIE(ListAPIView):
    queryset = TeacherUser.objects.all()
    serializer_class = TeacherSerializer

    def query_set(self):
        teacher = TeacherUser.objects.all().filter(
            user__codeIE=self.kwargs['codeIE']
        )
        return teacher

# Listar un teacher por id


class TeacherDetail(RetrieveAPIView):
    queryset=TeacherUser.objects.all()
    serializer_class=TeacherSerializer

# Crear teacher asignando un usuario ya existente


class TeacherCreate(ListCreateAPIView):
    queryset=TeacherUser.objects.all()
    serializer_class=CreateTeacherSerializer

# Crear un grupo de teacher completos


class TeacherCreateMultiple(APIView):
    queryset=TeacherUser.objects.all()

    def post(self, request):
        data=request.data
        for user in data:
            usuario=user.pop('user')
            print(usuario['documentIdUser'])
            codeIE=usuario.pop('codeIE')
            IE=EducationalInstitution.objects.get(nitIE = codeIE)
            codeHeadquarters=usuario.pop('codeHeadquarters')
            Headq=Headquarters.objects.get(codeHeadquarters = codeHeadquarters)
            usuario['passwordUser']=make_password(usuario['passwordUser'])
            print('Paso por aqui')
            custom=CustomUser.objects.create(
                codeIE = IE, codeHeadquarters = Headq, **usuario)
            print('Paso por aqui')
            teacher=TeacherUser.objects.create(user = custom, **user)
        return Response({"message": "Creacion exitoso",  "code": 200})

# Actualizar datos de teacher por id


class TeacherUpdate(UpdateAPIView):
    queryset=TeacherUser.objects.all()
    serializer_class=UpdateTeacherSerializer

# Eliminar Un teacher sin afectar usuario


class TeacherDelete(DestroyAPIView):
    queryset=TeacherUser.objects.all()
    serializer_class=TeacherSerializer


class TeacherAllowHeadquarters(ListAPIView):
    queryset=TeacherUser.objects.all()
    serializer_class=TeacherSerializer

    def get_queryset(self):
        charga=TeacherUser.objects.all().filter(
            user__codeHeadquarters=self.kwargs['codeHeadquarters'])
        return charga


# ========== CRUD para la informacion del Student==============================================
# Listar todos los student (anida info basica de usuario)


class StudentList(ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer


class StudentListByIE(ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer

    def query_set(self):
        teacher = StudentUser.objects.all().filter(
            user__codeIE=self.kwargs['codeIE']
        )
        return teacher

class StudentAllowHeadquarters(ListAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer

    def get_queryset(self):
        charga = StudentUser.objects.all().filter(
            user__codeHeadquarters=self.kwargs['codeHeadquarters'])
        return charga


# Listar un student por id


class StudentDetail(RetrieveAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer

# Crear student asignando un usuario ya existente


class StudentCreate(ListCreateAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = CreateStudentSerializer

# Crear un grupo de student completos


class StudentCreateMultiple(APIView):
    queryset = StudentUser.objects.all()

    def post(self, request):
        data = request.data
        for user in data:
            print(user)
            usuario = user.pop('user')
            codeIE = usuario.pop('codeIE')
            IE = EducationalInstitution.objects.get(nitIE=codeIE)
            codeHeadquarters = usuario.pop('codeHeadquarters')
            Headq = Headquarters.objects.get(codeHeadquarters=codeHeadquarters)
            usuario['passwordUser'] = make_password(usuario['passwordUser'])
            custom = CustomUser.objects.create(
                codeIE=IE, codeHeadquarters=Headq, **usuario)
            student = StudentUser.objects.create(user=custom, **user)
        return Response({"message": "Creacion exitoso",  "code": 200})

# Actualizar datos de Student por id


class StudentUpdate(UpdateAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = UpdateStudentSerializer

# Eliminar Un teacher sin afectar usuario


class StudentDelete(DestroyAPIView):
    queryset = StudentUser.objects.all()
    serializer_class = StudentSerializer

# ========== CRUD para la informacion del Relative==============================================
# Listar todos los Relative (anida info basica de usuario)


class RelativeList(ListAPIView):
    queryset = RelativeUser.objects.all()
    serializer_class = RelativeSerializer

# Listar un student por id


class RelativeDetail(RetrieveAPIView):
    queryset = RelativeUser.objects.all()
    serializer_class = RelativeSerializer

# Crear student asignando un usuario ya existente


class RelativeCreate(ListCreateAPIView):
    queryset = RelativeUser.objects.all()
    serializer_class = CreateRelativeSerializer

# Crear un grupo de Relative completos


class RelativeCreateMultiple(APIView):
    queryset = RelativeUser.objects.all()

    def post(self, request):
        data = request.data
        for user in data:
            print(user)
            usuario = user.pop('user')
            usuario['passwordUser'] = make_password(usuario['passwordUser'])
            custom = CustomUser.objects.create(**usuario)
            relative = RelativeUser.objects.create(user=custom, **user)
        return Response({"message": "Creacion exitoso",  "code": 200})

# Actualizar datos de Relative por id


class RelativeUpdate(UpdateAPIView):
    queryset = RelativeUser.objects.all()
    serializer_class = UpdateRelativeSerializer


# Eliminar Un Relative sin afectar usuario
"""class RelativetDelete(DestroyAPIView):
    queryset = RelativeUser.objects.all()
    serializer_class = RelativeSerializer
"""
# ========== CRUD para la informacion del trabajador =======================================

# Listar todos los Staff


class StaffList(ListAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = CreateStaffSerializer

# Listar un Staff por id


class StaffDetail(RetrieveAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffSerializer

# Crear un grupo de trabajadores


class StaffCreateMultiple(APIView):

    queryset = StaffUser.objects.all()

    def post(self, request):
        data = request.data
        for user in data:
            print(user)
            usuario = user.pop('user')
            codeIE = usuario.pop('codeIE')
            IE = EducationalInstitution.objects.get(nitIE=codeIE)
            codeHeadquarters = usuario.pop('codeHeadquarters')
            Headq = Headquarters.objects.get(codeHeadquarters=codeHeadquarters)
            usuario['passwordUser'] = make_password(usuario['passwordUser'])
            custom = CustomUser.objects.create(
                codeIE=IE, codeHeadquarters=Headq, **usuario)
            staff = StaffUser.objects.create(user=custom, **user)

        return Response({"message": "Creacion exitoso",  "code": 200})

# Crear staff incluyendo usuario al mismo tiempo


class StaffCreate(ListCreateAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = CreateStaffSerializer

# Actualizar datos del trabajador por id


class StaffUpdate(UpdateAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffSerializer

# Eliminar Un trabajador sin afectar usuario


class StaffDelete(DestroyAPIView):
    queryset = StaffUser.objects.all()
    serializer_class = StaffSerializer
