# Water2Wires Setup Guide

## Prerequisites

### Windows
- Windows 10/11 (64-bit)
- Python 3.10 or higher
- Node.js 18+ and npm
- Rust (for Tauri compilation)
- Visual Studio Build Tools (for native modules)

### Development Tools
- Git
- Python virtual environment tool (venv or conda)

## Installation Steps

### 1. Clone Repository
```bash
git clone <repository-url>
cd water2wires
```

### 2. Python Backend Setup

#### Create Virtual Environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate
```

#### Install Python Dependencies
```bash
pip install -r requirements.txt
```

**Note:** Some dependencies may require additional system libraries:
- `pytsk3` requires libtsk (The Sleuth Kit)
- `pywin32` is Windows-specific
- `onnxruntime-gpu` requires CUDA for GPU acceleration

#### Windows-specific Setup
```bash
# Install WMI support
pip install pywin32
python Scripts/pywin32_postinstall.py -install
```

### 3. Frontend Setup

#### Install Node.js Dependencies
```bash
npm install
```

### 4. Tauri Setup

#### Install Rust
Download and install from: https://www.rust-lang.org/tools/install

#### Install Tauri CLI
```bash
npm install -g @tauri-apps/cli
```

#### Verify Installation
```bash
tauri --version
```

### 5. Build Application

#### Development Mode
```bash
npm run tauri:dev
```

#### Production Build
```bash
npm run tauri:build
```

The built application will be in `src-tauri/target/release/`

## Configuration

### First Run
1. Launch Water2Wires
2. Configuration is stored in:
   - Windows: `%APPDATA%\water2wires\config.json`
   - Linux: `~/.config/water2wires/config.json`
   - macOS: `~/Library/Application Support/water2wires/config.json`

### AI Models
ONNX models will be downloaded automatically on first use. Models are stored in:
- `models/` directory in the application folder

To manually download models:
1. Models are hosted on Hugging Face
2. Download and place in `models/` directory
3. Required models:
   - `file_classifier.onnx` - File type classification
   - `corruption_detector.onnx` - Corruption detection
   - `fragment_assembler.onnx` - Fragment reassembly

## Running as Administrator

**IMPORTANT:** Water2Wires requires administrator/root privileges to access raw disk devices.

### Windows
1. Right-click the executable
2. Select "Run as administrator"

### Linux
```bash
sudo ./water2wires
```

## Troubleshooting

### Python Import Errors
- Ensure virtual environment is activated
- Verify all dependencies are installed: `pip list`
- Check Python version: `python --version` (should be 3.10+)

### Tauri Build Errors
- Ensure Rust is installed: `rustc --version`
- Update Rust: `rustup update`
- Clean build: `cd src-tauri && cargo clean`

### Disk Access Denied
- Run as administrator/root
- Check Windows User Account Control (UAC) settings
- Verify drive is not in use by another application

### GPU Not Detected
- Install CUDA toolkit for GPU acceleration
- Verify GPU drivers are up to date
- Check `onnxruntime-gpu` installation

## Development

### Running Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black src/
```

### Type Checking
```bash
mypy src/
```

## Support

For issues and questions:
- Check documentation in `docs/`
- Review error logs in application data directory
- Submit issues to project repository

