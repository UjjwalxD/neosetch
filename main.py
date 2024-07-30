import colorama
from colorama import Fore, Style
import asyncio

colorama.init()

async def neosetch():
    i = [
        f"{Fore.RED}{Style.BRIGHT}            '`\";i+-??+>;\"'                             ",
        f"{Fore.RED}{Style.BRIGHT}          ,????????????????!^                     ",
        f"{Fore.RED}{Style.BRIGHT}         '??????????????????,  .                                      {Fore.GREEN}{Style.BRIGHT}Ujjwwal@Windows11",
        f"{Fore.RED}{Style.BRIGHT}         ~?????????????????_.  Il,`..        ..'`^                {Fore.WHITE}{Style.BRIGHT}  ----------------------",
        f"{Fore.RED}{Style.BRIGHT}        \"??????????????????`  ^lllllll;:,,:;!llll.",
        f"{Fore.RED}{Style.BRIGHT}       .-?????????????????l  .llllllllllllllllll\" ",
        f"{Fore.RED}{Style.BRIGHT}       ,??????????????????.  \"llllllllllllllllll. ",
        f"{Fore.RED}{Style.BRIGHT}      .??????????????????:  .llllllllllllllllll^  ",
        f"{Fore.RED}{Style.BRIGHT}      ;?>:\"``''''`^,!???-.  ,lllllllllllllllllI   ",
        f"{Fore.RED}{Style.BRIGHT}      .               ',^  'llllllllllllllllll`   ",
        f"{Fore.GREEN}{Style.BRIGHT}     ..'``^^^^^^^^`'.      ;lllllllllllllllll;    ",
        f"{Fore.GREEN}{Style.BRIGHT}    .^^^^^^^^^^^^^^^^^`.    '^;lllllllllllI,`.    ",
        f"{Fore.GREEN}{Style.BRIGHT}    ^^^^^^^^^^^^^^^^^^`  .`.    .'````''.         ",
        f"{Fore.GREEN}{Style.BRIGHT}   '^^^^^^^^^^^^^^^^^^.  ^;;:^`..    ...'`\":.     ",
        f"{Fore.GREEN}{Style.BRIGHT}   ^^^^^^^^^^^^^^^^^^'  .;;;;;;;;;;;;;;;;;;`      ",
        f"{Fore.BLUE}{Style.BRIGHT}  `^^^^^^^^^^^^^^^^^^   \";;;;;;;;;;;;;;;;;;:       ",
        f"{Fore.BLUE}{Style.BRIGHT} .^^^^^^^^^^^^^^^^^^'  .;;;;;;;;;;;;;;;;;;'       ",
        f"{Fore.BLUE}{Style.BRIGHT} `^^^^^^^^^^^^^^^^^`   ,;;;;;;;;;;;;;;;;;,        ",
        f"{Fore.BLUE}{Style.BRIGHT}.^`'...     ..'`^^^.  `;;;;;;;;;;;;;;;;;;'        ",
        f"{Fore.YELLOW}{Style.BRIGHT}                 .'  .;;;;;;;;;;;;;;;;;;\"         ",
        f"{Fore.YELLOW}{Style.BRIGHT}                     ':;;;;;;;;;;;;;;;;:          ",
        f"{Fore.YELLOW}{Style.BRIGHT}                       .'^,:;;;;;:,\"`'.           "
    ]
    
    for line in i:
        print(line)
    print(Style.RESET_ALL)

async def main():
    await neosetch()

if __name__ == "__main__":
    asyncio.run(main())
