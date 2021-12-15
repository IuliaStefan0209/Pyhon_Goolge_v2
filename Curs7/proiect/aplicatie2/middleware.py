from aplicatie2.models import Logs


class RefreshMiddleware:         #nu mosteneste nimic

    def __init__(self, get_response):        #la initializare preia raspunsurile
        self.get_response = get_response     #alocam la initializare acest param

    def __call__(self, request):              #metoda pt ca am nevoie ca clasa mea sa inregistreze date la orice refresh de pe pagina
        if request.user.is_authenticated:     #daca utiliz e autentif
            if request.method == 'GET':
                new_instance = Logs()
                new_instance.user_id = request.user.id     #.user_id e un atribut
                new_instance.action = 'refresh'            #realizez un refresh la get
                new_instance.url = request.path            #daca vreau sa salvez si url-ul
                new_instance.save()                        #salvez datele in baza de date
            elif request.method =='POST':
                action = 'created'                         #aloc o valoare standard
                for item in str(request.path):             #url-ul paginii
                    if item.isdigit():
                        action = 'updated'
                        break
                    else:
                        action = 'created'
                print(action)
                Logs.objects.create(user_id=request.user.id, action=action, url=request.path)
        response = self.get_response(request)
        return response
