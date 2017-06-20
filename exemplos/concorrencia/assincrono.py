import asyncio
from time import time


async def tarefa(segundos):
    print(f'Iniciando async {segundos}', time())
    await asyncio.sleep(segundos)
    print(f'Finalizando Thread {segundos}', time())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*(tarefa(i) for i in (10, 5))))
    loop.close()
