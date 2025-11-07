// Word pool for random text generation
const wordPool = [
    "time", "code", "logic", "array", "cloud", "neural", "input", "output", "random",
    "quick", "brown", "fox", "data", "stream", "packet", "server", "client", "device",
    "python", "java", "kernel", "script", "debug", "silver", "ocean", "galaxy", "pixel",
    "canvas", "render", "engine", "memory", "storage", "thread", "queue", "network",
    "signal", "latency", "jitter", "upload", "download", "monitor", "secure", "token",
    "cipher", "design", "system", "module", "pattern", "object", "method", "class",
    "function", "variable", "state", "energy", "future", "bright", "green", "cyan",
    "magenta", "violet", "amber", "coral", "azure", "midnight", "keyboard", "display",
    "window", "focus", "cursor", "click", "tap", "drag", "drop", "type", "select",
    "copy", "optimize", "compile", "build", "deploy", "develop", "test", "release",
    "agile", "sprint", "feature", "bug", "fix", "update", "version", "control",
    "repository", "commit", "merge", "branch", "pull", "push", "clone", "fork"
];

class TypingSpeedTest {
    constructor() {
        this.startTime = null;
        this.testActive = false;
        this.currentText = "";
        this.userInput = "";
        this.correctChars = 0;
        this.totalChars = 0;
        this.durationSeconds = 60;
        this.remainingSeconds = this.durationSeconds;
        this.timerInterval = null;
        this.statsInterval = null;
        
        this.initializeElements();
        this.attachEventListeners();
        this.loadNewText();
    }
    
    initializeElements() {
        this.wpmEl = document.getElementById('wpm');
        this.cpmEl = document.getElementById('cpm');
        this.accuracyEl = document.getElementById('accuracy');
        this.timeLeftEl = document.getElementById('timeLeft');
        this.progressFill = document.getElementById('progressFill');
        this.progressText = document.getElementById('progressText');
        this.textDisplay = document.getElementById('textDisplay');
        this.inputField = document.getElementById('inputField');
        this.statusMessage = document.getElementById('statusMessage');
        this.newTextBtn = document.getElementById('newTextBtn');
        this.resetBtn = document.getElementById('resetBtn');
        this.resultsModal = document.getElementById('resultsModal');
        this.modalTitle = document.getElementById('modalTitle');
        this.modalSubtitle = document.getElementById('modalSubtitle');
        this.resultWPM = document.getElementById('resultWPM');
        this.resultCPM = document.getElementById('resultCPM');
        this.resultAccuracy = document.getElementById('resultAccuracy');
        this.resultTime = document.getElementById('resultTime');
        this.modalNewBtn = document.getElementById('modalNewBtn');
        this.modalCloseBtn = document.getElementById('modalCloseBtn');
    }
    
    attachEventListeners() {
        this.inputField.addEventListener('input', () => this.onInput());
        this.inputField.addEventListener('keydown', (e) => this.onKeyDown(e));
        this.newTextBtn.addEventListener('click', () => this.loadNewText());
        this.resetBtn.addEventListener('click', () => this.loadNewText());
        this.modalNewBtn.addEventListener('click', () => {
            this.closeModal();
            this.loadNewText();
        });
        this.modalCloseBtn.addEventListener('click', () => this.closeModal());
        
        // Close modal on outside click
        this.resultsModal.addEventListener('click', (e) => {
            if (e.target === this.resultsModal) {
                this.closeModal();
            }
        });
    }
    
    generateRandomText(minWords = 80, maxWords = 120) {
        const numWords = Math.floor(Math.random() * (maxWords - minWords + 1)) + minWords;
        const words = [];
        
        for (let i = 0; i < numWords; i++) {
            words.push(wordPool[Math.floor(Math.random() * wordPool.length)]);
        }
        
        // Create sentences with proper capitalization and punctuation
        const sentences = [];
        let i = 0;
        
        while (i < words.length) {
            const sentenceLength = Math.floor(Math.random() * (16 - 8 + 1)) + 8;
            const chunk = words.slice(i, i + sentenceLength);
            
            if (chunk.length === 0) break;
            
            // Capitalize first word
            chunk[0] = chunk[0].charAt(0).toUpperCase() + chunk[0].slice(1);
            
            // Add punctuation
            const punctuation = Math.random() < 0.7 ? '.' : (Math.random() < 0.9 ? '!' : '?');
            sentences.push(chunk.join(' ') + punctuation);
            
            i += sentenceLength;
        }
        
        return sentences.join(' ');
    }
    
    loadNewText() {
        this.cancelTimers();
        this.currentText = this.generateRandomText();
        this.testActive = false;
        this.startTime = null;
        this.userInput = "";
        this.correctChars = 0;
        this.totalChars = 0;
        this.remainingSeconds = this.durationSeconds;
        
        this.inputField.value = "";
        this.inputField.disabled = false;
        this.inputField.focus();
        
        this.updateTextDisplay();
        this.updateProgress();
        this.updateStats();
        this.updateTimeDisplay();
        this.updateStatusMessage("Ready to start typing! Press any key to begin.", "normal");
    }
    
    onKeyDown(e) {
        // Prevent default for Tab to avoid losing focus
        if (e.key === 'Tab') {
            e.preventDefault();
        }
        
        // Start test on first key press
        if (!this.testActive && this.startTime === null && e.key.length === 1) {
            this.startTest();
        }
    }
    
    startTest() {
        this.startTime = Date.now();
        this.testActive = true;
        this.updateStatusMessage("⚡ Typing in progress...", "active");
        this.startTimer();
        this.startStatsUpdate();
    }
    
    onInput() {
        this.userInput = this.inputField.value;
        this.updateTextDisplay();
        this.updateProgress();
        this.calculateAccuracy();
        
        // Check if text is complete
        if (this.userInput === this.currentText) {
            this.completeTest(false);
        }
    }
    
    updateTextDisplay() {
        const display = this.textDisplay;
        display.innerHTML = '';
        
        for (let i = 0; i < this.currentText.length; i++) {
            const span = document.createElement('span');
            const char = this.currentText[i];
            
            if (i < this.userInput.length) {
                if (char === this.userInput[i]) {
                    span.className = 'char-correct';
                    span.textContent = char;
                } else {
                    span.className = 'char-incorrect';
                    span.textContent = char;
                }
            } else if (i === this.userInput.length) {
                span.className = 'char-current';
                span.textContent = char;
            } else {
                span.className = 'char-normal';
                span.textContent = char;
            }
            
            display.appendChild(span);
        }
    }
    
    calculateAccuracy() {
        this.correctChars = 0;
        this.totalChars = this.userInput.length;
        
        for (let i = 0; i < this.userInput.length; i++) {
            if (i < this.currentText.length && this.userInput[i] === this.currentText[i]) {
                this.correctChars++;
            }
        }
    }
    
    updateProgress() {
        if (!this.currentText) return;
        
        const progress = Math.min((this.userInput.length / this.currentText.length) * 100, 100);
        this.progressFill.style.width = `${progress}%`;
        this.progressText.textContent = `${Math.round(progress)}%`;
    }
    
    updateStats() {
        if (this.startTime === null) {
            this.wpmEl.textContent = '0';
            this.cpmEl.textContent = '0';
            this.accuracyEl.textContent = '0%';
            return;
        }
        
        const elapsedTime = (Date.now() - this.startTime) / 1000; // in seconds
        
        if (elapsedTime > 0) {
            // Calculate WPM (5 characters = 1 word)
            const words = this.correctChars / 5.0;
            const wpm = Math.round((words / elapsedTime) * 60);
            
            // Calculate CPM
            const cpm = Math.round((this.correctChars / elapsedTime) * 60);
            
            // Calculate Accuracy
            const accuracy = this.totalChars > 0 
                ? Math.round((this.correctChars / this.totalChars) * 100) 
                : 0;
            
            this.wpmEl.textContent = wpm;
            this.cpmEl.textContent = cpm;
            this.accuracyEl.textContent = `${accuracy}%`;
        }
    }
    
    startStatsUpdate() {
        this.statsInterval = setInterval(() => {
            if (this.testActive) {
                this.updateStats();
            }
        }, 100);
    }
    
    updateTimeDisplay() {
        this.timeLeftEl.textContent = `${Math.max(Math.round(this.remainingSeconds), 0)}s`;
    }
    
    startTimer() {
        this.cancelTimer();
        this.remainingSeconds = this.durationSeconds;
        this.updateTimeDisplay();
        
        this.timerInterval = setInterval(() => {
            if (!this.testActive) {
                this.cancelTimer();
                return;
            }
            
            this.remainingSeconds--;
            this.updateTimeDisplay();
            
            if (this.remainingSeconds <= 0) {
                this.completeTest(true);
            }
        }, 1000);
    }
    
    cancelTimer() {
        if (this.timerInterval) {
            clearInterval(this.timerInterval);
            this.timerInterval = null;
        }
    }
    
    cancelStatsUpdate() {
        if (this.statsInterval) {
            clearInterval(this.statsInterval);
            this.statsInterval = null;
        }
    }
    
    cancelTimers() {
        this.cancelTimer();
        this.cancelStatsUpdate();
    }
    
    completeTest(timeUp = false) {
        this.testActive = false;
        this.cancelTimers();
        
        const elapsedTime = this.startTime ? (Date.now() - this.startTime) / 1000 : 0;
        
        // Final calculations
        const words = this.correctChars / 5.0;
        const wpm = Math.round((words / elapsedTime) * 60);
        const cpm = Math.round((this.correctChars / elapsedTime) * 60);
        const accuracy = this.totalChars > 0 
            ? Math.round((this.correctChars / this.totalChars) * 100) 
            : 0;
        
        // Disable input
        this.inputField.disabled = true;
        
        // Determine performance level
        let title, subtitle, colorClass;
        if (wpm >= 60) {
            title = "Excellent!";
            subtitle = timeUp ? "Time limit reached" : "Text completed";
            colorClass = "performance-excellent";
        } else if (wpm >= 40) {
            title = "Great Job!";
            subtitle = timeUp ? "Time limit reached" : "Text completed";
            colorClass = "performance-good";
        } else if (wpm >= 20) {
            title = "Keep Practicing";
            subtitle = timeUp ? "Time limit reached" : "Text completed";
            colorClass = "performance-fair";
        } else {
            title = "Don't Give Up";
            subtitle = timeUp ? "Time limit reached" : "Text completed";
            colorClass = "performance-poor";
        }
        
        this.updateStatusMessage(
            `${timeUp ? "⏰ Time's up! " : "✅ Completed! "}WPM ${wpm}, Accuracy ${accuracy}%`,
            colorClass
        );
        
        // Update modal
        this.modalTitle.textContent = title;
        this.modalTitle.className = colorClass;
        this.modalSubtitle.textContent = subtitle;
        this.resultWPM.textContent = wpm;
        this.resultCPM.textContent = cpm;
        this.resultAccuracy.textContent = `${accuracy}%`;
        this.resultTime.textContent = `${Math.round(elapsedTime)}s`;
        
        // Show modal
        this.showModal();
    }
    
    showModal() {
        this.resultsModal.classList.add('show');
    }
    
    closeModal() {
        this.resultsModal.classList.remove('show');
    }
    
    updateStatusMessage(message, className = "normal") {
        this.statusMessage.textContent = message;
        this.statusMessage.className = `status-message ${className}`;
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new TypingSpeedTest();
});

