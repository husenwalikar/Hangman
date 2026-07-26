from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.theme import Theme

console = Console()
# custom_theme = Theme({
#     "good" : "green",
#     "bad": "bold red"
# })
# console.print("File corrupted!", style="bad")
# console.print("The internet is [bad]down![/bad]")
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

def display_board(hangman_art: str, current_word: str, attempts: int, guessed_letters: set):
    
    styled_hangman = f"[bold yellow]{hangman_art}[/]"
    left_panel = Panel(styled_hangman, title="Gallows")

    styled_word = f"[bold cyan]{' '.join(current_word)}[/]"
    styled_attempts = f"[bold red]Lives: {attempts}[/]"
    styled_guesses = f"Guessed: {', '.join(guessed_letters)}"
    right_stack = Group(
        styled_word,
        "",
        styled_attempts,
        styled_guesses
    )
    right_panel = Panel(right_stack, title="Status")

    dashboard = Columns([left_panel, right_panel])
    master_panel = Panel(dashboard, title="HANGMAN", border_style="bold magenta")
    console.print(master_panel)