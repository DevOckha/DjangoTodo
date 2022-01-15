from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo

def index(request):
    todos = Todo.objects.all() # Anasayfamızda listeleyeceğimiz todoların tümünü todos değişkenine atıyoruz
    form = TodoForm() #Eğer sayfaya gelen istek GET isteği ise oluşturduğumuz formun döndürdüğü değerleri form adlı değişkende tutuyoruz ve  boş bir form çağırıyoruz 

    if request.method == 'POST': # anasayfamıza gelen isteğin POST isteği olup olmadığını kontrol ediyoruz 

        form = TodoForm(request.POST) # eğer istek POST isteğiyse gelen bilgileri form'a gönderiyoruz
       
        if form.is_valid(): # Eğer form düzgün bir şekilde doldurulmuşsa doğrulama işleminden geçip geçmediğini kontrol ediyoruz
       
            form.save() # eğer doğrulama işleminden geçmişse form'u kaydediyoruz ve form'a doldurulan bilgileri database'e kaydediyoruz
       
            return redirect('/') # form kaydedildikten sonra anasayfamıza yönlendiriyoruz.
    
    context = {'todos':todos, 'form':form} #burada ise anasayfımızda göstermek istediğimiz içeriğimizi ayarlıyoruz
    
    return render(request, 'todo/home.html', context) # ve render ediyoruz



def updateTodo(request, pk):# Burada  oluşturulan todo'nun güncelleme işlemini yapıyoruz onun için gelen istekle birlikte  pk alıyoruz

    todo = Todo.objects.get(id=pk) # güncellenmek istenen todo'yu gelen pk veritabındaki id'si ile  getirip todo değişkenine atıyoruz
    
    form = TodoForm(instance=todo) # Burada gelen istek GET ise form değişkenine TodoForm'u güncellenmek istenen todo'nun bilgileriyle birlikte çağırıyoruz 
    #ve sayfamızda güncellenmek istenen todo'nun bilgileriyle doldurulan TodoForm'u gösteriyoruz

    if request.method == 'POST': # Eğer güncelleme işlemi yapılacaksa  gelen isteğin POST olup olmadığını kontrol ediyoruz POST ise Güncelleme işlemine geçiş yapıyoruz

        form = TodoForm(request.POST, instance=todo) # POST isteği ile gelen değiştirilmiş  bilgileri instance  olarak atadığımız todo'ya yolluyoruz

        if form.is_valid():# Eğer form düzgün bir şekilde doldurulmuşsa doğrulama işleminden geçip geçmediğini kontrol ediyoruz
        
            form.save() # eğer doğrulama işleminden geçmişse form'u güncelliyoruz  ve form'a doldurulan güncellenmiş bilgileri database'e kaydediyoruz
            
            return redirect('/') # form güncellendikten  sonra anasayfamıza yönlendiriyoruz.
    
    context = {'form':form} # burada ise güncellenmiş içeriği  anasayfımızda göstermek için  ayarlıyoruz

    return render(request, 'todo/update_todo.html', context) # ve render ediyoruz




def deleteTodo(request, pk):# Burada ise silmek istediğimiz todo'nun id'si için request ile birlikte bir pk parametresi alıyoruz
    
    todo = Todo.objects.filter(id=pk) # silmek istediğimiz todo'yu databasemizden getirip todo değişkenine atıyoruz

    if request.method == 'POST': # silmek istediğimiz todo için gelen isteğin POST olup olmadığını kontrol ediyoruz eğer istek POST ise silme işlemine geçiyoruz

        todo.delete() # burada ise silinmek istenen todo'nun silme işlemini gerçekleştiriyoruz ve databasemizden siliyoruz

        return redirect('/') # silme işleminden sonra anasayfamıza yönlendiriyoruz

    context = {'todo':todo} # burada ise silmek istediğimiz todo'yu sayfamızda görüntülemek istediğimiz içeriğimizde belirtiyoruz.

    return render(request, 'todo/todo_delete.html', context) # silme işleminin yapılacağı sayfayı render ediyoruz.