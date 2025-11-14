# Car CRUD Operations via curl Commands

This guide shows how to perform CRUD operations on vehicles using curl commands. The API requires authentication.

## Prerequisites

1. **Server running:** 
   ```powershell
   python manage.py runserver
   ```

2. **Have a staff/admin user** for create/update/delete operations. Users can read cars without staff privileges.

---

## Authentication Setup

First, get your authentication credentials:

```powershell
# Create a staff user if you don't have one
python manage.py createsuperuser

# Username: admin
# Email: admin@example.com
# Password: your_password
```

---

## API Endpoints

| Method | Endpoint | Description | Requires Staff |
|--------|----------|-------------|-----------------|
| GET | `/api/cars/` | List all cars | ❌ No |
| POST | `/api/cars/` | Create new car | ✅ Yes |
| GET | `/api/cars/<id>/` | Get car details | ❌ No |
| PUT | `/api/cars/<id>/` | Update car | ✅ Yes |
| DELETE | `/api/cars/<id>/` | Delete car | ✅ Yes |

---

## 1. READ - List All Cars

```powershell
$username = "admin"
$password = "your_password"
$creds = "$($username):$($password)"
$encoded = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($creds))

curl.exe -H "Authorization: Basic $encoded" `
  http://127.0.0.1:8000/api/cars/
```

**Expected Response:**
```json
[
  {
    "id": 1,
    "category": "Ambassador",
    "ac_type": "AC",
    "total_cars": 3,
    "registration_number": "DL01AB0001",
    "image": "/media/cars/DL01AB0001.jpg",
    "price": "5000.00",
    "price_per_hour": 200,
    "price_per_km": 12.5,
    "fuel_consumption": "petrol",
    "status": "available"
  }
]
```

---

## 2. READ - Get Single Car Details

```powershell
$username = "admin"
$password = "your_password"
$creds = "$($username):$($password)"
$encoded = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($creds))

# Get car with ID 1
curl.exe -H "Authorization: Basic $encoded" `
  http://127.0.0.1:8000/api/cars/1/
```

---

## 3. CREATE - Add a New Car

```powershell
$username = "admin"
$password = "your_password"
$creds = "$($username):$($password)"
$encoded = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($creds))

# Create a new car (JSON data)
$jsonData = @{
    category = "Mahindra XUV"
    ac_type = "AC"
    total_cars = 2
    registration_number = "DL01AB9999"
    price = 6500
    price_per_hour = 250
    price_per_km = 15
    fuel_consumption = "diesel"
    status = "available"
} | ConvertTo-Json

curl.exe -X POST `
  -H "Authorization: Basic $encoded" `
  -H "Content-Type: application/json" `
  -d $jsonData `
  http://127.0.0.1:8000/api/cars/
```

**Expected Response (201 Created):**
```json
{
  "id": 6,
  "category": "Mahindra XUV",
  "ac_type": "AC",
  "total_cars": 2,
  "registration_number": "DL01AB9999",
  "image": null,
  "price": "6500.00",
  "price_per_hour": 250,
  "price_per_km": 15,
  "fuel_consumption": "diesel",
  "status": "available"
}
```

---

## 4. UPDATE - Modify Existing Car

```powershell
$username = "admin"
$password = "your_password"
$creds = "$($username):$($password)"
$encoded = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($creds))

# Update car with ID 1 (partial update)
$jsonData = @{
    price = 5500
    total_cars = 5
} | ConvertTo-Json

curl.exe -X PUT `
  -H "Authorization: Basic $encoded" `
  -H "Content-Type: application/json" `
  -d $jsonData `
  http://127.0.0.1:8000/api/cars/1/
```

**Expected Response (200 OK):**
```json
{
  "id": 1,
  "category": "Ambassador",
  "ac_type": "AC",
  "total_cars": 5,
  "registration_number": "DL01AB0001",
  "image": "/media/cars/DL01AB0001.jpg",
  "price": "5500.00",
  "price_per_hour": 200,
  "price_per_km": 12.5,
  "fuel_consumption": "petrol",
  "status": "available"
}
```

---

## 5. DELETE - Remove a Car

```powershell
$username = "admin"
$password = "your_password"
$creds = "$($username):$($password)"
$encoded = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($creds))

# Delete car with ID 6
curl.exe -X DELETE `
  -H "Authorization: Basic $encoded" `
  http://127.0.0.1:8000/api/cars/6/
```

**Expected Response (204 No Content):**
```
(empty response, just status 204)
```

---

## Example Scripts for Testing

### PowerShell Script - Full CRUD Demo

Save as `car_crud_demo.ps1`:

```powershell
param(
    [string]$Username = "admin",
    [string]$Password = "your_password",
    [string]$BaseUrl = "http://127.0.0.1:8000"
)

$creds = "$($Username):$($Password)"
$encoded = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($creds))

function Make-ApiCall {
    param(
        [string]$Method,
        [string]$Endpoint,
        [object]$Body = $null
    )
    
    $url = "$BaseUrl$Endpoint"
    $params = @{
        Uri = $url
        Method = $Method
        Headers = @{ "Authorization" = "Basic $encoded"; "Content-Type" = "application/json" }
    }
    
    if ($Body) {
        $params.Body = $Body | ConvertTo-Json
    }
    
    Write-Host "`n📢 $Method $Endpoint"
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    $response = Invoke-RestMethod @params
    $response | ConvertTo-Json | Write-Host
    return $response
}

# 1. LIST all cars
Write-Host "`n🚗 CRUD DEMO - Car Management API" -ForegroundColor Cyan
Write-Host "════════════════════════════════════════════" -ForegroundColor Cyan

$cars = Make-ApiCall -Method GET -Endpoint "/api/cars/"

# 2. CREATE a new car
$newCar = Make-ApiCall -Method POST -Endpoint "/api/cars/" -Body @{
    category = "Hyundai Creta"
    ac_type = "AC"
    total_cars = 2
    registration_number = "MH02AB1234"
    price = 7000
    price_per_hour = 300
    price_per_km = 18
    fuel_consumption = "diesel"
    status = "available"
}

$newCarId = $newCar.id
Write-Host "`n✅ Created car with ID: $newCarId" -ForegroundColor Green

# 3. READ specific car
$carDetail = Make-ApiCall -Method GET -Endpoint "/api/cars/$newCarId/"

# 4. UPDATE the car
$updated = Make-ApiCall -Method PUT -Endpoint "/api/cars/$newCarId/" -Body @{
    price = 7200
    total_cars = 3
}

# 5. DELETE the car
Make-ApiCall -Method DELETE -Endpoint "/api/cars/$newCarId/"

Write-Host "`n✅ Demo complete!" -ForegroundColor Green
```

**Run it:**
```powershell
.\car_crud_demo.ps1 -Username admin -Password your_password
```

---

## Error Responses

### 401 Unauthorized
```json
{
  "detail": "Invalid username/password."
}
```
**Fix:** Verify credentials

### 403 Forbidden
```json
{
  "error": "Only staff members can create cars."
}
```
**Fix:** Use a staff/admin account

### 404 Not Found
```json
{
  "error": "Car not found."
}
```
**Fix:** Use a valid car ID

### 400 Bad Request
```json
{
  "registration_number": ["A car with this registration number already exists."]
}
```
**Fix:** Use a unique registration number

---

## Testing without Authentication

For testing without storing passwords, you can also use Django sessions (requires browser login first):

```powershell
# After logging in via browser and getting sessionid cookie:
curl.exe -b "sessionid=your_session_id_here" `
  http://127.0.0.1:8000/api/cars/
```

---

## Summary of Operations

| Operation | Command | Requires Staff |
|-----------|---------|-----------------|
| List all cars | `GET /api/cars/` | No |
| Get car by ID | `GET /api/cars/<id>/` | No |
| Create car | `POST /api/cars/` | Yes |
| Update car | `PUT /api/cars/<id>/` | Yes |
| Delete car | `DELETE /api/cars/<id>/` | Yes |

---

## Notes

- All API responses are JSON format
- Required fields for CREATE: category, ac_type, total_cars, registration_number, price, price_per_hour, price_per_km, fuel_consumption, status
- Image upload via API requires form-data (multipart); use web UI for images
- Registration number is auto-converted to uppercase
- All prices are validated and must be positive numbers
