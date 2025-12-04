# Water2Wires Architecture

## Overview

Water2Wires is a professional data recovery application built with a modern, modular architecture separating concerns between backend recovery engine and frontend user interface.

## System Architecture

```
┌─────────────────────────────────────────┐
│         Tauri + Svelte Frontend         │
│  (UI Components, State Management)       │
└──────────────┬──────────────────────────┘
               │
               │ IPC / API Calls
               │
┌──────────────▼──────────────────────────┐
│         Python Backend Engine            │
│  ┌──────────────────────────────────┐  │
│  │   Recovery Orchestrator           │  │
│  └───────────┬───────────────────────┘  │
│              │                           │
│  ┌───────────▼───────────┐              │
│  │  Drive Manager        │              │
│  │  Filesystem Parser    │              │
│  │  Carver Engine        │              │
│  │  Signature Engine     │              │
│  │  AI Engine            │              │
│  │  SSD Forensics        │              │
│  │  Export Manager       │              │
│  └───────────────────────┘              │
└─────────────────────────────────────────┘
               │
               │ Direct Disk Access
               │
┌──────────────▼──────────────────────────┐
│         Operating System                 │
│  (Disk Drivers, Filesystem APIs)         │
└──────────────────────────────────────────┘
```

## Component Overview

### Frontend (Tauri + Svelte)

**Technology Stack:**
- Tauri 2.0 - Native application framework
- Svelte 5 - Reactive UI framework
- TailwindCSS - Utility-first CSS
- Chart.js - Data visualization

**Key Components:**
- `App.svelte` - Main application shell
- `Dashboard.svelte` - Drive selection and overview
- `SplashScreen.svelte` - Application startup
- `Sidebar.svelte` - Navigation
- `DriveCard.svelte` - Drive information display
- `ScanConfigModal.svelte` - Scan configuration wizard
- `StatusPanel.svelte` - System monitoring

**State Management:**
- Svelte stores for global state
- Component-level state for UI
- Tauri commands for backend communication

### Backend (Python)

**Core Modules:**

#### 1. DriveManager (`drive_manager.py`)
- Detects and enumerates disk drives
- Gathers drive information (model, serial, capacity)
- Monitors drive health (SMART data)
- Detects TRIM status
- Manages write protection

**Key Functions:**
- `detect_drives()` - Enumerate all drives
- `enable_write_protection()` - Protect source drive
- `get_drive()` - Get drive information

#### 2. FilesystemParser (`fs_parser.py`)
- Parses filesystem metadata
- Extracts deleted file entries
- Supports NTFS, FAT32, exFAT, ext4, ext3

**Key Functions:**
- `detect_filesystem()` - Identify filesystem type
- `get_deleted_files()` - Extract deleted file metadata
- `get_filesystem_info()` - Get filesystem statistics

#### 3. SignatureEngine (`signature_engine.py`)
- File type detection using magic bytes
- 100+ file signature database
- Header/footer validation
- Custom signature support

**Key Functions:**
- `identify_file_type()` - Detect file type from data
- `find_signature_in_data()` - Search for signatures
- `get_signature_by_extension()` - Lookup by extension

#### 4. CarverEngine (`carver_engine.py`)
- Sector-by-sector file carving
- Parallel processing for performance
- Fragment detection and reassembly
- Memory-mapped I/O for speed

**Key Functions:**
- `carve_drive()` - Main carving operation
- `extract_file_data()` - Extract file from device
- `_validate_file()` - Validate carved files

#### 5. AIReconstructionEngine (`ai_engine.py`)
- ONNX Runtime for inference
- File type classification
- Corruption detection
- Fragment reassembly

**Key Functions:**
- `classify_file_type()` - ML-based classification
- `detect_corruption()` - Identify corrupted data
- `reassemble_fragments()` - AI-powered reassembly

#### 6. SSDForensicsModule (`ssd_forensics.py`)
- TRIM detection and warnings
- SSD-specific recovery strategies
- Emergency mode for time-sensitive recovery
- Over-provisioning area access

**Key Functions:**
- `scan_ssd()` - Analyze SSD characteristics
- `enter_emergency_mode()` - Disable TRIM
- `get_recovery_plan()` - Generate recovery strategy

#### 7. RecoveryOrchestrator (`orchestrator.py`)
- Coordinates all recovery modules
- Manages scan workflow
- Progress tracking and reporting
- Error handling and recovery

**Key Functions:**
- `start_scan()` - Begin recovery operation
- `get_recovered_files()` - Retrieve results
- `calculate_checksum()` - Verify file integrity

#### 8. ExportManager (`export_manager.py`)
- File recovery and export
- Batch processing
- Checksum verification
- Recovery report generation

**Key Functions:**
- `recover_files()` - Export files to destination
- `generate_recovery_report()` - Create reports
- `_preserve_timestamps()` - Maintain file metadata

#### 9. LiveMonitorService (`live_monitor.py`)
- Background file deletion monitoring
- Real-time caching of deleted files
- Instant recovery capability
- Automatic cleanup

**Key Functions:**
- `start_monitoring()` - Begin monitoring paths
- `handle_deletion()` - Cache deleted files
- `get_cached_deletions()` - Retrieve cached files
- `recover_cached_file()` - Instant recovery

#### 10. ConfigManager (`config_manager.py`)
- Persistent configuration storage
- User preference management
- Default value handling

**Key Functions:**
- `load()` - Load configuration
- `save()` - Save configuration
- `get()` / `set()` - Access configuration values

## Data Flow

### Scan Workflow

1. **User Initiates Scan**
   - Frontend: User selects drive and configures scan
   - Frontend → Backend: API call with scan configuration

2. **Drive Validation**
   - Backend: DriveManager validates drive access
   - Backend: SSD Forensics checks TRIM status

3. **Filesystem Parsing** (Quick Scan)
   - Backend: FilesystemParser extracts deleted entries
   - Backend: Progress updates sent to frontend

4. **Deep Carving** (Deep Scan)
   - Backend: CarverEngine scans unallocated space
   - Backend: SignatureEngine identifies file types
   - Backend: Progress updates with files found

5. **AI Enhancement** (AI-Enhanced Scan)
   - Backend: AIReconstructionEngine processes files
   - Backend: Classification and corruption detection
   - Backend: Fragment reassembly

6. **Results Compilation**
   - Backend: Orchestrator merges results
   - Backend: Confidence scoring and sorting
   - Backend → Frontend: Return file list

7. **File Recovery**
   - Frontend: User selects files to recover
   - Frontend → Backend: Export request
   - Backend: ExportManager writes files
   - Backend: Checksum verification
   - Backend → Frontend: Recovery report

## Performance Optimizations

### Backend
- **Async I/O**: All disk operations use asyncio
- **Multiprocessing**: CPU-intensive carving uses process pools
- **Memory Mapping**: Large files use mmap for efficient access
- **Chunked Reading**: Large drives processed in chunks
- **Parallel Scanning**: Multiple signatures searched simultaneously

### Frontend
- **Lazy Loading**: Components loaded on demand
- **Virtual Scrolling**: Large file lists use virtualization
- **Debounced Updates**: Progress updates throttled
- **Caching**: Drive information cached

## Security Considerations

1. **Read-Only Operations**: Never writes to source drive
2. **Admin Privileges**: Required for disk access
3. **Input Validation**: All user inputs validated
4. **Error Handling**: Graceful degradation on errors
5. **Forensic Mode**: Optional disk imaging before recovery

## Extension Points

### Adding New File Types
1. Add signature to `SignatureEngine._load_default_signatures()`
2. Update file type labels in `AIReconstructionEngine._get_file_type_labels()`
3. Add preview support in frontend

### Adding Filesystem Support
1. Implement parser in `FilesystemParser`
2. Add filesystem detection logic
3. Test with sample filesystem images

### Custom AI Models
1. Train model and export to ONNX format
2. Place in `models/` directory
3. Update `AIReconstructionEngine` to load model

## Testing Strategy

- **Unit Tests**: Individual module functionality
- **Integration Tests**: Module interactions
- **End-to-End Tests**: Complete recovery workflows
- **Performance Tests**: Large drive scanning
- **Error Handling Tests**: Edge cases and failures

## Future Enhancements

- Cloud backup integration
- RAID reconstruction
- Network drive support
- Advanced forensic timeline
- Blockchain verification
- Multi-language support

