from django.shortcuts import render

def tweet_detail_view(request, id=1):
    # Example context data for the detail view
    context = {
        'id': id,
        'tweet': f'This is a detailed view of tweet {id}'  # Placeholder tweet
    }
    return render(request, 'tweets/detail_view.html', context)

def tweet_list_view(request):
    # Example context data for the list view
    context = {
        'tweets': [
            {'id': 1, 'content': 'First tweet!'},
            {'id': 2, 'content': 'Another tweet here.'},
            {'id': 3, 'content': 'Yet another tweet.'}
        ]
    }
    return render(request, 'tweets/list_view.html', context)
