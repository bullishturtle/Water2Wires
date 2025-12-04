# Water2Wires Quick Start Guide

## Installation (5 minutes)

### Step 1: Install Prerequisites
```bash
# Python 3.10+
python --version

# Node.js 18+
node --version

# Rust (for Tauri)
rustc --version
```

### Step 2: Setup Backend
```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Setup Frontend
```bash
# Install Node.js dependencies
npm install
```

### Step 4: Run Application
```bash
# Development mode
npm run tauri:dev

# Or build for production
npm run tauri:build
```

## First Recovery

1. **Launch Water2Wires** (as Administrator)
2. **Select a Drive** from the dashboard
3. **Choose Scan Type:**
   - Quick Scan: Fast filesystem parsing (5-15 min)
   - Deep Scan: Full sector carving (1-4 hours)
   - AI-Enhanced: ML-powered recovery (variable)
4. **Select File Types** to recover
5. **Configure Options:**
   - Enable AI enhancement
   - Create forensic image (recommended)
   - Choose destination folder
6. **Start Recovery** and monitor progress
7. **Preview and Recover** files from results

## Key Features

### Quick Scan
- Parses filesystem metadata (MFT, FAT tables)
- Finds deleted file entries
- Fast results in minutes

### Deep Scan
- Sector-by-sector file carving
- Scans unallocated space
- Finds files even after format

### AI-Enhanced
- Machine learning file classification
- Corruption detection
- Fragment reassembly

### SSD Emergency Mode
- Automatic TRIM detection
- Emergency shutdown option
- Time-sensitive recovery

### Live Monitor
- Background deletion monitoring
- Instant recovery of recently deleted files
- 30-day rolling cache

## Tips for Best Results

1. **Stop using the drive immediately** after data loss
2. **Run as Administrator** for full disk access
3. **Use forensic image mode** for safety
4. **Enable AI enhancement** for better recovery
5. **Save to different drive** than source
6. **Don't format** the drive before recovery

## Common Scenarios

### Accidentally Deleted Files
- Use **Quick Scan** for fastest results
- Check **Live Monitor** if enabled

### Formatted Drive
- Use **Deep Scan** for complete recovery
- May take several hours

### Corrupted Drive
- Use **AI-Enhanced Scan**
- Enable bad sector retry
- Create forensic image first

### SSD with TRIM
- **Emergency Mode** activates automatically
- Act quickly - data loss imminent
- Consider professional recovery service

## Troubleshooting

**"Permission Denied"**
- Run as Administrator
- Close other programs using the drive

**"No Files Found"**
- Try Deep Scan instead of Quick Scan
- Check if drive was overwritten
- Verify file types selected

**"Scan Too Slow"**
- Reduce file types selected
- Disable AI enhancement
- Skip bad sectors option

**"Out of Memory"**
- Reduce RAM allocation in settings
- Use smaller chunk sizes
- Close other applications

## Support

- Documentation: See `ARCHITECTURE.md` and `SETUP.md`
- Logs: Check application data directory
- Issues: Submit to project repository

## Safety Reminders

⚠️ **NEVER write to the source drive**
⚠️ **Always create forensic image for important data**
⚠️ **Verify recovered files before deleting originals**
⚠️ **SSD recovery is time-sensitive - act quickly**

