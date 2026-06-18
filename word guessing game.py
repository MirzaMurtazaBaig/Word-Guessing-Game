import random
import tkinter as tk
from tkinter import messagebox, ttk

class WordGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("700x800")
        self.root.configure(bg="#2c3e50")
        
        # Game variables
        self.words = ["python", "programming", "hangman", "computer", "algorithm", 
                     "developer", "keyboard", "function", "variable", "syntax",
                     "javascript", "database", "network", "software", "hardware"]
        self.secret_word = ""
        self.guessed_letters = []
        self.attempts = 6
        self.max_attempts = 6
        self.word_display = []
        self.user_wins = 0
        self.computer_wins = 0
        self.game_active = False
        self.current_page = 1
        
        # Create all pages
        self.create_welcome_page()
        self.create_game_page()
        self.create_thanks_page()
        
        # Show welcome page first
        self.show_page(1)
    
    def create_welcome_page(self):
        """Create the welcome page"""
        self.welcome_frame = tk.Frame(self.root, bg="#2c3e50")
        
        # Title
        title_label = tk.Label(self.welcome_frame, text="🎯 WORD GUESSING GAME", 
                               font=("Helvetica", 36, "bold"), 
                               fg="#ecf0f1", bg="#2c3e50")
        title_label.pack(pady=50)
        
        # Subtitle
        subtitle_label = tk.Label(self.welcome_frame, text="Can you guess the word?", 
                                  font=("Helvetica", 18), 
                                  fg="#95a5a6", bg="#2c3e50")
        subtitle_label.pack(pady=10)
        
        # Decorative line
        line_frame = tk.Frame(self.welcome_frame, bg="#3498db", height=3)
        line_frame.pack(pady=30, padx=100, fill="x")
        
        # Game rules frame
        rules_frame = tk.Frame(self.welcome_frame, bg="#34495e", padx=30, pady=20)
        rules_frame.pack(pady=20, padx=50, fill="both")
        
        rules_title = tk.Label(rules_frame, text="📋 How to Play", 
                              font=("Helvetica", 16, "bold"), 
                              fg="#ecf0f1", bg="#34495e")
        rules_title.pack(pady=10)
        
        rules = [
            "🎯 Guess the hidden word one letter at a time",
            "💡 You have 6 wrong guesses allowed",
            "✅ Guess the whole word to win instantly",
            "🎮 Use the virtual keyboard or type your guess",
            "🏆 Track your wins against the computer"
        ]
        
        for rule in rules:
            rule_label = tk.Label(rules_frame, text=rule, 
                                 font=("Helvetica", 12), 
                                 fg="#bdc3c7", bg="#34495e", 
                                 anchor="w", justify="left")
            rule_label.pack(pady=5, anchor="w")
        
        # Start button
        start_button = tk.Button(self.welcome_frame, text="🚀 Start Game", 
                                font=("Helvetica", 16, "bold"), 
                                bg="#2ecc71", fg="white", 
                                padx=50, pady=15,
                                command=lambda: self.show_page(2))
        start_button.pack(pady=30)
        
        # Version info
        version_label = tk.Label(self.welcome_frame, text="Version 2.0", 
                                font=("Helvetica", 10), 
                                fg="#7f8c8d", bg="#2c3e50")
        version_label.pack(side="bottom", pady=10)
    
    def create_game_page(self):
        """Create the game page"""
        self.game_frame = tk.Frame(self.root, bg="#2c3e50")
        
        # Top bar with navigation
        top_bar = tk.Frame(self.game_frame, bg="#34495e", padx=20, pady=10)
        top_bar.pack(fill="x")
        
        # Back to Welcome button
        back_btn = tk.Button(top_bar, text="🏠 Welcome", 
                            font=("Helvetica", 10, "bold"), 
                            bg="#e67e22", fg="white", 
                            padx=15, pady=5,
                            command=lambda: self.show_page(1))
        back_btn.pack(side="left")
        
        # Page title
        page_title = tk.Label(top_bar, text="🎮 Game Page", 
                             font=("Helvetica", 14, "bold"), 
                             fg="#ecf0f1", bg="#34495e")
        page_title.pack(side="left", padx=20)
        
        # Score Frame
        self.score_frame = tk.Frame(self.game_frame, bg="#34495e", padx=20, pady=10)
        self.score_frame.pack(pady=10, fill="x", padx=20)
        
        self.score_label = tk.Label(self.score_frame, text="🏆 You: 0  |  💻 Computer: 0", 
                                    font=("Helvetica", 14), fg="#ecf0f1", bg="#34495e")
        self.score_label.pack()
        
        # Word Display Frame
        self.word_frame = tk.Frame(self.game_frame, bg="#34495e", padx=20, pady=30)
        self.word_frame.pack(pady=20, fill="x", padx=20)
        
        self.word_label = tk.Label(self.word_frame, text="Click 'New Game' to start!", 
                                   font=("Courier", 32, "bold"), 
                                   fg="#ecf0f1", bg="#34495e")
        self.word_label.pack()
        
        # Word Hint Frame
        self.hint_frame = tk.Frame(self.game_frame, bg="#2c3e50")
        self.hint_frame.pack(pady=5)
        
        self.hint_label = tk.Label(self.hint_frame, text="", 
                                   font=("Helvetica", 12), 
                                   fg="#95a5a6", bg="#2c3e50")
        self.hint_label.pack()
        
        # Attempts Frame
        self.attempts_frame = tk.Frame(self.game_frame, bg="#2c3e50")
        self.attempts_frame.pack(pady=10)
        
        self.attempts_label = tk.Label(self.attempts_frame, 
                                       text=f"❤️ Attempts: {self.attempts}/{self.max_attempts}", 
                                       font=("Helvetica", 14), 
                                       fg="#e74c3c", bg="#2c3e50")
        self.attempts_label.pack()
        
        # Progress Bar
        self.progress_frame = tk.Frame(self.game_frame, bg="#2c3e50")
        self.progress_frame.pack(pady=5, padx=50, fill="x")
        
        self.progress = ttk.Progressbar(self.progress_frame, length=500, 
                                        mode='determinate', maximum=self.max_attempts)
        self.progress.pack()
        self.progress['value'] = self.attempts
        
        # Guessed Letters Display
        self.guessed_frame = tk.Frame(self.game_frame, bg="#34495e", padx=20, pady=10)
        self.guessed_frame.pack(pady=10, fill="x", padx=20)
        
        self.guessed_label = tk.Label(self.guessed_frame, text="Guessed Letters: None", 
                                      font=("Helvetica", 12), 
                                      fg="#bdc3c7", bg="#34495e")
        self.guessed_label.pack()
        
        # Input Frame
        self.input_frame = tk.Frame(self.game_frame, bg="#2c3e50")
        self.input_frame.pack(pady=20)
        
        self.input_label = tk.Label(self.input_frame, text="Enter a letter or word:", 
                                    font=("Helvetica", 12), 
                                    fg="#ecf0f1", bg="#2c3e50")
        self.input_label.pack()
        
        self.input_entry = tk.Entry(self.input_frame, font=("Helvetica", 14), 
                                    width=25, justify='center')
        self.input_entry.pack(pady=10)
        self.input_entry.bind('<Return>', self.handle_guess)
        
        # Button Frame
        self.button_frame = tk.Frame(self.game_frame, bg="#2c3e50")
        self.button_frame.pack(pady=10)
        
        self.guess_button = tk.Button(self.button_frame, text="Guess", 
                                      font=("Helvetica", 12, "bold"), 
                                      bg="#3498db", fg="white", 
                                      padx=30, pady=10,
                                      command=self.handle_guess,
                                      state="disabled")
        self.guess_button.pack(side="left", padx=5)
        
        self.new_game_button = tk.Button(self.button_frame, text="🔄 New Game", 
                                         font=("Helvetica", 12, "bold"), 
                                         bg="#2ecc71", fg="white", 
                                         padx=30, pady=10,
                                         command=self.new_game)
        self.new_game_button.pack(side="left", padx=5)
        
        self.reset_button = tk.Button(self.button_frame, text="🔄 Reset Scores", 
                                      font=("Helvetica", 12, "bold"), 
                                      bg="#e67e22", fg="white", 
                                      padx=30, pady=10,
                                      command=self.reset_scores)
        self.reset_button.pack(side="left", padx=5)
        
        self.end_game_button = tk.Button(self.button_frame, text="🏁 End Game", 
                                         font=("Helvetica", 12, "bold"), 
                                         bg="#e74c3c", fg="white", 
                                         padx=30, pady=10,
                                         command=lambda: self.show_page(3))
        self.end_game_button.pack(side="left", padx=5)
        
        # Status Frame
        self.status_frame = tk.Frame(self.game_frame, bg="#34495e", padx=20, pady=10)
        self.status_frame.pack(pady=10, fill="x", padx=20)
        
        self.status_label = tk.Label(self.status_frame, text="Welcome! Click 'New Game' to start.", 
                                     font=("Helvetica", 11), 
                                     fg="#ecf0f1", bg="#34495e", wraplength=600)
        self.status_label.pack()
        
        # Keyboard Frame (Virtual Keyboard)
        self.keyboard_frame = tk.Frame(self.game_frame, bg="#2c3e50")
        self.keyboard_frame.pack(pady=10, padx=20)
        
        self.key_buttons = []
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for row in rows:
            row_frame = tk.Frame(self.keyboard_frame, bg="#2c3e50")
            row_frame.pack(pady=2)
            for letter in row:
                btn = tk.Button(row_frame, text=letter, width=4, height=1,
                               font=("Helvetica", 10, "bold"),
                               bg="#7f8c8d", fg="white",
                               relief="raised", bd=2,
                               command=lambda l=letter: self.keyboard_guess(l),
                               state="disabled")
                btn.pack(side="left", padx=2)
                self.key_buttons.append(btn)
    
    def create_thanks_page(self):
        """Create the thank you page"""
        self.thanks_frame = tk.Frame(self.root, bg="#2c3e50")
        
        # Main container
        main_container = tk.Frame(self.thanks_frame, bg="#2c3e50")
        main_container.pack(expand=True, fill="both")
        
        # Thank you message
        thanks_label = tk.Label(main_container, text="🙏 THANK YOU FOR PLAYING!", 
                               font=("Helvetica", 36, "bold"), 
                               fg="#ecf0f1", bg="#2c3e50")
        thanks_label.pack(pady=60)
        
        # Final Score Frame
        score_frame = tk.Frame(main_container, bg="#34495e", padx=40, pady=30)
        score_frame.pack(pady=30, padx=50, fill="x")
        
        final_score_title = tk.Label(score_frame, text="🏆 Final Score", 
                                    font=("Helvetica", 20, "bold"), 
                                    fg="#ecf0f1", bg="#34495e")
        final_score_title.pack(pady=10)
        
        self.final_score_label = tk.Label(score_frame, text="You: 0  |  Computer: 0", 
                                          font=("Helvetica", 24, "bold"), 
                                          fg="#f1c40f", bg="#34495e")
        self.final_score_label.pack(pady=20)
        
        # Result message
        self.result_label = tk.Label(score_frame, text="", 
                                     font=("Helvetica", 14), 
                                     fg="#2ecc71", bg="#34495e")
        self.result_label.pack(pady=10)
        
        # Statistics Frame
        stats_frame = tk.Frame(main_container, bg="#34495e", padx=40, pady=20)
        stats_frame.pack(pady=20, padx=50, fill="x")
        
        stats_title = tk.Label(stats_frame, text="📊 Game Statistics", 
                              font=("Helvetica", 16, "bold"), 
                              fg="#ecf0f1", bg="#34495e")
        stats_title.pack(pady=10)
        
        stats_text = "Thanks for playing our Word Guessing Game!\nWe hope you enjoyed it."
        stats_label = tk.Label(stats_frame, text=stats_text, 
                              font=("Helvetica", 12), 
                              fg="#bdc3c7", bg="#34495e", 
                              justify="center")
        stats_label.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(main_container, bg="#2c3e50")
        button_frame.pack(pady=40)
        
        play_again_btn = tk.Button(button_frame, text="🔄 Play Again", 
                                  font=("Helvetica", 14, "bold"), 
                                  bg="#2ecc71", fg="white", 
                                  padx=40, pady=15,
                                  command=lambda: self.show_page(1))
        play_again_btn.pack(side="left", padx=10)
        
        quit_btn = tk.Button(button_frame, text="🚪 Quit Game", 
                            font=("Helvetica", 14, "bold"), 
                            bg="#e74c3c", fg="white", 
                            padx=40, pady=15,
                            command=self.root.quit)
        quit_btn.pack(side="left", padx=10)
    
    def show_page(self, page_number):
        """Show the specified page"""
        self.current_page = page_number
        
        # Hide all pages
        self.welcome_frame.pack_forget()
        self.game_frame.pack_forget()
        self.thanks_frame.pack_forget()
        
        # Show the selected page
        if page_number == 1:
            self.welcome_frame.pack(expand=True, fill="both")
        elif page_number == 2:
            self.game_frame.pack(expand=True, fill="both")
            # Update final score if coming from thanks page
            self.update_score_display()
        elif page_number == 3:
            self.thanks_frame.pack(expand=True, fill="both")
            # Update final score display
            self.final_score_label.config(text=f"You: {self.user_wins}  |  Computer: {self.computer_wins}")
            
            # Determine winner message
            if self.user_wins > self.computer_wins:
                self.result_label.config(text="🎉 You are the CHAMPION! 🎉", fg="#2ecc71")
            elif self.computer_wins > self.user_wins:
                self.result_label.config(text="💻 Computer wins this time! Better luck next time!", fg="#e74c3c")
            else:
                self.result_label.config(text="🤝 It's a TIE! Great competition!", fg="#f1c40f")
    
    def keyboard_guess(self, letter):
        """Handle virtual keyboard button press"""
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, letter)
        self.handle_guess()
    
    def handle_guess(self, event=None):
        """Handle player's guess"""
        if not self.game_active:
            messagebox.showinfo("Game Over", "Please start a new game first!")
            return
        
        guess = self.input_entry.get().strip().lower()
        self.input_entry.delete(0, tk.END)
        
        if not guess:
            return
        
        # If user guesses the whole word
        if len(guess) > 1:
            if guess == self.secret_word:
                self.game_won()
            else:
                self.status_label.config(text=f"❌ '{guess}' is not the correct word!", fg="#e74c3c")
                self.attempts -= 1
                self.update_display()
                if self.attempts == 0:
                    self.game_lost()
            return
        
        # Single letter guess
        if len(guess) != 1 or not guess.isalpha():
            self.status_label.config(text="Please enter a single letter or the whole word!", fg="#f39c12")
            return
        
        # Check if letter already guessed
        if guess in self.guessed_letters:
            self.status_label.config(text=f"You already guessed '{guess}'!", fg="#f39c12")
            return
        
        self.guessed_letters.append(guess)
        
        # Disable keyboard button
        for btn in self.key_buttons:
            if btn['text'].lower() == guess:
                btn.config(state="disabled", bg="#95a5a6")
        
        # Check if letter is in the word
        if guess in self.secret_word:
            self.status_label.config(text=f"✅ Good guess! '{guess}' is in the word.", fg="#2ecc71")
            # Update display
            for i, letter in enumerate(self.secret_word):
                if letter == guess:
                    self.word_display[i] = guess
            self.update_word_display()
            
            # Check if word is complete
            if "_" not in self.word_display:
                self.game_won()
        else:
            self.status_label.config(text=f"❌ '{guess}' is not in the word.", fg="#e74c3c")
            self.attempts -= 1
            self.update_display()
            
            if self.attempts == 0:
                self.game_lost()
        
        self.update_guessed_display()
    
    def game_won(self):
        """Handle game win"""
        self.game_active = False
        self.user_wins += 1
        messagebox.showinfo("🎉 Congratulations!", 
                           f"You guessed the word '{self.secret_word}' correctly!")
        self.status_label.config(text=f"🎉 You won! The word was '{self.secret_word}'", fg="#2ecc71")
        self.update_score_display()
        self.guess_button.config(state="disabled")
        for btn in self.key_buttons:
            btn.config(state="disabled")
    
    def game_lost(self):
        """Handle game loss"""
        self.game_active = False
        self.computer_wins += 1
        messagebox.showinfo("💀 Game Over", f"The word was '{self.secret_word}'")
        self.status_label.config(text=f"💀 Game Over! The word was '{self.secret_word}'", fg="#e74c3c")
        # Reveal the word
        self.word_display = list(self.secret_word)
        self.update_word_display()
        self.update_score_display()
        self.guess_button.config(state="disabled")
        for btn in self.key_buttons:
            btn.config(state="disabled")
    
    def new_game(self):
        """Start a new game"""
        self.secret_word = random.choice(self.words)
        self.guessed_letters = []
        self.attempts = self.max_attempts
        self.word_display = ["_"] * len(self.secret_word)
        self.game_active = True
        
        # Reset display
        self.update_word_display()
        self.update_guessed_display()
        self.update_display()
        self.status_label.config(text=f"New game started! The word has {len(self.secret_word)} letters.", 
                                fg="#3498db")
        
        # Enable guess button and virtual keyboard
        self.guess_button.config(state="normal")
        for btn in self.key_buttons:
            btn.config(state="normal", bg="#7f8c8d")
        
        self.input_entry.focus()
    
    def update_word_display(self):
        """Update the word display"""
        display_text = " ".join(self.word_display)
        self.word_label.config(text=display_text)
        
        # Show hint with number of letters
        self.hint_label.config(text=f"📝 {len(self.secret_word)} letters")
    
    def update_guessed_display(self):
        """Update guessed letters display"""
        if self.guessed_letters:
            text = "Guessed Letters: " + ", ".join(sorted(self.guessed_letters))
        else:
            text = "Guessed Letters: None"
        self.guessed_label.config(text=text)
    
    def update_display(self):
        """Update attempts display and progress bar"""
        self.attempts_label.config(text=f"❤️ Attempts: {self.attempts}/{self.max_attempts}")
        self.progress['value'] = self.attempts
        self.progress['maximum'] = self.max_attempts
        
        # Change progress bar color based on attempts
        if self.attempts <= 2:
            self.progress['style'] = 'red.Horizontal.TProgressbar'
        elif self.attempts <= 4:
            self.progress['style'] = 'yellow.Horizontal.TProgressbar'
        else:
            self.progress['style'] = 'green.Horizontal.TProgressbar'
    
    def update_score_display(self):
        """Update the score display"""
        self.score_label.config(text=f"🏆 You: {self.user_wins}  |  💻 Computer: {self.computer_wins}")
    
    def reset_scores(self):
        """Reset the scores"""
        self.user_wins = 0
        self.computer_wins = 0
        self.update_score_display()
        self.status_label.config(text="Scores have been reset!", fg="#f39c12")
        messagebox.showinfo("Reset", "Scores have been reset to 0!")

def main():
    root = tk.Tk()
    
    # Set up custom styles for progress bar
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('green.Horizontal.TProgressbar', background='#2ecc71')
    style.configure('yellow.Horizontal.TProgressbar', background='#f1c40f')
    style.configure('red.Horizontal.TProgressbar', background='#e74c3c')
    
    game = WordGuessingGame(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()