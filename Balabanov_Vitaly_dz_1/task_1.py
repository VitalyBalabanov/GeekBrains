#Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#в остальных случаях: <d> дн <h> час <m> мин <s> сек.

def convert_time(duration: int) -> str:

    time_string = ""

    if duration < 60:

        time_string = f'{duration} секунд '

    elif duration < 3600:

        minutes = duration // 60

        time_string = f'{minutes} минут , {duration % 60}, cекунд'

    elif duration < 86400:

        hours = duration // 3600

        minutes = (duration - (duration // 3600) * 3600) // 60

        time_string = F'{hours} час, {minutes} минут, {duration % 60} cекунд'

    else:

        days = duration // 86400

        hours = (duration - days * 86400) // 3600

        minutes = (duration - days * 86400 - hours * 3600) // 60

        time_string = F'{days} суток, {hours} часа, {minutes} минут, {duration % 60} cекунд '
    return time_string


duration = 400153
result = convert_time(duration)
print(result)