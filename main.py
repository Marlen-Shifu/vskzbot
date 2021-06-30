import logging

import hashlib

from aiogram import Bot, Dispatcher, executor, types

from config import OLD_TOKEN

from aiogram.types import InlineQuery, \
	InputTextMessageContent, InlineQueryResultArticle

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=OLD_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
	"""
	This handler will be called when user sends `/start` or `/help` command
	"""
	await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.inline_handler()
async def inline_echo(inline_query: InlineQuery):

	text = inline_query.query or 'echo'
	input_content = InputTextMessageContent(text)
	result_id: str = hashlib.md5(text.encode()).hexdigest()
	item = InlineQueryResultArticle(
		id=result_id,
		title=f'Result {text!r}',
		input_message_content=input_content,
	)
	# don't forget to set cache_time=1 for testing (default is 300s or 5m)
	await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates=True)