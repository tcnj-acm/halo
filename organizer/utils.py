import csv
import random
from django.http import HttpResponse

def download_csv(request, model, attributes_to_export, filter, filter_attr, filter_value, hackers, checked_in):
    if not request.user.is_staff:
        raise PermissionDenied

    field_names = [field.name for field in model._meta.fields if field.name in attributes_to_export]

    model = model.objects
    if filter == True:
        model =  model.objects.filter(**{filter_attr :filter_value})
        
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    data = list(model.values_list(*field_names))
    if hackers ==  True:
        for i in range(len(data)) :
            tup = list(data[i])
            tempTup = []
            for el in tup:
                if ',' in str(el):
                    el = el.replace(',', '')
                tempTup.append(el)
            tup = tempTup
            tup.append('True')
            tup.append('True')
            decider = random.randint(0, 10)
            if decider != 1:
                tup.append('False')
            else:
                tup.append('True')
            tup = tuple(tup)
            data[i] = tup
        field_names.extend(['mlh_code_of_conduct', 'logistics_info', 'communication_from_mlh'])
    if checked_in == True:
        for i in range(len(data)) :
            tup = list(data[i])
            tempTup = []
            for el in tup:
                if ',' in str(el):
                    el = el.replace(',', '')
                tempTup.append(el)
            tup = tempTup
            tup.append('True')
            tup = tuple(tup)
            data[i] = tup
        field_names.append("checked_in")
    # the csv writer
    writer = csv.writer(response, delimiter=";")
    # Write a first row with header information
    writer.writerow(field_names)
    for row in data:
        row = list(row)
        writer.writerow(row)
    return response