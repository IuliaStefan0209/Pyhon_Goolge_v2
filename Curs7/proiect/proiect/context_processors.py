from aplicatie2.models import Pontaj


def is_ready_to_work(request):
    if request.user.is_authenticated:
        #filter => poate sa returneze unul sau mai multe obiecte
        #       => daca nu gaseste niciun obiect, nu apare eroare
        #get => returneaza un singur obiect
        #    => daca nu gaseste niciun obiect sau returneaza mai multe obiecte, atunci apare eroarea
        if Pontaj.objects.filter(user_id=request.user.id, end_date=None).exists():
            return {'ready_to_work': False}       #pt ca deja a pornit pontajul; context proc returneaza un dict
        return {'ready_to_work': True}
    return {}