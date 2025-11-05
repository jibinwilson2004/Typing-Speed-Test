# ⚡ Typing Speed Test ⚡

<div align="center">

![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-8.6+-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**A beautiful, colorful typing speed test application built with Python and Tkinter**

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

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes pre-installed with Python)

### Step-by-Step Installation

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

3. **Run the application**
   ```bash
   python speed.py
   # or
   python3 speed.py
   ```

That's it! No additional dependencies required! 🎉

---

## 📖 Usage

### Getting Started

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

## 🎨 Screenshots

<div align="center">

### Main Interface
![Main Screen](https://via.placeholder.com/800x500/1a1a2e/00ff88?text=Typing+Speed+Test+Interface)

*Beautiful dark theme with colorful stat cards and gradient progress bar*

### Results Window
![Results](https://via.placeholder.com/600x400/0f1b2b/00d4ff?text=Results+Window)

*Styled results display with comprehensive statistics*

</div>

---

## 🛠️ Technical Details

### Built With
- **Python 3.7+**: Core programming language
- **Tkinter**: GUI framework for the user interface
- **Random Module**: For generating random text passages
- **Time Module**: For accurate timing and statistics

### Architecture
- **Object-Oriented Design**: Clean class-based structure
- **Event-Driven**: Responsive to user input and timer events
- **Real-time Updates**: Continuous UI refresh during typing

### Key Components
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
- 📱 Responsive design improvements

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

