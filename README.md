# ⚡ Typing Speed Test ⚡

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6+-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**A beautiful, colorful typing speed test application available as Desktop (Python/Tkinter) and Web (HTML/CSS/JS) versions**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 🎨 Overview

**Typing Speed Test** is a modern, feature-rich typing speed testing application that provides real-time accuracy tracking, beautiful UI design, and comprehensive statistics. Test your typing skills with randomly generated text passages and compete against the 60-second timer!

<div align="center">

### 🌟 **Key Highlights**

✨ **Real-time Accuracy Tracking** • 🎯 **Character-by-Character Feedback** • ⏱️ **60-Second Timer Challenge**  
🎨 **Beautiful Colorful UI** • 📊 **Comprehensive Statistics** • 🔄 **Random Text Generation**

</div>

---

## ✨ Features

### 🎯 **Accuracy & Performance**
- **Real-time Character Matching**: Every keystroke is compared instantly with the original text
- **Color-Coded Visual Feedback**: 
  - 🟢 **Green** for correct characters
  - 🔴 **Red** for incorrect characters
  - 🟡 **Yellow** cursor indicator for current position
- **Precise Accuracy Calculation**: Based on correct vs total characters typed

### 📊 **Statistics Dashboard**
- **WPM (Words Per Minute)**: Real-time calculation based on standard 5-character word count
- **CPM (Characters Per Minute)**: Track your typing speed in characters
- **Accuracy Percentage**: Monitor your typing precision
- **Time Remaining**: Live countdown timer with visual indicators

### 🎨 **Beautiful UI Design**
- **Colorful Stat Cards**: Each metric displayed in vibrant, distinct colors
- **Gradient Progress Bar**: Visual progress indicator with smooth color transitions
- **Dark Theme**: Modern dark background with neon accents
- **Responsive Layout**: Clean, organized interface optimized for typing

### 🔄 **Random Text Generation**
- **Dynamic Text Creation**: Each test uses freshly generated random passages
- **Natural Language**: Realistic word combinations with proper punctuation
- **Variable Length**: Texts generated with 80-120 words for variety

### ⏱️ **Timer Features**
- **60-Second Challenge**: Test your speed under time pressure
- **Auto-Submit**: Automatically ends test when time expires
- **Live Countdown**: Real-time timer display with second-by-second updates

### 🎉 **Results Display**
- **Beautiful Results Window**: Styled popup with comprehensive statistics
- **Performance Assessment**: Get feedback based on your typing speed
- **Quick Actions**: Easy restart or exit options

---

## 🚀 Installation & Deployment

### 🌐 Web Application (Recommended)

The web version can be deployed on Vercel in minutes!

#### Option 1: Deploy to Vercel (One-Click)

1. **Fork or clone this repository**
   ```bash
   git clone https://github.com/jibinwilson2004/Typing-Speed-Test.git
   cd Typing-Speed-Test
   ```

2. **Deploy to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Sign in with GitHub
   - Click "New Project"
   - Import this repository
   - Click "Deploy"
   - That's it! Your app is live! 🚀

#### Option 2: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

#### Option 3: Run Locally

Simply open `index.html` in your browser or use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

Then open `http://localhost:8000` in your browser.

### 💻 Desktop Application

#### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)

#### Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jibinwilson2004/Typing-Speed-Test.git
   cd Typing-Speed-Test
   ```

2. **Verify Python installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the desktop application**
   ```bash
   python speed.py
   # or
   python3 speed.py
   ```

That's it! No additional dependencies required! 🎉

---

## 📖 Usage

### 🌐 Web Application
1. **Open the web application** (either deployed on Vercel or locally)
2. **Start typing** in the input field
3. **Watch your statistics** update in real-time
4. **Complete the test** by finishing the text or waiting for the 60-second timer
5. **View results** in the beautiful modal popup

### 💻 Desktop Application

1. **Launch the Application**
   - Run `python speed.py` from the terminal
   - The application window will open with a randomly generated text passage

2. **Start Typing**
   - Click on the input field or press any key to begin
   - The 60-second timer starts automatically on your first keystroke
   - Type the displayed text as accurately as possible

3. **Monitor Your Progress**
   - Watch your real-time statistics update in the colorful cards
   - See color-coded feedback on the text display
   - Track your progress with the gradient progress bar

4. **Complete the Test**
   - Complete when you finish typing the entire text, OR
   - Wait for the 60-second timer to expire (auto-submit)

5. **View Results**
   - A beautiful results window displays your performance
   - Review your WPM, CPM, Accuracy, and Time
   - Start a new test or close the results window

### Controls

| Button | Action |
|:------:|:-------|
| 🔄 **New Text** | Load a fresh random text passage |
| ⏹️ **Reset** | Reset the current test and start over |
| **Type** | Begin the test by typing in the input field |

---

## 🎨 Features Comparison

| Feature | Web Version | Desktop Version |
|:--------|:-----------:|:---------------:|
| **Platform** | 🌐 Browser (Any OS) | 💻 Windows/Mac/Linux |
| **Deployment** | ✅ Vercel/Netlify/GitHub Pages | 📦 Local Installation |
| **Real-time Stats** | ✅ Yes | ✅ Yes |
| **60-Second Timer** | ✅ Yes | ✅ Yes |
| **Color-Coded Feedback** | ✅ Yes | ✅ Yes |
| **Random Text Generation** | ✅ Yes | ✅ Yes |
| **Responsive Design** | ✅ Yes (Mobile Friendly) | ⚠️ Desktop Only |
| **No Installation** | ✅ Yes | ❌ Requires Python |
| **Offline Usage** | ⚠️ Requires Internet (initial load) | ✅ Yes |

## 🎨 Screenshots

<div align="center">

### Web Application Interface
![Web Main Screen](https://via.placeholder.com/800x500/1a1a2e/00ff88?text=Web+Typing+Speed+Test)

*Beautiful responsive web interface with colorful stat cards and gradient progress bar*

### Desktop Application Interface
![Desktop Main Screen](https://via.placeholder.com/800x500/1a1a2e/00ff88?text=Desktop+Typing+Speed+Test)

*Beautiful desktop application with colorful stat cards and gradient progress bar*

### Results Window
![Results](https://via.placeholder.com/600x400/0f1b2b/00d4ff?text=Results+Window)

*Styled results display with comprehensive statistics*

</div>

---

## 🛠️ Technical Details

### Web Application
- **HTML5**: Semantic markup and structure
- **CSS3**: Modern styling with gradients, animations, and responsive design
- **JavaScript (ES6+)**: Vanilla JavaScript for all functionality
- **No Dependencies**: Pure client-side application, no frameworks required
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **PWA Ready**: Can be easily converted to a Progressive Web App

### Desktop Application
- **Python 3.7+**: Core programming language
- **Tkinter**: GUI framework for the user interface
- **Random Module**: For generating random text passages
- **Time Module**: For accurate timing and statistics

### Architecture

#### Web Version
- **Pure JavaScript Class**: `TypingSpeedTest` class handles all functionality
- **Event-Driven**: Responsive to user input and timer events
- **Real-time Updates**: Continuous UI refresh during typing
- **DOM Manipulation**: Efficient text rendering with color-coded feedback

#### Desktop Version
- **Object-Oriented Design**: Clean class-based structure
- **Event-Driven**: Responsive to user input and timer events
- **Real-time Updates**: Continuous UI refresh during typing

### Key Components

#### Web Version
- `TypingSpeedTest`: Main application class
- `generateRandomText()`: Random text passage creation
- `updateStats()`: Real-time statistics calculation
- `updateTextDisplay()`: Color-coded feedback rendering
- `startTimer()`: 60-second countdown timer

#### Desktop Version
- `TypingSpeedTest`: Main application class
- `create_stat_card()`: Dynamic stat card generation
- `generate_random_text()`: Random text passage creation
- `update_stats()`: Real-time statistics calculation
- `update_text_display()`: Color-coded feedback rendering

---

## 📊 Statistics Calculation

### WPM (Words Per Minute)
```
WPM = (Correct Characters / 5) / Time (minutes) × 60
```
Standard typing test uses 5 characters per word.

### CPM (Characters Per Minute)
```
CPM = (Correct Characters / Time (seconds)) × 60
```
Total correct characters typed per minute.

### Accuracy
```
Accuracy = (Correct Characters / Total Characters) × 100%
```
Percentage of correctly typed characters.

---

## 🎯 Performance Levels

| WPM Range | Performance Level | Badge Color |
|:---------:|:----------------:|:-----------:|
| 60+ | 🌟 **Excellent** | 🟢 Green |
| 40-59 | 👍 **Great Job** | 🔵 Cyan |
| 20-39 | ✨ **Keep Practicing** | 🟡 Yellow |
| <20 | 💪 **Don't Give Up** | 🔴 Red |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository** 🍴
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request** 🚀

### Ideas for Contribution
- 🌍 Add more languages for text generation
- 🎨 Additional UI themes and color schemes
- 📈 Statistics history and leaderboards
- ⌨️ Custom keyboard layouts support
- 🎵 Sound effects and audio feedback
- 📱 PWA support for web version
- 🔄 Sync stats between web and desktop
- 📊 Advanced analytics and charts
- 🏆 Achievement system
- 🌙 Dark/Light mode toggle

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Jibin Wilson**

- GitHub: [@jibinwilson2004](https://github.com/jibinwilson2004)
- Repository: [Typing-Speed-Test](https://github.com/jibinwilson2004/Typing-Speed-Test)

---

## 🙏 Acknowledgments

- **Tkinter Community**: For the excellent GUI framework
- **Python Community**: For continuous improvements and support
- **Open Source Contributors**: For inspiration and best practices

---

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ on GitHub!

<div align="center">

### 🚀 **Start Typing Now!**

**Improve your typing speed and accuracy with this beautiful, feature-rich application!**

---

Made with ❤️ and Python 🐍

![Typing](https://img.shields.io/badge/Keep-Typing-blue?style=for-the-badge)
![Practice](https://img.shields.io/badge/Practice-Makes%20Perfect-green?style=for-the-badge)

</div>

