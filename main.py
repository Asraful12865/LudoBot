# main.py

from aiogram import executor
from bot import dp
import handlers.user  # হ্যান্ডলার ইমপোর্ট

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)