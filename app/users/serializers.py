from rest_framework import serializers
from users.models import CustomUser, TeacherUser, StudentUser, RelativeUser, StaffUser
from django.contrib.auth.hashers import make_password
from json import JSONEncoder


# Para agregar las avidencias al usuario
from files.serializers import EvidenceSerializer
from files.models import Evidence

# ========== Serializador para el usuario ================================================================


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
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
            'codeIE',
            'codeHeadquarters',
            'is_active',
            'is_staff',
            'is_superuser'
        ]

# ========== Serializador para  el  login usuario ==========


class UserEncoder(JSONEncoder, serializers.ModelSerializer):
    def default(self, o):
        return o

# ========== Serializador para crear el usuario ==========


class CreateUserSerializer(serializers.ModelSerializer):

    passwordUser = serializers.CharField(
        max_length=128, style={'input_type': 'passwordUser'})

    class Meta:
        model = CustomUser
        fields = [
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
            'codeIE',
            'codeHeadquarters',
            'is_active',
            'is_staff',
            'is_superuser'
        ]
        extra_kwargs = {'passwordUser': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create(
            documentIdUser=validated_data['documentIdUser'],
            typeIdeUser=validated_data['typeIdeUser'],
            firstNameUser=validated_data['firstNameUser'],
            lastNameUser=validated_data['lastNameUser'],
            emailUser=validated_data['emailUser'],
            phoneUser=validated_data['phoneUser'],
            addressUser=validated_data['addressUser'],
            passwordUser=make_password(validated_data['passwordUser']),
            dateOfBirthUser=validated_data['dateOfBirthUser'],
            dateLastAccessUser=validated_data['dateLastAccessUser'],
            genderUser=validated_data['genderUser'],
            rhUser=validated_data['rhUser'],
            codeIE=validated_data['codeIE'],
            codeHeadquarters=validated_data['codeHeadquarters'],
            is_active=validated_data['is_active'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser']
        )
        user.save()
        return user

# ========== Serializador para inactivar un user ==========


class InactivateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

    def patch(self, request, *args, **kwargs):
        user = self.partial_update(request, *args, **kwargs)
        return user

# ========== Serializador para actualizar el usuario ==========


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
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
            'codeIE',
            'codeHeadquarters',
            'is_active',
            'is_staff',
            'is_superuser'
        ]

    def update(self, instance, validated_data):
        print(validated_data)
        validated_data['passwordUser'] = make_password(
            validated_data['passwordUser'])
        user = super().update(instance, validated_data)
        return user

# ========== Serializador para el teacher ============================================================


class TeacherSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    evidences = EvidenceSerializer(many=True, read_only=True)

    class Meta:
        model = TeacherUser
        fields = [
            'codeTeacher',
            'degreesTeacher',
            'user',
            'evidences'
        ]

# ========== Serializador para crear teacher con usuario ==========


class CreateTeacherSerializer(serializers.ModelSerializer):

    user = UserSerializer()
    #evidences = EvidenceSerializer(many=True)

    class Meta:
        model = TeacherUser
        fields = [
            'codeTeacher',
            'degreesTeacher',
            'user'
        ]

    def create(self, validated_data):
        """upload neted objects"""
        user = validated_data.pop('user')
        user['passwordUser'] = make_password(user['passwordUser'])
        custom = CustomUser.objects.create(**user)
        teacher = TeacherUser.objects.create(user=custom, **validated_data)
        #evidences = validated_data.pop('evidences')
        # for track_data in evidences:
        #    Evidence.objects.create(teacher=teacher, **track_data)
        return teacher

# ========== Serializador para actualizar el teacher ==========


class UpdateTeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = TeacherUser
        fields = [
            'codeTeacher',
            'degreesTeacher'
        ]

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        return user


class StudentSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = StudentUser
        fields = [
            'codeStudent',
           # 'groupStudent',
           # 'journeyStudent',
            'user'
        ]

# ========== Serializador para crear student con usuario ==========


class CreateStudentSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = StudentUser
        fields = [
            'codeStudent',
            #'groupStudent',
            #'journeyStudent',
            'user'
        ]

    def create(self, validated_data):
        user = validated_data.pop('user')
        user['passwordUser'] = make_password(user['passwordUser'])
        custom = CustomUser.objects.create(**user)
        student = StudentUser.objects.create(user=custom, **validated_data)
        return student

# ========== Serializador para actualizar el student ==========


class UpdateStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentUser
        fields = [
            'codeStudent',
            #'groupStudent',
            #'journeyStudent'
        ]

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        return user


# ========== Serializador para el relative ============================================================


class RelativeSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = RelativeUser
        fields = [
            'codeRelative',
            'typeRelative',
            'student',
            'user']

# ========== Serializador para crear relative con usuario ==========


class CreateRelativeSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = RelativeUser
        fields = [
            'codeRelative',
            'typeRelative',
            'student',
            'user'
        ]

    def create(self, validated_data):
        user = validated_data.pop('user')
        user['passwordUser'] = make_password(user['passwordUser'])
        custom = CustomUser.objects.create(**user)
        relative = RelativeUser.objects.create(user=custom, **validated_data)
        return relative

# ========== Serializador para actualizar el relative ==========


class UpdateRelativeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RelativeUser
        fields = [
            'codeRelative',
            'typeRelative',
            'student',
        ]

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        return user

# ========== Serializador para el trabajador ==========================================================


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffUser
        fields = ['codeStaff', 'ocupationStaff']

# ========== Serializador: crea trabajador con usuario al tiempo ==========


class CreateStaffSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StaffUser
        fields = ['codeStaff', 'ocupationStaff', 'user']

    def create(self, validated_data):
        user = validated_data.pop('user')
        user['passwordUser'] = make_password(user['passwordUser'])
        custom = CustomUser.objects.create(**user)
        staff = StaffUser.objects.create(user=custom, **validated_data)
        return staff

# ========== Serializador para actualizar el staff ==========


class UpdateStaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffUser
        fields = ['codeStaff', 'ocupationStaff']

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        return user
