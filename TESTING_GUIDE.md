# Water2Wires Testing Guide

## Quick Start Testing

### 1. Start the Backend API Server
```bash
python src/api/server.py
```
Expected: Server starts on `http://127.0.0.1:8742`

### 2. Test API Endpoints

#### Health Check
```bash
curl http://127.0.0.1:8742/api/health
```
Expected: `{"status": "ok", "version": "2.0.1"}`

#### Get System Info
```bash
curl http://127.0.0.1:8742/api/system
```
Expected: Real OS, CPU, RAM, GPU info

#### Get Drives
```bash
curl http://127.0.0.1:8742/api/drives
```
Expected: Array of real drives (C:\, D:\, etc.)

#### Start Scan
```bash
curl -X POST http://127.0.0.1:8742/api/scan/start \
  -H "Content-Type: application/json" \
  -d '{"device": "C:\\", "config": {"type": "quick"}}'
```
Expected: `{"scan_id": "...", "status": "started"}`

#### Get Scan Progress
```bash
curl http://127.0.0.1:8742/api/scan/progress/<scan_id>
```
Expected: Progress data with files_found, bytes_scanned, etc.

#### Get Scan Files
```bash
curl http://127.0.0.1:8742/api/scan/files/<scan_id>
```
Expected: Array of recovered files

## Frontend Testing

### 1. Start Development Server
```bash
npm run dev
```

### 2. Test Workflows

#### Full Recovery Flow
1. Open app → Dashboard
2. Click on a drive (e.g., C:\)
3. Select "Quick Scan"
4. Configure scan (file types, options)
5. Start scan
6. Watch progress (should show real progress)
7. Wait for completion
8. View results (should show real files from Recycle Bin)
9. Select files
10. Click "Recover Selected"
11. Enter destination folder
12. Wait for recovery completion

#### Error Cases
1. **API Server Down**: Stop backend, try scan → Should show error
2. **No Files Found**: Scan empty drive → Should show "No files found"
3. **Permission Denied**: Try to scan protected drive → Should show error
4. **Invalid Destination**: Enter invalid path → Should show error

## Expected Behaviors

### Scan Progress
- Progress updates every 500ms
- Shows real files found count
- Shows real bytes scanned
- Shows current operation
- Completes at 100%

### File Recovery
- Shows progress percentage
- Displays errors if any
- Shows success message on completion
- Updates localStorage with recovery count

### Error Handling
- All errors displayed to user
- Clear, actionable error messages
- No crashes or unhandled exceptions
- Graceful degradation

## Known Issues & Workarounds

### Issue: Deep Scan Requires Admin
**Workaround**: Use Quick Scan (works without admin)

### Issue: No Files Found in Recycle Bin
**Workaround**: Files may have been permanently deleted (TRIM on SSD)

### Issue: Recovery Destination Prompt
**Workaround**: Type full path or use default location

## Success Criteria

✅ All API endpoints respond correctly
✅ Scans complete and return real files
✅ Recovery works for Recycle Bin files
✅ Errors are handled gracefully
✅ UI shows real-time progress
✅ No fake/mock data displayed

## Performance Benchmarks

- **Scan Start**: < 1 second
- **Progress Updates**: Every 500ms
- **File Recovery**: ~100MB/s (depends on drive)
- **API Response**: < 50ms

## Troubleshooting

### API Server Won't Start
- Check if port 8742 is available
- Verify Python dependencies installed
- Check for permission errors

### Scan Returns No Files
- Verify Recycle Bin has files
- Check drive permissions
- Try different drive

### Recovery Fails
- Check destination folder exists
- Verify write permissions
- Check disk space

