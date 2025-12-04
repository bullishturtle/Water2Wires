# Water2Wires - Data Recovery & System Optimizer

<p align="center">
  <img src="assets/logo.png" width="120" alt="Water2Wires Logo">
  <br>
  <strong>World forgot us. So we rewired it.</strong>
</p>

[![Version](https://img.shields.io/badge/version-2.0.1-00E5FF)](https://water2wires.com)
[![Build](https://img.shields.io/badge/build-W2W--02-FF0080)](https://water2wires.com)
[![License](https://img.shields.io/badge/license-Commercial-gold)](LICENSE)

## 🚀 What Is Water2Wires?

Water2Wires is a **professional-grade data recovery application** with a cyberpunk aesthetic. It combines powerful recovery tools with a Windows system optimizer, all in one beautiful, futuristic interface.

### ✨ Features

**Data Recovery:**
- 🔍 Quick Scan - Fast recovery of recently deleted files
- 🔬 Deep Scan - Thorough sector-by-sector recovery
- 💾 SSD Forensic Mode - Specialized recovery for SSDs with TRIM
- 📊 Real-time progress with 5-stage system
- 🧠 AI-Enhanced recovery (Pro)

**System Optimizer:**
- ⚡ Performance tweaks for Windows 8-11
- 🔒 Privacy enhancements
- 🧹 System cleanup and maintenance
- 🌡️ SMART drive health monitoring

**Smart Features:**
- 📱 Real device detection (OS, CPU, RAM, GPU, Drives)
- 💡 Context-aware recommendations
- ⚠️ TRIM and drive health warnings
- 📅 Scan scheduling (Pro)

## 📦 Quick Start

### Prerequisites

- Node.js 18+ (for frontend)
- Python 3.8+ (for backend API)
- Windows 8/8.1/10/11, macOS, or Linux

### Installation

```bash
# Clone the repository
git clone https://github.com/water2wires/water2wires.git
cd water2wires

# Install dependencies
npm install
pip install psutil

# Start the application
# On Windows, double-click start-water2wires.bat
# Or run manually:
python src/api/server.py  # Terminal 1
npm run dev               # Terminal 2
```

### Windows Quick Launch

Simply double-click `start-water2wires.bat` to launch both the API server and frontend automatically.

## 🖥️ Usage

1. **Dashboard** - View detected drives and system info
2. **Select Drive** - Click a drive card to configure scan
3. **Choose Scan Type** - Quick (5-15 min), Deep (1-4 hours), or SSD Forensic
4. **Review Results** - Preview and recover files
5. **Optimizer** - Apply Windows tweaks (requires admin)

## 🔑 Pro Features

Some advanced features require Pro access:
- Deep Scan & SSD Forensic modes
- AI-Enhanced recovery
- Scan scheduling
- Full System Optimizer
- Cloud export

**Get Pro:** Contact Landon
- 📱 Instagram: [@iclosedealz](https://instagram.com/iclosedealz)
- 📧 Email: Idontsmoke420@gmail.com (Subject: water2wires)
- 🌐 Website: [www.Water2Wires.com](https://water2wires.com)

**Price:** $29.99 lifetime access

## 🏗️ Architecture

```
water2wires/
├── src/
│   ├── components/     # Svelte UI components
│   ├── lib/           # Frontend utilities
│   ├── api/           # Python backend API
│   └── water2wires/   # Python recovery engine
├── src-tauri/         # Tauri desktop wrapper
├── start-water2wires.bat  # Windows launcher
└── README.md
```

## 🛠️ Development

```bash
# Frontend only (browser mock data)
npm run dev

# Full stack (real device detection)
python src/api/server.py  # Terminal 1
npm run dev               # Terminal 2

# Build for production
npm run build
```

## ⚠️ Important Notes

- **SSD TRIM Warning:** SSDs with TRIM enabled permanently erase deleted data. Recovery chances are very low.
- **Read-Only:** Water2Wires operates in read-only mode. It never writes to source drives.
- **Admin Rights:** Some optimizer tweaks require administrator privileges.
- **Backup First:** Always back up important data before recovery attempts.

## 🎨 Brand Identity

Water2Wires features a **cyberpunk streetwear tech aesthetic**:
- 🔷 Primary: Electric Cyan (#00E5FF)
- 🔶 Accent: Hot Pink (#FF0080)
- ⬛ Background: Deep Black (#0A0A0A)
- Typography: Space Grotesk, Inter, JetBrains Mono

## 📞 Support

Need help? Reach out:
- 📱 DM [@iclosedealz](https://instagram.com/iclosedealz) on Instagram
- 📧 Email Idontsmoke420@gmail.com (Subject: water2wires)
- 🌐 Visit [www.Water2Wires.com](https://water2wires.com)

---

<p align="center">
  <strong>Water2Wires v2.0.1 | W2W-02</strong><br>
  Built by those the world forgot. We rewired it.
</p>
