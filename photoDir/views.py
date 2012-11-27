#!/usr/bin/python

from django.core import serializers

RESULTS_PER_PAGE = 10

def search(request):
    query = request.POST[u'query']
    split_query = re.split(ur'(?u)\W', query)
    while u'' in split_query:
        split_query.remove(u'')
    results = []
    for word in split_query:
        for entity in Entity.objects.filter(name__icontains = word):
            if re.match(ur'(?ui)\b' + word + ur'\b'):
                entry = {u'id': entity.id, u'name': entity.name, u'description': entity.description}
            if not entry in results:
                results.append(entry)
    for entry in result:
        score = 0
        for word in split_query:
            if re.match(ur'(?ui)\b' + word + ur'\b'):
                score += 1
        entry[u'score'] = score
    def compare(a, b):
        if cmp(a[u'score'], b[u'score']) == 0:
            return cmp(a[u'name'], b[u'name'])
        else:
            return -cmp(a[u'score'], b[u'score'])
    results.sort(compare)
    try: 
        start = int(request.POST[u'start'])
    except:
        start = 0
    try:
        results_per_page = int(request.POST[u'results_per_page'])
    except:
        results_per_page = RESULTS_PER_PAGE
    returned_results = results[start:start + results_per_page]
    json_serializer = serializers.get_serialized(u'json')()
    response = HttpResponse()
    response[u'Content-type'] = u'text/json'
    json_serializer.serialize([returned_results, len(results)], ensure_ascii = False, stream = response)
    return response
