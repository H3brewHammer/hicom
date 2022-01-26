from telethon import TelegramClient
import time
import random

## Paste values from Step 4 here:
api_id = ''
api_hash = ''

## Dont Touch ##
client = TelegramClient('anon', api_id, api_hash)


async def main():
    # Send message to claim reward
    await client.send_message(entity='@hiofficialbot', message="👋 Claim Daily Reward")
    # Wait for multiple choice response - sometimes bot is slow so wait 5 mins to be safe
    time.sleep(60 * 5)
    # Parse the message and choose a random answer
    async for message in client.iter_messages('@hiofficialbot'):
        # Only need to get the first message as this should be latest
        random_answer = random.choice(random.choice(message.reply_markup.rows).buttons).text
        break
    # Respond with the random answer
    await client.send_message(entity='@hiofficialbot', message=random_answer)


with client:
    client.loop.run_until_complete(main())
