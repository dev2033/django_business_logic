from django.http import JsonResponse

from .services import add_to_common_mailchimp_list, \
    add_email_to_case_mailchimp_list


def add_to_common_mailchimp_list_view(request):
    """Веб-сервис, добавляющий email в общий лист рассылки"""

    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success': False, 'message': 'Передайте email'})
    add_to_common_mailchimp_list(email=email)
    return JsonResponse({'success': True})


def add_to_case_mailchimp_list_view(request):
    """Веб-сервис добавляющий email в лист рассылок по конкретному делу"""

    email = request.GET.get('email')
    if not email:
        return JsonResponse({'success': False, 'message': 'Передайте email'})
    case_id = request.GET.get('case_id')
    if not case_id:
        return JsonResponse({'success': False, 'message': 'Передайте case_id'})
    add_email_to_case_mailchimp_list(email=email, case_id=case_id)

    return JsonResponse({'success': True})
