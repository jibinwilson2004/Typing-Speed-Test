import tkinter as tk
from tkinter import ttk, messagebox
import time
import random
import string

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("⚡ Typing Speed Test ⚡")
        self.root.geometry("1200x800")
        self.root.configure(bg="#1a1a2e")
        
        # Variables
        self.start_time = None
        self.test_active = False
        self.current_text = ""
        self.user_input = ""
        self.correct_chars = 0
        self.total_chars = 0
        self.words_typed = 0
        
        # Timer
        self.duration_seconds = 60
        self.remaining_seconds = self.duration_seconds
        self._timer_job = None
        
        # Word pool for random text generation
        self.word_pool = (
            "time code logic array cloud neural input output random quick brown fox "
            "data stream packet server client device python java kernel script debug "
            "silver ocean galaxy pixel canvas render engine memory storage thread queue "
            "network signal latency jitter upload download monitor secure token cipher "
            "design system module pattern object method class function variable state "
            "energy future bright green cyan magenta violet amber coral azure midnight "
            "keyboard display window focus cursor click tap drag drop type select copy "
            "optimize compile build deploy develop test release agile sprint feature bug"
        ).split()
        
        self.setup_ui()
        self.load_new_text()
        
    def setup_ui(self):
        # Main container with gradient background effect
        main_frame = tk.Frame(self.root, bg="#1a1a2e")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Title with colorful styling
        title_frame = tk.Frame(main_frame, bg="#1a1a2e")
        title_frame.pack(pady=(0, 20))
        
        title_label = tk.Label(
            title_frame,
            text="⚡ TYPING SPEED TEST ⚡",
            font=("Arial", 32, "bold"),
            bg="#1a1a2e",
            fg="#00ff88"
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Test your typing speed and accuracy",
            font=("Arial", 14),
            bg="#1a1a2e",
            fg="#8888ff"
        )
        subtitle_label.pack(pady=(5, 0))
        
        # Statistics frame with colorful cards
        stats_frame = tk.Frame(main_frame, bg="#1a1a2e")
        stats_frame.pack(pady=20, fill=tk.X)
        
        # WPM Card
        wpm_card, self.wpm_label = self.create_stat_card(stats_frame, "WPM", "0", "#ff6b6b")
        wpm_card.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
        
        # CPM Card
        cpm_card, self.cpm_label = self.create_stat_card(stats_frame, "CPM", "0", "#4ecdc4")
        cpm_card.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
        
        # Accuracy Card
        accuracy_card, self.accuracy_label = self.create_stat_card(stats_frame, "Accuracy", "0%", "#ffe66d")
        accuracy_card.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
        
        # Time Card (shows remaining seconds)
        time_card, self.time_label = self.create_stat_card(stats_frame, "Time Left", f"{self.duration_seconds}s", "#a8e6cf")
        time_card.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
        
        # Text display frame
        text_frame = tk.Frame(main_frame, bg="#16213e", relief=tk.RAISED, bd=3)
        text_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Text to type label
        text_label_header = tk.Label(
            text_frame,
            text="Text to Type:",
            font=("Arial", 12, "bold"),
            bg="#16213e",
            fg="#ffd93d"
        )
        text_label_header.pack(anchor=tk.W, padx=15, pady=(15, 5))
        
        # Text display area with scrollbar
        text_container = tk.Frame(text_frame, bg="#16213e")
        text_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))
        
        self.text_display = tk.Text(
            text_container,
            wrap=tk.WORD,
            font=("Courier New", 16),
            bg="#0f3460",
            fg="#eaeaea",
            padx=15,
            pady=15,
            relief=tk.FLAT,
            borderwidth=0,
            selectbackground="#4a90e2",
            height=8
        )
        self.text_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(text_container, command=self.text_display.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_display.config(yscrollcommand=scrollbar.set)
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg="#16213e", relief=tk.RAISED, bd=3)
        input_frame.pack(pady=20, fill=tk.X)
        
        input_label_header = tk.Label(
            input_frame,
            text="Start Typing:",
            font=("Arial", 12, "bold"),
            bg="#16213e",
            fg="#ff6b9d"
        )
        input_label_header.pack(anchor=tk.W, padx=15, pady=(15, 5))
        
        self.input_field = tk.Text(
            input_frame,
            wrap=tk.WORD,
            font=("Courier New", 16),
            bg="#0f3460",
            fg="#ffffff",
            padx=15,
            pady=15,
            relief=tk.FLAT,
            borderwidth=0,
            insertbackground="#ff6b9d",
            height=4
        )
        self.input_field.pack(fill=tk.X, padx=15, pady=(0, 15))
        self.input_field.bind('<KeyPress>', self.on_key_press)
        self.input_field.bind('<KeyRelease>', self.on_key_release)
        self.input_field.bind('<Button-1>', self.on_click)
        
        # Control buttons frame
        button_frame = tk.Frame(main_frame, bg="#1a1a2e")
        button_frame.pack(pady=20)
        
        self.start_button = tk.Button(
            button_frame,
            text="🔄 New Text",
            font=("Arial", 14, "bold"),
            bg="#00d4ff",
            fg="#000000",
            activebackground="#00b8e6",
            activeforeground="#000000",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.load_new_text
        )
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(
            button_frame,
            text="⏹️ Reset",
            font=("Arial", 14, "bold"),
            bg="#ff6b6b",
            fg="#ffffff",
            activebackground="#ff5252",
            activeforeground="#ffffff",
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=10,
            cursor="hand2",
            command=self.reset_test
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        # Progress frame
        progress_frame = tk.Frame(main_frame, bg="#1a1a2e")
        progress_frame.pack(pady=10, fill=tk.X, padx=20)
        
        progress_label = tk.Label(
            progress_frame,
            text="Progress:",
            font=("Arial", 11, "bold"),
            bg="#1a1a2e",
            fg="#8888ff"
        )
        progress_label.pack(side=tk.LEFT, padx=(0, 10))
        
        self.progress_bar = tk.Canvas(
            progress_frame,
            height=25,
            bg="#0f3460",
            highlightthickness=0,
            relief=tk.FLAT
        )
        self.progress_bar.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.progress_text = tk.Label(
            progress_frame,
            text="0%",
            font=("Arial", 11, "bold"),
            bg="#1a1a2e",
            fg="#00ff88",
            width=5
        )
        self.progress_text.pack(side=tk.LEFT, padx=(10, 0))
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Ready to start typing!",
            font=("Arial", 12, "italic"),
            bg="#1a1a2e",
            fg="#8888ff"
        )
        self.status_label.pack(pady=10)
        
        # Initialize text display
        self.update_text_display()
        
    def create_stat_card(self, parent, title, value, color):
        """Create a colorful statistics card"""
        card = tk.Frame(parent, bg=color, relief=tk.RAISED, bd=2)
        
        title_label = tk.Label(
            card,
            text=title,
            font=("Arial", 11, "bold"),
            bg=color,
            fg="#ffffff"
        )
        title_label.pack(pady=(10, 5))
        
        value_label = tk.Label(
            card,
            text=value,
            font=("Arial", 24, "bold"),
            bg=color,
            fg="#ffffff",
            name="label2"
        )
        value_label.pack(pady=(0, 10))
        
        return card, value_label

    def generate_random_text(self, min_words: int = 80, max_words: int = 120) -> str:
        """Generate a random passage with basic punctuation and capitalization."""
        num_words = random.randint(min_words, max_words)
        words = [random.choice(self.word_pool) for _ in range(num_words)]
        sentences = []
        i = 0
        while i < len(words):
            sentence_len = random.randint(8, 16)
            chunk = words[i:i + sentence_len]
            if not chunk:
                break
            chunk[0] = chunk[0].capitalize()
            end_punct = random.choices(['.', '!', '?'], weights=[0.7, 0.2, 0.1])[0]
            sentences.append(" ".join(chunk) + end_punct)
            i += sentence_len
        return " ".join(sentences)
    
    def load_new_text(self):
        """Load a new random text for typing"""
        self.cancel_timer()
        self.current_text = self.generate_random_text()
        self.test_active = False
        self.start_time = None
        self.user_input = ""
        self.correct_chars = 0
        self.total_chars = 0
        self.words_typed = 0
        self.remaining_seconds = self.duration_seconds
        
        self.input_field.delete(1.0, tk.END)
        self.input_field.config(state=tk.NORMAL)
        self.input_field.focus()
        
        self.update_text_display()
        self.update_progress()
        self.update_stats()
        self.update_time_card()
        self.status_label.config(text="Ready to start typing! Press any key to begin.", fg="#8888ff")
        
    def reset_test(self):
        """Reset the current test"""
        self.load_new_text()
        
    def update_text_display(self):
        """Update the text display with color coding"""
        self.text_display.delete(1.0, tk.END)
        
        # Insert the full text
        self.text_display.insert(1.0, self.current_text)
        
        # Configure color tags
        self.text_display.tag_config("correct", foreground="#00ff88", background="#0f3460", 
                                     font=("Courier New", 16, "bold"))
        self.text_display.tag_config("incorrect", foreground="#ff6b6b", background="#3d1a1a", 
                                     font=("Courier New", 16, "bold"))
        self.text_display.tag_config("normal", foreground="#888888", background="#0f3460")
        self.text_display.tag_config("cursor", background="#ff6b9d", foreground="#ffffff")
        
        # Apply tags based on user input
        pos = 1.0
        for i, char in enumerate(self.current_text):
            char_start = pos
            char_end = f"{pos}+1c"
            
            if i < len(self.user_input):
                if char == self.user_input[i]:
                    # Correct character - green
                    self.text_display.tag_add("correct", char_start, char_end)
                else:
                    # Incorrect character - red
                    self.text_display.tag_add("incorrect", char_start, char_end)
            else:
                if i == len(self.user_input):
                    # Current position - cursor indicator
                    self.text_display.tag_add("cursor", char_start, char_end)
                else:
                    # Not typed yet - gray
                    self.text_display.tag_add("normal", char_start, char_end)
            
            # Move to next character
            pos = f"{pos}+1c"
    
    def on_key_press(self, event):
        """Handle key press events"""
        if event.keysym in ['BackSpace', 'Delete', 'Return', 'Tab']:
            return
        
        # Start the test on first key press
        if not self.test_active and self.start_time is None:
            self.start_time = time.time()
            self.test_active = True
            self.status_label.config(text="⚡ Typing in progress...", fg="#00ff88")
            self.start_timer()
        
        # Schedule update after a short delay
        self.root.after(10, self.update_after_input)
    
    def on_key_release(self, event):
        """Handle key release events"""
        if event.keysym in ['BackSpace', 'Delete']:
            self.root.after(10, self.update_after_input)
    
    def on_click(self, event):
        """Handle click events"""
        # Prevent clicking in the middle of text
        content = self.input_field.get(1.0, tk.END).strip()
        cursor_pos = self.input_field.index(tk.INSERT)
        line, col = map(int, cursor_pos.split('.'))
        
        # Move cursor to end if clicked elsewhere
        if line > len(content.split('\n')) or (line == len(content.split('\n')) and col > len(content.split('\n')[-1])):
            self.input_field.mark_set(tk.INSERT, tk.END)
    
    def update_after_input(self):
        """Update after user input"""
        # Get current input (remove trailing newline from Text widget)
        self.user_input = self.input_field.get(1.0, tk.END).rstrip('\n')
        
        # Calculate accuracy - character by character comparison
        self.correct_chars = 0
        self.total_chars = len(self.user_input)
        
        # Compare each character with the original text
        for i, char in enumerate(self.user_input):
            if i < len(self.current_text) and char == self.current_text[i]:
                self.correct_chars += 1
        
        # Count words (only count complete words)
        if self.user_input:
            # Count words up to the current position
            typed_text = self.user_input[:min(len(self.user_input), len(self.current_text))]
            self.words_typed = len([w for w in typed_text.split() if w])
        
        # Update display
        self.update_text_display()
        self.update_progress()
        self.update_stats()
        
        # Check if test is complete
        if self.user_input == self.current_text:
            self.complete_test()
    
    def update_progress(self):
        """Update progress bar"""
        if not self.current_text:
            return
        
        progress = min(len(self.user_input) / len(self.current_text) * 100, 100)
        progress = max(0, progress)
        
        # Update progress bar
        self.progress_bar.delete("all")
        width = self.progress_bar.winfo_width()
        if width > 1:
            fill_width = int(width * progress / 100)
            # Create gradient effect with rectangles
            segments = 20
            segment_width = fill_width / segments
            for i in range(segments):
                if i * segment_width >= fill_width:
                    break
                segment_start = int(i * segment_width)
                segment_end = int(min((i + 1) * segment_width, fill_width))
                ratio = i / segments
                # Gradient from cyan (#00d4ff) to green (#00ff88)
                r = int(0 + (0 * ratio))
                g = int(212 + (255 * ratio))
                b = int(255 + (136 * ratio))
                color = f"#{r:02x}{g:02x}{b:02x}"
                self.progress_bar.create_rectangle(segment_start, 0, segment_end, 25, 
                                                   fill=color, outline=color)
        
        self.progress_text.config(text=f"{int(progress)}%")
    
    def update_stats(self):
        """Update statistics display"""
        if self.start_time is None:
            self.wpm_label.config(text="0")
            self.cpm_label.config(text="0")
            self.accuracy_label.config(text="0%")
            self.update_time_card()
            return
        
        elapsed_time = time.time() - self.start_time
        
        if elapsed_time > 0:
            # Calculate WPM (words per minute)
            # Standard: 5 characters = 1 word
            words = self.correct_chars / 5.0
            wpm = int((words / elapsed_time) * 60)
            
            # Calculate CPM (characters per minute)
            cpm = int((self.correct_chars / elapsed_time) * 60)
            
            # Calculate Accuracy
            if self.total_chars > 0:
                accuracy = int((self.correct_chars / self.total_chars) * 100)
            else:
                accuracy = 0
            
            # Update labels
            self.wpm_label.config(text=str(wpm))
            self.cpm_label.config(text=str(cpm))
            self.accuracy_label.config(text=f"{accuracy}%")
            self.update_time_card()
            
            # Schedule next update
            if self.test_active:
                self.root.after(100, self.update_stats)
    
    def complete_test(self, time_up: bool = False):
        """Handle test completion"""
        self.test_active = False
        self.cancel_timer()
        elapsed_time = (time.time() - self.start_time) if self.start_time else 0
        
        # Final calculations
        words = self.correct_chars / 5.0
        wpm = int((words / elapsed_time) * 60)
        cpm = int((self.correct_chars / elapsed_time) * 60)
        accuracy = int((self.correct_chars / self.total_chars) * 100) if self.total_chars > 0 else 0
        
        # Disable input
        self.input_field.config(state=tk.DISABLED)
        
        # Choose color & title
        if wpm >= 60:
            title = "Excellent!"
            color = "#00ff88"
        elif wpm >= 40:
            title = "Great Job!"
            color = "#4ecdc4"
        elif wpm >= 20:
            title = "Keep Practicing"
            color = "#ffe66d"
        else:
            title = "Don't Give Up"
            color = "#ff6b6b"
        
        self.status_label.config(text=("⏰ Time's up! " if time_up else "✅ Completed! ") + f"WPM {wpm}, Accuracy {accuracy}%", fg=color)
        
        # Styled results window
        result = tk.Toplevel(self.root)
        result.title("Your Results")
        result.configure(bg="#0f1b2b")
        result.geometry("520x320")
        result.resizable(False, False)
        
        header = tk.Label(result, text=title, font=("Arial", 22, "bold"), fg=color, bg="#0f1b2b")
        header.pack(pady=(20, 10))
        
        sub = tk.Label(result, text=("Time limit reached" if time_up else "Text completed"), font=("Arial", 12), fg="#9bb3c8", bg="#0f1b2b")
        sub.pack(pady=(0, 10))
        
        card = tk.Frame(result, bg="#16213e", relief=tk.RAISED, bd=2)
        card.pack(padx=20, pady=10, fill=tk.X)
        
        def metric_row(parent, label, value, accent):
            row = tk.Frame(parent, bg="#16213e")
            row.pack(fill=tk.X, padx=16, pady=6)
            tk.Label(row, text=label, font=("Arial", 12, "bold"), fg=accent, bg="#16213e").pack(side=tk.LEFT)
            tk.Label(row, text=value, font=("Courier New", 16, "bold"), fg="#eaeaea", bg="#16213e").pack(side=tk.RIGHT)
        
        metric_row(card, "WPM", str(wpm), "#00d4ff")
        metric_row(card, "CPM", str(cpm), "#00ff88")
        metric_row(card, "Accuracy", f"{accuracy}%", "#ffe66d")
        metric_row(card, "Time", f"{int(elapsed_time)}s", "#cfa9ff")
        
        btns = tk.Frame(result, bg="#0f1b2b")
        btns.pack(pady=16)
        
        def close_and_new():
            result.destroy()
            self.reset_test()
        
        tk.Button(btns, text="🔁 New Test", command=close_and_new, bg="#00d4ff", fg="#000", font=("Arial", 12, "bold"), bd=0, padx=16, pady=8, activebackground="#00b8e6").pack(side=tk.LEFT, padx=8)
        tk.Button(btns, text="✖ Close", command=result.destroy, bg="#223047", fg="#eaeaea", font=("Arial", 12, "bold"), bd=0, padx=16, pady=8, activebackground="#2d405f").pack(side=tk.LEFT, padx=8)

    def update_time_card(self):
        """Refresh the time card to show remaining seconds."""
        self.time_label.config(text=f"{int(max(self.remaining_seconds, 0))}s")

    def start_timer(self):
        """Start countdown timer."""
        self.cancel_timer()
        self.remaining_seconds = self.duration_seconds if self.remaining_seconds is None else self.remaining_seconds
        self._tick()

    def _tick(self):
        if not self.test_active:
            return
        self.remaining_seconds -= 1
        self.update_time_card()
        if self.remaining_seconds <= 0:
            self.complete_test(time_up=True)
            return
        self._timer_job = self.root.after(1000, self._tick)

    def cancel_timer(self):
        """Cancel an active timer if any."""
        if self._timer_job is not None:
            try:
                self.root.after_cancel(self._timer_job)
            except Exception:
                pass
            self._timer_job = None

def main():
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
