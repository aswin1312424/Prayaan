# Car CRUD API - Copy-Paste Commands

These are ready-to-use curl commands. Just replace `admin` and `password` with your credentials.

---

## 1. LIST ALL CARS

```powershell
# Set credentials
$username = "admin"
$password = "password"
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$username`:$password"))

# Get all cars
curl.exe -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  http://127.0.0.1:8000/api/cars/
```

---

## 2. GET SPECIFIC CAR (ID=1)

```powershell
$username = "admin"
$password = "password"
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$username`:$password"))

curl.exe -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  http://127.0.0.1:8000/api/cars/1/
```

---

## 3. CREATE NEW CAR

```powershell
$username = "admin"
$password = "password"
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$username`:$password"))

$body = @{
    category = "Honda City"
    ac_type = "AC"
    total_cars = 2
    registration_number = "DL-HONDA-2024"
    price = 5800
    price_per_hour = 220
    price_per_km = 14
    fuel_consumption = "petrol"
    status = "available"
} | ConvertTo-Json

curl.exe -X POST `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d $body `
  http://127.0.0.1:8000/api/cars/
```

---

## 4. UPDATE CAR (ID=1)

```powershell
$username = "admin"
$password = "password"
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$username`:$password"))

$body = @{
    price = 6500
    total_cars = 4
    price_per_hour = 250
} | ConvertTo-Json

curl.exe -X PUT `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  -d $body `
  http://127.0.0.1:8000/api/cars/1/
```

---

## 5. DELETE CAR (ID=6)

```powershell
$username = "admin"
$password = "password"
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$username`:$password"))

curl.exe -X DELETE `
  -H "Authorization: Basic $creds" `
  -H "Content-Type: application/json" `
  http://127.0.0.1:8000/api/cars/6/
```

---

## BONUS: BATCH OPERATIONS

### Create 3 Cars in Loop

```powershell
$username = "admin"
$password = "password"
$creds = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes("$username`:$password"))

$cars = @(
    @{ category = "Maruti Swift"; registration = "DL-MS-001"; price = 4500 },
    @{ category = "Hyundai i20"; registration = "DL-HI-001"; price = 5200 },
    @{ category = "Tata Nexon"; registration = "DL-TN-001"; price = 6800 }
)

foreach ($car in $cars) {
    $body = @{
        category = $car.category
        ac_type = "AC"
        total_cars = 2
        registration_number = $car.registration
        price = $car.price
        price_per_hour = [int]($car.price / 20)
        price_per_km = [int]($car.price / 500)
        fuel_consumption = "petrol"
        status = "available"
    } | ConvertTo-Json
    
    Write-Host "Creating: $($car.category)"
    curl.exe -X POST `
      -H "Authorization: Basic $creds" `
      -H "Content-Type: application/json" `
      -d $body `
      http://127.0.0.1:8000/api/cars/
    
    Write-Host ""
}
```

---

## TIPS

1. **Save as script**: Copy any command block to a `.ps1` file
   ```powershell
   # Save as: create_car.ps1
   # Run with: .\create_car.ps1
   ```

2. **View response prettily**:
   ```powershell
   $response = curl.exe ... | ConvertFrom-Json
   $response | Format-Table -AutoSize
   ```

3. **Check HTTP status**:
   ```powershell
   $response = curl.exe -w "`nHTTP_CODE:%{http_code}" ...
   ```

4. **Save response to file**:
   ```powershell
   curl.exe ... -o response.json
   ```

---

## STATUS CODES

| Code | Meaning |
|------|---------|
| 200 | Success (GET, PUT) |
| 201 | Created (POST) |
| 204 | Deleted (DELETE) |
| 400 | Bad Request |
| 401 | Unauthorized (bad credentials) |
| 403 | Forbidden (not staff) |
| 404 | Not Found (car doesn't exist) |

---

## REQUIRED FIELDS FOR CREATE

```json
{
  "category": "string",
  "ac_type": "AC or Non-AC",
  "total_cars": "integer",
  "registration_number": "string (unique)",
  "price": "decimal",
  "price_per_hour": "float",
  "price_per_km": "float",
  "fuel_consumption": "petrol|diesel|gas|electric",
  "status": "available|repair"
}
```

---

## OPTIONAL FIELDS FOR UPDATE

Any of the above fields can be partially updated:

```powershell
$body = @{
    price = 7000
    total_cars = 5
} | ConvertTo-Json

# Only these two fields will be updated; others remain unchanged
```

---

Start with **LIST ALL CARS** to test your setup!
