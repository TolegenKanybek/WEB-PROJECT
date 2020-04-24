from django.http.response import JsonResponse, Http404
from api.models import Company, Vacancy
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import CompanySerializer, VacancySerializer


class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

"""""
@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
"""""


class CompanyDetailsAPIView(APIView):
    def get(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

        if request.method == 'GET':
            serializer = CompanySerializer(company)
            return Response(serializer.data)

    def put(self,request,company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, company_id):
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist as e:
            return Response({'error': str(e)})

        company.delete()

        return Response({'delete': True})



"""""
@api_view(['GET', 'PUT', 'DELETE'])
def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error':serializer.errors})

    elif request.method == 'DELETE':
        company.delete()

        return Response({'delete': True})
    """""


class VacancyListAPIView(APIView):
    def get(self,request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)

    def post(self,request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""""
@api_view(['GET', 'POST'])
def vacancies_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
"""""


class VacancyDetailAPIView(APIView):
    def get(self,request,vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self,request,vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        vacancy.delete()

        return Response({'delete': True})

"""""
@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancy.delete()

        return Response({'delete': True})
"""""


class TopTenAPIView(APIView):
    def get(self, request):
        ordered_vacancies = Vacancy.objects.order_by('salary')[:10]
        serializer = VacancySerializer(ordered_vacancies, many=True)
        return Response(serializer.data)

"""""
@api_view(['GET'])
def top_ten(request):
    ordered_vacancies = Vacancy.objects.order_by('salary')[:10]
    serializer = VacancySerializer(ordered_vacancies, many=True)
    return Response(serializer.data)
"""""


class CompanyVacanciesAPIView(APIView):
    def get(self, request,company_id):
        try:
            vacancies = Vacancy.objects.filter(company_id=company_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def put(self,request,company_id):
        try:
            vacancies = Vacancy.objects.filter(company_id=company_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        serializer = VacancySerializer(instance=vacancies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, company_id):
        try:
            vacancies = Vacancy.objects.filter(company_id=company_id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

        vacancies.delete()
        return Response({'deleted': True})




"""""
@api_view(['GET', 'PUT', 'DELETE'])
def company_vacancies(request, company_id):
    try:
        vacancies = Vacancy.objects.filter(company_id=company_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VacancySerializer(instance=vacancies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        vacancies.delete()
        return Response({'deleted': True})
"""""


