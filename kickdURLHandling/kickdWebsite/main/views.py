#Assuming this is how it sends stuff over the internet. API Stuff.
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import ScanData
from .stWebScraping import webScraper

# This file displays html to user. Shows webpage.

#Each function is a view. Returns HTML Code

def kickDScanPage(request):

    #Get Connecting URL
    URL=str(request.build_absolute_uri())

    #If URL is the home page then point render home page
    #TODO Fix URL to kickd.io once we get hosting
    if URL == 'http://127.0.0.1:8000/':
        return render(request, "main/homepage.html")

    #Get URL fields
    try:
        URLSPLIT = URL.split("=")
        URLFields=URLSPLIT[1]

        #Validate from ST WEBSERVER
        stCheck = webScraper(URLSPLIT[1])
        if stCheck != 0:
            return HttpResponse("<h1>NOT ABLE TO AUTHENICATE<h1>")
        
        #Variables from needed for verification
        UID=URLFields.split("x")[0]
        CUSTOM_MSG = URLFields.split("x")[1]
        UTC = URLFields.split("x")[2]
    except:
        return HttpResponse("<h1>NOT ABLE TO AUTHENICATE<h1>")

    #TODO Scrape from Blockchain...

    #For Users
    Model = "Air Jordan 1 'Lucky Green'"
    ValidScan = "AUTHENTIC"
    ImageFile = "'Air_Jordan_1_Lucky_Green.png'"
    StoreName = "status"
    StoreSite = 'https://instagram.com/status?igshid=YmMyMTA2M2Y='

    #Build Dictionary to return to html
    scan_dict = {
    "Model": Model,
    "ValidScan": ValidScan, #Always True for now
    "UID": UID,
    "ImageFile": ImageFile,
    "StoreName": StoreName,
    "StoreSite": StoreSite,
    }

    #TODO Check ST and Webserver and render the correct page
    return render(request, "main/scanPage.html", scan_dict)

#Add to database
#scanEntry = ScanData(UID = UID, UTC = UTC, TKN_ID = TKN_ID, TAMP_CHCK=TAMP_CHCK, 
#                     Model = Model)
#scanEntry.save()

#Get Data from database
#show_ScanData = ScanData.objects.all().values()
#show_ScanData = ScanData.objects.get(UID="1")

#Helper Functions########################
