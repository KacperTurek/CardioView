from django.shortcuts import render
from .models import Database, Signal
from .libs.plot import load_signal, plot_signal

def index(request):
    all_databases = Database.objects.all()
    context = {
        'all_databases':all_databases,
    }
    return render(request, 'sig/index.html', context)

def signal_plot(request):
    database_id = request.POST['database_id']
    signal_display = request.POST['signal_display']
    signals = Signal.objects.all().filter(database_id=database_id).filter(display=signal_display)
    databases = Database.objects.all().filter(pk=database_id)
    signal = signals[0]
    database = databases[0]
    signal_array, comments_array, dict, annotation = load_signal(database.shortcut, signal.shortcut)
    fig = plot_signal(signal_array, annotation)
    context = {
        'signal_array':signal_array,
        'comments_array':comments_array,
        'dict':dict,
        'fig':fig,
    }
    return render(request, 'sig/signal_plot.html', context)
