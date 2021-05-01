import csv

from django.http import HttpResponse


def some_view(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["Student name", "Creation date", "Teacher name"])
    response["Content-Distribution"] = "attachment; filename='report.csv'"
    return response
