from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.theme import Theme

game_theme = Theme({
    "primary":      "bold #4ade80",
    "secondary":    "bold #c084fc",

    "gallows":      "bold #facc15",
    "word":         "bold #67e8f9",
    "muted":        "bold #bd92eb",
    "separator":    "#374151",

    "lives.ok":     "bold #4ade80",   
    "lives.mid":    "bold #fb923c",
    "lives.low":    "bold #f87171",

    "success":      "bold #4ade80",
    "danger":       "bold #f87171",
    "warning":      "bold #fb923c",
    "info":         "#67e8f9",

    "prompt":       "bold #c084fc",
    "label":        "bold #e5e7eb", 
    "value":        "italic #a78bfa",
})

console = Console(theme=game_theme, color_system="truecolor")
DIFFICULTIES = {10: "easy", 8: "medium", 5: "hard"}

gallow_stages: list[str] = [
    # Stage 0: Empty Gallows (0 mistakes)
    r"""   +-----------+            
   |/                       
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 1: The Rope (1 mistake)
    r"""   +-----------+            
   |/          |            
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 2: Head Outline (2 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        /     \         
   |        \     /         
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 3: Face (3 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 4: Torso & Belt (4 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |       ./'---'\.        
   |         \ . /          
   |         | . |          
   |         |===|          
   |          \_/           
   |                        
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 5: Left Arm Tied (5 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |       ./'---'\.        
   |     /`/ \ . /          
   |    ; | >| . |          
   |    | |  |===|          
   |    |-|_/ \_/           
   |     \_|                
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 6: Right Arm Tied (6 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |       ./'---'\.        
   |     /`/ \ . / \`\      
   |    ; | >| . |< | ;     
   |    | |  |===|  | |     
   |    |-|_/ \_/ \_|-|     
   |     \_|       |_/      
   |                        
   |                        
   |                        
   |                        
   =========================""",

    # Stage 7: Left Leg (7 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |       ./'---'\.        
   |     /`/ \ . / \`\      
   |    ; | >| . |< | ;     
   |    | |  |===|  | |     
   |    |-|_/ \_/ \_|-|     
   |     \_|___|   |_/      
   |       |   |            
   |       |___|            
   |                        
   |                        
   =========================""",

    # Stage 8: Right Leg (8 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |       ./'---'\.        
   |     /`/ \ . / \`\      
   |    ; | >| . |< | ;     
   |    | |  |===|  | |     
   |    |-|_/ \_/ \_|-|     
   |     \_|___|___|_/      
   |       |   |   |        
   |       |___|___|        
   |                        
   |                        
   =========================""",

    # Stage 9: Left Boot (9 mistakes)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / o o \         
   |        \  =  /         
   |       ./'---'\.        
   |     /`/ \ . / \`\      
   |    ; | >| . |< | ;     
   |    | |  |===|  | |     
   |    |-|_/ \_/ \_|-|     
   |     \_|___|___|_/      
   |       |   |   |        
   |       |___|___|        
   |       / /              
   |      (__/              
   =========================""",

    # Stage 10: Right Boot & Dead Face (10 mistakes - Game Over!)
    r"""   +-----------+            
   |/          |            
   |         .---.          
   |        / x x \         
   |        \ -U- /         
   |       ./'---'\.        
   |     /`/ \ . / \`\      
   |    ; | >| . |< | ;     
   |    | |  |===|  | |     
   |    |-|_/ \_/ \_|-|     
   |     \_|___|___|_/      
   |       |   |   |        
   |       |___|___|        
   |       / /   \ \        
   |      (__/   \__)       
   ========================="""
]

def display_board(  hangman_art: str,
                    current_word: str,
                    attempts: int,
                    guessed_letters: set,
                    max_attempts: int,
                    category: str,
                    difficulty: int,
                    message: str = ""     
                  ):
    
    styled_hangman = f"[gallows]{hangman_art}[/]"
    left_panel = Panel(Align.center(styled_hangman, vertical="middle"), border_style="secondary", title="Gallows")

    if attempts > 6:
      life_color = "lives.ok"
    elif attempts > 3:
      life_color = "lives.mid"
    else:
      life_color = "lives.low"
        
    styled_word = f"[word]{' '.join(current_word)}[/]"
    hearts = f"[danger]{'♥ ' * attempts}[/][dim]{'♡ ' * (max_attempts - attempts)}[/dim]"
    styled_attempts = f"[{life_color}]Lives: {attempts}/{max_attempts}[/]  {hearts}"
    styled_guesses = f"[success]Guessed: {', '.join(sorted(guessed_letters))}[/]"
    separator = f"[separator]{'─' * 30}[/]"
    styled_category = f"[label]Category  :[/]  [value]{category}[/]"
    styled_difficulty = f"[label]Difficulty:[/]  [value]{DIFFICULTIES[difficulty]}[/]"
    right_stack = Group(
        styled_category,
        styled_difficulty,
        "",
        separator,
        "",
        styled_word,
        "",
        separator,
        "",
        styled_attempts,
        "",
        styled_guesses
    )
    right_panel = Panel(Align.center(right_stack, vertical="middle"), border_style="secondary", title="Status", padding=(2, 4), width=45)

    dashboard = Table.grid(padding=(0, 2))
    dashboard.add_row(left_panel, right_panel)

    if message:
       alert = Panel(f"[danger] ⚠  {message}[/]", border_style="danger", expand=False)
       final_layout = Group(dashboard, alert)
    else:
       final_layout = dashboard
    master_panel = Panel(final_layout, title="[primary]☠  H A N G M A N ☠[/]  ", style="on #15131B", border_style="primary", box=box.DOUBLE, expand=False)
    console.print(Align.center(master_panel))

def display_welcome():
    banner = r"""
[gallows]
 _   _                                                
| | | |  __ _  _ __    __ _  _ __ ___    __ _  _ __   
| |_| | / _` || '_ \  / _` || '_ ` _ \  / _` || '_ \  
|  _  || (_| || | | || (_| || | | | | || (_| || | | | 
|_| |_| \__,_||_| |_| \__, ||_| |_| |_| \__,_||_| |_| 
                      |___/    
[/]
[info]How to play!:[/]
  · Guess the WORD from chosen category (one letter at time).
  · Type [success]easy[/] / [warning]medium[/] / [danger]hard[/] for difficulty level. 
  · Type [gallows]?[/] for a hint (costs 1 life).
  · Hints are [danger]disabled[/] on hard mode.
"""
    welcome_panel = Panel(Align.center(banner), style="on #15131B", border_style="secondary")
    console.print(welcome_panel)
    console.print()