# ⚡ 30-Second Quick Start - Car API with curl

## Step 1: Start Server (Keep Running)
```powershell
python manage.py runserver
```

## Step 2: List All Cars (No Auth Needed)
```powershell
curl.exe http://127.0.0.1:8000/api/cars/
```

## Step 3: Create Admin User (One Time)
```powershell
python manage.py createsuperuser
# Username: admin
# Password: admin123
```

## Step 4: Create a Car
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:admin123"))
$body = @{
    category = "Honda City"
    ac_type = "AC"
    total_cars = 2
    registration_number = "DL-2024-001"
    price = 5800
    price_per_hour = 220
    price_per_km = 14
    fuel_consumption = "petrol"
    status = "available"
} | ConvertTo-Json

curl.exe -X POST -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" -d $body `
  http://127.0.0.1:8000/api/cars/
```

## Step 5: Update a Car (ID=1)
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:admin123"))
curl.exe -X PUT -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d '{"price":6500,"total_cars":5}' `
  http://127.0.0.1:8000/api/cars/1/
```

## Step 6: Delete a Car (ID=6)
```powershell
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("admin:admin123"))
curl.exe -X DELETE -H "Authorization: Basic $creds" `
  http://127.0.0.1:8000/api/cars/6/
```

---

## OR Run Full Demo Script
```powershell
.\test_car_crud.ps1 -Username admin -Password admin123
```

---

## 📖 Full Documentation
- `CURL_API_GUIDE.md` - Complete guide
- `CURL_COMMANDS.md` - More examples
- `API_SETUP_COMPLETE.md` - Detailed setup
