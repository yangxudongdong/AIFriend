from django.contrib.messages.context_processors import messages
from langchain_core.messages import HumanMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.friend import Friend
from web.views.friend.message.chat.graph import ChatGraph


class MessageChatView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
       friend_id = request.data['friend_id']
       message = request.data['messages'].strip()
       if not message:
           return Response({
               'result': '消息不能为空'
           })
       friends = Friend.objects.get(id=friend_id, me__user=request.user)
       if not friends.exists():
           return Response({
               'result': '好友不存在'
           })
       friends = friends.first()
       app = ChatGraph.create_app()

       inputs = {
           'messages': [HumanMessage(message)]
       }
       res = app.invoke(inputs)
       print(res['messages'][-1].content)

       return Response({
           'result': 'success',
       })


