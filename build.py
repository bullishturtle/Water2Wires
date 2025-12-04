#!/usr/bin/env python3
"""
Water2Wires Build Script
Creates standalone Windows installer using PyInstaller and Inno Setup
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Build configuration
APP_NAME = "Water2Wires"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "Professional Data Recovery & System Optimization"
APP_AUTHOR = "Water2Wires Team"
APP_ICON = "assets/icon.ico"

ROOT_DIR = Path(__file__).parent
DIST_DIR = ROOT_DIR / "dist"
BUILD_DIR = ROOT_DIR / "build"


def clean():
    """Clean build directories"""
    print("🧹 Cleaning build directories...")
    for dir_path in [DIST_DIR, BUILD_DIR]:
        if dir_path.exists():
            shutil.rmtree(dir_path)
    print("✓ Clean complete")


def build_frontend():
    """Build the Svelte frontend"""
    print("🔨 Building frontend...")
    result = subprocess.run(["npm", "run", "build"], cwd=ROOT_DIR, shell=True)
    if result.returncode != 0:
        print("❌ Frontend build failed")
        sys.exit(1)
    print("✓ Frontend built")


def build_backend():
    """Build the Python backend with PyInstaller"""
    print("📦 Building backend with PyInstaller...")
    
    # Create spec file content
    spec_content = f'''
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/main.py'],
    pathex=['{ROOT_DIR}'],
    binaries=[],
    datas=[
        ('dist', 'web'),
        ('models', 'models'),
    ],
    hiddenimports=[
        'psutil',
        'aiosqlite',
        'aiofiles',
        'numpy',
        'PIL',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{APP_NAME}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='{APP_ICON}' if Path('{APP_ICON}').exists() else None,
)
'''
    
    spec_path = ROOT_DIR / "water2wires.spec"
    spec_path.write_text(spec_content)
    
    result = subprocess.run(
        ["pyinstaller", "--clean", str(spec_path)],
        cwd=ROOT_DIR,
        shell=True
    )
    
    if result.returncode != 0:
        print("❌ Backend build failed")
        sys.exit(1)
    
    print("✓ Backend built")


def create_installer():
    """Create Windows installer using Inno Setup"""
    print("📀 Creating Windows installer...")
    
    # Create Inno Setup script
    iss_content = f'''
#define MyAppName "{APP_NAME}"
#define MyAppVersion "{APP_VERSION}"
#define MyAppPublisher "{APP_AUTHOR}"
#define MyAppExeName "{APP_NAME}.exe"

[Setup]
AppId={{{{8A7E3D2C-1234-5678-9ABC-DEF012345678}}}}
AppName={{#MyAppName}}
AppVersion={{#MyAppVersion}}
AppPublisher={{#MyAppPublisher}}
DefaultDirName={{autopf}}\\{{#MyAppName}}
DefaultGroupName={{#MyAppName}}
AllowNoIcons=yes
OutputDir={DIST_DIR}\\installer
OutputBaseFilename={APP_NAME}_Setup_{APP_VERSION}
SetupIconFile={APP_ICON}
Compression=lzma2
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=admin

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked

[Files]
Source: "{DIST_DIR}\\{APP_NAME}\\*"; DestDir: "{{app}}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{{group}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"
Name: "{{group}}\\Uninstall {{#MyAppName}}"; Filename: "{{uninstallexe}}"
Name: "{{autodesktop}}\\{{#MyAppName}}"; Filename: "{{app}}\\{{#MyAppExeName}}"; Tasks: desktopicon

[Run]
Filename: "{{app}}\\{{#MyAppExeName}}"; Description: "Launch {APP_NAME}"; Flags: nowait postinstall skipifsilent
'''
    
    iss_path = ROOT_DIR / "installer.iss"
    iss_path.write_text(iss_content)
    
    # Try to run Inno Setup
    inno_paths = [
        r"C:\Program Files (x86)\Inno Setup 6\ISCC.exe",
        r"C:\Program Files\Inno Setup 6\ISCC.exe",
    ]
    
    inno_exe = None
    for path in inno_paths:
        if Path(path).exists():
            inno_exe = path
            break
    
    if inno_exe:
        result = subprocess.run([inno_exe, str(iss_path)], shell=True)
        if result.returncode == 0:
            print("✓ Installer created")
            return
    
    print("⚠️ Inno Setup not found. Manual installer creation required.")
    print(f"   Run: ISCC.exe {iss_path}")


def create_assets():
    """Create default assets if they don't exist"""
    assets_dir = ROOT_DIR / "assets"
    assets_dir.mkdir(exist_ok=True)
    
    # Create a simple placeholder icon if needed
    icon_path = assets_dir / "icon.ico"
    if not icon_path.exists():
        print("⚠️ No icon.ico found. Using default.")
        # Would create a default icon here


def main():
    """Main build process"""
    print(f"\n{'='*60}")
    print(f"  {APP_NAME} Build System v{APP_VERSION}")
    print(f"{'='*60}\n")
    
    # Parse arguments
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "clean":
            clean()
            return
        elif command == "frontend":
            build_frontend()
            return
        elif command == "backend":
            build_backend()
            return
        elif command == "installer":
            create_installer()
            return
    
    # Full build
    clean()
    create_assets()
    build_frontend()
    build_backend()
    create_installer()
    
    print(f"\n{'='*60}")
    print(f"  ✅ Build Complete!")
    print(f"  Installer: {DIST_DIR / 'installer'}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()

