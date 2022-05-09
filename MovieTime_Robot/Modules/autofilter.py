import re, asyncio, random
# from pyrogram import Client as MovieTime_Robot, filters as Worker
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MovieTime_Robot.database._utils import get_size, split_list
from MovieTime_Robot.database.autofilter_db import get_filter_results, get_poster
from config import BUTTONS, bot_info, SPELL_MODE, SET_SPEL_M, SUPPORT, BOT_PICS
from translation import MovieTime


#@MovieTime_Robot.on_message(Worker.text & Worker.group & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def group_filters(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"➠ {get_size(file.file_size)} ➠ {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"movietime_robot#{file_id}")]
                )
        else:
            if SPELL_MODE:
                reply = search.replace(" ", '+')  
                reply_markup = InlineKeyboardMarkup([[
                 InlineKeyboardButton("♻️ HELP ♻️", callback_data='help')
                 ],[
                 InlineKeyboardButton("🔍 GOOGLE", url="https://www.google.com/search?q={reply}"),
                 InlineKeyboardButton("IMDB 🔎", url='https://www.imdb.com/find?q={reply}'),
                 ],[
                 InlineKeyboardButton("🗑️ ClOSE 🗑️", callback_data='close')
                 ]]  
                )    
                MovieTime_delete=await message.reply_text(
                    text=SET_SPEL_M.format(query=search, mention=message.from_user.mention),
                    reply_markup=reply_markup                 
                )
                await asyncio.sleep(30) 
                await LuciferMoringstar_delete.delete()
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 1/1",callback_data="pages"),
                 InlineKeyboardButton("🗑️", callback_data="close")]
            )
            buttons.append(
                [InlineKeyboardButton(text="🤖 Check Bot PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
            )

            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"Request For {search} Closed 🗑️")
            elif imdb:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"Request For {search} Closed 🗑️")
            else:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"Request For {search} Closed 🗑️")
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("🗑️", callback_data="close")]
        )
        buttons.append(
            [InlineKeyboardButton(text="🤖 Check Bot PM 🤖", url=f"https://telegram.dog/{bot_info.BOT_USERNAME}")]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            dell=await message.reply_photo(photo=imdb.get('poster'), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"Request For {search} Closed 🗑️")         
        elif imdb:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"Request For {search} Closed 🗑️")
        else:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=message.chat.title), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"Request For {search} Closed 🗑️")



# ---------- Bot PM ---------- #



#@MovieTime_Robot.on_message(Worker.text & Worker.private & Worker.incoming & Worker.chat(AUTH_GROUPS) if AUTH_GROUPS else Worker.text & Worker.group & Worker.incoming)
async def pm_autofilter(client, message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if 2 < len(message.text) < 50:    
        btn = []
        search = message.text
        files = await get_filter_results(query=search)
        if files:
            for file in files:
                file_id = file.file_id
                filename = f"➠ {get_size(file.file_size)} ➠ {file.file_name}"
                btn.append(
                    [InlineKeyboardButton(text=f"{filename}", callback_data=f"pmfile#{file_id}")]
                )
        else:
            await message.reply_photo(
                photo=random.choice(BOT_PICS),
                caption=LuciferMoringstar.ADD_YOUR_GROUP,
                reply_markup=InlineKeyboardMarkup([[
                   InlineKeyboardButton("🔗 Movie Time", url=f"{SUPPORT}")
                   ]]
                )
            )
            return
        if not btn:
            return

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
            keyword = f"{message.chat.id}-{message.message_id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 1/1",callback_data="pages"),
                 InlineKeyboardButton("🗑️", callback_data="close")]
            )


            imdb=await get_poster(search)
            if imdb and imdb.get('poster'):
                dell=await message.reply_photo(photo=imdb.get('poster'), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"Request For {search} Closed 🗑️")
            elif imdb:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"Request For {search} Closed 🗑️")
            else:
                dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))
                await asyncio.sleep(1000)
                await dell.edit(f"Request For {search} Closed 🗑️")

            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="Next Page ➡",callback_data=f"nextgroup_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 1/{data['total']}",callback_data="pages"),
             InlineKeyboardButton("🗑️", callback_data="close")]
        )

        imdb=await get_poster(search)
        if imdb and imdb.get('poster'):
            dell=await message.reply_photo(photo=imdb.get('poster'), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"Request For {search} Closed 🗑️")         
        elif imdb:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_1.format(mention=message.from_user.mention, query=search, title=imdb.get('title'), genres=imdb.get('genres'), year=imdb.get('year'), rating=imdb.get('rating'), url=imdb['url']), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"Request For {search} Closed 🗑️")
        else:
            dell=await message.reply_photo(photo=random.choice(BOT_PICS), caption=MovieTime.GET_MOVIE_2.format(query=search, mention=message.from_user.mention, chat=bot_info.BOT_NAME), reply_markup=InlineKeyboardMarkup(buttons))
            await asyncio.sleep(1000)
            await dell.edit(f"Request For {search} Closed 🗑️")
