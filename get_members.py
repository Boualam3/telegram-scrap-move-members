from telethon.sync import TelegramClient
import csv


api_id = 'YOUR_API_ID'
api_hash = '_YOUR_API_HASH'
# international format
phone_number = 'YOUR_PHONE_NUMBER'


# create a new instance of TelegramClient
client = TelegramClient('session_name', api_id, api_hash)


async def scrape_group_users(group_username):
    # connect to telegram
    await client.start(phone_number)

    # get the input entity for the group
    entity = await client.get_entity(group_username)

    # get the list of members from the group
    members = await client.get_participants(entity)

    # Sscrape data from the group members
    scraped_data = []
    for member in members:
        user_data = {
            'User ID': member.id,
            'First Name': member.first_name,
            'Last Name': member.last_name,
            'Username': member.username
        }
        scraped_data.append(user_data)

    # save the scraped data to a csv file
    filename = "users.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=['User ID', 'First Name', 'Last Name', 'Username'])
        writer.writeheader()
        writer.writerows(scraped_data)

    print(f"user data from the group '{group_username}' saved to {filename}")

    # disconnect from telegram
    await client.disconnect()


async def prompt_and_select_group():
    # connect agin to telegram
    await client.start(phone_number)

    # get list of available groups
    dialogs = await client.get_dialogs()

    # filter and print only own groups
    all_groups = []
    print("Your Groups: ")
    for dialog in dialogs:
        if dialog.is_group:
            all_groups.append(dialog)
            print(f"{len(all_groups)}. {dialog.entity.title}")

    # prompt the user to select a group
    group_index = int(
        input("Enter the index of the group you want to scrap there members : "))
    selected_group = all_groups[group_index - 1].entity

    # disconnect from telegram
    await client.disconnect()
    return selected_group

group_username = client.loop.run_until_complete(prompt_and_select_group())

#trigger function to start scraping user data from the group
with client:
    client.loop.run_until_complete(scrape_group_users(group_username))
