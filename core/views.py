from django.shortcuts import render
from .models import HomePage,HomePageCard,HomePageAbout,HomePageServicesTitle,HomePageServices,HomePageTeam,HomePageTeamTitle,HomePageContact
def home(request):
    home_page_items = HomePage.objects.last()
    home_page_card_items=HomePageCard.objects.filter()[0:6]
    home_page_about_section=HomePageAbout.objects.last()
    home_page_services_titles_section=HomePageServicesTitle.objects.last()
    home_page_services_section=HomePageServices.objects.all()
    home_page_team_title=HomePageTeamTitle.objects.last()
    home_page_team_members=HomePageTeam.objects.all()
    home_page_contact=HomePageContact.objects.last()
    return render(
        request,'core/home.html',{
            "home_page":home_page_items,
            "home_page_card":home_page_card_items,
            "home_page_about_sec":home_page_about_section,
            "services_titles":home_page_services_titles_section,
            "services":home_page_services_section,
            'team_title':home_page_team_title,
            'team':home_page_team_members,
            'contact_info':home_page_contact
        }

    )