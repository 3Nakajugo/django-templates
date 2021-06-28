from django.shortcuts import render

# Create your views here.
def index(request):
    meetups = [{
        'title': 'First meetup',
        'location': 'uganda',
        'slug':'first-meetup'
    }, 
    {
        'title': 'second meetup',
        'location': 'uganda',
        'slug':'second-meetup'
    }
    ]
    return render(request, 'meetups/index.html', {'showmeetups':True,'meetups':meetups})


def meetup_detials(request, meetup_slug):
    selected_meetup = {
        'title': 'second meetup',
        'description': 'this is the first meetup'
    }
    return render(
request, 'meetups/meetup-details.html', {
    'meetup_title': selected_meetup['title'],
    'meetup_desc': selected_meetup['description']
}
    )