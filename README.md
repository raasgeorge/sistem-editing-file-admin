# WhatsApp File Editor Bot

Personal WhatsApp bot untuk edit file (Word, Excel, PDF) dengan instruksi terstruktur via WhatsApp.

**Tech Stack:** Node.js + Baileys + SQLite

---

## Fitur

✅ Edit Word (.docx), Excel (.xlsx), PDF files  
✅ Instruksi terstruktur: `FIND:text REPLACE:new_text`  
✅ Preview sebelum send (accuracy first!)  
✅ Job history tracking (SQLite)  
✅ QR code authentication (Baileys)  
✅ Lightweight, no cloud dependencies  
✅ Simple HTML dashboard  

---

## Setup

### 1. Install Dependencies
```bash
cd C:\Users\satria\whatsapp-file-editor
npm install
```

### 2. Setup .env
Copy `.env.example` ke `.env` dan isi:
```bash
cp .env .env.example
```

Edit `.env` dengan credentials kamu (optional, Baileys pakai QR code)

### 3. Run Bot
```bash
npm start
```

Atau development mode:
```bash
npm run dev
```

Scan QR code dengan WhatsApp kamu di terminal.

---

## Cara Pakai

### 1. Edit File
Send pesan ke bot dengan format:
```
FIND:text_yang_dicari REPLACE:text_pengganti + attach file
```

**Contoh:**
```
FIND:Kompany REPLACE:Company + document.docx
```

### 2. Preview
Bot akan send preview dengan 5 contoh perubahan.

### 3. Konfirmasi
- Reply "OK" → file dikirim
- Reply "CANCEL" → discard

### Commands
- `HELP` - Bantuan
- `HISTORY` - Lihat 5 job terakhir
- `FIND:x REPLACE:y` - Edit file

---

## Struktur Project

```
whatsapp-file-editor/
├── app.js                 # Main entry point
├── package.json
├── .env                   # Environment variables
├── .gitignore
├── requirements.txt       # Old (ignore, for reference)
├── config.py              # Old (ignore, for reference)
├── models.py              # Old (ignore, for reference)
├── utils/
│   ├── database.js        # SQLite operations
│   ├── messageHandler.js  # WhatsApp message handler
│   ├── fileProcessor.js   # File processing (DOCX, XLSX, PDF)
│   └── instructionParser.js # Parse FIND/REPLACE format
├── routes/
│   └── jobs.js            # API endpoints
├── storage/
│   ├── uploads/           # Temporary uploaded files
│   └── results/           # Processed files
├── public/
│   └── dashboard.html     # Job history dashboard
└── auth_info_baileys/     # Baileys auth (auto-generated)
```

---

## API Endpoints

### Get Recent Jobs
```
GET http://localhost:3000/api/jobs?limit=10
```

### Get Specific Job
```
GET http://localhost:3000/api/jobs/{id}
```

### Health Check
```
GET http://localhost:3000/health
```

---

## Dashboard

Open di browser:
```
http://localhost:3000/public/dashboard.html
```

Lihat semua jobs, status, instructions, dan download hasil files.

---

## Troubleshooting

### QR Code tidak muncul?
Pastikan terminal support QR code rendering. Coba di PowerShell atau Git Bash.

### File tidak terproses?
- Check format: `FIND:x REPLACE:y`
- File size < 50MB
- Format supported: .docx, .xlsx, .pdf, .txt, .csv

### Bot disconnect?
Auto-reconnect dalam 3 detik. Check `.env` dan internet connection.

---

## Limitations

⚠️ Baileys unofficial, WhatsApp bisa block account  
⚠️ Phone harus online untuk send/receive (via Baileys)  
⚠️ PDF: text mode only (layout tidak preserved)  
⚠️ Max file size: 50MB  

---

## Next Steps (Phase 2)

- [ ] Regex support
- [ ] Multiple find/replace dalam satu instruction
- [ ] Better PDF handling (preserves layout)
- [ ] Scheduled cleanup old files
- [ ] Better error messages
- [ ] File preview (inline dalam chat)

---

**Created:** 2026-07-10  
**Status:** MVP ✅
