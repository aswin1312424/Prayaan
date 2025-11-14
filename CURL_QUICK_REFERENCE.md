# 🚗 Car CRUD via Curl - Quick Reference

## Setup (One-time)

```powershell
# 1. Start server
python manage.py runserver

# 2. Have admin credentials (or create one)
python manage.py createsuperuser
```

## Quick Commands

### 📋 List all cars
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
curl.exe -H "Authorization: Basic $creds" http://127.0.0.1:8000/api/cars/
```

### ➕ Create car
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
$json = @{
    category = "Honda City"
    ac_type = "AC"
    total_cars = 2
    registration_number = "DL01CD1234"
    price = 5800
    price_per_hour = 220
    price_per_km = 14
    fuel_consumption = "petrol"
    status = "available"
} | ConvertTo-Json

curl.exe -X POST `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d $json `
  http://127.0.0.1:8000/api/cars/
```

### 🔍 Get car (ID=1)
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
curl.exe -H "Authorization: Basic $creds" http://127.0.0.1:8000/api/cars/1/
```

### ✏️ Update car (ID=1)
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
$json = @{
    price = 6000
    total_cars = 5
} | ConvertTo-Json

curl.exe -X PUT `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d $json `
  http://127.0.0.1:8000/api/cars/1/
```

### 🗑️ Delete car (ID=6)
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:password"))
curl.exe -X DELETE `
  -H "Authorization: Basic $creds" `
  http://127.0.0.1:8000/api/cars/6/
```

## Endpoints

| Operation | Method | URL | Staff? |
|-----------|--------|-----|--------|
| List | GET | `/api/cars/` | ❌ |
| Get one | GET | `/api/cars/<id>/` | ❌ |
| Create | POST | `/api/cars/` | ✅ |
| Update | PUT | `/api/cars/<id>/` | ✅ |
| Delete | DELETE | `/api/cars/<id>/` | ✅ |

## Run Demo Script
```powershell
# Make script executable (if needed)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Run with credentials
.\test_car_crud.ps1 -Username admin -Password your_password
```

## Status Codes
- **200**: Success (GET, PUT)
- **201**: Created (POST)
- **204**: Deleted (DELETE)
- **400**: Bad request (invalid data)
- **401**: Unauthorized (bad credentials)
- **403**: Forbidden (not staff for write ops)
- **404**: Not found (invalid car ID)

## Required Fields for CREATE
- `category` (string)
- `ac_type` (string: "AC" or "Non-AC")
- `total_cars` (integer)
- `registration_number` (string, must be unique)
- `price` (decimal)
- `price_per_hour` (float)
- `price_per_km` (float)
- `fuel_consumption` (string)
- `status` (string: "available" or "repair")

---

📚 Full guide: See `CURL_API_GUIDE.md`
