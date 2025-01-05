from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import random

# Replace 'YOUR_BOT_TOKEN' with your Telegram Bot API token
BOT_TOKEN = '8053216650:AAEEGYOchLI0cEqcCiZiUdpmpkFkaPEDZK0'

# List of unique movie titles with YouTube links
MOVIE_TITLES = [
    {"title": "Inception", "link": "https://www.youtube.com/watch?v=YoHD9XEInc0"},
    {"title": "The Matrix", "link": "https://www.youtube.com/watch?v=m8e-FF8MsqU"},
    {"title": "The Shawshank Redemption", "link": "https://www.youtube.com/watch?v=6hB3S9bIaco"},
    {"title": "Interstellar", "link": "https://www.youtube.com/watch?v=zSWdZVtXT7E"},
    {"title": "Parasite", "link": "https://www.youtube.com/watch?v=SEUXfv87Wpk"},
    {"title": "The Dark Knight", "link": "https://www.youtube.com/watch?v=EXeTwQWrcwY"},
    {"title": "Fight Club", "link": "https://www.youtube.com/watch?v=SUXWAEX2jlg"},
    {"title": "Pulp Fiction", "link": "https://www.youtube.com/watch?v=s7EdQ4FqbhY"},
    {"title": "Forrest Gump", "link": "https://www.youtube.com/watch?v=bLvqoHBptjg"},
    {"title": "The Godfather", "link": "https://www.youtube.com/watch?v=sY1S34973zA"},
    {"title": "The Lord of the Rings", "link": "https://www.youtube.com/watch?v=V75dMMIW2B4"},
    {"title": "Titanic", "link": "https://www.youtube.com/watch?v=kVrqfYjkTdQ"},
    {"title": "Avatar", "link": "https://www.youtube.com/watch?v=5PSNL1qE6VY"},
    {"title": "Gladiator", "link": "https://www.youtube.com/watch?v=owK1qxDselE"},
    {"title": "Joker", "link": "https://www.youtube.com/watch?v=zAGVQLHvwOY"},
    {"title": "The Social Network", "link": "https://www.youtube.com/watch?v=lB95KLmpLR4"},
    {"title": "Whiplash", "link": "https://www.youtube.com/watch?v=7d_jQycdQGo"},
    {"title": "The Prestige", "link": "https://www.youtube.com/watch?v=o4gHCmTQDVI"},
    {"title": "Mad Max: Fury Road", "link": "https://www.youtube.com/watch?v=hEJnMQG9ev8"},
    {"title": "The Wolf of Wall Street", "link": "https://www.youtube.com/watch?v=iszwuX1AK6A"}
]

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply(
        "Welcome to the Movie Bot!\n"
        "Send me a number, and I'll provide that many unique movies with YouTube links!"
    )

@dp.message_handler()
async def send_movies(message: Message):
    try:
        # Convert the message text to an integer
        num_movies = int(message.text)

        if num_movies < 1:
            await message.reply("Please send a number greater than 0.")
            return

        # Select random movies (ensure no duplicates)
        selected_movies = random.sample(MOVIE_TITLES, min(num_movies, len(MOVIE_TITLES)))

        # Format the response with movie titles and links
        response = "\n\n".join([f"{movie['title']}\nWatch here: {movie['link']}" for movie in selected_movies])

        # Send the movies as a reply
        await message.reply(response)

    except ValueError:
        await message.reply("Please send a valid number.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
