from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from api.models import Company, Vacancy


# Create your views here.
def company_list(request):
    companies=Company.objects.all()
    company_json=[company.to_json() for company in companies]
    return JsonResponse(company_json,safe=False)

def company_vacancies(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)



def company_details(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        raise Http404
    return JsonResponse(company.to_json(), safe=False)


def top_ten(request):
    ordered_vacancies = Vacancy.objects.order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in ordered_vacancies]
    return JsonResponse(vacancies_json, safe=False)


def company_vacancies(request, company_id):
    vacancies = Vacancy.objects.filter(company=company_id)
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)


def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        raise Http404
    return JsonResponse(vacancy.to_json(), safe=False)
    


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)




