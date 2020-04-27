from django.db import models
from users.models import TeacherUser
from groups.models import Group

# Create models here........................................................................


class Area(models.Model):
    """Represent a Area object"""
    codeArea = models.AutoField(auto_created=True, primary_key=True,
                                serialize=False, verbose_name='ID')
    nameArea = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return 'The Area was created as: {}, with a code {}'.format(self.nameArea, self.codeArea)


class Course(models.Model):
    """Represent a Course object"""
    codeCourse = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nameCourse = models.CharField(max_length=100, null=False)
    areaCourse = models.ForeignKey(Area, related_name='courses',
                                   on_delete=models.CASCADE)

    def __str__(self):
        return 'The Course was created as: {}, with a code: {}'.format(
            self.nameCourse,
            self.areaCourse)


class AcademicCharge(models.Model):
    """Represent a Academic Charge object"""
    codeAcademicCharge = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    teacherDictate = models.ForeignKey(TeacherUser, on_delete=models.CASCADE)
    courseDictate = models.ForeignKey(Course, on_delete=models.CASCADE)
    groupDictate = models.ForeignKey(Group, on_delete=models.CASCADE)
    hourlyintensity = models.IntegerField(null=False)

    def __str__(self):
        return 'The Academic Charge was created as: course {}, group {}, teacher {} with a intensiti: {}'.format(
            self.courseDictate,
            self.groupDictate,
            self.teacherDictate,
            self.hourlyintensity)


class TimeTable(models.Model):
    """Represent a TimTable object"""
    codeTimeTable = models.AutoField(
        auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    dayTimeTable = models.CharField(max_length=100, null=False)
    startHourTimeTable = models.CharField(max_length=100, null=False)
    endHourTimeTable = models.CharField(max_length=100, null=False)
    courseTimeTable = models.ForeignKey(AcademicCharge, related_name='schedule',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return 'The Timtable was created as: {} the {} at {}, with a code: {}'.format(
            self.dayTimeTable,
            self.startHourTimeTable,
            self.endHourTimeTable,
            self.codeTimeTable)
