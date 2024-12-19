from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = 'Главная страница'
    text = 'Главная'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'text': text,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'third_task/main_page.html', context)

def first_additional_page(request):
    title = 'Магазин'
    text = 'Игры'
    buy = 'Купить'
    back = 'Вернуться обратно'
    game_1 = "Baldur's Gate III"
    game_2 = 'Cyberpunk 2077'
    game_3 = 'Dragon Age Veilguard'
    context = {
        'title': title,
        'text': text,
        'buy': buy,
        'back': back,
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
    }
    return render(request, 'third_task/first_additional_page.html', context)

def second_additional_page(request):
    title = 'Корзина'
    text = "Извините, Ваша корзина пуста"
    back = 'Вернуться обратно'
    context = {
        'title': title,
        'text': text,
        'back': back
    }
    return render(request, 'third_task/second_additional_page.html', context)
