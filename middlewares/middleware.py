from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
import logging

logger = logging.getLogger(__name__)
#logging.basicConfig(filename='logs/bot.log', level=logging.INFO)

class MyLoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        # Логирование до обработки
        logging.info(
            f"[{event.date}] Получено сообщение от {event.from_user.full_name} (ID: {event.from_user.id}): {event.text}"
        )

        # Добавляем данные в контекст, доступные в обработчике
        data["start_time"] = event.date

        # Вызываем следующий обработчик в цепочке
        result = await handler(event, data)

        # Логирование после обработки
        logging.info(
            f"Сообщение обработано. Время обработки: {event.date - data['start_time']}"
        )
        return result
