from django.shortcuts import render
from django.http import HttpResponse
from modeling.models import Creature
from django.db.models import Q
import json
from django.views.decorators.csrf import csrf_exempt

def home_page(request):
    #return render(request, "search.html")
    return render(request, "index.html")

def add_to_db(request):
    with open("rewrite.txt") as f:
        for records in f:
            c_id, s_name, c_name, category, iucn_level, level, location,\
                  location_number, location_style = records.strip().split('_')[0:9]
            try:
                Creature.objects.create(
                    c_id=c_id,
                    s_name=s_name,
                    c_name=c_name,
                    category=category,
                    iucn_level=iucn_level,
                    level=level,
                    location=location,
                    location_number=location_number,
                    location_style=location_style
                )
            except:
                print("duplicate :", c_id)
        return HttpResponse("<html><title>EOL homepage</title><body>insert complete"\
                            "</body></html>")

def re_write(request):
    f1 = open("rewrite.txt", "w")
    with open("baseLine.txt") as f:
        for i in f:
            f1.write(i.strip()+'\n')
    f1.close()
    return HttpResponse("<html><title>EOL homepage</title><body>"\
                        "rewrite complete</body></html>")

@csrf_exempt
def results(request):
    creature = Creature.objects.filter(c_name__icontains=request.POST['item_text'])
    return render(request, "location-detail.html", {"Creature":creature})

def location(request):
    return render(request, "slice.html")

def creature_search(loc):
    # return a creature querySet which lives in seletecd location
    creature = Creature.objects.filter(Q(location__icontains="9999"))
    for i in loc:
        #print(Creature.objects.filter(location__icontains=i).count())
        creature = creature|Creature.objects.filter(location__icontains=i)
        # Use | to combine two QuerySets
    pages = creature.count()
    return creature, pages

@csrf_exempt
def location_detail(request):
    loc = request.POST['locations'].split(',')[:-1]
    creature, pages = creature_search(loc)
    pages = int(pages/5) + 2
    if pages % 5 == 0:
        pages -= 1
    return render(request, "location-detail.html", {"Creature":creature[0:5],
                                                    "pages":range(1, pages),
                                                    "current":1,
                                                    "loc":request.POST['locations']})

def page(request, num):
    loc = request.GET['locations'].split(',')[:-1]
    creature, pages = creature_search(loc)
    page_start = (int(num) - 1) * 5
    pages = int(pages/5) + 2
    if pages % 5 == 0:
        pages -= 1
    return render(request, "location-detail.html", {"Creature":creature[page_start:page_start+5],
                                                    "pages":range(1, pages),
                                                    "current":int(num),
                                                    "loc":request.GET['locations']})

def auto(request):
    # this view is for autocomplete, and it'll return a json
    item_text = request.GET['item_text']
    response_data = Creature.objects.filter(c_name__icontains=item_text)
    list1 = [x.c_name for x in response_data]
    return HttpResponse(json.dumps(list1), content_type="application/json")

def c_search(request):
    return render(request, "search.html")

def location_count(request):
    return render(request, 'slice_count.html')

def evaluate(request):
    return render(request, 'slice.html', {'eva':'on'})

@csrf_exempt
def evaluate_output(request):
    loc = request.POST['locations'].split(',')[:-1]
    level = 0
    point_list = []
    with open('Model7_placeScores.txt') as f:
        for i in f:
            point_list.append(float(i.strip()))
        for i in loc:
            print(point_list[int(i)],int(i))
            level += point_list[int(i)] / len(loc)
    #return HttpResponse('<html><body>'+str(level)+'</body></html>')
    return render(request, 'point.html', {'level':level})

@csrf_exempt
def show_loc(request, c_id):
    c = Creature.objects.filter(c_id=c_id)[0]
    loc = c.location.strip().split(',')[:-1]
    loc_t = []
    for i in loc:
        x = int(i) // 64
        y = int(i) % 64
        loc_t.append(str(y*64+x))
    # return HttpResponse(json.dumps(loc), content_type="application/json")
    return render(request, 'slice.html', {'loc':loc_t})

def parameter_count(request):
    return render(request, 'parameter_count.html')