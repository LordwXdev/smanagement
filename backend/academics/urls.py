from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcademicYearViewSet, GradeViewSet, SectionViewSet, SubjectViewSet, ExamTypeViewSet, ExamViewSet, StudentGradeViewSet
router = DefaultRouter()
router.register("academic-years", AcademicYearViewSet)
router.register("grades", GradeViewSet)
router.register("sections", SectionViewSet)
router.register("subjects", SubjectViewSet)
router.register("exam-types", ExamTypeViewSet)
router.register("exams", ExamViewSet)
router.register("student-grades", StudentGradeViewSet)
urlpatterns = [path("", include(router.urls))]
