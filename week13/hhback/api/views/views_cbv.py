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


def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json(), safe=False)


def company_vacancies(request, company_id):
    try:
        comp = Company.objects.get(id=company_id)
        return JsonResponse(
            [v.to_json() for v in Vacancy.objects.filter(company=comp)],
            safe=False
        )
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json(), safe=False)


def top_ten(request):
    ordered_vacancies = Vacancy.objects.order_by('salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in ordered_vacancies]
    return JsonResponse(vacancies_json, safe=False)


#def @csrf_exempt(view_func):
 #   def wrapped_view(*args, **kwargs):
  #      return view_func(*args, **kwargs)
   # wrapped_views.csrf_exempt=True
    #return wraps(view_func)(wrapped_view)