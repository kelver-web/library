from .models import CartItem

def cart_item_count(request):
    session_key = request.session.session_key
    if not session_key:
        return {'cart_item_count': 0}
    
    count = CartItem.objects.filter(cart_key=session_key).count()
    return {'cart_item_count': count}
