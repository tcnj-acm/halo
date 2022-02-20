from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


# Returns the type of object for the date that we pass from the shoulder of chop_chop
# If you pass mappings, then you need to pass it in the template, i did Go to the page where you are using it, ill follow u to see it 
@register.filter(name='get_description')
@stringfilter
def get_type(mapping, key):
    thismap = { 
        "statistics" : "View the Statistics for This Years Event",
        "edit-waiting-list" : "Perform Operations on the Waiting List",
        "waiting-list" : "View the Waiting List",
        "manual-checkin" : "Check Hackers in Manually",
        "display-hackers" : "View All of the Registered Hackers"
    }
    return thismap[key]