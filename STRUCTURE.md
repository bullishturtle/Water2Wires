# Water2Wires Project Structure

```
water2wires/
├── src/
│   ├── components/           # Svelte UI Components
│   │   ├── Dashboard.svelte        # Main drive selection & stats
│   │   ├── DriveCard.svelte        # Individual drive card
│   │   ├── HelpCenter.svelte       # Help & support modal
│   │   ├── MainHub.svelte          # Main layout container
│   │   ├── ProUnlockModal.svelte   # Pro tier unlock dialog
│   │   ├── ResultsExplorer.svelte  # Recovered files browser
│   │   ├── ScanConfigModal.svelte  # 3-step scan wizard
│   │   ├── ScanProgress.svelte     # Scan progress view
│   │   ├── Scheduler.svelte        # Scan scheduling UI
│   │   ├── SettingsPanel.svelte    # Application settings
│   │   ├── Sidebar.svelte          # Navigation sidebar
│   │   ├── SmartDataViewer.svelte  # SMART diagnostics modal
│   │   ├── SplashScreen.svelte     # App loading screen
│   │   └── SystemOptimizer.svelte  # Windows tweaks UI
│   │
│   ├── lib/                  # Frontend Utilities
│   │   ├── brand.js              # Brand constants & helpers
│   │   ├── proTier.js            # Pro feature management
│   │   ├── recovery.js           # Recovery utilities
│   │   ├── scheduler.js          # Scan scheduling logic
│   │   └── systemInfo.js         # System detection & API
│   │
│   ├── api/                  # Python Backend
│   │   ├── backend.py            # Main backend API wrapper
│   │   └── server.py             # HTTP API server
│   │
│   ├── water2wires/          # Python Recovery Engine
│   │   ├── __init__.py
│   │   ├── ai_engine.py          # AI file detection
│   │   ├── carver_engine.py      # File carving
│   │   ├── config_manager.py     # Configuration management
│   │   ├── drive_manager.py      # Drive detection & health
│   │   ├── export_manager.py     # File export handlers
│   │   ├── fs_parser.py          # Filesystem parsing
│   │   ├── live_monitor.py       # Real-time monitoring
│   │   ├── orchestrator.py       # Scan orchestration
│   │   ├── signature_engine.py   # File signature detection
│   │   ├── ssd_forensics.py      # SSD-specific recovery
│   │   └── windows_optimizer.py  # Windows tweaks
│   │
│   ├── App.svelte            # Root Svelte component
│   ├── app.css               # Global styles
│   └── main.js               # Application entry point
│
├── src-tauri/                # Tauri Desktop Wrapper
│   ├── src/
│   │   └── main.rs              # Tauri Rust backend
│   ├── Cargo.toml               # Rust dependencies
│   └── tauri.conf.json          # Tauri configuration
│
├── scripts/                  # Build & Run Scripts
│   ├── run-dev.bat              # Development mode launcher
│   └── build-prod.bat           # Production build script
│
├── assets/                   # Static Assets (icons, images)
├── dist/                     # Production build output
├── node_modules/             # Node.js dependencies
│
├── index.html                # HTML entry point
├── package.json              # Node.js config
├── vite.config.js            # Vite bundler config
├── tailwind.config.js        # Tailwind CSS config
├── postcss.config.js         # PostCSS config
├── svelte.config.js          # Svelte config
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Python project config
│
├── README.md                 # Main documentation
├── STRUCTURE.md              # This file
├── ARCHITECTURE.md           # Technical architecture
├── QUICKSTART.md             # Quick start guide
└── start-water2wires.bat     # One-click launcher
```

## Key Files

| File | Purpose |
|------|---------|
| `src/lib/systemInfo.js` | Detects real system info via API or browser fallback |
| `src/api/server.py` | Python HTTP server providing real OS/drive data |
| `src/components/Dashboard.svelte` | Main UI showing drives and stats |
| `src/lib/proTier.js` | Manages free vs Pro feature access |
| `start-water2wires.bat` | One-click launcher for Windows |

## Running the App

### Development Mode
```bash
# Option 1: Use launcher script
./scripts/run-dev.bat

# Option 2: Manual
python src/api/server.py  # Terminal 1
npm run dev               # Terminal 2
```

### Production Build
```bash
npm run build
npm run preview  # Test production build
```

### Desktop App (Tauri)
```bash
npm run tauri:dev    # Development
npm run tauri:build  # Production .exe
```

