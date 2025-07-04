# CuteSymbols 🔥

A Python library for managing and accessing cute emoji symbols in your applications. Perfect for adding visual flair to your console output, logging, or user interfaces!

## ✨ Features

- **🚀 Easy Access**: Direct access to symbols using simple attribute syntax
- **🔍 Smart Search**: Powerful regex-based search with case-insensitive matching
- **📁 Organized Categories**: Symbols grouped by purpose (State, Activity, Emotion, Objects)
- **🔄 Reverse Lookup**: Find symbol names and groups from emoji values
- **📊 Complete Listing**: List all available symbols with their metadata
- **🛠️ Developer Friendly**: Full type hints and comprehensive documentation

## 🎯 Available Symbol Categories

### State ✅
- `CHECK` ✅ - Success indicator
- `CROSS` ❌ - Error indicator  
- `WARNING` ⚠️ - Warning indicator
- `INFO` ℹ️ - Information indicator
- `SUCCESS` ✔️ - Success marker
- `FAILURE` ✖️ - Failure marker
- `QUESTION` ❓ - Question marker

### Activity 🚀
- `ROCKET` 🚀 - Launch/start indicator
- `LOOP` 🔄 - Process/refresh indicator
- `CLOCK` ⏱️ - Timing indicator
- `HOURGLASS` ⏳ - Loading indicator
- `FLASH` ⚡ - Speed/power indicator

### Emotion 💡
- `THINK` 🤔 - Thinking indicator
- `BRAIN` 🧠 - Intelligence indicator
- `LIGHT` 💡 - Idea indicator
- `FIRE` 🔥 - Hot/trending indicator
- `MAGIC` ✨ - Special indicator
- `STAR` ⭐ - Favorite indicator
- `EYES` 👀 - Attention indicator

### Objects 🛠️
- `FOLDER` 📁 - Directory indicator
- `GEAR` ⚙️ - Settings indicator
- `TOOL` 🛠️ - Tool/utility indicator
- `BUG` 🐞 - Bug/issue indicator

## 📚 Quick Start
```python
from cuteSymbols import CuteSymbols
# Create an instance
symbols = CuteSymbols()
# Access symbols directly
print(f"Task completed {symbols.CHECK}") # Task completed ✅ print(f"Loading {symbols.HOURGLASS}") # Loading ⏳ print(f"Great idea {symbols.LIGHT}") # Great idea 💡
``` 

## 🔧 Core Methods

### Direct Symbol Access
```python
# Access any symbol directly
fire_emoji = symbols.FIRE # 🔥 check_emoji = symbols.CHECK # ✅ rocket_emoji = symbols.ROCKET # 🚀
# Use in your applications
print(f"Deployment started {symbols.ROCKET}") print(f"Tests passed {symbols.SUCCESS}") print(f"Found issue {symbols.BUG}")
``` 

### Search Functionality 🔍

The `search()` method provides powerful pattern matching:
```python
# Simple text search (case-insensitive by default)
results = CuteSymbols.search("fire")
# Returns: [('Emotion', 'FIRE', '🔥')]
# Search by emoji
results = CuteSymbols.search("🔥")
# Returns: [('Emotion', 'FIRE', '🔥')]
# Regex patterns
results = CuteSymbols.search(r"^F") # Symbols starting with 'F'
# Returns: [('Emotion', 'FIRE', '🔥'), ('State', 'FAILURE', '✖️'), ('Objects', 'FOLDER', '📁')]
# Advanced regex with custom flags
import re results = CuteSymbols.search(r"fire", flags=0) # Case-sensitive results = CuteSymbols.search(r"f.*e$", flags=re.MULTILINE) # Multi-line pattern
``` 

### Reverse Lookup 🔄

Find information about emojis:
```python
# Get complete info (name and group)
info = CuteSymbols.info_from_emoji("🔥")
# Returns: ('FIRE', 'Emotion')
# Get just the name
name = CuteSymbols.name_from_emoji("✅")
# Returns: 'CHECK'
# Handle unknown emojis
info = CuteSymbols.info_from_emoji("🌟")
# Returns: None
``` 

### List All Symbols 📋
```python
# Get all symbols as tuples (group, name, value)
all_symbols = CuteSymbols.list_all()
# Returns: [('State', 'CHECK', '✅'), ('State', 'CROSS', '❌'), ...]
# Print a formatted table
CuteSymbols.print_table()
``` 

## 🎨 Usage Examples

### Console Logging
```python 
from cuteSymbols import CuteSymbols
symbols = CuteSymbols()
def log_status(message, status): if status == "success": print(f"{symbols.CHECK} {message}") elif status == "error": print(f"{symbols.CROSS} {message}") elif status == "warning": print(f"{symbols.WARNING} {message}") else: print(f"{symbols.INFO} {message}")
# Usage
log_status("Database connected", "success") # ✅ Database connected log_status("Connection timeout", "error") # ❌ Connection timeout log_status("Memory usage high", "warning") # ⚠️ Memory usage high
``` 

### Progress Indicators
```python 
import time from cuteSymbols import CuteSymbols
symbols = CuteSymbols()
def show_progress(task_name): print(f"{symbols.HOURGLASS} Starting {task_name}...") time.sleep(1) print(f"{symbols.LOOP} Processing {task_name}...") time.sleep(1) print(f"{symbols.FLASH} Finalizing {task_name}...") time.sleep(1) print(f"{symbols.CHECK} {task_name} completed!")
show_progress("Data Analysis")
``` 

### Dynamic Symbol Discovery
```python
# Find all symbols containing "tool"
tools = CuteSymbols.search("tool") for group, name, emoji in tools: print(f"{emoji} {name} (from {group})")
# Find all fire-related symbols
fire_symbols = CuteSymbols.search("fire") print(f"Fire symbols: {[emoji for _, _, emoji in fire_symbols]}")
# Search by pattern
question_symbols = CuteSymbols.search(r".*TION") # Ends with "TION"
``` 

## 🧠 Advanced Features

### Custom Search Flags
```python 
import re
# Case-sensitive search
results = CuteSymbols.search("Fire", flags=0) # Won't find "FIRE"
# Multi-line patterns
results = CuteSymbols.search(r"^FIRE$", flags=re.MULTILINE)
# Combine multiple flags
results = CuteSymbols.search(r"pattern", flags=re.MULTILINE | re.DOTALL)
``` 

### Integration with Other Libraries
```python
# With logging
import logging from cuteSymbols import CuteSymbols
symbols = CuteSymbols()
# Custom formatter
class EmojiFormatter(logging.Formatter): def format(self, record): if record.levelno == logging.ERROR: record.msg = f"{symbols.CROSS} {record.msg}" elif record.levelno == logging.WARNING: record.msg = f"{symbols.WARNING} {record.msg}" elif record.levelno == logging.INFO: record.msg = f"{symbols.INFO} {record.msg}" return super().format(record)
``` 

## 🔍 Error Handling
```python
# Handle search errors
try: results = CuteSymbols.search("[invalid regex") except ValueError as e: print(f"{symbols.CROSS} Search error: {e}")
# Handle missing symbols
try: info = CuteSymbols.info_from_emoji(None) except AttributeError as e: print(f"{symbols.WARNING} {e}")
``` 

## 🚀 Installation
```bash
# Clone the repository
git clone [https://github.com/yourusername/cutesymbols.git](https://github.com/yourusername/cutesymbols.git) cd cutesymbols

# Run tests
python -m unittest tests/tests.py -v
``` 

## 📖 API Reference

### Methods

- `search(pattern, flags=re.IGNORECASE)` - Search symbols by pattern
- `info_from_emoji(emoji)` - Get name and group from emoji
- `name_from_emoji(emoji)` - Get symbol name from emoji
- `list_all()` - Get all symbols as tuples
- `print_table()` - Print formatted symbol table

### Properties

Access any symbol directly: `symbols.FIRE`, `symbols.CHECK`, etc.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## 📄 License

This project is licensed under the MIT License.

---

Made with 💡 and 🔥 by the CuteSymbols team!
```
