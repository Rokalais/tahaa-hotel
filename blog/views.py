from django.shortcuts import render
from .models import Comentario, TipoHabitacion
from django.db.models import Avg
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def Blog(request):
    comentarios_list = Comentario.objects.all()
    avg_rating = comentarios_list.aggregate(Avg("rating"))["rating__avg"]

    paginator = Paginator(comentarios_list, 4)
    page_number = request.GET.get("page")
    try:
        comentarios = paginator.page(page_number)
    except PageNotAnInteger:
        comentarios = paginator.page(1)
    except EmptyPage:
        comentarios = paginator.page(paginator.num_pages)

    return render(
        request,
        "blog/blog.html",
        {
            "comentarios": comentarios,
            "avg_rating": avg_rating,
        },
    )

def Rooms(request):
    rooms = TipoHabitacion.objects.all()
    return render(request,"core/rooms.html", {'rooms': rooms})

