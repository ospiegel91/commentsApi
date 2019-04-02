from django.http import JsonResponse
import urllib, json

URL = "https://jsonplaceholder.typicode.com/comments"


def get_posts(request, post_id):
    try:
        response = urllib.request.urlopen(URL)
    except Exception as e:
        print(e)

    all_comments = json.loads(response.read())
    filtered_list_of_comments = [comment for comment in all_comments if comment["postId"] is post_id];
    return JsonResponse(filtered_list_of_comments, safe=False)
