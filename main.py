from aiogram.utils import executor
import logging
from loader import dp, client
import handlers




logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)



if __name__ == '__main__':
 
    client.start()
    executor.start_polling(dp)
    client.run_until_disconnected()

