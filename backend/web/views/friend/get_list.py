from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend


class GetListFriendView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            items_count = int(request.query_params.get('items_count', 0))
            friend_raw = Friend.objects.filter(
                me__user=request.user
            ).order_by('-update_time')[items_count: items_count + 20]
            friends = []
            for friend in friend_raw:
                characater = friend.character
                author = characater.author
                friends.append({
                    'id': friend.id,
                    'character': {
                        'id': characater.id,
                        'name': characater.name,
                        'profile': characater.profile,
                        'photo': characater.photo.url,
                        'background_image': characater.background_image.url,
                        'author': {
                            'user_id': author.user_id,
                            'username': author.user.username,
                            'photo': author.photo.url,
                        }
                    }
                })
            return Response({
                'result': 'success',
                'friends': friends,
            })
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })